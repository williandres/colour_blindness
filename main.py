import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import daltonism_simulator as daltsim
import daltonism_friendly as daltfri

##################---- MAIN FUNCTIONS----##################
def upload_img(route:str)->list:
  return mpimg.imread(route).tolist()

def image_view(img:list)->None:
  plt.imshow(img)
  plt.axis('off')
  plt.savefig(f'/home/willian/colour_blindness/output/new_img.png', bbox_inches='tight', pad_inches=0, dpi=1200)

##################---- SIMULATION ----##################
def sim(img:list)->list:
  height = len(img)
  width = len(img[0])
  new_img = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(daltsim.p(img[i][j])) # p = protanopia, d = deuteranopia, t = tritanopia
    new_img.append(row)
  return new_img

##################---- RUN ----##################
def run():
  image_view(sim(upload_img('/home/willian/colour_blindness/content/normal.png'))) # Image route

if __name__ == '__main__':
  run()