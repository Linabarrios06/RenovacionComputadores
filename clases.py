#import importa en este caso la libreria de json 
#json es una entidad que acumula valores


import json

#Creamos las funciones para modificar

#CLASE
class GestorComputadores:
    
    #METODOS
    def _init_(self):
        self.computadores = []
    
    def agregarComputador(self):
        computador = {} #Datos a pedir al usuario 
        computador["ambiente"] = input("¿A que ambiente pertenece?: ")
        computador["id"] = int(input("Digite el ID del computador: "))
        computador["cargador"] = input("¿El computador tiene CARGADOR (si)/(no)?: ")
        computador["mouse"] = input("¿El computador tiene MOUSE (si)/(no)?: ")
        computador["novedad"] = input("¿Tiene alguna NOVEDAD el computador?: ")
        self.computadores.append(computador)
                                            #Datos guardados
    def guardarDatos(self):
        # Convertir la lista a formato json
        datos = json.dumps(self.computadores, indent=2) #.dumps: es una funcion de json 
                                                        #intend: nos permite serializar un objeto Python a un objeto JSON.
        
        # Guardar en el archivo
        with open('computadores.txt', 'w') as archivo: #open almacena en texto todo lo que emos echo y lo llama
            archivo.write(datos) #escribe un texto específico en el archivo
        print("Datos guardados correctamente!")

    def modificarComputador(self):
        id_modificar = int(input("Digite el ID del computador que desea modificar: ")) #Si se encuentra el id va a dar la opcion de seguir
        for comp in self.computadores:
            if comp["ID"] == id_modificar:
                comp["Novedad"] = input("Ingrese la nueva NOVEDAD para el computador: ")
                print("Computador modificado correctamente.")
                return
        print("No se encontro ningun computador con ese ID.") #Si no se encuentra el id no seguira

    def eliminarComputador(self): #Para eliminar la computadora ingresada
        id_eliminar = int(input("Digite el ID del computador que desea eliminar: "))
        for comp in self.computadores:
            if comp["ID"] == id_eliminar:
                self.computadores.remove(comp)
                print("Computador eliminado correctamente.")
                return
        print("No se encontro ningun computador con ese ID.") #No se va a eliminar  nada porque no se encontro el id

    def mostrarLista(self):
        print("Lista de COMPUTADORES:\n", json.dumps(self.computadores, indent=2)) #Muestra los datos que se ingresaron 


# Main 
#OBJETOS                             los llamamos 
gestor = GestorComputadores()

numCompu = int(input("¿Cuantos computadores son?: "))

for i in range(numCompu): 
    gestor.agregarComputador()

# Guardar datos 
gestor.guardarDatos()

# Mostrar lista 
gestor.mostrarLista()

# Modificar un computador
gestor.modificarComputador()

# Eliminar un computador
gestor.eliminarComputador()

# Mostrar la lista actualizada
gestor.mostrarLista() 