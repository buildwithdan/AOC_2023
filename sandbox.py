
people_ages = {
    'Alice': 30,
    'Bob': 25,
    'Carol': 27,
    'Dave': 22
}

for item in people_ages:
    print(item)
    

for person in people_ages:
    age = people_ages[person]
    print(f"{person} is {age} years old.")


dict1 = { 1: 30, 2: 40, 3:60 }

print("Just items, and seems to be keys only")
for item in dict1:
  print(item)
  
print("printing key and values from items")
for key, value in dict1.items():
  print(key)
  print(value)
  
print("printing the values")
for item in dict1.values():
  print(item)
  
print("printing the keys")
for item in dict1.keys():
  print(item)
  
  
  
  
  
import re


number_words = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}


# Example string
text = "eight9fhstbssrplmdlncmmqqnklb39ninejz"

# Regular expression pattern for number words
pattern = '|'.join(number_words.keys())

# Find all occurrences of number words
found_words = re.findall(pattern, text, re.IGNORECASE)
print(found_words)