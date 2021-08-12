'''
import random
toatlalman = int(input("How many name you want to input : "))
allname = []
count = 0
print("Input total is =",toatlalman)
while count<toatlalman:
    nowinputname = input("Enter the name : ")
    allname.append(nowinputname)
    count+=1
    print("All name = ",allname)

    #print(count)
lotari = random.randint(allname)
print("Winner is =",lotari)
'''

'''
import random
toatlalman = int(input("How many name you want to input : "))
allname = []
count = 0
print("Input total is =",toatlalman)
while count<toatlalman:
    nowinputname = input("Enter the name : ")
    allname.append(nowinputname)
    count+=1
    print("All name = ",allname)

    #print(count)
lotari = random.randint(0,len(allname)-1)
print(lotari)
print("Winner is =  "+str(lotari+1)+". "+allname[lotari])
'''


'''
#input by for loop
count_input = 0
namelist = []
howmany = int(input("How many name you want to input : "))
for new in range(0,howmany):
    subject = input("Enter the name : ")
    #"(",count_input,")",
    #count_input = count_input + 1
    howmany = howmany + 1
    namelist.append(subject)
print(namelist)
#print("Total input = ",howmany)
'''
'''
result = []
inputnum = input("Enter the number : ")
if inputnum % 3==0 and inputnum%5==0:
    result.append(inputnum)
'''
import random
toatlalman = int(input("How many name you want to input : "))
allname = []
count = 0
print("Input total is =",toatlalman)
while count<toatlalman:
    nowinputname = input("Enter the name : ")
    allname.append(nowinputname)
    count+=1
    print("All name = ",allname)

    #print(count)
lotari = random.randint(0,len(allname)-1)
print(lotari)
print("Winner is =  "+str(lotari+1)+". "+allname[lotari])
