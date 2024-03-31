# ms-reader

This software reads radio astronomy MeasurementSets and produces:
- .npy binaries for visibilities, UVW data, and frequency channels.
- .txt file incorporating the phase-tracking centre in (RA, DEC), in degrees.
- .png image of the UV tracks for all frequency channels.

Libraries required:
- astropy;
- matplotlib;
- numpy;
- python-casacore.
