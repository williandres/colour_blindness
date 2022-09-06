import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def run():
  upload_image(route)

def upload_image():
  matrix = mpimg.imread(route).tolist()
  height = len(matriz)
  width = len(matriz[0])
  img = []
  for i in range(alto):
    row = []
      for j in range(ancho):
        r = matriz[i][j][0]
        g = matriz[i][j][1]
        b = matriz[i][j][2]
        rgb = (r, g, b)
        row.append(rgb)
    img.append(row)
  
  return imagen

if __name__ == '__main__':
  run()