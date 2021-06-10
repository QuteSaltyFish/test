# %%
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import time
# %%
# pyautogui.mouseInfo()

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
