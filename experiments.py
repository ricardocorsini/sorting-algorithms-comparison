from sortingScripts import Sorting
from input_generator import InputGen
from Charts import bar_chart

import pandas as pd
from timeit import timeit


def experiment(n, nameChart):

    #Definição das entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)

    #Insertion sort

    insertion_random = timeit(lambda: Sorting().insertion_sort(totRandom), number=10) / 10
    insertion_partially = timeit(lambda: Sorting().insertion_sort(partially), number=10) / 10
    insertion_descending = timeit(lambda: Sorting().insertion_sort(descending), number=10) / 10

    media_insertion = (insertion_random + insertion_partially + insertion_descending) / 3

    insertion_resumeTime = [insertion_random, insertion_partially, insertion_descending, media_insertion]

    #Recriando as entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)

    #Bubble sort

    bubble_random = timeit(lambda: Sorting().bubble_sort(totRandom), number=10) / 10
    bubble_partially = timeit(lambda: Sorting().bubble_sort(partially), number=10) / 10
    bubble_descending = timeit(lambda: Sorting().bubble_sort(descending), number=10) / 10

    media_bubble = (bubble_random + bubble_partially + bubble_descending) / 3

    bubble_resumeTime = [bubble_random, bubble_partially, bubble_descending, media_bubble]

    #Recriando as entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)

    #Heap sort

    heap_random = timeit(lambda: Sorting().heap_sort(totRandom), number=10) / 10
    heap_partially = timeit(lambda: Sorting().heap_sort(partially), number=10) / 10
    heap_descending = timeit(lambda: Sorting().heap_sort(descending), number=10) / 10

    media_heap = (heap_random + heap_partially + heap_descending) / 3

    heap_resumeTime = [heap_random, heap_partially, heap_descending, media_heap]

    #Recriando as entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)    

    #Quick sort

    quick_random = timeit(lambda: Sorting().quick_sort(totRandom), number=10) / 10
    quick_partially = timeit(lambda: Sorting().quick_sort(partially), number=10) / 10
    quick_descending = timeit(lambda: Sorting().quick_sort(descending), number=10) / 10

    media_quick = (quick_random + quick_partially + quick_descending) / 3

    quick_resumeTime = [quick_random, quick_partially, quick_descending, media_quick]

    #Recriando as entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)

    #Merge sort

    merge_random = timeit(lambda: Sorting().merge_sort(totRandom), number=10) / 10
    merge_partially = timeit(lambda: Sorting().merge_sort(partially), number=10) / 10
    merge_descending = timeit(lambda: Sorting().merge_sort(descending), number=10) / 10

    media_merge = (merge_random + merge_partially + merge_descending) / 3

    merge_resumeTime = [merge_random, merge_partially, merge_descending, media_merge]

    #Recriando as entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)

    #Radix sort

    radix_random = timeit(lambda: Sorting().radix_sort(totRandom), number=10) / 10
    radix_partially = timeit(lambda: Sorting().radix_sort(partially), number=10) / 10
    radix_descending = timeit(lambda: Sorting().radix_sort(descending), number=10) / 10

    media_radix = (radix_random + radix_partially + radix_descending) / 3

    radix_resumeTime = [radix_random, radix_partially, radix_descending, media_radix]

    #Recriando as entradas

    totRandom = InputGen().totally_random(n)
    descending = InputGen().descending_order(n)
    partially = InputGen().partially_sorted(n, 50)

    #Selection sort

    selection_random = timeit(lambda: Sorting().selection_sort(totRandom), number=10) / 10
    selection_partially = timeit(lambda: Sorting().selection_sort(partially), number=10) / 10
    selection_descending = timeit(lambda: Sorting().selection_sort(descending), number=10) / 10

    media_selection = (selection_random + selection_partially + selection_descending) / 3

    selection_resumeTime = [selection_random, selection_partially, selection_descending, media_selection]

    dict = {
        'Bubble Sort': bubble_resumeTime,
        'Heap Sort': heap_resumeTime,
        'Insertion Sort': insertion_resumeTime,
        'Quick Sort': quick_resumeTime,
        'Merge Sort': merge_resumeTime,
        'Radix Sort': radix_resumeTime,
        'Selection Sort': selection_resumeTime
    }

    df = pd.DataFrame(dict) * 1000
    df_round = df.round(3)

    df_round.index = ['Random', 'Partially (.5)', 'Descending', 'Mean']

    print(df_round)

    bar_chart(df_round, nameChart, n)
    latex_table = df_round.to_latex(index=True, caption='legenda da tebela', label='tab:legenda da tabela', float_format="{:0.3f}".format)

    return latex_table




