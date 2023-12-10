import threading
import multiprocessing
import time

def fibonacci(i):
    if i <= 1:
        return i

    prev_prev = 0
    prev = 1

    for _ in range(2, i + 1):
        current = prev_prev + prev
        prev_prev, prev = prev, current

    return prev

def run_sync(n, num_runs):
    return [fibonacci(n) for _ in range(num_runs)]

def worker(results, n, num_runs):
    results.extend(run_sync(n, num_runs))

def run_with_threads(n, num_threads, num_runs):
    results = []

    threads = [threading.Thread(target=worker, args=(results, n, num_runs)) for _ in range(num_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return results


def run_with_processes(n, num_processes, num_runs):
    results = []

    processes = [multiprocessing.Process(target=worker, args=(results, n, num_runs)) for _ in range(num_processes)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    return results

def main():
    n = 200000
    num_runs = 10
    num_threads = 10
    num_processes = 10

    with open('artifacts/fibonacci_results.txt', 'w') as file:
        file.write("Method\t\t\tTime (seconds)\n")
        file.write("---------------------------------\n")

        # Synchronous run
        start_time = time.time()
        run_sync(n, num_runs)
        end_time = time.time()
        file.write(f"Synchronous\t\t{(end_time - start_time) / num_runs:.6f}\n")

        # Run with threads
        start_time = time.time()
        run_with_threads(n, num_threads, num_runs)
        end_time = time.time()
        file.write(f"With Threads\t\t{(end_time - start_time) / num_runs:.6f}\n")

        # Run with processes
        start_time = time.time()
        run_with_processes(n, num_processes, num_runs)
        end_time = time.time()
        file.write(f"With Processes\t\t{(end_time - start_time) / num_runs:.6f}\n")

if __name__ == "__main__":
    main()
