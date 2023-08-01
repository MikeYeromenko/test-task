import numpy as np
import matplotlib.pyplot as plt

from work import calc_loss, create_f, solve

n = 100
# исходные данные
y = np.random.uniform(0, 3, size=n)
x = np.random.uniform(-10, 10, size=n)
# сортировака данных по x
idx = np.argsort(x)
x = x[idx]
y = y[idx]

A = np.stack([x, y]).T

a = []
b = []
c = []
r = []
for i in range(1, n):
    c.append(x[i])
    a.append(np.mean(y[:i]))
    b.append(np.mean(y[i:]))
    r.append(np.std(y[:i]) + np.std(y[
                                    i:]))  # в сумме std для подмножеств y[:i] и y[i:] сладагемые участвуют с разными "коэфициентами": 1/i и 1/(n - i) соответственно, в отличие от mse, где все слагаемые участвуют с 1/n. Минимум суммы std не совпадает с минимумом mse (строго убедиться в этом можно, взяв производные) и, следовательно, не решает задачу.
idx = np.argmin(r)
print(a[idx], b[idx], c[idx])
a, b, c = a[idx], b[idx], c[idx]
calc_loss(A, create_f(a, b, c))  # mse для данных a, b, c

a, b, c = solve(A)
calc_loss(A, create_f(a, b, c))  # mse для данных a, b, c

plt.plot(x, y, 'ro')
stepx = np.array([x[0], c, c, x[-1]])
stepy = np.array([a, a, b, b])
plt.plot(stepx, stepy, 'g-')
