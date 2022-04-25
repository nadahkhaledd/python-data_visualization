import matplotlib.pyplot as plt

pLanguages = 'Python', 'C++', 'Java', 'Javascript', 'Ruby', 'R'
sizes = [33, 52, 62, 48, 12, 17]

plt.pie(sizes, labels=pLanguages, autopct='%1.1f%%')
plt.axis('equal')
plt.show()