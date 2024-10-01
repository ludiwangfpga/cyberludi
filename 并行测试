import math
import numpy as np
from timebudget import timebudget
from multiprocessing import Pool

# Parameters for the robot arm calculations
X, Y, Z = 1, 1, 1  # Position coordinates
a1, a2, a3, a4 = 4, 6, 6, 6  # Robot arm lengths
P = 8  # Radius of the base disc
if X == 0 and Y < 0:
    j1 = 180
elif X == 0 and Y >= 0:
    j1 = 0
else:
    j1 = math.atan(Y / X) * (180 / math.pi)
    if X < 0:
        j1 += 180
    elif Y < 0:
        j1 += 360# Fixed j1 angle

def calculate_joint_angles(input_index):
    print("Calculating joint angles. Input index: {:2d}".format(input_index))

    step_size = 0.1  # 每次增加的步长
    for _ in np.arange(0, 180, step_size):  # Repeat the calculations 181 times

        j_all = math.pi * _ / 180
        len_ = math.sqrt(Y ** 2 + X ** 2) - P
        high = Z - a1

        L = math.sqrt(len_**2 + high**2) - a4 * math.cos(j_all)
        H = high - a4 * math.sin(j_all)

        Cosj3 = (L**2 + H**2 - a2**2 - a3**2) / (2 * a2 * a3)
        Cosj3 = min(max(Cosj3, -1), 1)  # Ensure Cosj3 is within [-1, 1]

        Sinj3 = math.sqrt(1 - Cosj3**2)
        j3 = math.atan2(Sinj3, Cosj3) * (180 / math.pi)

        K2 = a3 * Sinj3
        K1 = a2 + a3 * Cosj3

        Cosj2 = (L * K1 + H * K2) / (K1**2 + K2**2)
        Sinj2 = (L * K2 - H * K1) / (K1**2 + K2**2)
        j2 = math.atan2(Sinj2, Cosj2) * (180 / math.pi)

        j4 = 90 - (j2 + j3)
        if j4 >=1000000:
            print(" ")


@timebudget
def run_joint_angle_calculations(operation, input, pool):
    pool.map(operation, input)

# Number of processes to use
processes_count = 32

if __name__ == '__main__':
    processes_pool = Pool(processes_count)
    run_joint_angle_calculations(calculate_joint_angles, range(1000), processes_pool)

