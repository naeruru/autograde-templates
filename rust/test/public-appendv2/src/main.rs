use my_project_name::warmup_functions;

use std::fs;


fn main() {
    let a = vec![1, 2, 3];
    let b = vec![4, 5, 6];

    let new = warmup_functions::append(a, b);

    // serialize result (py pickle format)
    let serialized = serde_pickle::to_vec(&new, true).unwrap();
    //let deserialized: Vec<i32> = serde_pickle::from_slice(&serialized).unwrap();


    // dump answer to serialized file (do this ahead of time!)
    //let answer_serl = serde_pickle::to_vec(&vec![1, 2, 3, 4, 5, 6], true).unwrap();
    //fs::write("answer", answer_serl).expect("Unable to create answer file");

    // dump result to serialized file
    fs::write("result", serialized).expect("Unable to create result file");
}
