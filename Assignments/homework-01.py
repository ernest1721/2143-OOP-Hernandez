'''python
"""
Name: Ernest Hernandez
Email: ernest1721@yahoo.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan @ 11:00 a.m.
"""

#A
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

#B
x = [3, 1, 2, 1, 5, 1, 1, 7]
def remove_all(el, lst):
  """
  Removes all instances of el from lst. 
  Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
  Usage: remove_all(1, x)
  Would result in: [3, 2, 5, 7]
  """
  while el in lst:
    lst.remove(el)
    
remove_all(1, x)
print(x)

#C
lst = [1, 2, 4, 2, 1]

def add_this_many(x, y, lst):
  """
  Adds y to the end of lst the number of times x occurs in lst. 
  Given: lst = [1, 2, 4, 2, 1]
  Usage: add_this_many(1, 5, lst)
  Results in: [1, 2, 4, 2, 1, 5, 5]
  """
  count = 0
  #counts how many times x in in lst
  for el in lst:
    if el == x:
      count += 1
  #adds y to lst based on count taken from for loop above
  while count > 0:
    lst.append(y)
    count -= 1

add_this_many(1, 5, lst)
print(lst)

#D
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: 1, 2, 3]

print(a[:])
# Prints: 3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

#E
x = [3, 2, 4, 5, 1]
def reverse(lst):
  """
  Reverses lst in place. 
  Given: x = [3, 2, 4, 5, 1] 
  Usage: reverse(x)
  Results: [1, 5, 4, 2, 3]
  """
  
  #i = variable for containing element "i" in "lst"
  #n = variable used to regulate swap
  i, n = 0, len(lst)
  while i < n / 2:
    temp = lst[i]
    lst[i] = lst[n - 1 - i]
    lst [n - 1 -i] = temp
    i += 1

reverse(x)
print(x)

#F
x = [1, 2, 3, 4, 5]
print(x)
def rotate(lst, k):
  """
  Return a new list, with the same elements of lst, rotated to the right k.
  Given: x = [1, 2, 3, 4, 5]
  Usage: rotate(x, 3)
  Results: [3, 4, 5, 1, 2]
  """
  n = len(lst)
  #rot is a lst containing 'n' number of 0's
  rot = [0] * n
  for i in range(n):
    #moves element 'k' number of spaces while staying in range of list
    j = (i + k) % n
    #fills rot with value calculated from above
    rot[j] = lst[i]
  return rot

print(rotate(x, 3))

      
#H
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])
# Prints: 3

superbowls['peyton manning'] = 1
print(superbowls)
# Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}

superbowls['joe flacco'] = 1
print(superbowls)
# Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe montana': 4, 'tom brady': 3, 'joe flacco': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'tom brady': 3, 'joe flacco': 1, ('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe montana': 4}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {3: 'cat', 'tom brady': 3, 'joe flacco': 1, ('eli manning', 'giants'): 5, 'peyton manning': 1, 'joe montana': 4}

#superbowls[['steelers', '49ers']] = 11
#print(superbowls)
#Prints: "TypeError: unhashable type: 'list'"

#I
d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
def replace_all(d, x, y):
  """
  Replaces all values of x with y. 
  Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
  Usage: replace_all(d,3,1)
  Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
  """
  for k in d.keys():
    #checks for 'x' in current instance of 'd'
    if d[k] == x:
      d[k] = y
      #do if current instance of 'd' is a dictionary
    elif type(d[k]) is dict:
      replace_all(d[k], x, y)

replace_all(d, 3, 1)
print(d)

#J
d = {1:2, 2:3, 3:2, 4:3}
def rm(d, x):
  """
  Removes all pairs with value x. 
  Given:  d = {1:2, 2:3, 3:2, 4:3}
  Usage:  rm(d,2)
  Results: {2:3, 4:3}
  """
  #empty list
  rem_lst = []
  for k in d.keys():
    #checks for 'x' in 'd'
    if d[k] == x:
      #adds current element of d to 'rem_lst'
      rem_lst.append(k)
  #deletes all elements of 'rem_lst'
  for k in rem_lst:
    del d[k]

rm(d, 2)
print(d)
'''
