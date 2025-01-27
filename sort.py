import time
import random

def sort(list):
    sortas = list
    sortas.sort()
    print(sortas)

# Generate a list of 1000 random numbers
list_a= [random.randint(0, 100) for i in range(1000)]
print("List: ", list_a)
print("------------------")
# Sort the list
start_time = time.time()
sort(list_a)
end_time = time.time()
print("Time: ", end_time - start_time)
