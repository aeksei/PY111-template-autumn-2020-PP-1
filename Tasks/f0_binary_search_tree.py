"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

bts = {}  # дерево бинарного поиска (корневой узел)


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    def _insert(subtree: dict):
        if not subtree:
            subtree['key'] = key
            subtree['value'] = value
            subtree['left'] = {}
            subtree['right'] = {}
        else:
            dst_subtree = subtree['right'] if key >= subtree['key'] else subtree['left']
            _insert(dst_subtree)

    _insert(bts)


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    print(key)
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    def _find(subtree: dict) -> Optional[Any]:
        if not subtree:
            raise KeyError('Элемент не найден')

        if key == subtree['key']:
            return subtree['value']
        else:
            dst_subtree = subtree['right'] if key >= subtree['key'] else subtree['left']
            return _find(dst_subtree)

    return _find(bts)


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    bts.clear()
    return None
