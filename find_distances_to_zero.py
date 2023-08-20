# номер посылки 89738351


def distances_to_nearest_zero(numbers, zero_value='0'):
    street_length = len(numbers)
    distances = [0] * street_length
    zeroes = [
        pos for pos, value in enumerate(numbers) if value == zero_value
    ]
    first, last = zeroes[0], zeroes[-1]
    distances[:first] = [
        first - pos for pos in range(first)
    ]
    for left, right in zip(zeroes, zeroes[1:]):
        distances[left + 1:right] = [
            min(pos - left, right - pos) for pos in range(left + 1, right)
        ]

    distances[last + 1:] = [
        pos - last for pos in range(last + 1, street_length)
    ]
    return distances


if __name__ == '__main__':
    input()
    print(*distances_to_nearest_zero(numbers=input().split()))
