ans = 0
def mergesort(arr):
    global ans
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)

        ptr = Lptr = Rptr = 0
        while Lptr < len(left) and Rptr< len(right):
            if left[Lptr] <= right[Rptr]:
                arr[ptr] = left[Lptr]
                ptr += 1
                Lptr += 1
            else:
                arr[ptr] = right[Rptr]
                ptr += 1
                Rptr += 1
                ans += len(left)-Lptr
        while Lptr < len(left):
            arr[ptr] = left[Lptr]
            ptr += 1
            Lptr += 1
        while Rptr<len(right):
            arr[ptr] = right[Rptr]
            ptr += 1
            Rptr += 1
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.reverse()
mergesort(s)
print(ans)