precioAdulto= 80
precioInfante= 40
precioTerceraEdad= 20 

print("Cartelera")
print("Avengers: Doomsday 4:00pm")
print("Resident Evil 5:00pm")
print("Corazón de la Bestia 6:00pm")
print("Harry Potter 7:00pm")

print("Precio Adulto", precioAdulto)
print("Precio Infantes", precioInfante)
print("Precio Adulto Mayor", precioTerceraEdad)

peliculas= ["Avengers: Doomsday", "Resident Evil", "Corazón de la Bestia", "Harry Potter"]
selecciónPelicula = input ("Ingrese la pelicula: ")
edad= int(input("Ingrese su edad: "))

if selecciónPelicula == "Resident Evil":
    if edad < 18:
        print("Para mayores de 18, no se puede vender el boleto")

else:

    if selecciónPelicula == "Avengers: Doomsday" or selecciónPelicula == "Resident Evil" or selecciónPelicula == "Corazón de la Bestia" or selecciónPelicula == "Harry Potter":

        print("Película seleccionada:", selecciónPelicula)

        if edad < 12:

            print("Categoría: Infante")
            print("Precio:", precioInfante)

        elif edad < 65:

            print("Categoría: Adulto")
            print("Precio:", precioAdulto)

        else:

            print("Categoría: Tercera Edad")
            print("Precio:", precioTerceraEdad)

    else:

        print("Película no encontrada")