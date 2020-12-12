import pandas as pd
import numpy as np
import os
from pathlib import Path

keylist = [dI for dI in os.listdir(directory) if os.path.isdir(os.path.join(directory,dI))]

# temporarily cutting down the list
keylist = keylist[:3]

for i in keylist:
    
