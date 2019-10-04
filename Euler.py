import matplotlib.pyplot as plt

def f(i):
  return -i

initValue = 1
iterations = 30
h = 3.1415 / 6

x = [initValue]
v = [0]

for i in range(iterations):
    x.append(x[i] + h * v[i])
    v.append(v[i] - h * x[i-1])

#for j in range(len(x)):
#   print("%.2f %.2f" %(x[j],v[j]))

plt.plot(x,v)
plt.show()
