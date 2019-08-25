"""
first line will contain N (No. of boxes). Next line will contain N space separated integers denoting Ci, the number of chocolates in ith box.
Next line will contain Q (No. of times Pranjul will ask her). Then each next Q lines will contain the asked index I.
"""
from bisect import bisect_left
boxes = []

def gen_boxes(c):
    i = 0
    j = 0
    boxes.append(j)
    while i < len(c):
        j += int(c[i])
        boxes.append(j)
        i += 1

def get_answer(box):
    print(bisect_left(boxes, box))

if __name__ == "__main__":
    n = int(input())
    gen_boxes(input().strip().split())
    t = int(input())
    for i in range(t):
        get_answer(int(input()))