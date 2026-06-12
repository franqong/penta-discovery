import tkinter as tk
from modelo import DiscoveryModel
from vista import DiscoveryView
from controlador import DiscoveryController

def main():
    
    root = tk.Tk() #ahora se inicializa la ventana principal de tkinter de esta forma y no en vista
    modelo = DiscoveryModel()
    vista = DiscoveryView(root) #y aca se inicializa el resto del lienzo
    controlador = DiscoveryController(modelo, vista, root)
    root.mainloop() #arranca el loop principal

if __name__ == '__main__':
    main()