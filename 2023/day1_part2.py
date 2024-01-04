cleaned = []
line_counter = 0
data_dict = {}

words_to_replace = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

with open("day1_data.txt", "r") as data:
    for line in data:
      old_line = line
      new_line = line

      if line_counter < 1000000:
        line_counter += 1
        
        for word, replace in words_to_replace.items():
          new_line = new_line.replace(word, str(replace))
        
        print(old_line)
        print(new_line)
        
        digits_in_line = []  # List to store all digits found in the line
        
        for letter in new_line:
            if letter.isdigit():
                number = letter
                print(number)
                digits_in_line.append(number)
                
            # this is to add another digit, if it only had 1
        if len(digits_in_line) == 1:
          number1 = digits_in_line[0]
          digits_in_line.append(number1)
          
        # if more than 2 digits, i need to keep the first and last one.
        
        if len(digits_in_line) > 2:
          number1 = digits_in_line[0]
          number2 = digits_in_line[-1]
          digits_in_line.clear()
          
          digits_in_line.append(number1)
          digits_in_line.append(number2) 
                
        data_dict[line_counter] = digits_in_line  # Store the list of digits with the line number as key
        
        print(f"Line: {line_counter}")

# Print the final data_dict
print(data_dict)


# concat numbers together and then add them back into the dict. replacing the old numbers
for key in data_dict:
  concat_values = ""
  for item in data_dict[key]:
    concat_values += item
    
  data_dict[key] = int(concat_values)
  print(concat_values)
  
print(data_dict)


# adding them all together
total = 0

for value in data_dict.values():
  total += value
  print(total)

print(f"total = {total}")

{1: 89, 2: 36, 3: 55, 4: 72, 5: 21, 6: 34, 7: 11, 8: 35, 9: 32, 10: 53}