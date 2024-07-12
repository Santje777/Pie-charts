import matplotlib.pyplot as plt

languages = ['French', "English", "Spanish", "Portuguese", "Greek", "Chinese"]
counts = [10, 40, 30, 20, 5, 66]

plt.pie(counts, labels=languages)

plt.ylabel('Speakers')
plt.title('Native speakers in the classroom')
plt.legend(counts)

plt.show()


condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]

plt.pie(days, labels=condition)
plt.title('Weather in Lisbon')
plt.legend(days)
plt.show()