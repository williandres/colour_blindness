import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import daltonism as dalt

##################---- MAIN FUNCTIONS----##################
def upload_img(route:str)->list:
  return mpimg.imread(route).tolist()

def image_view(img:list)->None:
  plt.imshow(img)
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