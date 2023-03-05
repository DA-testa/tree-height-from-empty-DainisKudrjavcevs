# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    koks = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else :
            koks[parents[i]].append(i)
    return height(root, koks)

def height(x, koks):
    if not koks[x]:
        return 1
    else:
        return max(height(berns, koks) for berns in koks[x]) + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))

    print(compute_height(n,parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
