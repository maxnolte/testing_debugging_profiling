

def find_maximum(series):
    maxima = []

    for i, n in enumerate(series):
        if i == len(series) - 1:
            if n > series[i - 1]:
                maxima.append(i)
        elif n > series[i + 1]:
            if i == 0:
                maxima.append(i)
            elif n > series[i - 1]:
                maxima.append(i)
    return maxima

test_series = [3, 2, 2, 2, 3, 7, 4, 3, 7, 3, 8, 10, 8, 11]
print test_series
print find_maximum(test_series)
