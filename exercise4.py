import threading
import time
import sys

STEP_COUNT = 10**7
STEP = 1.0 / STEP_COUNT
THREAD_COUNTS = [1, 2, 4, 8, 12]

def calculate_pi_fragment(start, end, step, results, index):
    """
    Calculates a partial sum of the Pi integral for the range [start, end).
    The result is stored in results[index].
    """
    local_sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        local_sum += 4.0 / (1.0 + x**2)
    
    results[index] = local_sum

def main():
    print(f"Python version: {sys.version}")
    status = getattr(sys, "_is_gil_enabled", lambda: "Unknown")()
    print(f"Is GIL enabled: {status}\n")

    baseline_time = 0.0

    print(f"{'Threads':<10} | {'Pi Result':<12} | {'Time (s)':<10} | {'Speedup':<10}")
    print("-" * 50)

    for num_threads in THREAD_COUNTS:
        results = [0.0] * num_threads
        threads = []
        
        chunk_size = STEP_COUNT // num_threads
        
        start_time = time.perf_counter()

        for i in range(num_threads):
            start = i * chunk_size
            end = STEP_COUNT if i == num_threads - 1 else (i + 1) * chunk_size
            
            t = threading.Thread(
                target=calculate_pi_fragment, 
                args=(start, end, STEP, results, i)
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        final_pi = sum(results) * STEP
        end_time = time.perf_counter()
        duration = end_time - start_time

        if num_threads == 1:
            baseline_time = duration
            speedup = 1.0
        else:
            speedup = baseline_time / duration

        print(f"{num_threads:<10} | {final_pi:<12.10f} | {duration:<10.4f} | {speedup:<10.2f}x")

if __name__ == "__main__":
    main()
