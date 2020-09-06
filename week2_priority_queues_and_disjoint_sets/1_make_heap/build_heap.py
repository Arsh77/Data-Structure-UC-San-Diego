# python3
def parent(i):
    if(i%2==1):
        return i//2
    elif i>0 and i%2==0:
        return (i//2)
    else:
        return 0
def left(i):
    return 2*i+1
def right(i):
    return 2*(i+1)

##def heapify(A,i):
##    if A[i]>A[left(i)]:
##        A[i],A[left(i)]=A[left(i)],A[i]
##    if A[i]>A[right(i)]:
##        A[i],A[right[i]]=A[right[i]],A[i]

def heapify(data,i, swap):
    s=i
    if left(i)<len(data) and data[left(i)]<data[i]:
        s=left(i)
    if right(i)<len(data) and data[right(i)]<data[s]:
        s=right(i)
    if s!=i:
        swap.append([i,s])
        data[s],data[i]=data[i],data[s]
        heapify(data,s, swap)

def build_heap(data,i):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    if i<0:
        return
    swaps = []
    for i in range(len(data)//2,-1,-1):
        heapify(data,i,swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data,len(data)-1)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
