
import ptvsd

ptvsd.enable_attach(secret='my_secret')

 

first_num = int(raw_input('Enter first number: '))

second_num = int(raw_input('Enter second number: '))

sum = first_num + second_num

print('{0} + {1} = {2}: '.format(first_num, second_num, sum))