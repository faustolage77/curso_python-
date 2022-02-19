num_1 = input('Digite um número: ')
num_2 = input('Digite outro número ')

#  isnumeric , isdigit e isdecimal 

try:
   num_1 = float(num_1)
   num_2 = float(num_2)

   print(num_1 + num_2)

except:
    print('ERROR')