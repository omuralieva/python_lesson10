# b = 'Hello world!'
# food = ['манты', 'борщ', 'пирог', 'шорпо']
#
# for i in food:
#     if i == 'борщ':
#         print('я не ем борщ')
#         break
#     print('отлично, вкусные' + i)
# else:
#     print('классно, что не было борща')
#
# print('ужин был шикрным')
#
# fib = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for i in range(len(fib)):
#     print(i, fib[i])
#
# ints = [1, 2, 3, 4, 5]
# strings = ['1', '2', '3', '4', '5']
#
# for i in ints:
#     for e in strings:
#         print(str(i)+e)
#
# for i in b:
#     if i != '!':
#         print(i)
# else:
#     print('! знака не существует')

# x = 3
# for i in range(1, 11):
#     print(x, '*', i, '=', x * i)
#
# def addition(number):
#     number = number + 1
#     x = 0
#     for i in range(number):
#         x = x + i
#     print(x)
#
# y = [1, 2, 3, 4, 5]
# x = 1
# for i in y:
#     x *= i
# print(x)

# a = 100
# a += 1
# for i in range(a):
#     print(i)
#
# a = 0
# while a < 100:
#     a += 1
#     print(a)
#
# a = 33
# a += 1
# for i in range(11, a):
#     print(i)
#
# a = 10
# while a < 33:
#     a += 1
#     print(a)
#
# a = 100
# a += 1
# for i in range(a):
#     if i % 2 == 0:
#         print(i)

a = 0
while a < 100:
    a += 1
    if a % 2 == 0:
        print(a)

y = 100
x = 1
for i in range(1, 100):
    x *= i
print(x)

a = 0
x = 1
while a < 100:
    a += 1
    x *= a
print(x)

obj = {'Минск': 'Беларусь', 'Москва': 'Россия', 'Киев': 'Украина'}
for key in obj:
    print(key, '- это', obj[key])

if __name__ == '__main__':
    pass
# print(addition(5))