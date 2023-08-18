# номер посылки 89717458

def calculate_score(count_max, data):

    return sum(
        [1 if count_max >= data.count(str(i)) > 0 else 0 for i in range(1, 10)]
    )


if __name__ == '__main__':
    count_max = 2 * int(input())
    data = f'{input()}{input()}{input()}{input()}'

    print(calculate_score(count_max, data))
