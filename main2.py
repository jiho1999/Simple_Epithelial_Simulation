# main.py

from simulation import run_simulation
from constants import *
from utils import plot_combined_results, plot_results

if __name__ == "__main__":
    num_steps = 100

    for senescent_prob in constant_senescence_probability:
        run_simulation(senescent_prob, num_steps)

    # # Directory where Excel files are saved
    input_dir = '.'  # Current directory

    # Generate the combined plots for all senescence probabilities
    plot_combined_results(input_dir)

    #plot_results(input_dir)
    plot_results(input_dir)
