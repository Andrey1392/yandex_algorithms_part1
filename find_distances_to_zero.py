# номер посылки 89721121


def distances_to_nearest_zero(numbers, zero_value='0'):

    street_length = len(numbers)
    distances = [0] * street_length
    zeroes = [
        number_index for number_index, value in enumerate(numbers) if value == zero_value
    ]
    first, last = zeroes[0], zeroes[-1]
    distances[:first] = [
        first - number_index for number_index in range(first)
    ]
    for left_index, right_index in zip(zeroes, zeroes[1:]):
        for number_index in range(left_index + 1, right_index):
            distances[number_index] = min(
                number_index - left_index, right_index - number_index
            )
    distances[last + 1:] = [
        number_index - last for number_index in range(last + 1, street_length)
    ]

    return distances


if __name__ == '__main__':
    input()
    print(*distances_to_nearest_zero(numbers=input().split()))
