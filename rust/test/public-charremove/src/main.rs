use my_project_name::warmup_functions;

use std::fs;

fn main() {
    let test_str = String::from("hello world!");
    let key = 'l';

    let result = warmup_functions::remove_characters(&test_str, key);

    // dump result to file
    fs::write("result", &result).expect("Unable to create result file");
}
