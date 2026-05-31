
def difference (*args):     #  * - будь яка кільк чисел через ,
    if len(args) == 0:
        return 0
    maximum = max (args)   # найбіл число серед переданих
    minimum = min (args)   # наймен число серед переданих
    result = maximum - minimum
    return round(result, 2)   # округляє result до 2х після ,
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
