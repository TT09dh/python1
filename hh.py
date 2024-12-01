from random import randint
random_min = 0
random_max = 1000
truy = 10
rd = randint(random_min , random_max)

for i in range(truy):
    try:
        a = int(input('введите число от 1 до 100'))
 
        if a == rd:
            print('Вы угадали',(i + 1),'попыток')
            break

    except:
        print('ВВЕДИТЕ ЧИСЛО!')
    print('У вас осталось', truy - (i + 1),'попыток')

    
