num = input()

number = ""

for i in range(len(num)):
    largest_num = max(num)
    number += largest_num
    num = num.replace(largest_num, "", 1)

print(number)
