persons = [
    ['eunryong', 'Jinju', 'FrontEnd'],
    ['Lee', 'Seoul', 'BackEnd'],
]
print(persons[0][0])
 
for person in persons:
    print(person[0]+','+person[1]+','+person[2])
 
person = ['eunryong', 'Jinju', 'FrontEnd']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)
 
name, address, interest = ['eunryong', 'Jinju', 'FrontEnd']
print(name, address, interest)
 
for name, address, interest in persons:
    print(name+','+address+','+interest)