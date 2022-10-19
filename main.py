import matplotlib.image as mpimg
import matplotlib.pyplot as plt

##################---- MAIN FUNCTIONS----##################
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
  plt.savefig(f'/home/willian/colour_blindness/output/new_img.png')

##################---- FILTER ----##################
def rotate90_img(img:list)->list:
  height = len(img[0])
  width = len(img)
  new_img = []

  for i in range(height):
    row = []
    for j in range(width):
      row.insert(0,img[j][i])
    new_img.append(row)

  return new_img

##################---- RUN ----##################
def run():
  image_view(rotate90_img(upload_img('/home/willian/colour_blindness/content/tech.png'))) # Image route

if __name__ == '__main__':
  run()
