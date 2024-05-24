import re

# Compile a regular expression to find numbers written as digits or words.
search_pattern = re.compile(r'\b(?:\d|zero|one|two|three|four|five|six|seven|eight|nine)\b')

# Dictionary to convert number words to digits.
clean_dict = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

total = 0  # Initialize the sum outside the loop to accumulate the sum across all lines.

try:
    # Read from file and process each line.
    with open('day1_data.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove newline characters and whitespace.
            print("Line read from file:", line)  # Debug print to show the line read
            nums = search_pattern.findall(line)  # Find all numbers in the line.
            print("Numbers found:", nums)  # Debug print to show numbers found

            # Convert words to digits using the dictionary.
            nums = [clean_dict.get(num, num) for num in nums]
            
            # Ensure there are at least two numbers to add.
            if len(nums) >= 2:
                to_add = int(nums[0]) + int(nums[-1])  # Sum the first and last numbers.
                total += to_add  # Accumulate the sum.
                print("Current sum after processing line:", total)  # Debug print to show current sum
except FileNotFoundError:
    print("The file 'day1_data.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")