# declaring variables + taking users input
entered_String=(input("Enter the string:"))
VOWELS = "aeiouAEIOU" 
vowels_counter =  0
vowels_String = []

# to print the entered string
print("String is:",entered_String)
# to check if the entered string has vowels

for charecter in entered_String: 
    if charecter in VOWELS:
        # to count the number of vowels in the string
        vowels_counter += 1
     # 
        vowels_String.append(charecter)
    

# to calculate the number of vowels in the string
print("Vowels in the string are:",vowels_String)

if vowels_counter > 0:
    print("Vowels in the string are:", ", ".join(vowels_String))
    print("Number of vowels in the string are:", vowels_counter)
else:
    print("No vowels in the string")

