# Part one
list_line = []

with open("input1.txt", "r") as file:
  for line in file:
    arr_line = line.strip().split()
    int_line = [int(x) for x in arr_line]
    list_line.append(int_line)


def check_valid(list_line):
  safe = []
  for line in list_line:
    correct_line = True

    for i in range(1, len(line) - 1):
      if not ((line[i-1] < line[i] and line[i] < line[i+1]) or (line[i-1] > line[i] and line[i] > line[i+1])):
        correct_line = False
        break

      if not ((abs(line[i-1] - line[i]) <= 3) and (abs(line[i] - line[i+1]) <= 3)):
        correct_line = False
        break
    
    if correct_line:
      safe.append(line)
  
  return len(safe)

#print(check_valid(list_line))

# Part two

def is_safe_report(report):
    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
    
    if not (increasing or decreasing):
        return False
    
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True
    
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe_report(new_report):
            return True
    
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

print(count_safe_reports(list_line))
