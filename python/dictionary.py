person = {'name':'eunryong', 'address':'Jinju', 'interest':'FrontEnd'}
print(person['name'])
 
for key in person:
    print(key, person[key])

persons = [
    {'name':'eunryong', 'address':'Seoul', 'interest':'FrontEnd'},
    {'name':'Lee', 'address':'Seoul', 'interest':'BackEnd'},
]
for person in persons:
    for key in person:
        print(key, ':', person[key])
        print('-----------------')