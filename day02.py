courses = ['math','phy','chem']

print('art' in courses)

courses[len(courses):] = 'art'

# print(courses)

courses[-1:]=['art','hello']

# print(len(courses))

courses_2 = ['hey','rohan']

courses.extend(courses_2)

courses.pop(0)
nums = [ 34,32,34,3,4,342,4,4,2,4]

nums.reverse()
# print(nums)

# print(sorted(nums))
# print(nums)
# nums.sort()
# print(nums)

str1 = 'hello'

# print(str1)
# str1.upper()
# print(str1)
# print(sorted(courses))
# print(courses)
courses.sort()
# print(courses)



print(courses)

cou_str = ' '.join(courses)
print(cou_str)

cou_list = cou_str.split(' ')
print(cou_list)


dict_1 = {'name':'rohan', 'age': 23, 'mo': 7948342}

print(dict_1.get('mob'))

del dict_1['name']

print(dict_1)



