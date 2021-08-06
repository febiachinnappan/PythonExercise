#1.	Write a Python program which accepts a sequence
# of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Enter the numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#2.	Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file : " + repr(f_extns[-1]))

#3.	Write a Python program to display the first and last elements from any list.
a = [1, 2, 3, 4]
print("first element is" ,a[0])
print("last element is", a[-1])

#4.	Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.
def new_string(str):
  if len(str) >= 2 and str[:2] == "ls":
    return str
  return "ls" + str

print(new_string("Hello"))
print(new_string("World"))

#5.	Write a Python program to check whether a specified value is contained in a group of values.
def group_member(data, n):
   for value in data:
       if n == value:
           return True
   return False
print(group_member([1, 2, 3, 4], 3))
print(group_member([5, 6, 7], -1))

#6.	Write a Python program to print out a set containing all the colors from color_list_1 which are not
# present in color_list_2.
color_list1 = set(["White", "Black", "Red"])
color_list2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list1)
print(color_list2)
print("\nDifferent of color_list_1 and color_list_2:")
print(color_list1.difference(color_list2))
print("\nDifferent of color_list_2 and color_list_1:")
print(color_list2.difference(color_list1))

#7.	Write a Python program to remove and print every third number from a list of numbers until the
# list becomes empty.
def remove_nums(int_list):
  position = 3 - 1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [1,2,3,4,5,6,7,8,9]
remove_nums(nums)

#8.	Write a Python program to count the number of characters (character frequency) in a string.
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('febiachinnappan'))

#9.	Write a Python function that takes two lists and returns True if they have at least one common member
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

#10.	Write a Python program that accepts a string and calculate the number of digits and letters.
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
