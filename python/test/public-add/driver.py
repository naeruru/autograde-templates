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

# Comparison with answer and output here
try:
	with open('answer', 'r') as file1, open('output', 'r') as file2:
		answer = int(file1.read())
		output = int(file2.read())

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
except ValueError:
	os.remove('output')
	failtest(stdout+"\n"+stderr)
