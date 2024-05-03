

class Sorting:

    def __init__(self):

        pass


    def insertion_sort(self, arr):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key        

        return arr
    
    def bubble_sort(self, arr):

        n = len(arr)
        
        for i in range(n):
            
            swapped = False

            for j in range(0, n-i-1):
                
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if not swapped:
                break

        return arr
    
    def merge_sort(self, arr):

        if len(arr) > 1:

            mid = len(arr) // 2
            
            left_half = arr[:mid]
            right_half = arr[mid:]

            Sorting.merge_sort(self, left_half)
            Sorting.merge_sort(self, right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr
    
    def selection_sort(self, arr):
    
        for i in range(len(arr)):
            
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr
    
    def quick_sort(self, arr):
   
        def _quick_sort(items, low, high):
            
            if low < high:
                
                pi = partition(items, low, high)
                
                _quick_sort(items, low, pi - 1)
                _quick_sort(items, pi + 1, high)

        def median_of_three(items, low, high):
            
            mid = (low + high) // 2

            if items[mid] < items[low]:
                items[mid], items[low] = items[low], items[mid]
            if items[high] < items[low]:
                items[high], items[low] = items[low], items[high]
            if items[mid] < items[high]:
                items[mid], items[high] = items[high], items[mid]
            
            return items[high]

        def partition(items, low, high):
            
            pivot = median_of_three(items, low, high)
            i = low - 1

            for j in range(low, high):
                
                if items[j] <= pivot:
                    
                    i += 1
                    
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]

            return i + 1

        _quick_sort(arr, 0, len(arr) - 1)

        return arr
    
    def heap_sort(self, arr):
        
        def heapify(n, i):

            largest = i  
            left = 2 * i + 1  
            right = 2 * i + 2  

            if left < n and arr[largest] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  

                heapify(n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):

            heapify(n, i)

        for i in range(n-1, 0, -1):

            arr[0], arr[i] = arr[i], arr[0]  
            heapify(i, 0)

        return arr

    def radix_sort(self, arr):
        
        max_num = max(arr)
        exp = 1  

        def counting_sort_by_digit(arr, exp):
            
            n = len(arr)
            output = [0] * n  
            count = [0] * 10  

            for i in range(n):
                
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1

            while i >= 0:
                
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]

        
        while max_num // exp > 0:
            
            counting_sort_by_digit(arr, exp)
            exp *= 10

        return arr


print(Sorting().radix_sort([3, 8, 1, 10, 100, 2, 0, 4]))