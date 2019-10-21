import cmath  

print('  ')
print('  ')
print('  ')
print('Cubic function calculator')
print('                         by tun0')

print('  ')
print('  ')
print('  ')

a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

print('  ')
print('  ')
print('  ')

d = b*b - 4*a*c

print("discriminant: {}".format(d))

D = cmath.sqrt(d)
A = a * 2

print("discriminant root: {}".format(D))

x1 = (b - D)
x2 = (b + D)

print('  ')
print('  ')
print('  ')

print("X1: {}".format(x1/A))
print("X2: {}".format(x2/A))
