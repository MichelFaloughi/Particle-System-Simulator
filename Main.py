"""Entry point: run the interactive 2D particle system simulation."""
from ParticleSystem import ParticleSystem

# World and model parameters
WORLD_WIDTH = 90
WORLD_HEIGHT = 90
DELTA = 0.0001          # probability for an active particle to change direction
MU = 0.4                # particle density (probability a site is initially occupied)
EPSILON = 0.9           # probability an active particle follows its direction (vs. taking a random step)
ALPHA = 0.8             # probability for a particle to be active rather than a passive random walker
DOT_SIZE = 3            # pixel size of one lattice site
MIDDLE_CLUSTER_SIZE = -1  # -1 disables seeding an initial cluster in the middle of the world
NUM_ITERATIONS = 10**20   # effectively run until the user exits
INIT_REFRESH_RATE = 10
INIT_PAUSED_STATUS = False

running = True
while running:
    world = ParticleSystem(
        WORLD_WIDTH,
        WORLD_HEIGHT,
        DELTA,
        MU,
        EPSILON,
        ALPHA,
        DOT_SIZE,
        MIDDLE_CLUSTER_SIZE,
        NUM_ITERATIONS,
        INIT_REFRESH_RATE,
        INIT_PAUSED_STATUS,
    )

    world.run_simulation()

    user_input = input('Press R to restart the simulation, or any other key to exit: ')
    running = world.get_user_response(user_input)
