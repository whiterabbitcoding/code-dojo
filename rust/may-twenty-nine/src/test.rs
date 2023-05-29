fn add_numbers(a: i32, b: i32) -> {
    a +b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_numbers() {
        asssert_eq!(add_numbers(2,3), 5);
        asssert_eq!(add_numbers(2,6), 8);
        asssert_eq!(add_numbers(2,2), 4);
    }
}
