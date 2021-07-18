import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(messsage)s')
# logging.disable(logging.CRITICAL)
# logging.basicConfig( level=logging.DEBUG)
logging.debug('Start of program')
def factorial(n):
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is {i}, total is {total}')
    return total


print(factorial(5))
logging.debug('End of program')