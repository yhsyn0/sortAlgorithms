# Insertion Sort
def insertionSort(arr):
    
    for i in range(1, len(arr)):
        tmp = arr[i]
        k = i-1

        while(tmp < arr[k] and k >= 0):
            arr[k+1] = arr[k]
            k -= 1

        arr[k+1] = tmp
    
    return arr

# Quick Sort
def part(arr, low, high):
 
    piv = arr[high]
    k = low-1
 
    for i in range(low, high):
        if arr[i] <= piv:
            k += 1
            tmp = arr[k]
            arr[k] = arr[i]
            arr[i] = tmp
 
    tmp = arr[k+1]
    arr[k+1] = arr[high]
    arr[high] = tmp

    return k+1

def quickSort(arr, low, high):
    if low < high:
 
        piv = part(arr, low, high)
        quickSort(arr, low, piv - 1)
        quickSort(arr, piv + 1, high)

    return arr

# Merge Sort
def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
 
        mergeSort(left)
        mergeSort(right)
 
        i, j, k = [0, 0, 0]

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

# Heap Sort
def heapify(arr, n, i):
    top = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[i] < arr[left]:
        top = left

    if right < n and arr[top] < arr[right]:
        top = right

    if top != i:
        tmp = arr[i]
        arr[i] = arr[top]
        arr[top] = tmp

        heapify(arr, n, top)
  
def heapSort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        tmp = arr[i]
        arr[i] = arr[0]
        arr[0] = tmp

        heapify(arr, i, 0)
    
    return arr

# Counting Sort
def countingSort(arr):
   low = min(arr)
   high = max(arr)
   
   outArr = [0] * len(arr)
   countArr = [0 for i in range(low, high+1)]

   for i in arr:
      countArr[i-low] += 1            
   for j in range(1, len(countArr)):
      countArr[j] += countArr[j-1]
   for k in reversed(arr):
      outArr[countArr[k-low] - 1] = k  
      countArr[k-low] -= 1       

   return outArr 

# Radix Sort
def radixPositive(arr):
    last = False
    power = 1

    while not last:
        digits = [[] for _ in range(10)]
        last = True
        for i in arr:
            digit = i % (power*10) // power
            digits[digit].append(i)

            if i >= power*10:
                last = False
        
        arr = [i for dig in digits for i in dig]
        power *= 10

    return arr

def radixSort(arr):
    posList = radixPositive( x for x in arr if x >= 0)
    negList = radixPositive(-x for x in arr if x <  0)
    return [-x for x in reversed(negList)] + posList

# Topological Sort
# Kod https://python.plainenglish.io/topological-sort-python-119f2c012b52 adresinden alınmıştır.
# Kodu inceleyip çalışma biçimini anladım ancak algoritmasına bakarak kendim yazmaya çalıştığımda 
#   buradaki sonuç ile neredeyse aynı çıktılar elde ettim. Bu sebepten kaynağını ve orjinal 
#   kodu buraya ekliyorum.
from collections import defaultdict
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u-1].append(v-1)
    def helper(self,u,visited, res):
        visited[u] = True
        for i in self.graph[u]:
            if visited[i] == False:
                self.helper(i, visited, res)
        res.insert(0, u+1)
    def topological_sort(self):
        visited = [False]*self.V
        res =[]
        for i in reversed(range(self.V)):
            if visited[i] == False:
                self.helper(i, visited, res)
                
        return res
A = 6
B = [[6, 3], [6, 1], [5, 1], [5, 2], [3, 4], [4, 2]]
graph = Graph(A)
for u, v in B:
    graph.add_edge(u, v)
        
res = graph.topological_sort()
print(res) # [5, 6, 1, 3, 4, 2]

