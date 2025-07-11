# Particle System Simulation

Simulation Study of Interactive Particle Systems for Active Matter

Working under Professor Alexandre Stauffer at King's College London

## Project Overview

This project implements a particle system simulation for studying active matter dynamics. The simulation models particles that can move, cluster, and interact based on various parameters including density, direction change probability, and activity levels.

## Project Structure

```
particle_system_simulation/
├── src/                          # Source code
│   ├── core/                     # Core simulation components
│   │   ├── particle.py           # Particle class
│   │   ├── particle_system.py    # Main simulation system
│   │   └── one_dimensional/      # 1D variant
│   ├── utils/                    # Utilities and helpers
│   │   └── constants.py          # Global variables and constants
│   └── experiments/              # Experiment scripts
├── data/                         # Data storage
│   ├── raw/                      # Raw simulation outputs
│   ├── processed/                # Processed/analyzed data
│   └── results/                  # Final results and figures
├── notebooks/                    # Jupyter notebooks
│   ├── exploration/              # Experimental notebooks
│   ├── analysis/                 # Data analysis notebooks
│   └── visualization/            # Visualization notebooks
├── assets/                       # Static assets
│   └── images/                   # Images and icons
├── scripts/                      # Utility scripts
│   └── run_simulation.py         # Main entry point
├── tests/                        # Unit tests
├── docs/                         # Documentation
├── requirements.txt              # Python dependencies
└── setup.py                      # Package setup
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd particle-system-simulation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install the package in development mode:
```bash
pip install -e .
```

## Usage

### Running the Main Simulation

```bash
python scripts/run_simulation.py
```

### Running 1D Simulation

```bash
python src/core/one_dimensional_main.py
```

### Using Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

## Key Parameters

- **mu (μ)**: Density parameter - probability of particle spawning
- **delta (δ)**: Direction change probability
- **epsilon (ε)**: Probability to follow normal direction
- **alpha (α)**: Probability for a particle to be active
- **dot_size**: Visual size of particles
- **refresh_rate**: Display update frequency

## Controls

- **SPACE**: Pause/Resume simulation
- **R**: Restart simulation
- **D**: Increase speed
- **S**: Decrease speed
- **F**: Step forward one iteration
- **E**: Exit simulation

## Data Output

Simulation results are saved to:
- `data/raw/ParticleSystem_database.xlsx` - Run database
- `data/raw/run_ids.txt` - Run ID tracking

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

The project follows PEP 8 style guidelines.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Professor Alexandre Stauffer for academic supervision
- King's College London for research support
