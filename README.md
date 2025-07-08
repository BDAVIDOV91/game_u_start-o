# 2D Side-Scrolling Platformer

## Project Overview

This is a 2D side-scrolling platformer game, inspired by classics like Super Mario. The goal is to create a game where a player character navigates various levels, jumping, running, avoiding obstacles, and interacting with enemies to reach an exit point. The project emphasizes polished mechanics, smooth movement, and engaging gameplay.

## Features

### Core Gameplay
-   **Player Movement:** Responsive controls for left, right, and jump actions, including a double jump mechanic.
-   **Platforms:** Static platforms for player navigation.
-   **Enemies:** Basic patrolling enemies that turn at platform edges. Player takes damage and becomes temporarily invincible with blinking effect upon collision.
-   **Collision Detection:** Accurate collision handling for player-platform and player-enemy interactions.
-   **Lives System:** Player has a limited number of lives, displayed on the UI.
-   **Respawn System:** Player respawns at the last safe position after losing a life (from falling into a hole or enemy hit).
-   **Game States:** Implemented game running and game over states. Game over screen provides options to restart or quit.
-   **Level Loading:** Levels are loaded from simple text files, allowing for easy level design.
-   **Invisible Wall:** Prevents player from moving left past the starting point.

### Visuals & Audio
-   **Sprite Animations:** Basic player animations for idle, run, jump, and fall states.
-   **Camera System:** A camera that follows the player, enabling side-scrolling.

## Setup and Installation

To get the game running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd game_u_start-o # Or the directory where you cloned the project
    ```

2.  **Create a Python virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Game

1.  **Activate your virtual environment** (if not already active, see Setup steps 2 and 3).
2.  **Navigate to the `platformer` directory:**
    ```bash
    cd platformer
    ```
3.  **Run the main game file:**
    ```bash
    python main.py
    ```

## Controls

-   **Left Arrow Key:** Move player left
-   **Right Arrow Key:** Move player right
-   **Spacebar:** Jump
-   **R Key (from Game Over screen):** Restart the game
-   **Q Key (from Game Over screen):** Quit the game

## Project Structure

```
platformer/
│
├── assets/              # All images, sprites, sounds, and level files
│   ├── images/
│   │   └── player/      # Player sprite images
│   ├── sounds/          # (Planned)
│   └── levels/          # Level data files (e.g., level1.txt)
│
├── core/
│   ├── player.py        # Player logic, movement, and animations
│   ├── enemy.py         # Enemy classes and AI
│   ├── platform.py      # Platforms and collision logic
│   ├── level.py         # Level loading and generation
│   ├── camera.py        # Camera and scrolling logic
│   └── utils.py         # Utility functions (e.g., custom collision checks)
│
├── main.py              # Main game loop, state management, and initialization
├── settings.py          # Game constants and configurations (screen size, FPS, colors, etc.)
├── ui.py                # User interface elements (score display, menus)
├── save_manager.py      # Handles saving and loading game progress (Planned)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Future Improvements (Planned)

-   **Advanced Enemy Types:** Implement enemies with more complex behaviors (e.g., chasing, shooting).
-   **Collectibles:** Add coins, power-ups, and other items for players to collect.
-   **Hazards:** Introduce spikes, pits, and other traps.
-   **Sound and Music:** Integrate background music and sound effects.
-   **More Levels:** Design and implement multiple levels with increasing difficulty.
-   **Refined Animations:** Add more detailed player and enemy animations.
-   **Boss Enemies:** Introduce unique boss encounters.
-   **Weapons/Power-ups:** Implement player abilities like fireballs or shields.
-   **Level Selection Screen:** A dedicated screen for choosing levels.

---