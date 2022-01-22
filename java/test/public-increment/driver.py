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
import shutil

# prepare files
preparefile('./test.java')

# run test
runcmdsafe('javac -d ./ test.java ../../Counter.java')
b_stdout, b_stderr, b_exitcode = runcmdsafe('java p0.Test')


# Convert stdout bytes to utf-8
stdout = ""
stderr = ""
try:
	stdout = b_stdout.decode('utf-8')
	stderr = b_stderr.decode('utf-8')
except:
	pass


try:
	with open('answer', 'r') as file1, open('output', 'r') as file2:
		answer = file1.read().strip()
		output = file2.read().strip()

	# Delete output 
	os.remove('output')
	shutil.rmtree('p0') # .class build folder (folder = package name)

	# Built in tester.py function assertequals(expected, actual, info='')
	# If True, passes. If false, fails and gives expected != actual and and specified info.
	# parameters: 
	# - expected(required): the answer that was expected
	# - actual(required): the output from the user's code
	# - info(optional): any additional info you want printed if it fails
	assertequals(answer, output, stdout+"\n"+stderr)

except FileNotFoundError:
	failtest(stdout+"\n"+stderr)
