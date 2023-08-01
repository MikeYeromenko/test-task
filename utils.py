import numpy as np
import matplotlib.pyplot as plt


from schemas import PointsArray, MyResponse, Point
from work import calc_loss, create_f, solve


def worker(array: PointsArray) -> MyResponse:
    matrix = np.array([[item.x, item.y] for item in array.array])
    x = matrix[:, 0]
    y = matrix[:, 1]
    n = len(x)

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
        r.append(np.std(y[:i]) + np.std(y[i:]))
    # в сумме std для подмножеств y[:i] и y[i:] сладагемые участвуют с разными "коэфициентами": 1/i и 1/(n - i)
    # соответственно, в отличие от mse, где все слагаемые участвуют с 1/n. Минимум суммы std не совпадает с
    # минимумом mse (строго убедиться в этом можно, взяв производные) и, следовательно, не решает задачу.
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
    result = MyResponse(a=a, b=b, c=c)
    return result


def create_array(length: int) -> PointsArray:
    y = np.random.uniform(0, 3, size=length)
    x = np.random.uniform(-10, 10, size=length)
    return PointsArray(array=[Point(x=x[i], y=y[i]) for i in range(length)])
