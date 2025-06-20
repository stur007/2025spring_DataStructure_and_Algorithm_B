from functools import lru_cache

@lru_cache(maxsize=None)
def min_avl_nodes(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return min_avl_nodes(n-1)+min_avl_nodes(n-2)+1

if __name__ == '__main__':
    n = int(input())
    print(min_avl_nodes(n))

# the answer depend on the definition of the height of the tree.
# The code below could be better if 'height' means the number of the edges of the tree:
from functools import lru_cache

@lru_cache(maxsize=None)
def min_avl_nodes(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return min_avl_nodes(n-1)+min_avl_nodes(n-2)+1

if __name__ == '__main__':
    n = int(input())
    print(min_avl_nodes(n))