todos=open('todos.txt', 'a')
print("первая строка", file=todos)
print("вторая строка", file=todos)
todos.close()


tasks = open('todos.txt')
for str in tasks:
    print(str, end="")
tasks.close()
with open()
    for str in tasks:
    print(str, end="")
print("Тут файл уже закрыт")
