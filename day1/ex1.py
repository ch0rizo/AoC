left_arr, right_arr = [], []

with open("input1.txt", "r") as file:
  for line in file:
    common_arr = line.strip().split()
    left_arr.append(int(common_arr[0]))
    right_arr.append(int(common_arr[1]))

left_arr.sort()
right_arr.sort()

total_count = 0

# To find the difference
for i in range(len(left_arr)):
  total_count += abs(left_arr[i] - right_arr[i])

#print(total_count)

similarity_score = 0

# To get the similarity score
for left_nr in left_arr:
  count = 0
  for right_nr in right_arr:
    if left_nr == right_nr:
      count += 1
  similarity_score += left_nr * count

print(similarity_score)
