use rand::Rng;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let n: usize = args[1].parse().expect("Invalid input");

    let mut rng = rand::thread_rng();
    for _ in 0..n {
        print!("{} ", rng.gen_range(0..=n));
    }
    println!();
}
