import random
import sys

# students = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6', 'Name7', 'Name8', 'Name9', 'Name10']
students = ['Aline', 'Andrew', 'Damjan', 'Doro', 'Duc Hiep', 'Erik', 'Friedrich', 'Maria', 'Mark', 'Raul', 'Sebastian', 'Sven-Torben', 'Victor', 'Wolfram']
group_size = int(sys.argv[1])
number_of_groups = int(len(students)/group_size)
    
random.shuffle(students)

all_groups = []
for index in range(number_of_groups):
    group = students[index::number_of_groups]
    all_groups.append(group)
    
for index, group in enumerate(all_groups):
    print(f"Room {index+1}: {' / '.join(group)}") #\n")
