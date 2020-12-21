#!/usr/bin/python3
#####################################################
#############  LEAVE CODE BELOW  ALONE  #############
# Include base directory into path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

# Import tester
from tester import failtest, passtest, assertequals, runcmd, preparefile, runcmdsafe
#############    END UNTOUCHABLE CODE   #############
#####################################################

###################################
# Write your testing script below #
###################################
import pickle 

# prepare files
preparefile('./test.py')

# run test
python_bin = sys.executable
b_stdout, b_stderr, b_exitcode = runcmdsafe(f'{python_bin} ./test.py')
                                                                          

# Convert stdout bytes to utf-8
stdout = ""
stderr = ""
try:
	stdout = b_stdout.decode('utf-8')
	stderr = b_stderr.decode('utf-8')
except:
	pass


# With pickle, you can keep your raw data intact via serialization.
# In this example, two frozensets with different orders will
# still be equal with the use of serialization.
try:
	with open('answer', 'rb') as file1, open('output', 'rb') as file2:
		answer = pickle.load(file1) # frozenset({6, 5, 4, 3, 2, 1})
		output = pickle.load(file2) # frozenset({1, 2, 3, 4, 5, 6})
		file1.close()
		file2.close()

		# Delete output 
		os.remove('output')

		# Built in tester.py function assertequals(expected, actual, info='')
		# If True, passes. If false, fails and gives expected != actual and and specified info.
		# parameters: 
		# - expected(required): the answer that was expected
		# - actual(required): the output from the user's code
		# - info(optional): any additional info you want printed if it fails
		assertequals(answer, output, stdout+"\n"+stderr)

except FileNotFoundError:
	failtest(stdout+"\n"+stderr)
