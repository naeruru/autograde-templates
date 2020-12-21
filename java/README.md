# Java Template
An Autograde project template that demonstrates Java support.

## Tests
There is currently one test bundled with this example.

### public-increment
- Tests: Counter Class
- Method: compares `answer` and `output` file.
- Additional info: Basic example with no serializaton.

## Additional files
### Makefile
- make clean: Cleans the project folder of build directories (__pycache, tar files, etc).
- make archive: Creates an archive than can be submitted on autograde by a student.

### .gitignore
Useful so that students don't commit unnecessary files.

## Additional notes
The driver.py will usually be the exact same for all tests if you follow the answer/output method. The one part that might change between tests is what you need to use `preparefile()` on. If you include more files (for example, you want test.java to access a text file), you would need to prepare those.