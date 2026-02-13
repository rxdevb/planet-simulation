# Planet Simulation

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-333333?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## About The Project

Planet Simulation is a physics-based visualization of the Solar System. It calculates gravitational forces between celestial bodies using Kepler's laws to create a realistic orbital simulation.

The project features a dynamic zoom system that allows users to explore both the inner, rocky planets and the outer gas giants, bridging the vast scale differences of our solar system.

### Built With

*   **Language**: Python 3.14
*   **Graphics Engine**: Pygame 2.6.1
*   **Testing**: Pytest

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python (v3.8 or higher)

### Installation

1.  **Clone the repository**
    ```sh
    git clone https://github.com/your_username/planet-simulation.git
    cd planet-simulation
    ```

2.  **Setup Environment**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install pygame pytest
    ```

3.  **Run Simulation**
    ```sh
    python main.py
    ```

## Usage

*   **Launch**: Run `python main.py` to start the window.
*   **Zoom In**: Scroll **UP** with the mouse wheel to see inner planets (Mercury, Venus, Earth, Mars).
*   **Zoom Out**: Scroll **DOWN** with the mouse wheel to see the full solar system including Jupiter, Saturn, Uranus, and Neptune.

## Features

*   **N-Body Physics**: Calculates gravitational attraction between every pair of planets.
*   **Dynamic Zoom**: Solves the "scale problem" of visualizing the solar system.
*   **Full Solar System**: Includes the Sun and all 8 major planets with accurate relative masses and initial velocities.
*   **Visual Enhancements**: Orbital trails and distinct colors for each planet.

## Testing

This project maintains code quality through automated unit tests that verify the physics engine.

To run tests:
```sh
pytest test_simulation.py
```

## Structure

*   `main.py` - The core simulation loop and rendering logic.
*   `test_simulation.py` - Unit tests verifying the `Planet` class and gravity calculations.
