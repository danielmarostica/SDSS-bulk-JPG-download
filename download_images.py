import urllib.request
import pandas as pd
import numpy as np
from sys import argv

#See README file.

data = pd.read_csv("data.csv")
images = data.iloc[:, 0:2].values

start = int(argv[1])
end = int(argv[2])

def download_galaxy():
    for i in range(start, end):
        try:
            url = "http://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?ra={}&dec={}".format(images[i,0],images[i,1])
            img = "image_{:04d}.jpg".format(i)
            print("Downloading galaxy {}...".format(i))
            urllib.request.urlretrieve(url, img)
        except:
            print("Skipped galaxy {}. Not found.".format(i))
            pass


download_galaxy()
