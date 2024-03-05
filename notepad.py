import tkinter as tk, mouse, customtkinter as Ctk, keyboard, os, win32com.client
from tkinter import filedialog
# Crea el acceso directo si no existe
if not os.path.exists(f'{__file__}.lnk'):
	shell = win32com.client.Dispatch('WScript.Shell')
	path_py = os.path.abspath(__file__)
	lnk = shell.CreateShortCut(f'{path_py}.lnk')
	lnk.Targetpath = 'C:\\Python312\\pythonw.exe'
	lnk.Arguments = path_py
	lnk.Hotkey = 'Ctrl+Shift+D'
	lnk.save()
#Crea el bloc de notas
def bloc(w,h,px,py):
	color_tx = '#FFFFFF'
	color_bg = '#0F0F0F'
	bloc = Ctk.CTk()
	bloc.geometry(f'{w}x{h}+{px}+{py}')
	bloc.attributes('-alpha', 0.5,'-topmost', True)
	bloc.title('Bloc de notas')
	font = tk.font.Font(family='consolas', size=12)
	text = tk.Text(bloc, font=font, bg=color_bg, fg=color_tx, bd=0)
	text.pack(expand=True, fill='both')
	#Funcion para guardar archivo con Ctrl+S
	def save_file():
		file_path = filedialog.asksaveasfilename(filetypes=[('Archivos de texto', '*.txt')], defaultextension=".txt")
		if file_path:
			with open(file_path, "w") as file:
				file.write(text.get('1.0', "end"))
	keyboard.add_hotkey('ctrl+s', save_file)
	bloc.mainloop()
#Evento del maus para obtener la seleccion
def mouse_event(event):
	px = event.x
	py = event.y
	mouse.wait()
	rx,ry=mouse.get_position()
	main.destroy()
	bloc(abs(rx-px),abs(ry-py),px,py)
#Ventana principal para detectar el mous
main = tk.Tk()
main.attributes('-fullscreen', True, '-alpha', 0.05, '-topmost', True)
main.bind('<Escape>', lambda _:main.destroy())
main.bind('<Button-1>', mouse_event)
main.configure(bg='#0000FF')
main.overrideredirect(True)
main.mainloop()