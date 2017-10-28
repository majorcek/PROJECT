# Script for generating data and exporting it into csv
# When run, it will generate 4 csv files

from functions import *

# For each parameter, the different points will be generated 4000 times.
# We will look for and save min, max and average of:
#   - length of the convex hull,
#   - its area,
#   - the number of times it included the inner circle
#   - the probability of including it

# 'r' will go from 0 to 1 with 0.01 intervals
# 'n' will take the values 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 100, 200, 500

times = 4000
r_array = np.linspace(0, 1, 101)
n_array = np.array([3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 100, 200, 500])


save_to_csv(r_array,n_array,times)
