import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def upload_img(route)->list:
  mat = mpimg.imread(route).tolist()
  height = len(mat)
  width = len(mat[0])
  img = []

  for i in range(height):
    row = []
    for j in range(width):
      r = mat[i][j][0]
      g = mat[i][j][1]
      b = mat[i][j][2]
      pixel = (r, g, b)
      row.append(pixel)
    img.append(row)

  return img

def image_view(img:list)->None:
  height = len(img)
  width = len(img[0])
  mat = []
  for i in range(height):
    row = []
    for j in range(width):
      r, g, b = img[i][j]
      row.append([r, g, b])
    mat.append(row)
  plt.imshow(mat)
  plt.show

def run():
  upload_img('image.png') # Image route


if __name__ == '__main__':
  run()
