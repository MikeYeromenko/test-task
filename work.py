import numpy as np
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt


def solve(A):
    optimal_params = {k: 0 for k in 'abc'}
    best_mse = None
    domain = A[A[:, 0].argsort()]

    for i in range(1, len(domain) - 1):
        y_left, y_right = domain[:i, 1], domain[i:, 1]

        mean_left, mean_right = np.mean(y_left), np.mean(y_right)

        loss = np.mean(np.square(np.concatenate([y_left - mean_left, y_right - mean_right])))
        if (best_mse is None or loss < best_mse):
            best_mse = loss
            optimal_params['a'], optimal_params['b'], optimal_params['c'] = mean_left, mean_right, domain[i, 0]

    return optimal_params['a'], optimal_params['b'], optimal_params['c']


# для проверки решения
def create_f(a, b, c):
    return lambda x: a if x < c else b


def calc_loss(domain, f):
    return mse(domain[:, 1], np.array([f(x) for x in domain[:, 0]]))
