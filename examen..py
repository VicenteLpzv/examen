#Vicente Yahir Lopez Vazquez - 240010
c1 = 'hugo'
c2 = 'paco'
c3 = 'luis'

v1 = 0  # Votos para hugo
v2 = 0  # Votos para paco
v3 = 0  # Votos para luis


print("votacion de los 15 alumnos (escriba el nombre del candidato: hugo, paco o luis)")

a = 1  
while a <= 15:
    voto = input(f"alumno {a}, ingrese su voto: ")  
    if voto == c1:
        v1 += 1
        a += 1  
    elif voto == c2:
        v2 += 1
        a += 1
    elif voto == c3:
        v3 += 1
        a += 1
    else:
        print("voto invalido. por favor, ingrese 'hugo', 'paco' o 'luis'.")
t = v1 + v2 + v3

if v1 >= v2 and v1 >= v3:
    p1, vp1 = c1, v1
    if v2 >= v3:
        p2, vp2 = c2, v2
        p3, vp3 = c3, v3
    else:
        p2, vp2 = c3, v3
        p3, vp3 = c2, v2
        
elif v2 >= v1 and v2 >= v3:
    p1, vp1 = c2, v2
    if v1 >= v3:
        p2, vp2 = c1, v1
        p3, vp3 = c3, v3
    else:
        p2, vp2 = c3, v3
        p3, vp3 = c1, v1
else:
    p1, vp1 = c3, v3
   
porc1 = (vp1 / t) * 100
porc2 = (vp2 / t) * 100
porc3 = (vp3 / t) * 100
print("resultados de la votacion:")
print(f"jefe de grupo: {p1} con {vp1} votos ({porc1:.2f}%)")
print(f"tesorero: {p2} con {vp2} votos ({porc2:.2f}%)")
print(f"gracias por su participacion a: {p3} con {vp3} votos ({porc3:.2f}%)")
