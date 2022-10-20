import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import daltonism as dalt

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
  plt.axis('off')
  plt.savefig(f'/home/willian/colour_blindness/output/new_img.png', bbox_inches='tight', pad_inches=0, dpi=1200)

##################---- FILTER ----##################
def protanopia(img:list)->list:
  height = len(img)
  width = len(img[0])
  new_img = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(dalt.p(img[i][j])) # p = protanopia, d = deuteranopia, t = tritanopia
    new_img.append(row)
  return new_img

##################---- RUN ----##################
def run():
  image_view(upload_img('/home/willian/colour_blindness/content/art.png')) # Image route

if __name__ == '__main__':
  run()