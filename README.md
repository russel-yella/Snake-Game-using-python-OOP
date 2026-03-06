# Snake Game 🐍

## Description

This is a classic **Snake Game** built using Python and the Turtle graphics module. The player controls a snake that grows by eating food while avoiding collisions with walls and its own body.

The game features:

* Score tracking
* High score persistence
* Sound effects for eating and collisions
* Smooth movement and increasing difficulty

---

## Features

* Smooth snake movement
* Arrow key and WASD controls
* Random food spawning
* Score and high score tracking
* Persistent high score (saved to file)
* Sound effects for:

  * Eating food
  * Collisions / game over
* Increasing speed as the snake grows
* Collision detection with walls and tail

---

## Technologies Used

* Python 3
* Turtle Graphics
* Pygame (for sound effects)
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
snake-game/
│
├── main.py          # Game loop and screen setup
├── snake.py         # Snake movement and logic
├── food.py          # Food generation and placement
├── scoreboard.py    # Score and high score display
├── collision.wav    # Sound effect for collisions
├── eat.wav          # Sound effect for eating
├── README.md        # Documentation
```

---

## Installation

1. Make sure Python 3 is installed.
2. Install pygame (for sound support):

```bash
pip install pygame
```

3. Clone or download the repository.
4. Ensure sound files (`eat.wav`, `collision.wav`) are in the project folder.

---

## Running the Game

Run the main file:

```bash
python main.py
```

A game window will open and the snake will start moving.

---

## Controls

| Key   | Action     |
| ----- | ---------- |
| ↑ / W | Move Up    |
| ↓ / S | Move Down  |
| ← / A | Move Left  |
| → / D | Move Right |

---

## Game Rules

1. Eat the red food to grow and score points.
2. Avoid hitting the walls.
3. Avoid colliding with your own tail.
4. Game resets on collision but high score is saved.
5. Sound effects enhance gameplay feedback.

---

## Concepts Practiced

This project demonstrates:

* Object-Oriented Programming
* Event-driven programming
* Collision detection
* Game loops
* File handling (high score persistence)
* Multimedia integration (sound effects)

---

## Repository

Hosted on GitHub: https://github.com/russel-yella/Snake-Game-using-python-OOP
