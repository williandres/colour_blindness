def p(pixel:list)->list:
    new_pixel = [pixel[0]*255, pixel[1]*255, pixel[2]*255, pixel[3]]

    #red
    if new_pixel[0] > new_pixel[1] + new_pixel[2]:
        r = new_pixel[0]
        if new_pixel[1] + new_pixel[2] < 40:#rojo --->  amarillo oscuro
            new_pixel = [r * 0.55, new_pixel[1] + (r * 0.506), new_pixel[2] + (r * 0.102), new_pixel[3]]
        elif new_pixel[2] > new_pixel[1]:#rosado ---> azul claro apagado !!!!!!!
            new_pixel = [r * 0.306, new_pixel[1] + (r * 0.54), 255, new_pixel[3]]
        else:#naranja ---> amarillo
            new_pixel = [r * 0.6, new_pixel[1] + (r * 0.199), new_pixel[2] + (r * 0.12), new_pixel[3]]

    #green
    if new_pixel[1] > new_pixel[0] + new_pixel[2]:
        g = new_pixel[1]
        if new_pixel[0] + new_pixel[2] < 100:#verde  ---> amarillo
            new_pixel = [g*0.97, g*0.863, new_pixel[2]*0.862, new_pixel[3]]
        elif new_pixel[0] > new_pixel[2]:#amarillo  ---> blanco
            new_pixel = [255, g*0.96, g - (g*0.23), new_pixel[3]]
        else:#cyan --->  amarillo apagado
            new_pixel = [g * 0.92, g*0.88, new_pixel[2]*0.925, new_pixel[3]]

    #blue
    if new_pixel[2] > new_pixel[0] + new_pixel[1]:
        b = new_pixel[2]
        if new_pixel[0] + new_pixel[1] < 150:#azul oscuro  --->  azul oscuro apagado 
            new_pixel = [b*0.9, b*0.9, b*0.9, new_pixel[3]]
        if new_pixel[1] > new_pixel[0]:#azul claro  ---> blanco
            new_pixel = [b*0.16, new_pixel[1]*0.92, b*0.95, new_pixel[3]]
        else:#violeta  ---> azul claro apagado
            new_pixel = [new_pixel[0]*0.001, (b*0.9)*0.32, b*0.5, new_pixel[3]]

    new_pixel = [new_pixel[0]/255, new_pixel[1]/255, new_pixel[2]/255, new_pixel[3]]
    return new_pixel
