#во входной стоке записывается последовательность чисел через пробел.
# Для каждого числа выведите слово "yes" в новой строке, если это число ранее встречалось в последовательности
#или "no", если не встречалось 
list_inp=(input('введите числа через пробел: '))
list=[]
list=list_inp.split(' ')
list=[int (list_inp) for list_inp in list] 
print('входная строка: ', list)
i=1
j=i-1
print ("no")
for e in list:
    if list[i] in list[0:i-1]:
        print ("yes")
        
    else:
        print ("no")
    i=i+1


