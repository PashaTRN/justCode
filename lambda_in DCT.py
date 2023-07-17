def arithmetic_operation(operation):
    result = {'+': lambda x,y: x + y,
              '-': lambda x,y: x - y,
              '/': lambda x,y: x / y,
              '*': lambda x,y: x * y}
    return result[operation]


add = arithmetic_operation('+') ##############
div = arithmetic_operation('/')
print(add(10, 20))      #######################
print(div(20, 5))
