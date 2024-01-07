import time
from solver import hamming_heuristic, manhattan_heuristic, a_star
from main import generate_solvable_puzzle


def run_search(initial_state, heuristic):
    start_time = time.time()

    # Perform A* search using the specified heuristic
    goal_reached, path = a_star(initial_state, heuristic)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return goal_reached, len(path), elapsed_time


def compare_heuristics():
    initial_state = generate_solvable_puzzle()

    # Lists to store results for each heuristic
    memory_usage_hamming = []
    memory_usage_manhattan = []
    computation_time_hamming = []
    computation_time_manhattan = []

    for _ in range(100):
        # Run search with Hamming heuristic
        goal_reached, expanded_nodes, elapsed_time = run_search(initial_state, hamming_heuristic)
        memory_usage_hamming.append(expanded_nodes if goal_reached else float('inf'))
        computation_time_hamming.append(elapsed_time)

        # Run search with Manhattan heuristic
        goal_reached, expanded_nodes, elapsed_time = run_search(initial_state, manhattan_heuristic)
        memory_usage_manhattan.append(expanded_nodes if goal_reached else float('inf'))
        computation_time_manhattan.append(elapsed_time)

    # Analyze and print or visualize the results
    average_memory_hamming = sum(memory_usage_hamming) / len(memory_usage_hamming)
    average_memory_manhattan = sum(memory_usage_manhattan) / len(memory_usage_manhattan)

    average_time_hamming = sum(computation_time_hamming) / len(computation_time_hamming)
    average_time_manhattan = sum(computation_time_manhattan) / len(computation_time_manhattan)

    print("Hamming Heuristic:")
    print(f"Average Memory Usage: {average_memory_hamming}")
    print(f"Average Computation Time: {average_time_hamming}")

    print("\nManhattan Heuristic:")
    print(f"Average Memory Usage: {average_memory_manhattan}")
    print(f"Average Computation Time: {average_time_manhattan}")


if __name__ == "__main__":
    compare_heuristics()
