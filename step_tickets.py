import matplotlib.pyplot as plt

x = ['Регистрация', 'Назначение', 'Выполнение', 'Закрытие']
y = [1, 2, 10, 1]

plt.bar(x, y)
plt.xlabel('Этап обработки')
plt.ylabel('Время (часы)')
plt.title('Среднее время прохождения этапов обработки заявки')
plt.show()