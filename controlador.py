import tkinter as tk
from modelo import DiscoveryModel
from vista import DiscoveryView

class DiscoveryController:
    def __init__(self, model: DiscoveryModel, view: DiscoveryView, root: tk.Tk):
        self.model = model
        self.view = view
        self.root = root
        
        #enlazar el callback de busqueda de vista
        self.view.set_callbacks(search_callback=self.on_search)

    def on_search(self, query):
        print(f"Controlador: Solicitud recibida de búsqueda para: '{query}'")
        
        #busca en el modelo
        resultados = self.model.buscar_cancion(query)
        
        if not resultados:
            print("Controlador: No se encontraron resultados.")
        else:
            print(f"Controlador: Se encontraron {len(resultados)} resultado(s):")
            for idx, song in enumerate(resultados, start=1):
                print(f"  {idx}. Título: {song['title']} | Artista: {song['artist']['name']} | Álbum: {song['album']['title']}")