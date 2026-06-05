import tkinter as tk

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

def main():
    root = tk.Tk() #instancia raiz
    root.title("Discovery: Music Exploration")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT) #argumentos nuevos de la libreria tk
    canvas.pack() #visibilidad del lienzo
    
    #canvas de cada seccion
    busqueda(canvas)
    letras(canvas)
    info(canvas)
    sugerencias(canvas)
    reproductor(canvas)

    root.mainloop() #loop para que la ventana no se cierre

def busqueda(canvas):
    x = CANVAS_WIDTH / 4
    y = CANVAS_HEIGHT / 10
    x_top = x + (CANVAS_WIDTH - (x * 2))
    y_bottom = y + (CANVAS_HEIGHT / 12)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='', outline='black') #fill en lugar de color (a diferencia del IDE de Code in Place)

def letras(canvas):
    x = CANVAS_WIDTH / 14
    y = CANVAS_HEIGHT / 4
    x_top = x + ((CANVAS_WIDTH / 2) - x)
    y_bottom = y + (CANVAS_HEIGHT / 2)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='', outline='black')

def info(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 4
    x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
    y_bottom = y + (CANVAS_HEIGHT / 2)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='', outline='black')

def sugerencias(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 2
    x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
    y_bottom = y + (CANVAS_HEIGHT / 4)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='', outline='black')

def reproductor(canvas):
    x = CANVAS_WIDTH / 14
    y = CANVAS_HEIGHT - (CANVAS_HEIGHT / 6)
    x_top = x + (CANVAS_WIDTH - (x * 2))
    y_bottom = y + (CANVAS_HEIGHT / 12)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='', outline='black')

if __name__ == '__main__':
    main()