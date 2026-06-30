# 1-3
age = int(20)
my_height = float(175)
x = complex(1, 2)
# 4
base = input('Enter base: ')
height = input('Enter height: ')
print('The area of the triangle is', 0.5 *float(base) * float(height))
# 5
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
print('The perimeter of the triangle is', float(side_a) + float(side_b) + float(side_c))
# 6
length = input('Enter length: ')
width = input('Enter width: ')
print('area is', float(length) * float(width), 'perimeter is', 2 * (float(length) + float(width)))
# 7
radius = input('Enter radius: ')
print('area is', 3.14 * float(radius) ** 2, 'circumference is', 2 * 3.14 * float(radius))
# 8
print('Slop of y = 2x -2 is 2')
x = 2 / 2
y = -2
slop1 = 2
print('x-intercept is', x, 'x-intercept is', y, 'slop is', slop1)
# 9
slop2 = 6 - 2 / 10 - 2
print('slop is', slop2, 'Euclidean distance is', (10 - 2) ** 2 + (6 - 2) ** 2)
# 10
print('different between slop #8 and #9', slop1 - slop2)
# 14
print('jargon' in 'I hope this course is not full of jargon')
# 15
print('on' in 'dragon' and 'on' in 'python')
# 16
# print(str(float('python'))) # can not turn float to str
# 17
num = input('Enter your number:')
print(int(num) % 2)
# 18
print(7 // 3)
# 19
print('10' == 10)
# 20
print(int(9.8) == 10)
# 21
hours = int(input('Enter hours: '))
rph = int(input('Enter rate per hour'))
print('Your weakly earning is', hours * rph)
# 22
y_age = int(input('Enter your age:'))
print('you have live your life for', y_age * 365 * 24 * 60 * 60, 'seconds')
# 23
print('1 1 1 1 1')
print('2 1 2 4 8')
print('4 1 4 16 64')
print('5 1 5 25 125')