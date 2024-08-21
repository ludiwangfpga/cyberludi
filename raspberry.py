import math
import time
from concurrent.futures import ThreadPoolExecutor


def calculate_angles(X, Y, Z):
    # 初始化参数
    a1, a2, a3, a4 = 4, 6, 6, 6  # a1为底部圆台高度，剩下三个为三个机械臂长度
    P = 8  # 底部圆盘半径
    # 计算j1的值
    if X == 0 and Y < 0:
        j1 = 180
    elif X == 0 and Y >= 0:
        j1 = 0
    else:
        j1 = math.atan(Y / X) * (180 / math.pi)
        if X < 0:
            j1 += 180
        elif Y < 0:
            j1 += 360

    # 设置i为61
    i = 61
    j_all = math.pi * i / 180

    len_ = math.sqrt(Y ** 2 + X ** 2) - P
    high = Z - a1

    L = math.sqrt(len_ ** 2 + high ** 2) - a4 * math.cos(j_all)
    H = high - a4 * math.sin(j_all)

    Cosj3 = (L ** 2 + H ** 2 - a2 ** 2 - a3 ** 2) / (2 * a2 * a3)
    Cosj3 = min(max(Cosj3, -1), 1)  # 保证Cosj3的值在[-1, 1]之间

    Sinj3 = math.sqrt(1 - Cosj3 ** 2)
    j3 = math.atan2(Sinj3, Cosj3) * (180 / math.pi)

    K2 = a3 * Sinj3
    K1 = a2 + a3 * Cosj3

    Cosj2 = (L * K1 + H * K2) / (K1 ** 2 + K2 ** 2)
    Sinj2 = (L * K2 - H * K1) / (K1 ** 2 + K2 ** 2)
    j2 = math.atan2(Sinj2, Cosj2) * (180 / math.pi)

    j4 = 90 - (j2 + j3)

    if j2 >= 0 and j3 >= 0 and abs(j4) <= 90:
        return j1, j2, j3, j4
    else:
        return None


def perform_calculation(iteration):
    X, Y, Z = 1, 1, 1
    angles = calculate_angles(X, Y, Z)
    if angles:
        j1, j2, j3, j4 = angles
        print(f"Iteration {iteration + 1}: j1 = {j1:.2f}, j2 = {j2:.2f}, j3 = {j3:.2f}, j4 = {j4:.2f}")
    else:
        print(f"Iteration {iteration + 1}: No valid solution found.")
    return angles


# 开始计时
start_time = time.time()

# 使用并行处理计算1800次，并利用32个核心
with ThreadPoolExecutor(max_workers=32) as executor:
    executor.map(perform_calculation, range(1800))

# 结束计时
end_time = time.time()
total_time = end_time - start_time

print(f"Total time for 1800 parallel iterations using 32 cores: {total_time:.6f} seconds")
