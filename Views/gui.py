from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
from Controllers.controller import *
from Models.data import *
from Views.gantt_chart import *

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
            command=GUI.generate_button_onclick
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
            command=GUI.greedy_algorithm_button_onclick
        )

        input_data_button = Button(
            GUI.main_frame,
            width=21,
            text="Wprowadzanie danych wej.",
            command=GUI.input_data_button_onclick
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
    def input_data_button_onclick():
        path = askopenfilename(title='Wybierz plik danych wejściowych', filetypes=[('Pliki tekstowe', '*.txt'), ('Wszystkie pliki', '*.*')])
        if path:
            GUI.data.machines, GUI.data.jobs = Controller.load_input_file(path)
            GUI.data_var.set("Maszyny: " + str(GUI.data.machines) + "\n Procesy: " + str(GUI.data.jobs))

    @staticmethod
    def generate_button_onclick():
        path = askopenfilename(title='Wybierz plik, do którego wygenerowane zostaną dane', filetypes=[('Pliki tekstowe', '*.txt'), ('Wszystkie pliki', '*.*')])
        if path:
            Controller.save_generated_input(path)

    @staticmethod
    def greedy_algorithm_button_onclick():
        if GUI.data.machines is None or GUI.data.jobs is None:
            tkinter.messagebox.showwarning('Błąd', 'Brak danych wejściowych - wczytaj lub wygeneruj dane.')
            return
        cmax, assignment = Controller.run_greedy_algorithm(GUI.data)
        GUI._show_greedy_result_window(cmax, assignment)

    @staticmethod
    def _show_greedy_result_window(cmax, assignment):
        window = Toplevel(GUI.root)
        window.title('Wynik algorytmu zachłannego')
        message = 'Algorytm zachłanny - wynik\n\n'
        message += 'Cmax: ' + str(cmax) + '\n\n'
        message += 'Przydział zadań:\n'
        for machine_nr, jobs_on_machine in enumerate(assignment, start=1):
            if jobs_on_machine:
                jobs_str = ' + '.join(str(job) for job in jobs_on_machine)
                message += 'Maszyna ' + str(machine_nr) + ': ' + jobs_str + ' (suma: ' + str(sum(jobs_on_machine)) + ')\n'
            else:
                message += 'Maszyna ' + str(machine_nr) + ': brak zadań (suma: 0)\n'
        summary_label = Label(
            window,
            text=message,
            justify='left',
            anchor='w',
            font=("TkDefaultFont", 10)
        )
        summary_label.pack(fill='x', padx=10, pady=(10, 0))
        canvas = Canvas(window, bg='white')
        canvas.pack(padx=10, pady=10)
        GanttChart.draw(canvas, assignment)

    @staticmethod
    def show_main_view():
        GUI.main_frame.place(relwidth=1, relheight=1)