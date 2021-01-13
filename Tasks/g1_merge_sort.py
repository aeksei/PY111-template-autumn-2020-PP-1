from typing import List
from operator import gt, lt  # todo Реализовать сортировки по убыванию и возрастанию


def sort(container: List[int], reverse=False) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def _merge(left_container: List[int], right_container: List[int]) -> List[int]:
        """Функция для слияния отсортированных контейнеров"""
        merged_container = []
        while True:
            # 2. сравниваем первые элементы из каждого массива и в итоговый массив записываем наименьшее
            if left_container[0] < right_container[0]:
                elem = left_container.pop(0)  # 3. в массиве, в котором был наименьший элемент, переходим к следующему
                merged_container.append(elem)
            else:
                elem = right_container.pop(0)  # 3. в массиве, в котором был наименьший элемент, переходим к следующему
                merged_container.append(elem)

            # 4. когда один из массивов закончится, остаток второго «сливаем» в итоговый массив
            if not left_container:
                merged_container += right_container
                break
            elif not right_container:
                merged_container += left_container
                break

        return merged_container

    if len(container) == 1:  # Если массив состоит из 1 элемента – он отсортирова
        return container

    middle = len(container) // 2  # Иначе массив разбивается на две части, которые сортируются рекурсивно (см. ниже)
    return _merge(sort(container[:middle]), sort(container[middle:]))  # После сортировки двух частей массива к ним применяется процедура слияния

