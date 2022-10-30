from numba import njit

@njit
def p(pixel:list)->list:
    new_pixel = [pixel[0]*255, pixel[1]*255, pixel[2]*255, pixel[3]]

    #new_pixel = [pixel[0]/255, pixel[1]/255, pixel[2]/255, pixel[3]]
    return new_pixel
