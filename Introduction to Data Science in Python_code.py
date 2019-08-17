# Tuples are an immutable data structure (cannot be altered).
x = (1, 'a', 2, 'b')
type(x)


# Lists are a mutable data structure.
x = [1, 'a', 2, 'b']
type(x)

# Use + to concatenate lists.
[1,2] + [3,4] # [1, 2, 3, 4]

# Use * to repeat lists.
[1]*3 # 1 is repeated 3 times. [1, 1, 1]


x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters

#This will return the last element of the string.
x[-1]

# return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.
x[-4:-2]

# slice from the beginning of the string and stopping before the 3rd element.
x[:3]


# SPLITS after ' ' and chooses first value
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)


#Dictionaries
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator


# unpack a sequence into different variables:
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x


# String formatting
sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))


#Read CSV as list
import csv

%precision 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # The first three dictionaries in our list.



# Use set to return the unique values for the number of cylinders the cars in our dataset have.

cylinders = set(d['cyl'] for d in mpg)
cylinders



# --------- Time -----------
import datetime as dt
import time as tm

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow #datetime.datetime(2019, 8, 9, 6, 48, 5, 98282)

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime

# timedelta is a duration expressing the difference between two dates.
delta = dt.timedelta(days = 100) # create a timedelta of 100 days
delta

today = dt.date.today()
today - delta # the date 100 days ago
today > today-delta # compare dates


# --- The Python Programming Language: Objects and map() ---

class Person:
    department = 'School of Information' #a class variable

    def set_name(self, new_name): #a method
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))


# -- The Python Programming Language: Lambda and List Comprehensions --
#  lambda that takes in three parameters and adds the first two.
my_function = lambda a, b, c : a + b
my_function(1, 2, 3) # 3


# Another example:
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))




# --  Python Programming Language: Numerical Python (NumPy) --
import numpy as np


mylist = [1, 2, 3]
x = np.array(mylist)
x


n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30

# linspace returns evenly spaced numbers over a specified interval.
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4


# resize changes the shape and size of array in-place.
o.resize(3, 3)


# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
np.eye(3)

# diag extracts a diagonal or constructs a diagonal array.
np.diag(y)


# repeating lists

np.array([1, 2, 3] * 3) #array([1, 2, 3, 1, 2, 3, 1, 2, 3])
np.repeat([1, 2, 3], 3) # array([1, 1, 1, 2, 2, 2, 3, 3, 3])

# Use vstack to stack arrays in sequence vertically (row wise).
np.vstack([p, 2*p])
# array([[1, 1, 1],
#        [1, 1, 1],
#        [2, 2, 2],
#        [2, 2, 2]])

# Use hstack to stack arrays in sequence horizontally (column wise).
np.hstack([p, 2*p])
# array([[1, 1, 1, 2, 2, 2],
#        [1, 1, 1, 2, 2, 2]])


# ------ Operations ------
print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]

print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]

print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]


x.dot(y) # dot product  1*4 + 2*5 + 3*6

#Transpose
z.T


# argmax and argmin return the index of the maximum and minimum values in the array.
a = np.array([-4, -2, 1, 3, 5])
a.argmax()
a.argmin()




