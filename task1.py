NOTATION = 16
NOTATION_DIGITS = "0123456789ABCDEF"
def decimal_to_other(decimal):
    result = ""
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        remainder = decimal % NOTATION
        result = NOTATION_DIGITS[remainder] + result
        decimal //= NOTATION
    
    return result

number = int(input("Введите целое число: "))
hexadecimal_number = decimal_to_other(number)

print("Шестнадцатеричное представление числа:", hexadecimal_number)
print("Проверка с использованием функции hex:", hex(number))