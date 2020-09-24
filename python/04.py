import datetime

def calcula_decorator(function):
    def calcula():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return calcula

@calcula_decorator
def my_function():
    number1 = 19999999
    number2 = 6925262
    number3 = 322662626
    number4 = 55215425
    result = number1 + number2 + number3 + number4
    print(result)


my_function()

