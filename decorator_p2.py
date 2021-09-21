from datetime import datetime

link = 'test/log.log'

def logger(link):
    def output(func):
        def inner(*args,**kwargs):
            start_time = datetime.now()
            func_name =  func.__name__
            func_args = func(*args,**kwargs)
            with open(link,'w',encoding = 'utf-8') as fl:
                fl.write(f'Дата: {start_time}\n'
                         f'Имя ф-и: {func_name}\n'
                         f'Аргументы:{args, kwargs}\n'
                         f'Значение: {func_args} '
                         )
            return func_args
        return inner
    return output

@logger(link)
def func_1(*args,**kwargs):
    result = 1
    return result
print(func_1())

