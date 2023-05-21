import cv2
import matplotlib.pyplot as plt
import os

def saveImg(path):
  image = cv2.imread(path)
  height, width = image.shape[:2]
  cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)
  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  # Save the image to a file
  filename, file_extension = os.path.splitext(path)
  filepath = "/" + filename + file_extension
  plt.savefig(filepath)
  return filepath