import matplotlib.pyplot as plt

x = ['Перед внедрения системы', 'После внедрения системы']
y = [48, 18]

plt.bar(x, y)
plt.title('Среднее время обработки заявки')
plt.xlabel('Этапы внедрения системы')
plt.ylabel('Время (часы)')
plt.show()