import tkinter as tk


class PyUI:
    def __init__(self, master):
        self.master = master

        #Judul Program
        master.title("Input Text UI")

        #Label/Header
        self.label = tk.Label(master, text="Coba Ketik Sesuatu :")
        self.label.pack()

        #Untuk Tempat Input
        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Tombol", command=self.display_message)
        self.button.pack()

        self.message = tk.Label(master, text="")
        self.message.pack()

    def display_message(self):
        text = self.entry.get()
        message_text = "Anda Menulis : " + text + "\nProgram Selesai\n" \
                                                  "=================================="
        self.message.configure(text=message_text)

#Deklarasi tkinter
root = tk.Tk()

#Agar fullscreen
#root.attributes('-fullscreen', True)

#Menyetting Rasio Layar
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

my_ui = PyUI(root)
root.mainloop()
