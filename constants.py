# Constants for cell states
ALIVE = 1
DEAD = 0
DIVIDING = 2
SENESCENT = 3
EMPTY = -1  # New constant for empty spots

# Parameters for probabilities
division_probability = 0.8  # Probability of a cell dividing if space is available
migration_probability = 0.4  # Probability of migration happening during division
senescence_migration_probability = 0.8
death_probability = 0.01  # Probability of death happening per step
constant_senescence_probability = [0.1, 0.01, 0.001, 0.00001]  # Probability of senescence happening during division

# Size of the grid
grid_size_x = 100
grid_size_y = 100
