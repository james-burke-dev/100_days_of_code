with open("day_026/learning/file1.txt") as f1: 
    f1_contents = f1.readlines()
    f1_nums = [int(line) for line in f1_contents]

with open("day_026/learning/file2.txt") as f2: 
    f2_contents = f2.readlines()
    f2_nums = [int(line) for line in f2_contents]

result = [num for num in f1_nums if num in f2_nums]

print(result)