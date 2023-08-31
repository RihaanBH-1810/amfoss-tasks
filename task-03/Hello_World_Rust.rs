use std::io;

fn main() {
    let mut num:i32=0;
    let mut input = String::new();
    
    println!("Enter a number :");
    io::stdin().read_line(&mut input).expect("Not a valid string");
    num = input.trim().parse().expect("Not a valid number");
    
    if num <=1 {
        std::process::exit(0);
    }
    println!("{}",2);
    for i in 2..num+1{
        for j in 2..i{
            if i%j == 0{
                break;
            }else{
                println!("{}",i);
                break;
            }
        }
    }
}