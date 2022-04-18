import matplotlib.pyplot as plt

values = []
with open('measureData.txt', 'r') as f:
    values = f.read().split('\n')
    #print(values[0])

print(values)
T = 0
with open('settings.txt', 'r') as f:
    s = f.read().split('\n')
    T = float(s[1])
    print(T)

t = [val * T for val in range(0, len(values))]
for st in range(0, len(values)):
    print('{:.03f} = {:.3f}'.format(t[st], float(values[st])))

plt.plot(t, values)
ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.show()
