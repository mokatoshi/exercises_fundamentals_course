first_num = int(input())
second_num = int(input())
third_num = int(input())

if first_num > second_num and first_num > third_num:
    print(f"{first_num}")
elif second_num > first_num and second_num > third_num:
    print(f"{second_num}")
else:
    print(f"{third_num}")