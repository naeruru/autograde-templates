import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import add

addresult = str(add(1, 1))

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()

# Create the answer file ahead of time, and do not preparefile('') it in the driver.py.
# This guarantees that users cannot modify the file when the submission is being tested.
# Users also cannot modify you driver.py, so if you need a less precise comparison, it
# can be done in the driver.py as well (ex: answer is some approximate value).
# afile = open('answer', 'w')
# afile.write('2')
# afile.close()
