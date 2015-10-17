"""
benchmark 0.7.0

A suite of worlds to characterize the performance of BECCA variants.
Other agents may use this benchmark as well, as long as they have the 
same interface. (See BECCA documentation for a detailed specification.)
In order to facilitate apples-to-apples comparisons between agents, the 
benchmark will be version numbered.

The length of the training and testing epochs are somewhat arbitrary.
Feel free to adjust them if doing so better captures the ultimate
performance of an agent on the tasks.

Run at the command line as a script with no argmuments:
> python benchmark.py

Becca 0.7.0 performance:
Individual benchmark scores:  []
Overall benchmark score: 
"""
import matplotlib.pyplot as plt
import numpy as np
import tester
from core.brain import Brain

# Import all the world classes that are in the benchmark collection
from worlds.grid_1D import World as World_grid_1D
from worlds.grid_1D_delay import World as World_grid_1D_delay
from worlds.grid_1D_ms import World as World_grid_1D_ms
from worlds.grid_1D_noise import World as World_grid_1D_noise
from worlds.grid_2D import World as World_grid_2D
from worlds.grid_2D_dc import World as World_grid_2D_dc
from worlds.image_1D import World as World_image_1D
from worlds.image_2D import World as World_image_2D
from worlds.fruit import World as World_fruit

def main():
    """
    Run all the worlds in the benchmark and tabulate their performance.
    """
    performance = []
    performance.append(tester.train_and_test(World_grid_1D))
    performance.append(tester.train_and_test(World_grid_1D_delay))
    performance.append(tester.train_and_test(World_grid_1D_ms))
    performance.append(tester.train_and_test(World_grid_1D_noise))
    performance.append(tester.train_and_test(World_grid_2D))
    performance.append(tester.train_and_test(World_grid_2D_dc,
                                             training_period=2e4))
    performance.append(tester.train_and_test(World_image_1D))
    performance.append(tester.train_and_test(World_image_2D,
                                             training_period=2e4))
    performance.append(tester.train_and_test(World_fruit))
    print('Individual benchmark scores: {0:.2}'.format(performance))
    print('Overall benchmark score: {0:.2}'.format(np.mean(performance))) 
    
    # Block the program, displaying all plots.
    # When the plot windows are closed, the program closes.
    plt.show()
    
if __name__ == '__main__':
    main()
