import tkinter as tk
from modelo import DiscoveryModel
from vista import DiscoveryView

class DiscoveryController:
    def __init__(self, model: DiscoveryModel, view: DiscoveryView, root: tk.Tk):
        self.model = model
        self.view = view
        self.root = root
        
        self.current_track = None
        self.recommendations = []
        self.is_playing = False
        self.elapsed_time = 0
        self.timer_running = False
        
        #enlazar el callback de busqueda de vista
        self.view.set_callbacks(
            search_callback=self.on_search,
            tag_callback=self.on_search,
            play_callback=self.on_play_toggle,
            rec_callback=self.on_recommendation_click
        )

    def on_search(self, query):
        print(f"Controlador: Solicitud recibida de búsqueda para: '{query}'")
        
        #parar reproduccion simulada al buscar un nuevo tema
        self.stop_playback()
        
        #buscar en el modelo
        resultados = self.model.buscar_cancion(query)
        
        if not resultados:
            print("Controlador: No se encontraron resultados.")
            self.view.set_song_info("No encontrado", "-", "-")
            self.view.set_lyrics("\n\nNo se encontraron canciones que coincidan con la búsqueda.")
            self.view.set_recommendations([])
            self.view.set_player_track_text("Búsqueda sin resultados")
            self.current_track = None
            self.recommendations = []
        else:
            print(f"Controlador: Se encontraron {len(resultados)} resultado(s):")
            for idx, song in enumerate(resultados, start=1):
                print(f"  {idx}. Título: {song['title']} | Artista: {song['artist']['name']} | Álbum: {song['album']['title']}")
            
            #cargar primera cancion encontrada y actualizar interfaz
            track = resultados[0]
            self.current_track = track
            
            self.view.set_song_info(track['title'], track['artist']['name'], track['album']['title'])
            self.view.set_player_track_text(f"Preparado: {track['title']} - {track['artist']['name']}")
            self.view.update_progress(0, 30)
            
            self.view.set_lyrics("Buscando letra...")
            lyrics = self.model.obtener_letras(track['artist']['name'], track['title'])
            self.view.set_lyrics(lyrics)
            
            recs = self.model.obtener_recomendaciones(track['artist']['id'])
            self.recommendations = recs
            self.view.set_recommendations(recs)

    def on_play_toggle(self):
        if not self.current_track:
            print("Controlador: No hay canción cargada para reproducir.")
            return

        if self.is_playing:
            #pausar la simulacion de reproduccion
            self.is_playing = False
            self.view.set_playing_state(False)
            self.timer_running = False
        else:
            #iniciar o reanudar la simulacion
            self.is_playing = True
            self.view.set_playing_state(True)
            self.view.set_player_track_text(f"Reproduciendo (Local): {self.current_track['title']} - {self.current_track['artist']['name']}")
            self.start_timer()

    def on_recommendation_click(self, index):
        if 0 <= index < len(self.recommendations):
            rec_track = self.recommendations[index]
            search_query = f"{rec_track['title']} {rec_track['artist']['name']}"
            
            #escribir el termino de recomendacion en la busqueda y dispararla
            self.view.input_busqueda.delete(0, tk.END)
            self.view.input_busqueda.insert(0, search_query)
            self.on_search(search_query)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.run_timer()

    def run_timer(self):
        if not self.timer_running or not self.is_playing:
            return
            
        self.elapsed_time += 1
        self.view.update_progress(self.elapsed_time, 30)
        
        if self.elapsed_time >= 30:
            self.stop_playback()
        else:
            #actualizar de a 1 segundo (1000 ms)
            self.root.after(1000, self.run_timer)

    def stop_playback(self):
        self.is_playing = False
        self.timer_running = False
        self.elapsed_time = 0
        self.view.set_playing_state(False)
        self.view.update_progress(0, 30)
        if self.current_track:
            self.view.set_player_track_text(f"Preparado: {self.current_track['title']} - {self.current_track['artist']['name']}")
        else:
            self.view.set_player_track_text("No se está reproduciendo nada")