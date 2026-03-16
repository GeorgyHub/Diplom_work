import matplotlib.pyplot as plt

x = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн']
y = [82, 85, 88, 91, 89, 92]

plt.plot(x, y, marker='o')
plt.xlabel('Месяц')
plt.ylabel('Процент выполнения')
plt.title('Процент заявок, выполненных в срок (SLA)')
plt.show()