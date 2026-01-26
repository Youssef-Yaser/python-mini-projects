# =========================
# Shortest Path Finder
# =========================

import curses
from curses import wrapper
import queue
import time

# =========================
# Terminal Colors
# =========================
class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'
    CLEAR = '\033c'  # Clear terminal


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# =========================
# Print Maze with path
# =========================

def print_maze(maze,stdscr,path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i , row in enumerate(maze):
        for j , value in enumerate(row) :
            if (i,j) in path :
                stdscr.addstr(i,j*3, "•", RED)
            else : 
                stdscr.addstr(i,j*3,value , BLUE)

def find_start(maze , start):
    for i , row in enumerate(maze):
        for j , value in enumerate(row) :
            if value == start :
                return i , j
    return None

# =========================
# BFS Shortest Path
# =========================

def find_path(maze,stdscr):
    start = 'O'
    end = "X"
    start_pos = find_start(maze,start)

    q = queue.Queue()
    q.put((start_pos,[start_pos]))

    visited = set()

    while not q.empty():
        current_pos , path = q.get()
        row , col = current_pos 
        stdscr.clear()
        print_maze(maze, stdscr , path)
        time.sleep(0.2)
        stdscr.refresh()


        if maze [row][col] == end :
            return path
        
        neighbors = find_neighbors(maze, row , col)
        for neighbor in neighbors :
            if neighbor in visited :
                continue

            r , c = neighbor 

            if maze[r][c] == "#" :
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)

# =========================
# Get Valid Neighbors
# =========================

def find_neighbors(maze,row,col):
    neighbors = []

    if row > 0 :
        neighbors.append((row-1,col))
    if row +1 < len(maze) :
        neighbors.append((row+1,col))
    if col > 0:
        neighbors.append((row , col-1)) 
    if col +1 < len(maze[0]) :
        neighbors.append((row , col+1)) 

    return neighbors    

# =========================
# Main Function
# =========================

def main(stdscr) :
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    blueblack= curses.color_pair(1)

    find_path(maze , stdscr)

    # Final display
    stdscr.addstr(len(maze) + 2, 0,"Shortest path found! Press any key to exit..." )
    stdscr.getch()

    
wrapper(main)    