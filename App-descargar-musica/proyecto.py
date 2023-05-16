import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("Descarga de música")
        master.geometry("800x500")

        # Bloquear las dimensiones de la ventana
        master.resizable(width=False, height=False)

        
        # Fondo de pantalla
        bg_image = tk.PhotoImage(file="fondo.png")
        bg_label = tk.Label(master, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_image

        # Logo
        logo_image = tk.PhotoImage(file="logo.png")
        logo_label = tk.Label(master, image=logo_image)
        logo_label.place(x=350, y=50)
        logo_label.image = logo_image

        # Crear el input de texto y el botón
        self.url_label = ttk.Label(master, text="URL:", font=("Arial", 20))
        self.url_label.place(x=50, y=250)
        self.url_entry = ttk.Entry(master, font=("Arial", 16), width=50)
        self.url_entry.place(x=150, y=250)
        self.quality_label = ttk.Label(master, text="Calidad:", font=("Arial", 20))
        self.quality_label.place(x=50, y=300)
        self.quality_var = tk.StringVar()
        self.quality_var.set("128")  # Valor predeterminado
        self.quality_combobox = ttk.Combobox(master, values=["128", "320"], textvariable=self.quality_var, state="readonly", font=("Arial", 16), width=5)
        self.quality_combobox.place(x=180, y=300)
        self.download_button = ttk.Button(master, text="Descargar", command=self.download)
        self.download_button.place(x=350, y=400)

        # Crear el botón de selección de la carpeta de destino
        #self.directory_label = ttk.Label(master, text="Carpeta de destino:", font=("Arial", 20))
        #self.directory_label.place(x=50, y=350)
        self.directory_entry = ttk.Entry(master, font=("Arial", 16), width=45)
        self.directory_entry.place(x=180, y=350)
        self.directory_button = ttk.Button(master, text="Seleccionar carpeta", command=self.select_directory)
        self.directory_button.place(x=50, y=350)

        # Crear la barra de progreso
        self.progress = ttk.Progressbar(master, orient=tk.HORIZONTAL, length=500, mode='determinate')
        self.progress.place(x=150, y=450)

    def select_directory(self):
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)  # Borrar el contenido anterior
        self.directory_entry.insert(0, directory)

    def download(self):
        # Obtener la URL y la calidad de la música
        url = self.url_entry.get()
        quality = self.quality_var.get()

        # Obtener la carpeta de destino
        directory = self.directory_entry.get()
        if directory == "":
            tk.messagebox.showwarning("Carpeta no seleccionada", "Por favor seleccione una carpeta de destino.")
            return

        # Ejecutar el comando de deemix en la terminal
        command = f"deemix -b {quality} -p {directory} {url}"
        subprocess.run(command, shell=True)

        # Notificar que se ha completado la descarga
        self.progress['value'] = 100
        tk.messagebox.showinfo("Descarga completada", "La descarga ha sido completada.")
        self.progress['value'] = 0

root = tk.Tk()
app = App(root)
root.mainloop()
