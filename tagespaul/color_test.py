import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import colors as mcolors

from matplotlib import cm

print(cm.jet(0))


# def increase_to_color(j, color = [0,0,256]):

#     j = j % 256

#     rgb = [
#     int(color[0] / 256 * j), 
#     int(color[1] / 256 * j), 
#     int(color[2] / 256 * j)
#     ]

#     print(rgb)

#     return(rgb)

# # # fig = plt.figure()

# # # ax = fig.add_subplot(111)

# # t = np.linspace(0,2*np.pi, 15)
# # x = np.cos(t)
# # y = np.sin(t)

# # # colors = [0,0,0]

# # # ax.scatter(x, y, s=80, color = colors)

# # plt.ion()

# for j in range(500):

#     rgb = increase_to_color(j)

#     print(rgb)

#     # rgb = [rgb[0] / 256, rgb[1] / 256, rgb[2] / 256]

#     # colors = [mcolors.to_rgba(rgb) for i in t]

#     # plt.scatter(x, y, s=80, color = colors)
#     # plt.draw()
#     # plt.pause(0.0001)
#     # plt.clf()
#     # colors = mcolors.to_rgba(rgb)

#     # colors = colors)    

#     # print(colors)
#     # exit()

#     # ax.set_facecolor(colors)    

#     # fig.canvas.draw()
#     # fig.canvas.flush_events()