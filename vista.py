import tkinter as tk

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
BG_COLOR = '#222831' #color de fondo
BOXES_WIDTH = 2

def main():
    root = tk.Tk() #instancia raiz
    root.title("Discovery: Music Exploration")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR) #argumentos nuevos de la libreria tk
    canvas.pack() #visibilidad del lienzo
    
    #canvas de cada seccion
    header(canvas)
    busqueda(canvas)
    letras(canvas)
    info(canvas)
    sugerencias(canvas)
    reproductor(canvas)

    root.mainloop() #loop para que la ventana no se cierre

""" FUNCIONES """

def capsula(canvas, x, y, width, height, color):
    radio = height / 2
    canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline='') #rectangulo principal
    canvas.create_oval(x - radio, y, x + radio, y + height - 1, fill=color, outline='') #circulo izquierdo
    canvas.create_oval(x + width - radio, y, x + width + radio, y + height - 1, fill=color, outline='') #circulo derecho

""" BOXES """

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

    #linea temporal para marcar el lugar donde se hara el input de la busqueda
    x1 = x + 25
    y1 = (height * 3) + 15
    x2 = (width * 2) - 25
    y2 = (height * 3) + 15
    canvas.create_line(x1, y2, x2, y2, fill='#948979')


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

""" FIN DEL CODIGO """

if __name__ == '__main__':
    main()