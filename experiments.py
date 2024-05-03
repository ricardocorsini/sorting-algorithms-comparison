from sortingScripts import Sorting
from input_generator import InputGen

import pandas as pd


#Sorting().bubble_sort()
#Sorting().heap_sort()
#Sorting().insertion_sort()
#Sorting().quick_sort()
#Sorting().merge_sort()
#Sorting().radix_sort()
#Sorting().selection_sort()

def experiment(n):

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 30)

    dict = {
        ''
    }



    #df = pd.DataFrame()



    return 

print(experiment(10))