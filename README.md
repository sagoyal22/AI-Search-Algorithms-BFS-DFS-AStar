# AI Search Algorithms – BFS, DFS, and A* (Sliding Puzzle)

This project implements core **artificial intelligence search algorithms**, with a focus on **A\* search using admissible heuristics**, applied to a sliding-tile puzzle problem.

The implementation demonstrates how intelligent agents explore a state space, evaluate alternatives, and find optimal solutions under constraints — a foundational concept in AI, robotics, and algorithmic problem-solving.

---

## 🧠 Problem Description

The problem is a variant of the **sliding tile puzzle**, represented as a 3×3 grid flattened into a list of length 9.  
Two empty tiles (`0`) allow multiple movement possibilities.

- **Initial state**: arbitrary valid configuration
- **Goal state**:  
  `[1, 2, 3, 4, 5, 6, 7, 0, 0]`
- **Objective**: reach the goal state using the fewest moves

This is a classic **state-space search** problem.

---

## ⚙️ Algorithms Implemented

### A* Search (Primary Solver)
Implemented in `solve()` using:
- Priority queue (`heapq`)
- Cost function:  
  **f(n) = g(n) + h(n)**  
  where:
  - `g(n)` = path cost (number of moves)
  - `h(n)` = heuristic estimate to goal

The algorithm guarantees **optimal solutions** when the heuristic is admissible.

---

## 🧮 Heuristics Implemented

### 1. Manhattan Distance (`get_manhattan_distance`)
- Computes the sum of Manhattan distances for each tile from its goal position
- Admissible and consistent
- Widely used in real-world planning and navigation

```python
distance += abs(x1 - x2) + abs(y1 - y2)
