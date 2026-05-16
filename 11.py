from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    Проверяет, является ли частично заполненное поле судоку корректным.

    Правила проверки:
    1. В каждой строке заполненные цифры от 1 до 9 не повторяются.
    2. В каждом столбце заполненные цифры от 1 до 9 не повторяются.
    3. В каждом подблоке 3x3 заполненные цифры от 1 до 9 не повторяются.

    Пустые клетки обозначаются символом "." и не проверяются.

    Args:
        board: Список 9x9, содержащий строки с цифрами или "."

    Returns:
        True, если поле корректно, иначе False
    """

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue

            box_idx = (i // 3) * 3 + (j // 3)

            if (val in rows[i]) or (val in cols[j]) or (val in boxes[box_idx]):
                return False

            rows[i].add(val)
            cols[j].add(val)
            boxes[box_idx].add(val)

    return True