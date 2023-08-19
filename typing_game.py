# номер посылки 89721205

def calculate_score(
        count_max,
        data,
        values=('1', '2', '3', '4', '5', '6', '7', '8', '9',),
        players=2
):

    return sum(
        [count_max * players >= data.count(value) > 0 for value in values]
    )


if __name__ == '__main__':
    print(
        calculate_score(count_max=int(input()),
                        data=f'{input()}{input()}{input()}{input()}'
                        )
        )
