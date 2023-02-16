import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

class Window(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure((2, 3), weight=0)
		self.grid_rowconfigure((0, 1, 2), weight=1)
		self.title('Combo Menu')
		self.geometry(f'{1600}x{900}')
		self.iconbitmap('Icon.ico')
		
		frame = ctk.CTkFrame(self, corner_radius=0)
		frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
		frame.grid_rowconfigure(4, weight=1)
		label = ctk.CTkLabel(frame, text="Combo Menu GUI", font=ctk.CTkFont(size=20, weight="bold"))
		label.grid(row=0, column=0, padx=20, pady=(20, 10))
		
		Window.mainloop(self)
  