def Heapify(H,n,i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and H[i] > H[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and H[largest] > H[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        H[i], H[largest] = H[largest], H[i]  # swap

        # Heapify the root.
        Heapify(H, n, largest)


def HeapSort(H):
    n = len(H)

    # Build a maxheap.
    for i in range(n, -1, -1):
        Heapify(H, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        H[i], H[0] = H[0], H[i]  # swap
        Heapify(H, i, 0)

