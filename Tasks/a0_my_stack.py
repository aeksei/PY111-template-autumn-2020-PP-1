"""
My little Stack
"""
from typing import Any

my_stack = []  # Вершина стека справа


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    print(elem)
    my_stack.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if not my_stack:
        return None

    return my_stack.pop(-1)


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    print(ind)
    if ind >= len(my_stack):
        return None

    return my_stack[-1 - ind]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    my_stack.clear()
    return None


if __name__ == '__main__':
    print(my_stack)
    push(1)
    # print(my_stack)

    push(2)
    # print(my_stack)

    # clear()
    # print(my_stack)
    # push(3)
    # print(my_stack)
    #
    # print(pop())
    # print(my_stack)
    #
    # print(pop())

    print(peek(0))
    print(peek(1))
    print(peek(2))
