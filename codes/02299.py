while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    minimum = 0

    def mergesort(arr):
        global minimum

        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            left = mergesort(left)
            right = mergesort(right)

            Lptr = 0
            Rptr = 0
            ptr = 0
            while Lptr<len(left) and Rptr<len(right):
                if left[Lptr] <= right[Rptr]:
                    arr[ptr] = left[Lptr]
                    ptr += 1
                    Lptr += 1
                else:
                    arr[ptr] = right[Rptr]
                    ptr += 1
                    Rptr += 1
                    minimum += len(left)-Lptr
            while Lptr < len(left):
                arr[ptr] = left[Lptr]
                ptr += 1
                Lptr += 1
            while Rptr < len(right):
                arr[ptr] = right[Rptr]
                ptr += 1
                Rptr += 1
        return arr
    mergesort(arr)
    print(minimum)