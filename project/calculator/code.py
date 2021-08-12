'''
all_num = input("(Enter all number by using space)\nEnter all number : ")
#print(all_num)
if(" " in all_num):
    how = int(input("How many space on your text : "))
    while how>0:

        addnum = input("Enter all sign : ")
        how = how - 1
        list1 = []
        atlast = list1.append

#sign =input("Enter all sign by sireal : ")
#print(sign)

rep = all_num.replace(' ',atlast)
print(rep)
'''


#another
'''
count = 0
allnum = []
how = int(input("How many number you want to input : "))
while count<how:
    thenum = int(input("Enter the number : "))
    allnum.append(thenum)
    count = count + 1
last = allnum.replace(',','+')
print('Result is ',last)
'''

#another

