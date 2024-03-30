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