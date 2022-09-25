# Question 1 :
print("enter the number and 50 determine you're finished")
list = []
while (True):
    x = 0
    z = float(input("enter the number"))
    list.append(z)
    if (z == 50): break
for i in list:
    x += 1
print('length of list is : ', x)


# Question 2 :
def myfunction(a, b, c):
    if a == b or a == c or b == c:
        print('DUPlICATES', )
    else:
        print('AlL UNIQE')


a = input('enter a')
b = input('enter b')
c = input('enter c')
y = myfunction(a, b, c)
print(y)


# Question 3 :
def myfunction2(x, y, z):
    if x < y and z:
        print('The smallest var is :  ', x)
    elif y < x and z:
        print('The smallest var is : ', y)
    else:
        print('The smallest var is : ', z)


x = int(input('enter x'))
y = int(input('enter y'))
z = int(input('enter z'))
t = myfunction2(x, y, z)
print(t)

# Question 4 :


count_positive= 0
count_negative=0

print("enter numbers and 0 determine you're finished")
list = []
while True:
    item = float(input('enter the number  '))
    list.append(item)
    if item == 0: break
    if item > 0:
        count_positive += 1
    else:
        count_negative += 1
sum = sum(list)
avarege = sum / len(list)
print("The sum =  ", sum)
print("The avarege = ", avarege)
print("The positve numbers = ", count_positive)
print("The negative numbers = ", count_negative)
