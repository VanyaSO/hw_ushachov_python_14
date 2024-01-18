# 1. Напишіть функцію, яка відобразить на екрані такий форматований текст:
# "Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# Bill Gates
def print_text(t1, t2):
    print(f'"Don\'t compare yourself with anyone in this world… \n{t1} you {t2}", you are insulting yourself."')
    print("Bill Gates")
    
print_text("if", "do so")
print("--------------")


# 2. Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними
def even_numbers(start, end):
    while start <= end:
        if start % 2 == 0:
            print(start)
        start += 1
    return start

print(even_numbers(1,9))
print("--------------")



# 3. Напишіть функцію, яка відображає порожній або заповнений квадрат з певного
# символу. Функція приймає як параметри довжину сторони квадрата, символ і змінну логічного типу:
# • якщо вона дорівнює True, квадрат заповнений;
# • якщо — False, квадрат порожній.
def draw_square(width, char, state=True):
    for i in range(width):
        for k in range(width):
            if state:
                print(char, end='')
            else:
                if i == 0 or i == width-1 or k == 0 or k == width-1:
                    print(char, end='')
                else: 
                    print(" ", end='')   
                               
        if i == width-1: 
            print(end='')
        else: 
            print()
        
draw_square(4,"*", False)
print("\n--------------")



# 4. Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри.
def min_number(n1,n2,n3,n4,n5):
    min = n1
    for i in [n2,n3,n4,n5]:
        if i < min:
            min = i
        
    return min
        
print(min_number(3,2,3,4,5))
print("--------------")



# 5. Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі
# діапазону передаються як параметри. Якщо межі діапазону переплутані (наприклад,
# 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.

def multiplication_num(start, end):
    if end < start: 
        start,end = end,start
        
    product = 1
    
    while start < end:
        product *= start
        start += 1
        
    return product
    
print(multiplication_num(5,1))
print("--------------")



# 6. Напишіть функцію, яка рахує кількість цифр у числі. Число передається як
# параметр. З функції потрібно повернути отриману кількість цифр. Наприклад, якщо
# передали 3456, кількість цифр буде 4.
def count_digits(num):
    count = 0
    
    while num:
        num % 10
        num //= 10
        count += 1
        
    return count

print(count_digits(1234567))
print("--------------")


# 7. Напишіть функцію, яка перевіряє, чи є число паліндромом. Число передається як
# параметр. Якщо число є паліндромом, потрібно повернути з функції true, якщо ні — false.

def palindrome(num):
    Number = num
    reverse_num = 0
    
    while num:
        reverse_num = reverse_num * 10 + num % 10
        num //= 10
    
    if reverse_num == Number:
        return "True"
    else:
        return "False"

print(palindrome(1311))
print("--------------")

    

    
    
    