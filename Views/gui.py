from tkinter import *
from tkinter.filedialog import askopenfilename
from Controllers.controller import *
from Models.data import *

class GUI:
    root = Tk()
    root.geometry("800x600")
    root.title("Optymalizacja Kombinatoryczna - Projekt Zaliczeniowy")

    data = Data(None, None)
    data_var = StringVar(value="Maszyny: None\n Procesy: None")

    main_frame = Frame(root)
    main_frame.place(relwidth=1, relheight=1)

    @staticmethod
    def init_view():

        title_label = Label(
            GUI.main_frame,
            text="Optymalizacja Kombinatoryczna - Projekt Zaliczeniowy",
            font=("TkDefaultFont", 13)
        )

        instruction_label = Label(
            GUI.main_frame,
            text="Wybierz akcję:"
        )

        data_label = Label(
            GUI.main_frame,
            font=("TkDefaultFont", 10),
            textvariable=GUI.data_var
        )

        generate_button = Button(
            GUI.main_frame,
            width=17,
            text="Generator danych wej.",
            command=GUI.output_data_window
        )

        brute_force_button = Button(
            GUI.main_frame,
            width=15,
            text="s",
        )

        greedy_algorithm_button = Button(
            GUI.main_frame,
            width=17,
            text="Algorytm Zachłanny",     
        )

        input_data_button = Button(
            GUI.main_frame,
            width=21,
            text="Wprowadzanie danych wej.",
            command=GUI.input_data_window
        )

        title_label.place(relx=0.5, rely=0.15, anchor="center")
        instruction_label.place(relx=0.5, rely=0.7, anchor="center")
        data_label.place(relx=0.5, rely=0.4, anchor="center")

        generate_button.place(relx=0.10, rely=0.8, anchor="center")
        brute_force_button.place(relx=0.90, rely=0.8, anchor="center")
        greedy_algorithm_button.place(relx=0.75, rely=0.8, anchor="center")
        input_data_button.place(relx=0.50, rely=0.8, anchor="center")

        GUI.show_main_view()

    @staticmethod
    def input_data_window():
        path = askopenfilename(title='Wybierz plik danych wejściowych', filetypes=[('Pliki tekstowe', '*.txt'), ('Wszystkie pliki', '*.*')])
        if path:
            GUI.data.machines, GUI.data.jobs = Controller.file_input(path)
            GUI.data_var.set("Maszyny: " + str(GUI.data.machines) + "\n Procesy: " + str(GUI.data.jobs))

    @staticmethod
    def output_data_window():
        path = askopenfilename(title='Wybierz plik, do którego wygenerowane zostaną dane', filetypes=[('Pliki tekstowe', '*.txt'), ('Wszystkie pliki', '*.*')])
        if path:
            Controller.file_output(path)

    @staticmethod
    def show_main_view():
        GUI.main_frame.place(relwidth=1, relheight=1)

    @staticmethod
    def clear_work_frame():
        for widget in GUI.work_frame.winfo_children():
            widget.destroy()