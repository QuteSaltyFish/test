# %%
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import time
# %%
# pyautogui.mouseInfo()
computer = np.array([
    59.99, 10.99*3, 66.99, 49.99, 54.99,
])
print(np.sum(computer))

others = np.array([
    5.83, 239.99, 107.99, 152.35, 59.99, 139.99, 53.99
])
print(np.sum(others))
# %%
time.sleep(10)
for i in range(10):
    pyautogui.hscroll(-10)
    time.sleep(3)

# %%
time.sleep(10)
for i in range(10):
    pyautogui.hscroll(-10)
    time.sleep(3)
    pyautogui.hscroll(10)
    time.sleep(3)

# %%
pyautogui.size()
# %%
pyautogui.position()
# %%
pyautogui.hscroll(-10)
# %%
