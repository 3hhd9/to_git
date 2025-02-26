def generate_multiplication_table(number, range_values):
    
    for i in range_values:
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number to generate  multiplication table: "))


custom_range = input("Do you want to specify a custom range (yes/no)? ").lower()

if custom_range == 'yes':
    starting = int(input("Enter  starting number : "))
    ending = int(input("Enter the ending number : "))
    range_values = list(range(starting, ending + 1)) 
    
    generate_multiplication_table(number, range_values)
else:
    range_values = list(range(2, 11))  
    generate_multiplication_table(number, range_values)

































































