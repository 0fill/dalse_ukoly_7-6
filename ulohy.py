import time,math

from numpy import var

print("Hello World!")

def Task_1(list: list)-> float:
    a = list[0]
    for i in list[1:]:
        a *= i
    return a

def Task_2(list: list)-> float:
    list.sort()
    return list[0]

def Task_3(list: list)-> int:
    n = 0
    for i in list:
        if is_prime(i):
            n += 1
    return n

def is_prime(num):
    if num in [0,1,2]:
        return True
    if num % 2 == 0:
        return False
    for k in range(3,int(math.sqrt(num))+1,2):
        if num % k == 0:
            return False 
    return True

def Task_4(list: list, num: float)-> int:
    answer = []
    for i in range(len(list)):
        if list[i] == num:
            answer.append(i)
    for k in answer[::-1]:
        list.pop(k)
    return answer

def Task_5(list_A: list, list_B):
    return list(set(list_A).intersection(set(list_B)))


print(Task_5([1,5,7,8,4,2],[2,5,7,1,3]))