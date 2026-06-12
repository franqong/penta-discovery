import tkinter as tk
import math #necesario para la animacion del vinilo

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

        #atributos de la animacion del vinilo
        self.spin_angle = 0
        self.is_spinning = False
        
        #elementos dinamicos e identificadores
        self.input_busqueda = None
        self.search_btn_id = None
        self.lyrics_text = None
        
        self.info_title_id = None
        self.info_artist_id = None
        self.info_album_id = None
        
        self.rec_items = []  #lista de tuplas (rect_id, text_id)
        
        self.play_btn_bg = None
        self.play_btn_text = None
        self.player_track_text = None
        self.progress_bg_id = None
        self.progress_fg_id = None
        self.progress_knob_id = None
        self.progress_time_id = None

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

        #texto y overlays interactivos para sugerencias rapidas de generos

        #ARRIBA: GRUNGE
        self.canvas.create_text(x + (width + 1.58)/2, (y - 34) + height/2, text="Grunge", font=('Inter', 9, 'bold'), fill='#DFD0B8')
        self.canvas.create_rectangle(x - height/2, y - 34, x + width + height/2, y - 34 + height, fill='', outline='', tags='tag_grunge')
        self.canvas.tag_bind('tag_grunge', '<Button-1>', lambda event: self.on_tag_click("Grunge"))
        self.canvas.tag_bind('tag_grunge', '<Enter>', lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind('tag_grunge', '<Leave>', lambda event: self.canvas.config(cursor=""))

        #CENTRO: PROGRESSIVE ROCK
        self.canvas.create_text(x + (width + 1.58)/2, y + height/2, text="Progressive Rock", font=('Inter', 9, 'bold'), fill='#DFD0B8')
        self.canvas.create_rectangle(x - height/2, y, x + width + height/2, y + height, fill='', outline='', tags='tag_prog')
        self.canvas.tag_bind('tag_prog', '<Button-1>', lambda event: self.on_tag_click("Progressive Rock"))
        self.canvas.tag_bind('tag_prog', '<Enter>', lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind('tag_prog', '<Leave>', lambda event: self.canvas.config(cursor=""))

        #ABAJO: NU METAL
        self.canvas.create_text(x + (width + 1.58)/2, (y + 34) + height/2, text="Nu Metal", font=('Inter', 9, 'bold'), fill='#DFD0B8')
        self.canvas.create_rectangle(x - height/2, y + 34, x + width + height/2, y + 34 + height, fill='', outline='', tags='tag_numetal')
        self.canvas.tag_bind('tag_numetal', '<Button-1>', lambda event: self.on_tag_click("Nu Metal"))
        self.canvas.tag_bind('tag_numetal', '<Enter>', lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind('tag_numetal', '<Leave>', lambda event: self.canvas.config(cursor=""))

    def draw_letras(self):
        x = CANVAS_WIDTH / 14
        y = CANVAS_HEIGHT / 4
        x_top = x + ((CANVAS_WIDTH / 2) - x)
        y_bottom = y + (CANVAS_HEIGHT / 2)
        self.canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

        #titulo encabezado para la seccion de letras
        self.canvas.create_text(x + 20, y + 25, text="LETRA", font=('Inter', 12, 'bold'), fill='#DFD0B8', anchor='w')
        self.canvas.create_line(x + 20, y + 42, x + 80, y + 42, fill='#948979', width=2)
        
        #frame contenedor para scrollbar y text widget
        lyrics_frame = tk.Frame(self.root, bg='#393E46')
        scrollbar = tk.Scrollbar(lyrics_frame, bg='#393E46', troughcolor='#393E46')
        self.lyrics_text = tk.Text(lyrics_frame, bg='#393E46', fg='#DFD0B8', font=('Inter', 11), 
                                   wrap='word', bd=0, highlightthickness=0, yscrollcommand=scrollbar.set,
                                   selectbackground='#948979', selectforeground='#222831')
        
        scrollbar.config(command=self.lyrics_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.lyrics_text.pack(side='left', fill='both', expand=True)
        
        #texto inicial 
        self.lyrics_text.insert('1.0', "\n\nBusca una canción para ver su letra aquí...")
        self.lyrics_text.config(state='disabled')
        
        #widget en canvas
        width = x_top - x
        height = y_bottom - y
        self.canvas.create_window(x + width/2, y + 45 + (height - 65)/2, window=lyrics_frame, width=width - 40, height=height - 70)

    def draw_info(self):
        x = CANVAS_WIDTH / 2
        y = CANVAS_HEIGHT / 4
        x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
        y_bottom = y + (CANVAS_HEIGHT / 2)
        self.canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

        #detalle de canción
        self.canvas.create_text(x + 20, y + 25, text="DETALLE DE CANCIÓN", font=('Inter', 12, 'bold'), fill='#DFD0B8', anchor='w')
        self.canvas.create_line(x + 20, y + 42, x + 180, y + 42, fill='#948979', width=2)
        
        #coordenadas del vinilo grande
        self.large_vinyl_cx = x + 85
        self.large_vinyl_cy = y + 110
        self.large_vinyl_r = 50
        
        #vinilo - negro
        self.canvas.create_oval(self.large_vinyl_cx - self.large_vinyl_r, self.large_vinyl_cy - self.large_vinyl_r,
                                self.large_vinyl_cx + self.large_vinyl_r, self.large_vinyl_cy + self.large_vinyl_r,
                                fill='#111111', outline='#948979', width=2)
        
        #ranuras/grooves del vinilo
        self.canvas.create_oval(self.large_vinyl_cx - 38, self.large_vinyl_cy - 38,
                                self.large_vinyl_cx + 38, self.large_vinyl_cy + 38,
                                outline='#333333', width=1)
        self.canvas.create_oval(self.large_vinyl_cx - 26, self.large_vinyl_cy - 26,
                                self.large_vinyl_cx + 26, self.large_vinyl_cy + 26,
                                outline='#333333', width=1)
                                
        #vinilo - rojo
        self.canvas.create_oval(self.large_vinyl_cx - 15, self.large_vinyl_cy - 15,
                                self.large_vinyl_cx + 15, self.large_vinyl_cy + 15,
                                fill='#c62828', outline='')
        
        #linea blanca que gira en la animacion
        self.large_vinyl_line = self.canvas.create_line(self.large_vinyl_cx, self.large_vinyl_cy,
                                                        self.large_vinyl_cx + 12, self.large_vinyl_cy,
                                                        fill='#ffffff', width=2)
        
        #textos de informacion
        text_start_x = x + 160
        self.info_title_id = self.canvas.create_text(text_start_x, y + 70, text="Título: -", font=('Inter', 11, 'bold'), fill='#DFD0B8', anchor='w')
        self.info_artist_id = self.canvas.create_text(text_start_x, y + 100, text="Artista: -", font=('Inter', 10), fill='#DFD0B8', anchor='w')
        self.info_album_id = self.canvas.create_text(text_start_x, y + 130, text="Álbum: -", font=('Inter', 10), fill='#DFD0B8', anchor='w')

    def draw_sugerencias(self):
        x = CANVAS_WIDTH / 2
        y = CANVAS_HEIGHT / 2
        x_top = x + ((CANVAS_WIDTH / 2) - (CANVAS_WIDTH / 14))
        y_bottom = y + (CANVAS_HEIGHT / 4)
        self.canvas.create_rectangle(x, y, x_top, y_bottom, fill='#393E46', outline=BG_COLOR, width=BOXES_WIDTH)

        #encabezado de recomendaciones
        self.canvas.create_text(x + 20, y + 25, text="RECOMENDACIONES", font=('Inter', 12, 'bold'), fill='#DFD0B8', anchor='w')
        self.canvas.create_line(x + 20, y + 42, x + 160, y + 42, fill='#948979', width=2)
        
        #slots de 3 recomendaciones
        self.rec_items = []
        for i in range(3):
            item_y = y + 60 + (i * 35)
            tag_name = f"rec_card_{i}"
            
            #fondo de la cancion recomendada
            card_id = self.canvas.create_rectangle(x + 20, item_y, x_top - 20, item_y + 28, fill='#2c3138', outline='#948979', width=0, tags=tag_name)
            
            #texto de la recomendacion
            text_id = self.canvas.create_text(x + 35, item_y + 14, text=f"{i+1}. -", font=('Inter', 10), fill='#DFD0B8', anchor='w', tags=tag_name)
            
            self.rec_items.append((card_id, text_id))
            
            #bindeo de eventos interactivos para cada slot
            self.canvas.tag_bind(tag_name, '<Button-1>', lambda event, idx=i: self.on_rec_click(idx))
            self.canvas.tag_bind(tag_name, '<Enter>', lambda event, tn=tag_name, cid=card_id: self.on_rec_enter(tn, cid))
            self.canvas.tag_bind(tag_name, '<Leave>', lambda event, tn=tag_name, cid=card_id: self.on_rec_leave(tn, cid))

    def on_rec_enter(self, tag, card_id):
        self.canvas.config(cursor="hand2")
        self.canvas.itemconfig(card_id, fill='#948979')
        #cambio de texto activo a color oscuro
        for cid, tid in self.rec_items:
            if cid == card_id:
                self.canvas.itemconfig(tid, fill='#222831')

    def on_rec_leave(self, tag, card_id):
        self.canvas.config(cursor="")
        self.canvas.itemconfig(card_id, fill='#2c3138')
        #cambio de texto activo de vuelta a color anterior
        for cid, tid in self.rec_items:
            if cid == card_id:
                self.canvas.itemconfig(tid, fill='#DFD0B8')

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
        self.play_btn_text = self.canvas.create_text((CANVAS_WIDTH / 2) + 0.5, y + (height / 2.05), text= 'PLAY', font= ('Inter', 8, 'bold'), fill=BG_COLOR) #boton 'play' - texto
        self.canvas.create_oval(x + 10, y + 6, x + 44, y + 38, fill='black') #vinilo - border
        self.canvas.create_oval(x + 23, y + 18, x + 31, y + 26, fill='red') #vinilo - la parte roja

        #aca se guardan ids y referencias para interaccion dinamica
        self.small_vinyl_cx = x + 27
        self.small_vinyl_cy = y + 22
        self.small_vinyl_r = 17
        self.small_vinyl_line = self.canvas.create_line(self.small_vinyl_cx, self.small_vinyl_cy,
                                                        self.small_vinyl_cx + 4, self.small_vinyl_cy,
                                                        fill='#ffffff', width=1.5)

        bx = CANVAS_WIDTH / 2 - (height / 2)
        by = y + (height / 4)
        btn_w = x / 2
        btn_h = height / 2

        #zona interactiva para el boton play
        self.canvas.create_rectangle(bx - btn_h/2, by, bx + btn_w + btn_h/2, by + btn_h, fill='', outline='', tags='btn_play')
        self.canvas.tag_bind('btn_play', '<Button-1>', self.on_play_click)
        self.canvas.tag_bind('btn_play', '<Enter>', lambda event: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind('btn_play', '<Leave>', lambda event: self.canvas.config(cursor=""))

        #texto de la cancion que suena
        self.player_track_text = self.canvas.create_text(x + 55, y + 22, text="No se está reproduciendo nada", font=('Inter', 9, 'bold'), fill=BG_COLOR, anchor='w')
        
        #barra de progreso a la derecha
        self.prog_x1 = CANVAS_WIDTH / 2 + 100
        self.prog_x2 = CANVAS_WIDTH - x - 150
        self.prog_y = y + 22
        self.prog_h = 6
        
        #fondo de la barra de progreso
        self.progress_bg_id = self.canvas.create_line(self.prog_x1, self.prog_y, self.prog_x2, self.prog_y, fill='#222831', width=self.prog_h, capstyle='round')
        
        #progreso actual relleno (inicia vacio)
        self.progress_fg_id = self.canvas.create_line(self.prog_x1, self.prog_y, self.prog_x1, self.prog_y, fill='cornsilk2', width=self.prog_h, capstyle='round')
        
        #knob de progreso
        self.progress_knob_id = self.canvas.create_oval(self.prog_x1 - 5, self.prog_y - 5, self.prog_x1 + 5, self.prog_y + 5, fill='cornsilk2', outline='')
        
        #texto de tiempo transcurrido / tiempo total
        self.progress_time_id = self.canvas.create_text(self.prog_x2 + 50, self.prog_y, text="00:00 / 00:00", font=('Inter', 9, 'bold'), fill=BG_COLOR)

    #animacion de los vinilos - metodos
    def start_spinning(self):
        if not self.is_spinning:
            self.is_spinning = True
            self.animate_spin()
            
    def stop_spinning(self):
        self.is_spinning = False
        
    def animate_spin(self):
        if not self.is_spinning:
            return
            
        self.spin_angle += 0.1
        if self.spin_angle >= 2 * math.pi:
            self.spin_angle -= 2 * math.pi
            
        #vinilo grande (info) - giro
        lx = self.large_vinyl_cx + 12 * math.cos(self.spin_angle)
        ly = self.large_vinyl_cy + 12 * math.sin(self.spin_angle)
        self.canvas.coords(self.large_vinyl_line, self.large_vinyl_cx, self.large_vinyl_cy, lx, ly)
        
        #vinilo chico (reproductor) - giro
        sx = self.small_vinyl_cx + 4 * math.cos(self.spin_angle)
        sy = self.small_vinyl_cy + 4 * math.sin(self.spin_angle)
        self.canvas.coords(self.small_vinyl_line, self.small_vinyl_cx, self.small_vinyl_cy, sx, sy)
        
        #loop de animación en 50ms
        self.root.after(50, self.animate_spin)

    #metodos setters dinamicos llamados desde el controlador
    def set_song_info(self, title, artist, album):
        self.canvas.itemconfig(self.info_title_id, text=f"Título: {title}")
        self.canvas.itemconfig(self.info_artist_id, text=f"Artista: {artist}")
        self.canvas.itemconfig(self.info_album_id, text=f"Álbum: {album}")
        
    def set_lyrics(self, lyrics):
        self.lyrics_text.config(state='normal')
        self.lyrics_text.delete('1.0', tk.END)
        if lyrics:
            self.lyrics_text.insert('1.0', lyrics)
        else:
            self.lyrics_text.insert('1.0', "\n\nLetras no encontradas.")
        self.lyrics_text.config(state='disabled')
        
    def set_recommendations(self, tracks):
        for i in range(3):
            card_id, text_id = self.rec_items[i]
            if i < len(tracks):
                track = tracks[i]
                t_title = track.get('title', 'Desconocido')
                t_artist = track.get('artist', {}).get('name', 'Desconocido')
                self.canvas.itemconfig(text_id, text=f"{i+1}. {t_title} - {t_artist}")
                self.canvas.itemconfig(card_id, state='normal')
                self.canvas.itemconfig(text_id, state='normal')
            else:
                self.canvas.itemconfig(card_id, state='hidden')
                self.canvas.itemconfig(text_id, state='hidden')
                
    def set_player_track_text(self, text):
        if len(text) > 40:
            text = text[:37] + "..."
        self.canvas.itemconfig(self.player_track_text, text=text)
        
    def set_playing_state(self, is_playing):
        if is_playing:
            self.canvas.itemconfig(self.play_btn_text, text='PAUSE')
            self.start_spinning()
        else:
            self.canvas.itemconfig(self.play_btn_text, text='PLAY')
            self.stop_spinning()
            
    def update_progress(self, current_sec, total_sec):
        if total_sec <= 0:
            total_sec = 30
            
        fraction = min(1.0, current_sec / total_sec)
        new_x = self.prog_x1 + (self.prog_x2 - self.prog_x1) * fraction
        
        #mover barra y knob
        self.canvas.coords(self.progress_fg_id, self.prog_x1, self.prog_y, new_x, self.prog_y)
        self.canvas.coords(self.progress_knob_id, new_x - 5, self.prog_y - 5, new_x + 5, self.prog_y + 5)
        
        #formatear texto mm:ss
        def format_time(sec):
            m = int(sec) // 60
            s = int(sec) % 60
            return f"{m:02d}:{s:02d}"
            
        time_text = f"{format_time(current_sec)} / {format_time(total_sec)}"
        self.canvas.itemconfig(self.progress_time_id, text=time_text)

    #callbacks - para llamar al controlador cuando se hace una busqueda
    def set_callbacks(self, search_callback, tag_callback=None, play_callback=None, rec_callback=None):
        self.search_callback = search_callback
        self.tag_callback = tag_callback
        self.play_callback = play_callback
        self.rec_callback = rec_callback

    def on_search_click(self, event=None):
        query = self.input_busqueda.get().strip()
        if query and hasattr(self, 'search_callback'):
            self.search_callback(query)
        else:
            print(f"Búsqueda solicitada (sin callback registrado): {query}")

    def on_tag_click(self, tag):
        self.input_busqueda.delete(0, tk.END)
        self.input_busqueda.insert(0, tag)
        if hasattr(self, 'tag_callback') and self.tag_callback is not None:
            self.tag_callback(tag)
            
    def on_play_click(self, event=None):
        if hasattr(self, 'play_callback') and self.play_callback is not None:
            self.play_callback()
            
    def on_rec_click(self, index):
        if hasattr(self, 'rec_callback') and self.rec_callback is not None:
            self.rec_callback(index)

""" MAIN """

def main():
    root = tk.Tk() #instancia raiz
    view = DiscoveryView(root) #ahora busca el lienzo en la clase
    
    root.mainloop() #loop para que la ventana no se cierre

""" FIN DEL CODIGO """

if __name__ == '__main__':
    main()