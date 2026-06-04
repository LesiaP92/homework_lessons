def is_even(number):
    if (number & 1) == 0:
        """ умова яка порівнює число з 1 на рівні бітів &.
        дивит. чи в кінці число парне чи ні, та перевіряємо чи дорівнює 0,якщо так то істина."""
        return  True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
