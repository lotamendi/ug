# Programa de Python3 para convertir
# valores enteros a romanos

def printRoman(num:int):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    d = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    u = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    millares = m[num //1000]
    centenas = c[(num % 1000)//100]
    decenas = d[(num % 100)//10]
    unidades = u[num % 10]

    resultado = (millares + centenas + decenas + unidades)
    return resultado

# def printRoman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#     sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
#     i=12
#     while number:
#         div = number // num[i]
#         number %= num[i]

#         while div:
#             print(sym[i], end = "")
#             div -= 1
#         i -= 1

# number = 2023
# print("numero romano:", end = " ")
# printRoman(number)