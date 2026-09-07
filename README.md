# Particle System Simulator

An interactive lattice simulation for studying **active particle systems**: how self-propelled particles interacting through excluded volume spontaneously form clusters. Developed as a research project supervised by [Prof. Alexandre Stauffer](https://www.kcl.ac.uk/people/alexandrestauffer) (King's College London).

📄 **[Read the full project report (PDF)](report/Simulation_Study_of_Active_Particle_Systems.pdf)**: model definitions, clustering-time statistics, and analysis of metastable states.

![Simulation of an active particle system forming a cluster](https://github.com/user-attachments/assets/1eaee7a4-4dcd-4ca5-a856-07d9f6567ff3)

## The model

Particles live on a 2D torus (an `N × N` grid with periodic boundaries), with at most one particle per site. At initialization, each site is occupied independently with probability `mu`, and each particle is designated **active** with probability `alpha` or **passive** otherwise.

At every step, a randomly chosen particle attempts a move:

- An **active** particle carries a direction (up/down/left/right). With probability `delta` it *tumbles* (picks a fresh random direction); it then steps in its current direction with probability `epsilon`, or takes a uniformly random step otherwise.
- A **passive** particle performs a simple symmetric random walk.
- A move succeeds only if the target site is empty (excluded volume / hard-core interaction).

Despite these purely local rules, the system exhibits rich collective behavior: for suitable parameter regimes, active particles jam against one another and nucleate large, long-lived clusters, a lattice analogue of motility-induced phase separation.

| Parameter | Meaning |
|-----------|---------|
| `mu` | particle density (initial occupation probability per site) |
| `alpha` | probability that a particle is active rather than passive |
| `delta` | tumbling probability (active particles pick a new direction) |
| `epsilon` | probability an active particle follows its direction instead of stepping randomly |

## Features

- **Real-time visualization** with pygame: watch clusters nucleate, grow, and dissolve, with pause, single-step, and speed controls.
- **Cluster statistics**: cluster cardinality via breadth-first search on the occupancy grid, Manhattan and Euclidean cluster radii, and ring-based occupancy measurements around the world center.
- **Parameter sweep experiments**: scripts that vary the density `mu` and record the time for the system to reach a clustered state.
- **One-dimensional variant**: a companion implementation of the model on a ring, with its own renderer.

## Getting started

Requires Python 3.10+.

```bash
git clone https://github.com/MichelFaloughi/Particle-System-Simulator.git
cd Particle-System-Simulator
pip install -r requirements.txt
python Main.py
```

Model and world parameters (grid size, `mu`, `delta`, `epsilon`, `alpha`, …) are set at the top of `Main.py`.

### Controls

| Key | Action |
|-----|--------|
| `Space` | pause / resume |
| `F` | advance a single step while paused |
| `D` / `S` | speed up / slow down the refresh rate |
| `R` | toggle rendering (run the dynamics at full speed without drawing) |
| `E` | exit the simulation |

## Repository layout

| File | Description |
|------|-------------|
| `Main.py` | entry point; runs the interactive 2D simulation |
| `ParticleSystem.py` | the 2D world: dynamics loop, rendering, and cluster statistics |
| `Particle.py` | a single particle (active or passive) and its update rule |
| `OneDimensionalMain.py`, `OneDimensionalParticleSystem.py`, `OneDimensionalParticle.py` | the 1D variant of the model |
| `experimental_main.py` | sweeps the density `mu` and records the time to reach a clustered state |
| `middle_experiment.py` | earlier experiment studying the stability of a seeded central cluster |
| `main.ipynb` | parameter sweeps and plots (cluster cardinality over time, phase behavior) |
| `global_variables.py` | shared constants (lattice directions) |
| `report/` | the full project report (PDF) |

## Acknowledgements

This project was carried out under the supervision of Prof. Alexandre Stauffer at King's College London.

## License

[MIT](LICENSE)
