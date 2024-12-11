import re

with open("input1.txt", "r") as file:
  data = file.read()


def find_mul(data):
  pattern = r"\bmul\(\d+,\d+\)"
  matches = re.findall(pattern, data)
  
  return matches

def multiply(matches):
  multiple = []
  ex_digits = r"(\d+)"
  for mul in matches:
    digits = re.findall(ex_digits, mul)
    multiple.append(int(digits[0]) * int(digits[1]))
      
  return multiple

def part_one(data):
  matches = find_mul(data)
  multiple = multiply(matches)
  the_sum = sum(multiple)
  return the_sum

#print(part_one(data))

def part_two(data):
  combined_pattern = r"do\(\)|don't\(\)"

  enable_mul = True

  matches = re.finditer(combined_pattern, data)

  if enable_mul:
    find_mul(data)
  for match in matches:
    keyword = match.group()

    print(keyword)

part_two(data)