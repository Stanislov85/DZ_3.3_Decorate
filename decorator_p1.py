from datetime import datetime

def logger(func):
    def inner(*args,**kwargs):
        start_time = datetime.now()
        func_name =  func.__name__
        func_args = func(*args,**kwargs)
        with open('log.log','w',encoding = 'utf-8') as fl:
            fl.write(f'Дата: {start_time}\n'
                     f'Имя ф-и: {func_name}\n'
                     f'Аргументы:{args, kwargs}\n'
                     f'Значение: {func_args} '
                     )
        return func_args
    return inner

@logger
def func_1(*args,**kwargs):
    result = 1
    return result
print(func_1(4,5))

