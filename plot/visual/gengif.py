import matplotlib.pyplot as plt
import imageio,os
from PIL import Image
GIF = []

path="./png"
test = os.listdir(path)
test = sorted(test, key=lambda x: int(x.split('.',1)[0]))
print(test)
for fn in test:
    GIF.append(imageio.imread(path+'/'+fn))
#GIF = GIF[60:]
imageio.mimsave("./result.gif", GIF, duration=0.2)

