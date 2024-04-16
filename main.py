import re

def is_valid_math_expression(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    # İfade sadece izin verilen karakterleri içeriyor mu kontrol et
    if not re.match(r'^[-+*/()\d\s]+$', expression):
        return False

    # Sadece rakamlar ve operatörler dışındaki tüm karakterleri kaldır
    cleaned_expression = ''.join(char for char in expression if char.isdigit() or char in '+-*/().')

    # Sıfıra bölme hatası var mı kontrol et
    if '/0' in cleaned_expression:
        return False

    return True

def main():
    num_expressions = int(input("Kaç tane örnek ifade girmek istiyorsunuz? "))

    expressions = []
    for i in range(num_expressions):
        expression = input(f"{i+1}. ifadeyi giriniz: ")
        expressions.append(expression)

    for i, expression in enumerate(expressions, start=1):
        result = is_valid_math_expression(expression)
        if result:
            print(f"Girilen ifade {i}. ifade için matematiksel bir ifadedir.")
        else:
            print(f"Girilen ifade {i}. ifade için matematiksel bir ifade değildir veya parantez eşleşmesi hatası veya sıfıra bölme hatası içeriyor.")

if __name__ == "__main__":
    main()