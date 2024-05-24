
# ===============TRY 1=====================================
def words_to_digits(data):
    words_to_replace = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for word, digit in reversed(words_to_replace.items()):
        data = data.replace(word, digit)

    return data


def extract_num(data):
  num = []
  for i in data:
    if i.isdigit():
      num.append(i)

  num = int(str(num[0]) + str(num[-1]))
  return num

# ==============TRY 2 =====================================

def replace_number_words(text_list):
    pattern = re.compile('|'.join(words_and_digits.keys()))

    def replace_match(match):
        word = match.group(0)
        return words_to_digits.get(word, word)

    return [pattern.sub(replace_match, text)]


# -------------TESTING--------------------------------
test = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
# # # Example usage
# line = words_to_digits('4nineeightseven2')
# print(line)

# e = extract_num(line)
# print(e)

#### testing
total = 0
for i in test:
  print(i)
  line_x = words_to_digits(i)
  print(line_x)
  num = extract_num(line_x)
  print(num)
  total += num
print(total)

# ----------------------------------------------------

### final
# with open("day1_data.txt", "r") as data:
#   total = 0
#   for line in data:
#     line_x = convert_and_return_string(line)
#     num = extract_num(line_x)
#     total += num

#   print(total)


#not working
53255

## oneight must equal 18, then you'll get the correct answer. It was not a well worded problem.