mydict={
    'Apple' : 'Red',
    'Banana' : 'Yellow',
    'Mango' : 'Orange',
    'Grapes' : 'Green'
    }
print(mydict)
n=input('enter the key you want to delete : ')
try:
    del mydict[n]
    print(mydict)
except KeyError:
    print('Key doesnt exist')
    
