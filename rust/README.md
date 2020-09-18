# Rust Template

An Autograde project template that demonstrates Rust support.

## Tests

There are several tests bundled with this example.

### public-add

- Tests: add_vals()
- Method: compares `answer` and `output` file.
- Additional info: Basic example

### public-append

- Tests: append()
- Method: compares `answer` and `output` file.
- Additional info: Shows an easy way to format a variable to string for file output.

### public-appendv2

- Tests: append()
- Method: Serializes values (pickle format) to file. Compares `answer` and `output` file.
- Additional info: Rust does not have built in serialization support, so a library has to be imported. This greatly increases the time to compile a test on the grading daemon. Use only when it is necessary.

### public-charcount

- Tests: count_characters()
- Method: Checks `output` with constraints defined in the driver.py.
- Additional info: Technically unnecessary in this example, but useful when the answer is an approximate value.

### public-charremove

- Tests: remove_characters()
- Method: Compares `ouput` file within driver.py (no `answer` file).
- Additional info: N/A

## Additional files

### Makefile
- make clean: Cleans the project folder of build directories (__pychache, target/ dirs, etc).
- make archive: Creates an archive than can be submitted on autograde by a student.

### .gitignore
Useful so that students don't commit unnecessary files.
