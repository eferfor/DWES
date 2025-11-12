class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def mostrar_info(self):
        estado = "Completada" if self.completada else "Sin completar"
        print(f"- {self.titulo}: {self.descripcion} - Estado: {estado}")

    def marcar_completada(self):
        self.completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion


def main():
    def crear_tarea():
        """
        Pide al usuario un nombre y descripcion de la tarea.
        Crea la nueva tarea con la clase Tarea y la añade a la
        lista de tareas.

        :return:
        str: confirmación
        """
        titulo = input("Nombre de la tarea: ")
        descripcion = input("Descripcion de la tarea: ")
        tareas.append(Tarea(titulo, descripcion))
        return "Tarea creada."

    def mostrar_tareas():
        """
        Recorre la lista de tareas y devuelve la info de
        cada una con mostrar_info().
        """
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            for tarea in tareas:
                tarea.mostrar_info()

    def completar_tarea():
        """
        Pide al usuario una tarea, si está en la lista, la
        marca como completada.

        :return:
        str: mensaje de confirmación
        """
        tarea_seleccionada = input("¿Qué tarea quieres completar?")
        for tarea in tareas:
            if tarea.titulo.lower() == tarea_seleccionada.lower():
                tarea.marcar_completada()
                return f"{tarea_seleccionada} completada."

        return "No se encuentra la tarea indicada."

    def editar_tarea():
        """
        Pide indicar una tarea, si existe, pide su nuevo título y descripción
        y los modifica.

        :return:
        str: confirmación
        """
        tarea_seleccionada = input("¿Qué tarea quieres editar?")
        for tarea in tareas:
            if tarea.titulo.lower() == tarea_seleccionada.lower():
                nuevo_titulo = input("Nombre nuevo de la tarea: ")
                nueva_descripcion = input("Descripción nueva de la tarea: ")
                tarea.editar(nuevo_titulo, nueva_descripcion)
                return "Tarea modificada."

        return "No se encuentra la tarea indicada."

    def eliminar_tarea():
        """
        Pide al usuario una tarea, si está en la lista, la
        elimina.

        :return:
        str: mensaje de confirmación
        """
        tarea_seleccionada = input("¿Qué tarea quieres eliminar?")
        for tarea in tareas:
            if tarea.titulo.lower() == tarea_seleccionada.lower():
                tareas.remove(tarea)
                return f"{tarea_seleccionada} eliminada."

        return "No se encuentra la tarea indicada."

    # Main
    salir = False
    tareas = []

    while not salir:
        print("1. Crear tarea")
        print("2. Mostrar todas")
        print("3. Marcar completada")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        try:
            opcion = input("Ingresa una opcion: ")
            if opcion == "1":
                print(crear_tarea())
            elif opcion == "2":
                mostrar_tareas()
            elif opcion == "3":
                print(completar_tarea())
            elif opcion == "4":
                print(editar_tarea())
            elif opcion == "5":
                print(eliminar_tarea())
            elif opcion == "6":
                print("¡Chao!")
                salir = True
            else:
                raise Exception("Opción inválida")
        except Exception as e:
            print("Error", e)

main()
