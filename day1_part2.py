cleaned = []
line_counter = 0
data_dict = {}

values = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9 
}

with open("day1_data.txt", "r") as data:
    for line in data:
        line_counter += 1
        
        if line_counter < 10:
          digits_in_line = []  # List to store all digits found in the line
          answer = line.find("nine")
        
    print(answer)