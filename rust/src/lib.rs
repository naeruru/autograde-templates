/* 
 * Autograde
 * Rust Project Template
 */


pub mod warmup_functions {

    pub fn add_vals(x: i32, y: i32) -> i32 {
        x + y
    }

    pub fn append(mut a: Vec<i32>, mut b: Vec<i32>) -> Vec<i32> {
        a.append(&mut b);
        a
    }

    pub fn count_characters(s: &String, key: char) -> usize {
        let mut count = 0;

        for c in s.chars() { 
            if c == key {
                count = count + 1;
            }
        }
        count
    }

    pub fn remove_characters(s: &String, key: char) -> String {
        let mut result = String::with_capacity(s.len());

        let chars = s.chars();
        for c in chars {
            if c != key {
                result.push(c);
            }
        }
        result
    }
}
    