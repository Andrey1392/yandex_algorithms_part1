# номер посылки 89657307

def calculate_score(k, data):
    GAME_WIN_SCORE = 1

    test_values = [str(v) for v in range(1, 10)]

    round_scores = []
    for v in test_values:
        data_length_old = len(data)
        data = data.replace(v, '')
        data_length_new = len(data)
        if k >= data_length_old - data_length_new > 0:
            round_scores.append(GAME_WIN_SCORE)
        data_length_old = data_length_new
    return sum(round_scores)


def main():
    k = 2 * int(input())
    data = f'{input()}{input()}{input()}{input()}'

    print(calculate_score(k, data))


if __name__ == '__main__':
    main()
