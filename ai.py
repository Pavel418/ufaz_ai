import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

data = pn.read_csv('binaaz_train.csv')
data.describe()