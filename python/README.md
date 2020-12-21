# Python Template
An Autograde project template that demonstrates Python support.

## Tests
There are several tests bundled with this example.

### public-add
- Tests: add()
- Method: compares `answer` and `output` file.
- Additional info: Basic example with no serializaton.

### public-union
- Tests: union()
- Method: compares `answer` and `output` file.
- Additional info: Uses `pickle` to serialize the answer/output for data integrity. This is the preferred way to write tests in python.

### public-insecure
- Tests: add()
- Method: Checks answer in the test.py and uses exit codes to determine if right or wrong.
- Additional info: This method is insecure and allows the answer to be fabricated. It is meant to show what not to do.

## Additional files
### Makefile
- make clean: Cleans the project folder of build directories (__pycache, tar files, etc).
- make archive: Creates an archive than can be submitted on autograde by a student.

### .gitignore
Useful so that students don't commit unnecessary files.

## Additional notes
The driver.py will usually be the exact same for all tests if you follow the answer/output method. The one part that might change between tests is what you need to use `preparefile()` on. If you include more files (for example, you want test.py to access a text file), you would need to prepare those.