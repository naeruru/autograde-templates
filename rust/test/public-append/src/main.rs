use my_project_name::warmup_functions;

use std::fs;


fn main() {
    let a = vec![1, 2, 3];
    let b = vec![4, 5, 6];

    let result = warmup_functions::append(a, b);
    
    // Format result as string.
    // You can write it to a file however you want,
    // I just found this way to be the fastest.
    let result_str = format!("{:?}", result);

    // dump result to file
    fs::write("output", result_str).expect("Unable to create result file");

    // create answer file (generate this ahead of time!)
    //fs::write("answer", "[1, 2, 3, 4, 5, 6]").expect("Unable to create result file");

    // assert equal for debug purposes (prints useful info to user if test fails).
    // Normally, you can do this in the driver with our assertequal(), but assert_eq!() is nice too.
    // Be sure to pass stdout to failtest to display what is written!
    //assert_eq!(result, vec![1, 2, 3, 4, 5, 6]);
}
