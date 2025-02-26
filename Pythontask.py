# task 1
n = 6
for number_in_loop in range(6):
    for inner_line in range(1, number_in_loop+1):
        print(inner_line, end="")
  
    print("")
# task 2
for element_inLop in range(5):
    for inner_loop in range(element_inLop+1):
        print("*", end="")

    print("")

#task 3
nu = 5

for element_in_triangle in range(nu):  
    for inner_loop in range(nu - element_in_triangle - 1):  
        print(" ", end="") 
    
    for inner_loop in range(2 * element_in_triangle + 1):  
        print("*", end="")  
    
    print() 


    

#part 2:1

n = int(input("Enter the number of rows: "))
for number_in_loop in range(n):
    for inner_line in range(1, number_in_loop + 1):
        print(inner_line, end="") 

    print("")  