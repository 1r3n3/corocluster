# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:52:14 2020

@author: Yannic Sommer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# import csv file as pandas DataFrame
df = pd.read_csv("data.csv")
# df = df[df[:, 2] == "SK Magdeburg"]
# df = df.loc("SK Magdeburg")

# convert it to numpy array
arr = df.to_numpy()

arr = arr[arr[:, 2]=="LK Heinsberg"]

arr = arr.sort(axis=4)

# a = []
# i = 0
# while(arr[i, 2]=="SK Flensburg"):
#     a.append(arr[i, :])
#     i+=1

# a = np.array(a)

# def fermi(x):
#     return 1 / (np.exp(-x)+1)

# x = np.linspace(-10., 10., 1000)

# plt.figure()
# plt.grid()
# plt.plot(x + 10, fermi(x))
# plt.show()

