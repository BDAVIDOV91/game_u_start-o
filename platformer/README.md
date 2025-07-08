# Platformer Game

A 2D side-scrolling platformer game built with Pygame.

## Features

- Player movement: left, right, jump
- Player animations (idle, walk)
- Platforms and collision
- Patrolling enemies with platform collision detection
- Scrolling camera
- Scoring system
- Level loading from text files
- Save and load progress

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd platformer-game
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Play

- Run the game:
  ```bash
  python main.py
  ```
- **Controls:**
  - **Left/Right Arrow Keys:** Move the player
  - **Up Arrow Key:** Jump
  - **S:** Save game
  - **L:** Load game
  - **Spacebar:** Start game from the menu
  - **R:** Restart from the game over screen