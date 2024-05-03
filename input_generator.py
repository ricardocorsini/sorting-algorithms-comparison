import random

class InputGen:

    def __init__(self):

        pass

    def totally_random(self, n):

        min_value = 0
        max_value = n

        input = [random.randint(min_value, max_value) for _ in range(n)]
            
        return input
    
    def descending_order(self, n):

        input = list(range(n, 0, -1))
        
        return input
    
    def partially_sorted(self, n, disorder_percentage):
        
        if not (0 <= disorder_percentage <= 100):
            raise ValueError("Disorder percentage must be between 0 and 100")

        sorted_list = list(range(n))

        num_to_shuffle = int(n * (disorder_percentage / 100))

        indices_to_shuffle = random.sample(range(n), num_to_shuffle)

        elements_to_shuffle = [sorted_list[i] for i in indices_to_shuffle]
        random.shuffle(elements_to_shuffle)

        for idx, shuffled_val in zip(indices_to_shuffle, elements_to_shuffle):
            sorted_list[idx] = shuffled_val

        return sorted_list
