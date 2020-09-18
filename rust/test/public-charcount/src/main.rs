use my_project_name::warmup_functions;

use std::fs;


fn main() {
    let test_str = String::from("hello world!");
    let key = 'l';

    let result: usize = warmup_functions::count_characters(&test_str, key);

    // dump result to file
    fs::write("result", result.to_string()).expect("Unable to create result file");
}
