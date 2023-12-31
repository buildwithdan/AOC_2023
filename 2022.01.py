line_counter = 0
elf = 1

elf_dict = {}
total = 0

with open("2022_01_data.txt", "r") as data:
  for line in data:
    line_counter += 1
    
    if line.strip() != "" and line_counter < 10000:
      amount = int(line.strip())
      total += amount
      print(f"line counter: {line_counter} and {amount}")
    
    if line.strip() == "" and line_counter < 10000:
      total = 0
      elf += 1
      print(elf)
      
    elf_dict[elf] = total


print(elf_dict)

max_key = max(elf_dict, key=elf_dict.get)
max_value = elf_dict[max_key]
print(f"Max key: {max_key} and Max value: {max_value} ")