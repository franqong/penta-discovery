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

class DiscoveryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Discovery")
        self.root.resizable(False, False) #temporal. la idea es quitarlo a futuro para que sea mas dinamico

        #canvas principal definido
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack()

        #dibujar los componentes aca a partir de ahora - renombradas las secciones para mejor legibilidad
        self.draw_header()
        self.draw_busqueda()
        self.draw_busqueda_sugerencias()
        self.draw_letras()
        self.draw_info()
        self.draw_sugerencias()
        self.draw_reproductor()

    def draw_header(self):
        x = CANVAS_WIDTH / 2
        y = CANVAS_HEIGHT / 14
        self.canvas.create_text(x, y, text= 'Discovery', font= ('Allura', 30), fill='#e8d6bf')

    def draw_busqueda(self):
        x = CANVAS_WIDTH / 3
        y = CANVAS_HEIGHT / 7
        width = CANVAS_WIDTH / 3
        height = CANVAS_HEIGHT / 18
        border = 2
        capsula(self.canvas, x - border + 1.88, y - border, width + border, height + (border * 2), '#948979') 
        capsula(self.canvas, x, y, width + 1.58, height, '#DFD0B8')

        #input busqueda | se crea una variable y se la inserta luego en el canvas. para la variable es necesaria la funcion Entry de tkinter
        self.input_busqueda = tk.Entry(self.canvas, bg='#DFD0B8', fg=BG_COLOR, font=('Inter', 10), bd=0, insertbackground=BG_COLOR)
        self.canvas.create_window(x + (width / 2), y + (height / 2), window=self.input_busqueda, width= width - 40, height = height - 10)

        #linea del input | se coloca debajo del input para que se visualice, por jerarquia del canvas
        x1 = x + 20
        x2 = x + width - 20
        y2 = y + height - 5
        self.canvas.create_line(x1, y2, x2, y2, fill='#948979', width=1)

        #boton de busqueda
        self.canvas.create_oval(x2 + 10, y2 - 25, x2 + 25, y2 - 10, fill= '', outline=BG_COLOR, width=1.5)
        self.canvas.create_line(x2 + 22, y2 - 13, x2 + 29, y2 - 6, fill=BG_COLOR, width=1.5)

        #boton de busqueda - area invisible para interactuar
        self.canvas.create_rectangle(x2 + 5, y2 - 28, x2 + 32, y2 - 3, fill='', outline='', tags='btn_buscar')
        self.canvas.tag_bind('btn_buscar', '<Button-1>', self.on_search_click)
        self.canvas.tag_bind('btn_buscar', '<Enter>', lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind('btn_buscar', '<Leave>', lambda event: self.canvas.config(cursor=""))
        self.input_busqueda.bind('<Return>', self.on_search_click) #bindeo de la tecla Enter

    def draw_busqueda_sugerencias(self):
        x = CANVAS_WIDTH / 1.38
        y = CANVAS_HEIGHT / 6.6
        width = CANVAS_WIDTH / 5.8
        height = CANVAS_HEIGHT / 27
        border = 2
        capsula(self.canvas, x - border + 1.88, y - border, width + border, height + (border * 2), '#948979') #centro - border 
        capsula(self.canvas, x, y, width + 1.58, height, '#393E46') #centro - interior
        capsula(self.canvas, x - border + 1.88, (y - 34) - border, width + border, height + (border * 2), '#948979') #arriba - border
        capsula(self.canvas, x, y - 34, width + 1.58, height, '#393E46') #arriba - interior
        capsula(self.canvas, x - border + 1.88, (y + 34) - border, width + border, height + (border * 2), '#948979') #abajo - border
        capsula(self.canvas, x, y + 34, width + 1.58, height, '#393E46') #abajo - interior

    def draw_letras(self):
        x = CANVAS_WIDTH / 14
        y = CANVAS_HEIGHT / 4
        x_top = x + ((CANVAS_WIDTH / 2) - x)
        y_bottom = y + (CANVAS_HEIGHT / 2)
        self.canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

    def draw_info(self):
        x = CANVAS_WIDTH / 2
        y = CANVAS_HEIGHT / 4
        x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
        y_bottom = y + (CANVAS_HEIGHT / 2)
        self.canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

    def draw_sugerencias(self):
        x = CANVAS_WIDTH / 2
        y = CANVAS_HEIGHT / 2
        x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
        y_bottom = y + (CANVAS_HEIGHT / 4)
        self.canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

    def draw_reproductor(self):
        x = CANVAS_WIDTH / 14
        y = CANVAS_HEIGHT - (CANVAS_HEIGHT / 6)
        width = CANVAS_WIDTH - (x * 2)
        height = CANVAS_HEIGHT / 16
        border = 2
        capsula(self.canvas, x - border + 1.58, y - border, width + border, height + (border * 2), '#DFD0B8')  
        capsula(self.canvas, x, y, width + 1.58, height, '#948979')

        #botones y vinilo
        capsula(self.canvas, CANVAS_WIDTH / 2 - (height / 2), y + (height / 4), x / 2, height / 2, 'cornsilk2') #boton 'play'
        self.canvas.create_text((CANVAS_WIDTH / 2) + 0.5, y + (height / 2.05), text= 'PLAY', font= ('Inter', 8, 'bold'), fill=BG_COLOR) #boton 'play' - texto
        self.canvas.create_oval(x + 10, y + 6, x + 44, y + 38, fill='black') #vinilo - border
        self.canvas.create_oval(x + 23, y + 18, x + 31, y + 26, fill='red') #vinilo - la parte roja

    #callbacks - para llamar al controlador cuando se hace una busqueda
    def set_callbacks(self, search_callback):
        self.search_callback = search_callback

    def on_search_click(self, event=None):
        query = self.input_busqueda.get().strip()
        if query and hasattr(self, 'search_callback'):
            self.search_callback(query)
        else:
            print(f"Búsqueda solicitada (sin callback registrado): {query}")

""" MAIN """

def main():
    root = tk.Tk() #instancia raiz
    view = DiscoveryView(root) #ahora busca el lienzo en la clase
    
    root.mainloop() #loop para que la ventana no se cierre

""" FIN DEL CODIGO """

if __name__ == '__main__':
    main()