import tkinter as tk
from tkinter import filedialog

# <a href="https://www.flaticon.com/free-icons/notes" title="notes icons">Notes icons created by Freepik - Flaticon</a>

class Meny:
    def __init__(self, vebtext):
        default_font = ("arial", 12)
        meny = tk.Menu(vebtext.master, font=default_font)
        vebtext.master.config(menu=meny)

        # Instansierer en menybar, med font og størrelse. Tearoff gjør at dropdownmenyen ikke kan dras rundtom
        file_dropdown = tk.Menu(meny, font=default_font, tearoff=0)
        # Lager punkter i dropdownmenyen, der label er navnet og command er funksjonen som blir kalt når man trykker på knappen
        file_dropdown.add_command(label="New File", command=vebtext.new_file)
        file_dropdown.add_command(label="Open File", command=vebtext.open_file)
        # Seperator er bare en fin ting som skiller punktene i menyen
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save", command=vebtext.save_file)
        file_dropdown.add_command(label="Save As", command=vebtext.save_file_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=vebtext.master.destroy)

        meny.add_cascade(label="File", menu=file_dropdown)

class VebText:

    def __init__(self, master):
        self.master = master
        self.filename = None

        # Gir vinduet en default tittel, ikon, og størrelse på vinduet
        master.title("Untitled - VebText")
        # TODO få denne til å fungere
        # master.iconbitmap(default="/assets/programicon.bmp")
        master.geometry("900x700")

        default_font = ("Arial", 14)

        # Instansierer en textbox og scrollbar
        self.text = tk.Text(master, font=default_font)
        self.scroll = tk.Scrollbar(master, command=self.text.yview())
        self.text.configure(yscrollcommand=self.scroll.set)

        # Setter tekstområdet på venstreside og scrollbaren på høyreside
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Instansierer menyen
        self.meny = Meny(self)

    def new_title(self, name=None):
        if name:
            master.title(name + " - VebText")
        else:
            master.title("Untitled - VebText")

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.filename = None
        self.new_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Files", "*.txt"),
                ("Text Files", "*.docx"),
                ("Python Files", "*.py"),
                ("HTML Files", "*.html"),
                ("Css Files", "*.css"),
                ("C Files", "*.c"),
                ("JavaScript Files", "*.js")])

        if self.filename:
            self.text.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.text.insert(1.0, f.read())
            self.new_title(self.filename)

    def save_file(self):
        if self.filename:
            try:
                text_content = self.text.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(text_content)
            except Exception as e:
                print(e)
        else:
            self.save_file_as()

    def save_file_as(self):
        try:
            file_name = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[
                    ("All Files", "*.*"),
                    ("Text Files", "*.txt"),
                    ("Text Files", "*.docx"),
                    ("Python Files", "*.py"),
                    ("HTML Files", "*.html"),
                    ("Css Files", "*.css"),
                    ("C Files", "*.c"),
                    ("JavaScript Files", "*.js")])
            text_content = self.text.get(1.0, tk.END)
            with open(file_name, "w") as f:
                f.write(text_content)
            self.filename = file_name
            self.new_title(file_name)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # Instansierer en master tk
    master = tk.Tk()
    # Instansierer et objekt av vebtext
    vebtext = VebText(master)
    master.mainloop()