name = input("What's your name? ")
color = input("What's your favorite color? ")
age = int(input("How old are you today? "))

#print(name, end=" ")
#print("is " + str(age) + " years old", end=" ")
#print("and loves the color " + color + ".", end=" ")

print(name, 'is', age, 'years old and loves the color', color, '.', sep=" ")