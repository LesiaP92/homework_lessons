# homework 2.1.1.
numb = int (input('Введіть число: '))
print('Квадрат числа:', numb ** 2)

# homework 2.1.2.
user_num1 = int (input('Введіть перше число: '))
user_num2 = int (input('Введіть друге число: '))
user_num3 = int (input('Введіть третє число: '))
sums = (user_num1 + user_num2 + user_num3) / 3
print('Середнє:', sums )

# homework 2.1.3.
user_min = int (input('Введіть кількість хвилин: '))
hours = user_min // 60
minutes = user_min % 60
print('Годин:', hours )
print('хвилин:', minutes)

# homework 2.1.4.
price_product = int (input('Ціна товару: '))
discount = int (input('Знижка: '))
discount_price = price_product * discount / 100
final_price = price_product - discount_price
print('Ціна із знижкою: ' , final_price)

#homework 2.1.5.
user_value = int (input('Введіть ціле число: '))
digit_last = user_value % 10
print(digit_last)

#homework 2.1.6.
length = float (input('Введіть довжину: '))
width = float (input('Введіть ширину: '))
p = 2 * (length + width)
print('Периметр', p)

#homework 2.1.7.
us_num = str(input('Введіть 4-х значне число: '))
print(us_num, sep="\n")