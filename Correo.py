class Correo:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nCorreo: {}'.format(self.nombre, self.edad, self.correo)


Correo1= Correo('Alvaro', '19', 'Alvsolo23@mail.com')
Correo2= Correo('Atem', '30', 'atemyami.com')
Correo3= Correo('Pedro', '23', 'pedrosolod@mail.com')
Correo4= Correo('Juan', '67', 'jnslo2002@mail.com')
Correo5= Correo('Michel', '6', 'mc2019EL@mail.com')


print(Correo1)
print(Correo2)
print(Correo3)
print(Correo4)
print(Correo5)