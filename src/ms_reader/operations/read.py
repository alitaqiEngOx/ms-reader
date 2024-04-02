import os
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord
from casacore.tables import table
from numpy.typing import NDArray

from utils import tools


@dataclass
class Read:
    """
    Class to access, read & export MeasurementSet data.
    """

    ms_dir: str
    """MeasurementSet directory."""

    name: str
    """Name for outputs."""
    
    @property
    def frequencies(self) -> NDArray:
        """
        MeasurementSet frequency channels.
        """
        with tools.block_logging():
            try:
                chan_freq = table(
                    os.path.join(self.ms_dir, "SPECTRAL_WINDOW")
                ).getcol("CHAN_FREQ")
            except:
                raise FileNotFoundError(
                    "expected a 'SPECTRAL_WINDOW' table with a 'CHAN_FREQ' column"
                )
        return np.asarray(chan_freq.flatten())

    @property
    def phase_centre(self) -> SkyCoord:
        """
        MeasurementSet phase centre.
        """
        try:
            with tools.block_logging():
                phase_centre = table(
                    os.path.join(self.ms_dir, "FIELD")
                ).getcol("PHASE_DIR")
        except:
            raise FileNotFoundError(
                "expected a 'FIELD' table with a 'PHASE_DIR' column"
            )
        if np.array(phase_centre).shape != (1, 1, 2):
            raise ValueError("unsupported phase centre definition")
        return SkyCoord(
            phase_centre[0][0][0], phase_centre[0][0][1], unit="rad"
        )

    @property
    def saving_path(self) -> str:
        """
        Path to save outputs.
        """
        return os.path.abspath(
            os.path.join(self.ms_dir, os.pardir)
        )

    @property
    def uvw(self) -> NDArray:
        """
        MeasurementSet UVW coordinates.
        """
        try:
            with tools.block_logging():
                uvw = table(self.ms_dir).getcol("UVW")
        except:
            raise FileNotFoundError("expected a 'UVW' column")
        if len(np.asarray(uvw).shape) > 3:
            raise ValueError("unsupported UVW with more than 3 dimensions")
        if np.asarray(uvw).shape[-1] != 3:
            raise ValueError(
                "there must be 3 positional coordinates per observation"
            )
        return np.asarray(uvw)

    @property
    def visibilities(self) -> NDArray:
        """
        MeasurementSet Visiblities.
        """
        try:
            with tools.block_logging():
                visibilities = table(self.ms_dir).getcol("DATA")
        except:
            raise FileNotFoundError("expected a 'DATA' column")
        if len(np.asarray(visibilities).shape) > 4:
            raise ValueError("unsupported DATA with more than 4 dimensions")
        return np.asarray(visibilities)

    def uv_tracks(self, chans: NDArray) -> None:
        """
        Exports UV tracks of for all channels as a .png.
        Assumes UVW data are 2-dimensional.
        """
        print(self.uvw.shape)
        ax = plt.figure().add_subplot(111)
        for chan in chans:
            ax.scatter(
                self.uvw[:, 0] * chan / 299792458.,
                self.uvw[:, 1] * chan / 299792458.,
                np.ones(len(self.uvw[:, 0])),
                'k'
            )
            ax.scatter(
                -self.uvw[:, 0] * chan / 299792458.,
                -self.uvw[:, 1] * chan / 299792458.,
                np.ones(len(self.uvw[:, 0])),
                'k'
            )
        ax.set_aspect("equal")
        plt.xlabel('u - wavenumbers')
        plt.ylabel('v - wavenumbers')
        plt.title('UV tracks')
        plt.savefig(
            os.path.join(self.saving_path, f"{self.name}_uv_tracks.png"),
            dpi=500
        )
        plt.close()

    def to_npy(self, array: NDArray, *, var: str) -> None:
        """
        Exports numpy arrays as .npy binaries.
        """
        np.save(
            os.path.join(self.saving_path, f"{self.name}_{var}.npy"),
            array
        )

    def to_txt(self, phase_centre: SkyCoord, *, var: str):
        """
        Exports phase centre as a .txt.
        """
        line = f"phase centre (RA, DEC), deg = \
        ({phase_centre.ra.deg}, {phase_centre.dec.deg})"
        with open(os.path.join(self.saving_path, f"{self.name}_{var}.txt"), 'w') as file:
            file.write(line)


def ms(ms_dir: str, *, name: str) -> None:
    """
    Entry function to call the Read class on a MeasurementSet.
    """
    ms = Read(ms_dir, name)
    ms.to_npy(ms.frequencies, var="freq")
    ms.to_txt(ms.phase_centre, var="phase_centre")
    ms.to_npy(ms.uvw, var="uvw_geo")
    ms.to_npy(ms.visibilities, var="vis")
    ms.uv_tracks(ms.frequencies)