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

##################---- FILTER ----##################
def protanopia_sim(img:list)->list:
  height = len(img)
  width = len(img[0])
  new_img = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(daltsim.p(img[i][j])) # p = protanopia, d = deuteranopia, t = tritanopia
    new_img.append(row)
  print("---"*5)
  print("ROJO")
  print("---"*5)
  print(new_img[290][140])
  print(new_img[290][155])
  print(new_img[290][175])
  print("---"*5)
  print("ROSADO")
  print("---"*5)
  print(new_img[290][230])
  print(new_img[290][250])
  print(new_img[290][270])
  print("---"*5)
  print("NARANJA")
  print("---"*5)
  print(new_img[290][120])
  print(new_img[290][80])
  print(new_img[290][100])
  print("---"*5)
  print("VERDE")
  print("---"*5)
  print(new_img[290][620])
  print(new_img[290][650])
  print(new_img[290][690])
  print("---"*5)
  print("AMARILLO")
  print("---"*5)
  print(new_img[290][30])
  print(new_img[290][10])
  print(new_img[290][774])
  print("---"*5)
  print("CYAN")
  print("---"*5)
  print(new_img[290][550])
  print(new_img[290][525])
  print(new_img[290][580])
  print("---"*5)
  print("AZUL OSUCURO")
  print("---"*5)
  print(new_img[290][355])
  print(new_img[290][390])
  print(new_img[290][400])
  print("---"*5)
  print("AZUL CLARO")
  print("---"*5)
  print(new_img[290][440])
  print(new_img[290][460])
  print(new_img[290][480])
  print("---"*5)
  print("VIOLETA")
  print("---"*5)
  print(new_img[290][280])
  print(new_img[290][305])
  print(new_img[290][325])

  return new_img

##################---- RUN ----##################
def run():
  image_view(protanopia_sim(upload_img('/home/willian/colour_blindness/content/proto.png'))) # Image route

if __name__ == '__main__':
  run()