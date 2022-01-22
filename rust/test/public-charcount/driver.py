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

# prepare necessary files
preparefile('./Cargo.toml')
preparefile('./Cargo.lock')
preparefile('./src')
preparefile('./src/main.rs')

# run test file
b_stdout, b_stderr, b_exitcode = runcmdsafe(f'cargo run')


# convert stdout bytes to utf-8
stdout = ""
stderr = ""
try:
	stdout = b_stdout.decode('utf-8')
	stderr = b_stderr.decode('utf-8')
except:
	pass


try:
	with open('output', 'r') as file1:
		output = file1.read()

	os.remove('output')

	# Compare without an answer file.
	# In some situations, the answer may be an approximate value,
	# so this way would be preferred.
	if 2 < int(output) < 4:
		passtest('')
	else:
		failtest(f'Expected a value between 2 and 4, but got {result}.\n{stdout}\n{stderr}')

except FileNotFoundError:
	failtest(stdout+"\n\n"+stderr)
