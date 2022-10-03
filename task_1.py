#дано. Два списка чисел.
# Найти числа, которые входят как в первый, так и во второй список.
#вывести их в порядке возрастания
list1=[8,2,6]
list2=[8,3,6]
list3=[]
for i in list1:
    for j in list2:
       if i == j:
            list3.append(i)
print(list3)
list3.sort()
print(list3)
