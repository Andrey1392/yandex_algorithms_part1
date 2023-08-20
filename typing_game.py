# номер посылки 89738372

def calculate_score(
        count_max,
        data,
        values='123456789',
        players=2
):

    return sum(
        count_max * players + 1 > data.count(value) > 0 for value in values
    )


if __name__ == '__main__':
    print(calculate_score(
      count_max=int(input()),
      data=f'{input()}{input()}{input()}{input()}',
    ))
