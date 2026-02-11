AStarMaze:
==========
A simple implementation of the A* pathfinding algorithm that finds the shortest path through a maze.

Description:
============
This project demonstrates how the A* algorithm navigates through a grid maze from a start point to a goal. It’s useful for learning how heuristic search works and can be extended for games, robotics, or mapping applications.

Features:
=========
✔ Uses the A* algorithm
✔ Finds shortest path in a maze
✔ Handles obstacles (walls)
✔ Easy to understand and extend

How It Works:
=============
A* combines:
-> g-cost: distance from start to current node
-> h-cost: heuristic estimate to the goal
-> f-cost: g + h (total estimated cost)

How to Run:
===========
Step-1: Clone the repository:
-----------------------------
git clone https://github.com/Fazlul03/AStarMaze.git
cd AStarMaze

Step-2: Run the program:
------------------------
python astar_maze.py

Example:
========
Input:
------
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 S 1 G 1
1 1 1 1 1
here: S = Start | G = Goal | 1 = Wall | 0 = Empty

Output:
=======
Path found!
<img width="1920" height="1008" alt="Screenshot 2026-02-11 115930" src="https://github.com/user-attachments/assets/8c5deb92-9c64-4385-941c-ea0e644a41cf" />
