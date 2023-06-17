from fractions import Fraction

def simplify_fraction(numerator, denominator):
    
    def get_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    greatest_common_divisor = get_common_divisor(numerator, denominator)

    numerator //= greatest_common_divisor
    denominator //= greatest_common_divisor

    return numerator, denominator

def get_data(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))
    
    return numerator1, denominator1, numerator2, denominator2

def create_printable_fraction(product_numerator, product_denominator):
    if product_denominator == 1:
        product_fraction = str(product_numerator)
    else:   
        product_fraction = f"{product_numerator}/{product_denominator}"

    return product_fraction

def add_fractions(fraction1, fraction2):
    numerator1, denominator1, numerator2, denominator2 = get_data(fraction1, fraction2)
    
    common_denominator = denominator1 * denominator2
    
    numerator1 *= denominator2
    numerator2 *= denominator1

    sum_numerators = numerator1 + numerator2

    sum_numerator, sum_denominator = simplify_fraction(sum_numerators, common_denominator)

    sum_fraction = create_printable_fraction(sum_numerator, sum_denominator)

    return sum_fraction

def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1, numerator2, denominator2 = get_data(fraction1, fraction2)

    multiply_numerator = numerator1 * numerator2
    multiply_denominator = denominator1 * denominator2

    multiply_numerator, multiply_denominator = simplify_fraction(multiply_numerator, multiply_denominator)

    multiply_fraction = create_printable_fraction(multiply_numerator, multiply_denominator)
    return multiply_fraction

def operate_fractions(fraction1, fraction2):
    numerator1, denominator1, numerator2, denominator2 = get_data(fraction1, fraction2)

    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2

    return sum_result, product_result

fraction1 = input('Введите первую дробь (в формате a/b): ')
fraction2 = input('Введите вторую дробь (в формате a/b): ')

sum_fraction = add_fractions(fraction1, fraction2)
product_fraction = multiply_fractions(fraction1, fraction2)

print(fraction1, '+', fraction2, '=', sum_fraction)
print(fraction1, '*', fraction2, '=', product_fraction)
#fraction
sum_result, product_result = operate_fractions(fraction1, fraction2)

print("Сумма дробей (fraction):", sum_result)
print("Произведение дробей(fraction):", product_result)
