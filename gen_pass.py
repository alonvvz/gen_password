import random

def gen(longs):
    cars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = "".join(random.choice(cars) for i in range(longs))
    print("La clave generada es:", contra)
    return contra

claveaa = int(input("Longitud clave: "))
claveb = gen(longs=claveaa)
