import numpy as np


def reshape_rows(values, width):
    arr = np.asarray(values, dtype=float)
    # Пустой результат, если длина не делится на width нацело
    if width <= 0 or arr.size == 0 or arr.size % width != 0:
        return []
    return arr.reshape(-1, width).tolist()


def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    rows = np.asarray(rows, dtype=int)
    columns = np.asarray(columns, dtype=int)
    # np.ix_ выбирает строки и столбцы в заданном порядке
    return arr[np.ix_(rows, columns)].tolist()


def column_means(matrix):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    # Среднее по каждому столбцу, округление до шести знаков
    return np.round(arr.mean(axis=0), 6).tolist()


def column_range(matrix, column):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return 0.0
    col = arr[:, column]
    # Размах: наибольшее минус наименьшее
    return round(float(col.max() - col.min()), 6)


# Тесты: запускаются только при прямом запуске файла
if __name__ == "__main__":
    print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))  # [[12.0, 14.5, 11.0], [13.0, 15.5, 10.5]]
    print(reshape_rows([1, 2, 3, 4], 2))                     # [[1.0, 2.0], [3.0, 4.0]]
    print(reshape_rows([1, 2, 3], 2))                        # []
    print(reshape_rows([], 3))                               # []
    print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 2], [1, 2]))  # [[2.0, 3.0], [8.0, 9.0]]
    print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1], [0]))        # [[4.0]]
    print(block([[1, 2], [3, 4]], [1, 0], [1, 0]))           # [[4.0, 3.0], [2.0, 1.0]]
    print(column_means([[1, 2], [3, 4], [5, 6]]))            # [3.0, 4.0]
    print(column_means([[1.5, 2.5]]))                        # [1.5, 2.5]
    print(column_means([]))                                  # []
    print(column_range([[1, 2], [5, 7]], 1))                 # 5.0
    print(column_range([[3, 3], [3, 3]], 0))                 # 0.0
    print(column_range([], 0))                               # 0.0
