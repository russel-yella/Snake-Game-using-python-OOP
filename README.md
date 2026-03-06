# Snake Game 🐍

## Description

This project is a classic **Snake Game** built using **Python** and the **Turtle graphics module**. The player controls a snake that moves around the screen, eats food to grow longer, and avoids colliding with the walls or its own tail.

The game tracks both the **current score** and the **highest score** achieved during gameplay.

---

## Features

* Smooth snake movement
* Arrow key and **WASD** controls
* Random food spawning
* Snake grows when food is eaten
* Collision detection with walls and snake tail
* Score tracking
* High score tracking

---

## Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Object-Oriented Programming (OOP)**

---

## Project Structure

```
snake-game/
│
├── main.py          # Main game loop and screen setup
├── snake.py         # Snake class and movement logic
├── food.py          # Food generation and random placement
├── scoreboard.py    # Score and high score display
└── README.md        # Project documentation
```

---

## Installation

1. Make sure **Python 3** is installed on your computer.
2. Clone this repository or download the project files.
3. Navigate to the project folder.

---

## Running the Game

Run the main file:

```
python main.py
```

A game window will open and the snake will start moving.

---

## Controls

| Key         | Action     |
| ----------- | ---------- |
| ↑ Arrow / W | Move Up    |
| ↓ Arrow / S | Move Down  |
| ← Arrow / A | Move Left  |
| → Arrow / D | Move Right |

---

## Game Rules

1. Control the snake and guide it to the food.
2. Each time the snake eats food, it grows longer and the score increases.
3. Avoid hitting the walls.
4. Avoid colliding with the snake’s own body.
5. If a collision occurs, the game resets while keeping track of the highest score.

---

## Concepts Demonstrated

This project demonstrates several programming concepts:

* Object-Oriented Programming
* Class inheritance
* Event-driven programming
* Collision detection
* Game loops
* Working with multiple Python modules

---
.
