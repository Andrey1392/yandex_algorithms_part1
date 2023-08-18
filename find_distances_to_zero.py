# номер посылки 89659519

def calculate_distances_two_boundaries(array_length):
    '''
    Расчет минимальных расстояний до пустого дома
    для линии, имеющей пустые дома слева и справа
    '''
    rigth_half_distances = calculate_distances_left_boundary(array_length // 2)
    center_distance = [array_length // 2 + 1 for _ in range(array_length % 2)]
    left_half_distances = rigth_half_distances[::-1]
    return left_half_distances + center_distance + rigth_half_distances


def calculate_distances_left_boundary(array_length):
    '''
    Расчет минимальных расстояний до пустого дома
    для линии, не имеющех пустых домов слева
    '''
    return [array_length - i for i in range(array_length)]


def calculate_distances_to_empty_house(street_length, numbers_list):
    '''
    Расчет минимальных расстояний до пустого дома
    нулевая линия - массив, состоящий из номеров пустых домов
    ненулевая линия - массив, состоящий из номеров не пустых домов
    '''

    # итоговый массив
    distances_to_empty_house = [0] * street_length

    # левая и правая граница ненулевой линии
    left_boundary_index = 0
    right_boundary_index = 0

    # указатель прохождения цикла по нулевой линии
    empty_houses_line_flag = True
    for i in range(street_length):
        house_num = numbers_list[i]
        if house_num == '0':
            if empty_houses_line_flag:
                # проходим дальше по нулевой линии,
                # ставим краевые индексы на текущую позицию в массиве
                left_boundary_index, right_boundary_index = i, i
            else:
                # закончилась ненулевая линия,
                # рассчитываем расстояния для линии
                if left_boundary_index == 0:
                    distances_in_line = calculate_distances_left_boundary(
                        right_boundary_index - left_boundary_index + 1
                    )
                else:
                    distances_in_line = calculate_distances_two_boundaries(
                        right_boundary_index - left_boundary_index + 1
                    )

                # вставляем полученные расстояния в результирующий массив
                distances_to_empty_house[
                    left_boundary_index:right_boundary_index + 1
                ] = distances_in_line

                # ставим краевые индексы на текущую позицию в массиве
                left_boundary_index, right_boundary_index = i, i
                empty_houses_line_flag = True
        else:
            # если находимся в начале ненулевой линии,
            # ставим краевые индексы на текущую позицию в массиве
            if empty_houses_line_flag:
                left_boundary_index, right_boundary_index = i, i
                empty_houses_line_flag = False

            else:
                # идем по ненулевой линии
                # смещаем правый краевой индекс на 1 вправо
                right_boundary_index += 1

            # если дошли до конца массива по ненулевой линии,
            # вычисляем значения расстояний и вставляем в итоговый массив
            if right_boundary_index == street_length - 1:
                distances_in_line = calculate_distances_left_boundary(
                    right_boundary_index - left_boundary_index + 1
                )[::-1]

                distances_to_empty_house[
                    left_boundary_index:right_boundary_index + 1
                ] = distances_in_line

    return distances_to_empty_house


def main():
    street_length = int(input())
    numbers_list = input().split()
    result = calculate_distances_to_empty_house(street_length, numbers_list)
    print(*result)


if __name__ == '__main__':
    main()
