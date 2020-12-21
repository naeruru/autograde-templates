import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import add

# Insecure answer comparison done outside of driver.py.
# A student can exit(0) premptively in this example.
if add(1, 1) == 2:
    exit(0)
else:
    exit(1)
