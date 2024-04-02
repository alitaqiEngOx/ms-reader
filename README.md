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

Usage is currently as follows: Clone the repository then, from the parent directory, run the following command:

```
$ python3 ./src/ms_reader [options] dir/to/your/measurement_set.ms
```

The options include ```--name [NAME]``` to specify the name of the output directory.

The output directory will be generated in the same directory as your input MeasurementSet, in a sub-directory whose name matches the value you assign to ```--name```.

Linux OS and Python 3.9 are recommended. Set up a conda environment to avoid potential inconsistencies with other software you might have installed.
