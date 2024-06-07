import time

print("Hello World!")

def Task_1(list: list)-> float:
    a = list[0]
    for i in list[1:]:
        a *= i
    return a

def Task_2(list: list)-> float:
    list.sort()
    return list[0]

def Task_2_1(list:list)-> float:
    a = list[0]
    for i in list[1:]:
        if a<i:
            a = i
    return a
num = 80000
test = [1,5,4,8,-7,58,12,5,4,1,-58,8,4]
t = time.time()
for _ in range(num):
    Task_2(test)
t = time.time()-t
print (t,end= ", ")

t = time.time()
for _ in range(num):
    Task_2_1(test)
t = time.time()-t
print(t)
    