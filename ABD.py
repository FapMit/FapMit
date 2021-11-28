import math

def module(a):
    if a<0:
        a = a * (-1)
    return a

cosinus = math.cos(1)
error = 0.001
print('Значение коссинуса: ', cosinus) 
n = 1        
sum = -0.5
function = 1 + sum
while True:
        
    if (module((function-cosinus)/cosinus) <= error):
        break
               
    elif (module((function-cosinus)/cosinus) > error):        
        k = (-1)/(4*(n**2)+6*n+2)
        sum = k*sum
        function += sum
        n += 1
        
print('Значение правой части уравнения: ', function)        