import random

COUNTER_ITERATIONS = random.randint(5, 10)
N_OF_THREADS = random.randint(2, 5)

counter = 0

# insert your code here

assert counter == N_OF_THREADS * COUNTER_ITERATIONS
print("Done")
