a = input()
b = input()
if ('@' in a):
    print("Некорректный логин")
else:
    print("Корректный логин")
if ('@' in b):
    print("Корректный резервный адрес")
else:
    print("Некорректный резервный адрес")