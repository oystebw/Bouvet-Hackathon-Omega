import time
import sys
sys.setrecursionlimit(10_000)
start_time = time.time()

fibonaccis = [0 for i in range(10_000)]
def fibonacci(input):
    if(input == 1 or input == 2):
        return 1
    if(fibonaccis[input]):
        return fibonaccis[input]
    fibonaccis[input] = fibonacci(input - 1) + fibonacci(input - 2)
    return fibonaccis[input]

def fibfac(input):
    if(input == 1):
        return 1
    print(f"Started on fibfac number: {input} after {time.time()-start_time} seconds")

    return fibfac(input - 1) * fibonacci(input) 

print(fibfac(2000))
print(f"It took {time.time() - start_time} seconds")