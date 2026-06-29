# Day 2: 30 Days of python programming
firstname = 'chanatip'
lastname = 'juntip'
fullname = 'chanatip juntip'
country = 'thailand'
city = 'chaing mai'
age = '20'
year = '2016'
is_married = False
is_true = True
is_light_on = False
person_info = {
    'firstname' : 'chanatip',
    'lastname' : 'juntip',
    'country' : 'thailanf',
    'city' : 'chaing mai'
}

# exercise 2
print(type(firstname), type(lastname), type(fullname), type(country), type(city),
 type(age), type(year), type(is_married), type(is_married), type(is_true), type(is_light_on),
 type(person_info))

print(len(firstname))

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
print(area_of_circle, circum_of_circle)
radius = int(input('Enter radius(meter):'))
print('area of circle is: ', 3.14 * radius ** 2)

first_name = input('Enter your name ')
last_name = input('Enter your last name ')
country_ = input('Enter your country ')
age = input('Enter your age ')