# Create a script that 

message = input("Enter a message ")


print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalize:", message.capitalize())
print("Title case:", message.title())

# Separate the String and Present the individual words as a list

words = message.split()
print("Words:", words)

# Print the alphabetical  first and last  words from the User's input

sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])

print(ord('T'))
print(ord('i'))
print(ord('a'))
print(ord('t'))
print(ord('M'))