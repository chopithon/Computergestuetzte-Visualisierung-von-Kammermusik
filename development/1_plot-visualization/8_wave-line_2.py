# datasets
# problem: only one line (for datasets?)

from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

datasets = [{"x":[10,20,30], "y":[1,4,9], "colour": "red"} for _ in range(6)]

for dataset in datasets:
    ax.plot(dataset["x"], dataset["y"], color=dataset["colour"])

plt.show()

# source: Stack Over Flow: https://stackoverflow.com/questions/65683016/plotting-multiple-colored-lines-and-vectors-in-3d-with-matplotlib (23.06.22)