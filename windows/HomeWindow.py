import customtkinter as ctk

class HomeWindow:
    Title: str
    WindowSize: str
    WindowPaddingY: int
    WindowPaddingX: int

    PlaylistFrameForegroundColor: str

    def __init__(
        self, 
        title: str = "Unamed Music App",
        windowSize: str = "1300x750"
    ):
        self.__class__.Title = title
        self.__class__.WindowSize = windowSize
        self.__class__.WindowPaddingY = 10
        self.__class__.WindowPaddingX = 10

        self.__class__.PlaylistFrameForegroundColor = "#141414"

    def CreateFrames(self, app):
        PlaylistsFrame = ctk.CTkScrollableFrame(
            master = app,
            fg_color = self.__class__.PlaylistFrameForegroundColor,
            scrollbar_button_color = self.__class__.PlaylistFrameForegroundColor
        )
        PlaylistsFrame.grid(
            row = 0,
            column = 0,
            sticky = "nsew"
        )

        PlaylistsFrame.grid_rowconfigure(0, weight = 1)
        PlaylistsFrame.grid_columnconfigure(0, weight = 1)

        label = ctk.CTkLabel(
            master = PlaylistsFrame,
            text = "No playlists created",
            text_color = "white",
            anchor = "center"
        )
        label.grid(row = 0, column = 0, sticky = "ew")
        
    def CreateWindow(self):
        app = ctk.CTk()

        app.title(self.__class__.Title)
        app.grid_rowconfigure(0, weight = 1)
        app.grid_columnconfigure(0, weight = 1)
        app.grid_columnconfigure(1, weight = 9)
        app.geometry(self.__class__.WindowSize)

        app.config(
            padx = self.__class__.WindowPaddingX, 
            pady = self.__class__.WindowPaddingY
        )

        self.CreateFrames(app)

        app.mainloop()
