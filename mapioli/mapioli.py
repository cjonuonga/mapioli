# lets goooooo
import customtkinter
from tkintermapview import TkinterMapView

customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    APP_NAME = "MAPIOLI"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        # ============ creation of left and right frame ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ left frame ============

        self.frame_left.grid_rowconfigure(2, weight=1)
        
        # ========== Set Marker Button ==========
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Set Marker",
                                                command=self.set_marker)
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        # ========== Clear Marker Button ==========
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Clear Markers",
                                                command=self.clear_marker)
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        # ========== Map Type Selection w/ drop down menu ==========
        #   - OpenStreetMap
        #   - Google Default
        #   - Google Sattelite
        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Map Type:", anchor="w")
        self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google Default", "Google Satellite"],
                                                                       command=self.map_type_selection)
        self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

        # ========== Theme Selection w/ drop down menu ==========
        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Theme", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "Default"],
                                                                       command=self.theme_selection)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))

        # ============ right frame ============
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="Type Hiking Trail")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # ========== Default Map Location ==========
        self.map_widget.set_address("San Francisco")
        self.map_option_menu.set("OpenStreetMap")
        self.appearance_mode_optionemenu.set("Dark")

        # ===== Search Function =====
    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

        # ===== Set Marker Method =====
    def set_marker(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

        # ===== Clear Marker Method =====
    def clear_marker(self):
        for marker in self.marker_list:
            marker.delete()

        # ===== Change Theme Function =====
    def theme_selection(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def map_type_selection(self, new_map: str):
        if new_map == "Google Default":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google Satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)


    ''' 
    NEXT STEPS:
    -----------
    - We're going to need some type of database slq, mongodb.
    - Automatic search filler.
    - Pin Marker (tkinter library).
    - Favorites Section.
    - Pictures for each hiking spot, camera icon.
    - Highlight hiking trail in addition to marker.

    
    
    
    # hello my name is 
    
    '''


    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()


