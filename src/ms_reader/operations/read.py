import os
from dataclasses import dataclass

import numpy as np
from astropy.coordinates import SkyCoord
from casacore.tables import table
from numpy.typing import NDArray

from utils import tools


@dataclass
class Read:
    """
    """

    ms_dir: str
    """"""

    @property
    def phase_centre(self) -> SkyCoord:
        """
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