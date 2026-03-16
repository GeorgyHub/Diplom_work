import matplotlib.pyplot as plt

x = ['ПО', 'Оборудование', 'Сеть', 'Доступ', 'Другое']
y = [43, 27, 20, 15, 10]

plt.bar(x, y)
plt.xlabel('Категория')
plt.ylabel('Количество заявок')
plt.title('Распределение заявок по категориям')
plt.show()