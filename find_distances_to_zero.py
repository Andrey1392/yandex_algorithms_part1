# номер посылки 89718101


def distances_to_nearest_zero(numbers):

    street_length = len(numbers)
    distances = [0] * street_length

    zeroes_indexes = [i for i in range(street_length) if numbers[i] == '0']
    first_zero_index = zeroes_indexes[0]
    last_zero_index = zeroes_indexes[-1]

    distances[:first_zero_index] = [
        first_zero_index - i for i in range(first_zero_index)
    ]

    for i in range(len(zeroes_indexes) - 1):
        left_boundary_index = zeroes_indexes[i]
        right_boundary_index = zeroes_indexes[i+1]
        interval_length = right_boundary_index - left_boundary_index - 1
        if interval_length > 0:
            left_half_distances = [
                i + 1 for i in range(interval_length // 2)
            ]
            center_distance = [
                interval_length // 2 + 1 for _ in range(interval_length % 2)
            ]
            rigth_half_distances = left_half_distances[::-1]
            distances[
                left_boundary_index + 1: right_boundary_index
            ] = left_half_distances + center_distance + rigth_half_distances

    distances[last_zero_index+1:] = [
        i + 1 for i in range(street_length - (last_zero_index + 1))
    ]

    return (distances)


if __name__ == '__main__':
    input()
    numbers = input().split()
    result = distances_to_nearest_zero(numbers)
    print(*result)
