def print_products(*args):
    lst = [i for i in args if type(i) is str and len(i) > 0]
    if len(lst) == 0:
        print('Нет продуктов')
    else:
        for i in range(len(lst)):
            print(str(i + 1) + ')', lst[i])

print_products([4], {}, 1, 2, {'Beegeek'}, '') 

##########################################################
############## DICT ######################################

def info_kwargs(**kwargs):
    dct = {key: value for key, value in kwargs.items()}
    for key, value in sorted(dct.items()):
        print(f'{key}: {value}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
