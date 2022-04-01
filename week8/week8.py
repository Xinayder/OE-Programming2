import numpy as np
import multiprocessing as mp

def common_row_items():
    """
    Utilizes parallelism to obtain the intersection between each row of list_a and list_b 2D arrays.

    Expected result: [
        [2, 3], 
        [6], 
        [11, 12], 
        [21]
    ]
    """ 
    list_a = np.array([[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]], dtype=object)
    list_b = np.array([[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]], dtype=object)

    results = []

    # numpy.intersect1d calculates the intersection of 2 arrays
    with mp.Pool(mp.cpu_count()) as pool:
        results = [pool.apply(np.intersect1d, args=(list_a[row], list_b[row])) for row in range(0, 4)]
    
    results = [row.tolist() for row in results] # transform numpy array into python array
    
    return results

print("Problem 1 - Use Pool.apply() to get the row wise commom items in list_a and list_b:")
print(common_row_items())
print()

def execute_script(file):
    import os
    os.system(f'python {os.path.dirname(os.path.realpath(__file__))}/{file}')
    # the os.path.dirname part gets the directory where this program is located at.
    # we assume the scripts we need to run are located in the same directory as the main program.

def parallelize_scripts():
    """
    Parallelizes the execution of scripts script1.py, script2.py and script3.py.

    Expected result:
        Calculating the first 30 triangular numbers:
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435]

        Calculating the first 30 terms of the Catalan sequence:
        [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452, 18367353072152, 69533550916004, 263747951750360, 1002242216651368]

        Calculating the first 30 terms of the Fibonacci sequence:
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
    """
    scripts = ('script1.py', 'script2.py', 'script3.py')

    with mp.Pool(mp.cpu_count()) as pool:
        pool.map(execute_script, scripts)

print("Problem 2 - Use Pool.map() to run the following python scripts in parallel. Script names: 'script1.py', 'script2.py', 'script3.py'")
parallelize_scripts()
print()

def normalize_rows():
    """
    Normalizes (scales the range of the data to an interval from 0 to 1) each row of the list_a 2D array.

    Expected result: [
        [0.2721655269759087, 0.408248290463863, 0.5443310539518174, 0.6804138174397717], 
        [0.3157894736842105, 0.47368421052631576, 0.5263157894736842, 0.631578947368421], 
        [0.4382504900892777, 0.4780914437337575, 0.5179323973782373, 0.5577733510227171], 
        [0.4361768170171271, 0.49848779087671674, 0.51925811549658, 0.5400284401164431]
    ]
    """
    list_a = np.array([[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]], dtype=object)

    results = list()

    # loop through the list's rows
    for i in range(0, len(list_a)):
        norm = np.linalg.norm(list_a[i]) # find the norm of each row
        normalized_arr = list_a[i] / norm # obtain the normalized version of the row
        results.append(normalized_arr.tolist()) # append the result to a list
    
    return results

print("Problem 3 - Normalize each row of 2d array (list) to vary between 0 and 1:")
print(normalize_rows())
print()