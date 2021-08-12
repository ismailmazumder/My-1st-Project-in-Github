#word count
'''
a = input("Enter the sentence : ")
count = 0
for trans in a:
    if " " in a:
        count = count + 1
print("Total word is = ",count)
'''
'''
#text = input("Enter the sentence : ")
text = input("Enter the sentence : ")
vowel = ['a','e','i','o','u']
count = 0
for new in text:
    if new in vowel:
        count = count + 1
print("Total vowel is : ",count)




'''
'''
def vowelcheck(sentence):
    count = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for new in sentence:
        if new in vowel:
            count = count + 1
    return count
print(vowelcheck("How are you?"))
#sentence = 'How are you?'
'''
'''
def remove_duplicate(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

numbers = [22,11,3,1,4,5,5,2,2,11,66,89]
print(remove_duplicate(numbers))
'''
'''
list1 = ['Ismail','Mazumder','Mazumder','Sadia','Ismail','Ismail','Ismail','Mazumder']
unique = []

for new in list1:
    if (new not  in unique):
        unique.append(new)

print(unique)
'''
'''
import random
count = int(input("Total man = "))
name = ['Ismail','Sadia']
random_num = random.randint(0,count)
#print(random_num)
'''

'''
import random
while True:
    input("\nPress Enter To Toss\n")
    random_num = random.randint(0,10)
    if random_num%2==0:
        print("It's Head")
    else:
        print("It's Tell")
'''
