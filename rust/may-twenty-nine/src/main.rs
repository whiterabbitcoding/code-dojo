fn sum(a: u32, b: u32) -> u32{
    a + b
}

fn iterate(numbers: &Vec<i32>) {
    for number in numbers {
        println!("The number is {}", number);
    }
}


struct Person {
    name: String,
    age: u32,
}

impl Person {
    fn greet(&self) {
        println!("Hello, my name is {}.", self.name)
    }

    fn is_adult(&self) -> bool {
        self.age >= 18
    }
}

fn main() {
    println!("Hello, world!");
    let x = sum(10, 10);
    println!("{}", x);
    println!("{}", sum(5,5));

    let my_vector = vec![1,2,3,4,5];
    iterate(&my_vector);
    let person = Person {
        name: String::from("Alex"),
        age: 28,
    };

    println!("{}'s age is {}", person.name, person.age);
    person.greet();
    println!("{} is an adult: {}", person.name, person.is_adult());

    let practice = "Practice";
    println!("The first letter of practice is: {:?}",practice.chars().nth(0));
    let sub = &practice[0..2];
    println!("A substring of practice is: {}", sub);



    // While let example
    let mut v = vec![1, 3, 5, 7, 11]; loop {
        match v.pop() {
        Some(x) => println!("{}", x), None => break,
        } }
    // Same as
    let mut v = vec![1,2,3,4];

    while let Some(x) = v.pop() {
        println!("{}", x);
    }


    // closure example
    let num = 4;
    let output = |x| x + num;


}
