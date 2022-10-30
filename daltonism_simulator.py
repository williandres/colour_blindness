from numba import njit

@njit
def p(pixel:list)->list:
    new_pixel = [round(pixel[0]*255), round(pixel[1]*255), round(pixel[2]*255), pixel[3]]
    #red
    if new_pixel[0] > new_pixel[1] + new_pixel[2]:
        if new_pixel[1] + new_pixel[2] < 50:#rojo --->  amarillo oscuro
            pass
        elif new_pixel[2] > new_pixel[1]:#rosado ---> azul claro apagado
            pass
        else:#naranja ---> amarillo
            pass

    #green
    if new_pixel[1] > new_pixel[0] + new_pixel[2]:
        if new_pixel[0] + new_pixel[2] < 50:#verde  ---> amarillo
            pass
        elif new_pixel[0] > new_pixel[2]:#amarillo  ---> blanco
            pass
        else:#cyan --->  amarillo apagado
            pass

    #blue
    if new_pixel[2] > new_pixel[0] + new_pixel[1]:
        if new_pixel[0] + new_pixel[1] < 50:#azul oscuro  --->  azul oscuro apagado
            pass
        if new_pixel[1] > new_pixel[0]:#azul claro  ---> blanco
            pass
        else:#violeta  ---> azul claro apagado
            pass

    #new_pixel = [pixel[0]/255, pixel[1]/255, pixel[2]/255, pixel[3]]
    return new_pixel
