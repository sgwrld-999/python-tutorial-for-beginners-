list_num = ['a', 'b', 'c']

data_list = ['Siddhant', 'Placed', 'Secured internship','remote',60000,'remote']

empyt_list = []

print("Siddhant is unplaced" in empyt_list)

print(data_list[0])
print(data_list[-2])

print(data_list.index('Siddhant'))

print(data_list[0:3])
print(data_list[1:3])

print(data_list[-3:0])

print(len(data_list))

# adding the values in the list
data_list.append("placed at 15LPA")
print(data_list)

data_list += ['Placed at rolls royce'] # the brackets must be there other each character will be added individually in the list
print(data_list)
data_list += 'Placed at rolls royce'
print(data_list)


data_list.extend(['Publised 5 ranked papers'])
print(data_list)

data_list.extend(list_num)

list_num.insert(0,'inserted at 0')


print(list_num)
list_num[1:1] = ['f','6'] # this will insert
print(list_num)
list_num[1:3] = ['asdf','asdfsafdas'] # this replaces
print(list_num)

list_num.remove('a')
print(list_num)
list_num.pop()
print(list_num)

del list_num[0]
print(list_num)

list_num.sort()
print(list_num)

list_num.reverse()
print(list_num)

print(sorted(list_num))

list_num_copy = list_num.copy()

# tuples

tuple_num = tuple(list_num)
print(tuple_num)