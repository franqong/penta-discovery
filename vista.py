import tkinter as tk

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
BG_COLOR = '#222831' #color de fondo
BOXES_WIDTH = 2

""" FUNCIONES """

def capsula(canvas, x, y, width, height, color):
    radio = height / 2
    canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline='') #rectangulo principal
    canvas.create_oval(x - radio, y, x + radio, y + height - 1, fill=color, outline='') #circulo izquierdo
    canvas.create_oval(x + width - radio, y, x + width + radio, y + height - 1, fill=color, outline='') #circulo derecho

""" CLASES """

"""class DiscoveryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Discovery")
        self.root.resizable(False, False) #temporal. la idea es quitarlo a futuro para que sea mas dinamico"""

def header(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 14
    canvas.create_text(x, y, text= 'Discovery', font= ('Allura', 30), fill='#e8d6bf')

def busqueda(canvas):
    x = CANVAS_WIDTH / 3
    y = CANVAS_HEIGHT / 7
    width = CANVAS_WIDTH / 3
    height = CANVAS_HEIGHT / 18
    border = 2
    capsula(canvas, x - border + 1.88, y - border, width + border, height + (border * 2), '#948979') 
    capsula(canvas, x, y, width + 1.58, height, '#DFD0B8')

    #input busqueda | se crea una variable y se la inserta luego en el canvas. para la variable es necesaria la funcion Entry de tkinter
    input_busqueda = tk.Entry(canvas, bg='#DFD0B8', fg=BG_COLOR, font=('Inter', 10), bd=0, insertbackground=BG_COLOR)
    canvas.create_window(x + (width / 2), y + (height / 2), window=input_busqueda, width= width - 40, height = height - 10)

    #linea del input | se coloca debajo del input para que se visualice, por jerarquia del canvas
    x1 = x + 20
    x2 = x + width - 20
    y2 = y + height - 5
    canvas.create_line(x1, y2, x2, y2, fill='#948979', width=1)

    #boton de busqueda
    canvas.create_oval(x2 + 10, y2 - 25, x2 + 25, y2 - 10, fill= '', outline=BG_COLOR, width=1.5)
    canvas.create_line(x2 + 22, y2 - 13, x2 + 29, y2 - 6, fill=BG_COLOR, width=1.5)

def letras(canvas):
    x = CANVAS_WIDTH / 14
    y = CANVAS_HEIGHT / 4
    x_top = x + ((CANVAS_WIDTH / 2) - x)
    y_bottom = y + (CANVAS_HEIGHT / 2)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

def info(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 4
    x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
    y_bottom = y + (CANVAS_HEIGHT / 2)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

def sugerencias(canvas):
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 2
    x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
    y_bottom = y + (CANVAS_HEIGHT / 4)
    canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

def reproductor(canvas):
    x = CANVAS_WIDTH / 14
    y = CANVAS_HEIGHT - (CANVAS_HEIGHT / 6)
    width = CANVAS_WIDTH - (x * 2)
    height = CANVAS_HEIGHT / 16
    border = 2
    capsula(canvas, x - border + 1.58, y - border, width + border, height + (border * 2), '#DFD0B8')  
    capsula(canvas, x, y, width + 1.58, height, '#948979')

    #botones y vinilo
    capsula(canvas, CANVAS_WIDTH / 2 - (height / 2), y + (height / 4), x / 2, height / 2, 'cornsilk2') #boton 'play'
    canvas.create_text((CANVAS_WIDTH / 2) + 0.5, y + (height / 2.05), text= 'PLAY', font= ('Inter', 8, 'bold'), fill=BG_COLOR) #boton 'play' - texto
    canvas.create_oval(x + 10, y + 6, x + 44, y + 38, fill='black') #vinilo - border
    canvas.create_oval(x + 23, y + 18, x + 31, y + 26, fill='red') #vinilo - la parte roja

""" CAJAS INTERACTIVAS """

def busqueda_sugerencias(canvas):
    x = CANVAS_WIDTH / 1.38
    y = CANVAS_HEIGHT / 6.6
    width = CANVAS_WIDTH / 5.8
    height = CANVAS_HEIGHT / 27
    border = 2
    capsula(canvas, x - border + 1.88, y - border, width + border, height + (border * 2), '#948979') #centro - border 
    capsula(canvas, x, y, width + 1.58, height, '#393E46') #centro - interior
    capsula(canvas, x - border + 1.88, (y - 34) - border, width + border, height + (border * 2), '#948979') #arriba - border
    capsula(canvas, x, y - 34, width + 1.58, height, '#393E46') #arriba - interior
    capsula(canvas, x - border + 1.88, (y + 34) - border, width + border, height + (border * 2), '#948979') #abajo - border
    capsula(canvas, x, y + 34, width + 1.58, height, '#393E46') #abajo - interior

""" MAIN """

def main():
    root = tk.Tk() #instancia raiz
    root.title("Discovery: Music Exploration")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR) #argumentos nuevos de la libreria tk
    canvas.pack() #visibilidad del lienzo
    
    #canvas de cada seccion
    header(canvas)
    busqueda(canvas)
    #busqueda_sugerencias(canvas)
    letras(canvas)
    info(canvas)
    sugerencias(canvas)
    reproductor(canvas)

    root.mainloop() #loop para que la ventana no se cierre

""" FIN DEL CODIGO """

if __name__ == '__main__':
    main()