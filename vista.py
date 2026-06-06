import tkinter as tk

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
BG_COLOR = '#222831' #color de fondo

def main():
    root = tk.Tk() #instancia raiz
    root.title("Discovery: Music Exploration")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR) #argumentos nuevos de la libreria tk
    canvas.pack() #visibilidad del lienzo
    
    #canvas de cada seccion
    busqueda(canvas)
    letras(canvas)
    info(canvas)
    sugerencias(canvas)
    reproductor(canvas)

    root.mainloop() #loop para que la ventana no se cierre

def capsula(canvas, x, y, width, height, color):
    radio = height / 2
    canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline='') #rectangulo principal
    canvas.create_oval(x - radio, y, x + radio, y + height - 1, fill=color, outline='') #circulo izquierdo
    canvas.create_oval(x + width - radio, y, x + width + radio, y + height - 1, fill=color, outline='') #circulo derecho

def busqueda(canvas):
    x = CANVAS_WIDTH / 3
    y = CANVAS_HEIGHT / 7
    width = CANVAS_WIDTH / 3
    height = CANVAS_HEIGHT / 18
    border = 2
    capsula(canvas, x - border + 1, y - border, width + border, height + (border * 2), '#948979')
    capsula(canvas, x, y, width, height, '#DFD0B8')

def letras(canvas):
    x = CANVAS_WIDTH / 14
    y = CANVAS_HEIGHT / 4
    x_top = x + ((CANVAS_WIDTH / 2) - x)
    y_bottom = y + (CANVAS_HEIGHT / 2)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline='black')

def info(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 4
    x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
    y_bottom = y + (CANVAS_HEIGHT / 2)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline='black')

def sugerencias(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 2
    x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
    y_bottom = y + (CANVAS_HEIGHT / 4)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline='black')

def reproductor(canvas):
    x = CANVAS_WIDTH / 14
    y = CANVAS_HEIGHT - (CANVAS_HEIGHT / 6)
    x_top = x + (CANVAS_WIDTH - (x * 2))
    y_bottom = y + (CANVAS_HEIGHT / 16)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#948979', outline='')

if __name__ == '__main__':
    main()