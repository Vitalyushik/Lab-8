from num2words import num2words

employees_num = int(input('Введите количество сотруднников:  '))
summ = 0
distance_l = []
price_l = []
for i in range(employees_num):
    distance = int(input('Введите расстояние для {0}-го сотрудника(км): '.format(i+1)))
    distance_l.append(distance)
for i in range(employees_num):
    price = int(input('Введите тариф за 1 километр {0}-го такси(руб): '.format(i+1)))
    price_l.append(price)
c_distance_l = distance_l[:] 
c_price_l = price_l[:]
index_l_distance = []                  
index_l_price = []
max_distance = 0
for i in range(employees_num):                              
    index = c_distance_l.index(max(c_distance_l))
    index_l_distance.append(index)
    c_distance_l[index] = 0
for i in range(employees_num):
    index = c_price_l.index(min(c_price_l))
    index_l_price.append(index)
    c_price_l[index] = 10**10
print('Лучшее такси для каждого введенного клиента:')    
for i in range(employees_num):
    taxi_num = index_l_price[index_l_distance.index(i)]
    print(taxi_num+1, end=' ')
for i in range(employees_num):
    summ += distance_l[index_l_distance[i]]*price_l[index_l_price[i]]
number = summ
a = ('2', '3', '4')
def convert_currency(number):
    number_str = str(number)
    if number < 100001:
        if len(number_str) >= 2:
            if number_str[-1] == '1':
                if number_str[-2] == '1':
                    return 'рублей'
                else:
                    return 'рубль'
            elif number_str[-1] in a:
                return 'рубля'
            else:
                return 'рублей'
        else:
            if number_str[-1] == '1':
                return 'рубль'
            elif number_str[-1] in a:
                return 'рубля'
            else:
                return 'рублей'
print('')
print('Необходимо заплатить:')
print(summ, convert_currency(summ))
print(num2words(summ, lang='ru'), convert_currency(number))