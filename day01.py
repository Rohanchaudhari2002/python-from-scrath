# write 5 variables and print with f-string label
name = 'Rohan'
age = 23
cgpa= 7
college  = "IIT Palakkad"
is_mtech  = True

print(f'my name is {name}. my age is {age}, I am in {college} my cgpa is {cgpa}. Am i doing MTech -> {is_mtech}')

#intput any str and print len, uppercase, first 3 char. last 3 chars, reverse
str1 = input("Enter the string: ")

# print(dir(str1))
rev_str = reversed(str1)
print(f'len: {len(str1)}.\nuppercase: {str1.upper()}.\nFirst 3 char: {str1[:3]}\nlast 3 char: {str1[-3:]}\nreverse: {str1[-1::-1]}')


# Temperature converet. F = C * 9/5 +32
C = input("Enter the C value: ")
F = ((int(C) * (9/5)) +32)
print(f"value of F is {F} when C is {C}")
