import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import union
import pickle

answer = frozenset(union({1, 2, 3}, {4, 5, 6}))

with open('output', 'wb') as f:
  pickle.dump(answer, f)

# create answer file aheads of time, or specify it in the driver.py
# with open('answer', 'wb') as f:
#   pickle.dump(frozenset({6, 5, 4, 3, 2, 1}), f)
