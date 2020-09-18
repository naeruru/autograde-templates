use my_project_name::warmup_functions;

use std::fs;


fn main() {

    let a = 2;
    let b = 2;
    let result = warmup_functions::add_vals(a, b);
    println!("ADD: {} + {} = {}", a, b, result);

    // create result file
    fs::write("result", result.to_string()).expect("Unable to create result file");


    // using assert_eq!() is also possible in combination with a driver.py.
    // if it fails, info will be sent in stdout to the driver.py.
    assert_eq!(4, result);
}
