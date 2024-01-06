# main.py
from manhattan import manhattan_distance
from solver import a_star, hamming_heuristic, manhattan_heuristic, PuzzleState
from solvable import is_solvable


def print_puzzle_diff(current_state):
    print("Step:")
    print_puzzle(current_state)


def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()


def main():
    # Input initial state from the user
    print("Enter the initial state:")
    initial_state = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        initial_state.append(row)

    # Check if the initial state is solvable
    if not is_solvable(initial_state):
        print("The initial state is not solvable.")
        return

    print("The initial state is solvable.")

    #choose a heuristic
    print("Choose the heuristic: 1 for Hamming, 2 for Manhattan")
    choice = input("Your choice: ")
    if choice == "1":
        heuristic = hamming_heuristic
    elif choice == "2":
        heuristic = manhattan_heuristic
        print("Manhattan distance of the initial state:", manhattan_distance(initial_state))
    else:
        print("Invalid choice. Default ist Hamming heuristic.")
        heuristic = hamming_heuristic

    #Run A* algorithm with chosen heuristic
    goal_reached, path = a_star(initial_state, heuristic)

    if goal_reached:
        print("Goal state reached!")
        if not path:
            print("No steps required. The initial state is the goal state.")
        else:
            print("Steps taken:")
            for idx, step in enumerate(path):
                if idx == 0:
                    print_puzzle(step[0].state)
                print_puzzle_diff(step[1].state)
    else:
        print("Goal state not reached.")


if __name__ == "__main__":
    main()