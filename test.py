import main as m
import random
import collections

# создадим списки с входными str для различных случаев (10 проверок), а также ожидаемым результатом для них:
list_objects = [None for i in range(0, 9)]
list_rule = [None for i in range(0, 9)]
list_exp_error = [None for i in range(0, 9)]
list_exp_result = [None for i in range(0, 9)]

# тестирование сортировки #1
list_objects[0] = ''.join(random.choice('КЗС') for x in range(0, 50))
list_rule[0] = set(list_objects[0])
list_exp_error[0] = 0

# тестирование сортировки #2
list_objects[1] = ''.join(random.choice('КзСБч') for x in range(0, 100))
list_rule[1] = set(list_objects[1])
list_exp_error[1] = 0

# тестирование сортировки #3
list_objects[2] = ''.join(random.choice('КзСrGb') for x in range(0, 5000))
list_rule[2] = set(list_objects[2])
list_exp_error[2] = 0

# тестирование проверки ввода #1
list_objects[3] = ' '
list_rule[3] = ''
list_exp_error[3] = 1
list_exp_result[3] = 'Заполните поля "1" и "2"'

# тестирование проверки ввода #2
list_objects[4] = ' '
list_rule[4] = ' '
list_exp_error[4] = 1
list_exp_result[4] = 'Заполните поля "1" и "2"'

# тестирование проверки ввода #3
list_objects[5] = ''.join(random.choice('КЗС12#$_%^&*') for x in range(0, 50))
list_rule[5] = 'КЗС12#$_%^&*'
list_exp_error[5] = 1
list_exp_result[5] = 'Введите буквенные метки объектов!'

# тестирование проверки ввода #4
list_objects[6] = ''.join(random.choice('КЗС12#$_%^&*') for x in range(0, 50))
list_rule[6] = 'КЗС'
list_exp_error[6] = 1
list_exp_result[6] = 'Введите буквенные метки объектов!'

# тестирование проверки ввода #5
list_objects[7] = ''.join(random.choice('КЗС') for x in range(0, 50))
list_rule[7] = ' '.join(random.choice(['КЗ', 'ЗС', 'КС']))
list_exp_error[7] = 1
list_exp_result[7] = '"Порядок сортировки" должен содержать одну метку каждого типа!'

# тестирование проверки ввода #6
list_objects[8] = ''.join(random.choice('КЗС') for x in range(0, 50))
list_rule[8] = ' '.join(random.choice(['КЗСК', 'ЗСКС', 'ККСЗ']))
list_exp_error[8] = 1
list_exp_result[8] = 'Проверьте "порядок сортировки"! (метки не должны повторяться)'

for i in range(0, len(list_objects)):
    error_main, text_main = m.main(list_objects[i], list_rule[i])

    if error_main == 0:
        counter_in = str(collections.Counter(list_objects[i])).replace('Counter', '')
        counter_res = str(collections.Counter(text_main)).replace('Counter', '')
        print(
            'Проверка №%d' %i,
            '\n\tВходные объекты:', '"' + list_objects[i] + '"',  '\n\tПравило сортировки:', str(list_rule[i]),
            '\nВывод функции:\n\t' + 'Ошибка =', str(error_main), counter_res, str(text_main),
            '\nОжидаемый результат:\n\t' + 'Ошибка =', str(list_exp_error[i]), ', Результат:',  counter_in, '\n'
        )

    if error_main == 1:
        print(
            'Проверка №%d' % i,
            '\n\tВходные объекты:', '"' + list_objects[i] + '"', '\n\tПравило сортировки:', '"' + str(list_rule[i]) + '"',
            '\nВывод функции:\n\t' + 'Ошибка =', str(error_main) + ',', str(text_main),
            '\nОжидаемый результат:\n\t' + 'Ошибка =', str(list_exp_error[i]) + ',', list_exp_result[i], '\n'
        )