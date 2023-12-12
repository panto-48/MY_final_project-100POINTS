# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

file = open("c:/Users/USER/KUWORK/Final_Project/persons.csv")

type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
    rows.append(row)
rows

file.close()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r))
print(persons)

# add in code for a Database class
# class Database :
#     def __init__(self,persons_data):
#         self.persons_data = persons_data


# add in code for a Table class

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
