import threading
class SumOfSquaresThread(threading.Thread):
def __init__(self, numbers):
super().__init__()
self.numbers = numbers
self.result = 0
def run(self):
self.result = sum(x ** 2 for x in self.numbers)
def sum_of_squares(n, num_threads=4):
numbers = list(range(1, n + 1))
chunk_size = len(numbers) // num_threads
threads = []
results = []
for i in range(num_threads):
start = i * chunk_size
end = (i + 1) * chunk_size if i != num_threads - 1 else len(numbers)
thread = SumOfSquaresThread(numbers[start:end])
threads.append(thread)
thread.start()
for thread in threads:
thread.join()
results.append(thread.result)
return sum(results)
n = int(input("Enter the value for n to generate the sum of squares: "))
num_threads = 3
print(f"Sum of squares from 1 to {n} using {num_threads} threads: {sum_of_squares(n,
num_threads)}")
