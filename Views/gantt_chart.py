class GanttChart:
    MACHINE_COLORS = ('#4E79A7', '#F28E2B', '#59A14F', '#E15759', '#B07AA1', '#76B7B2', '#EDC948', '#FF9DA7', '#9C755F')
    LEFT_MARGIN = 90
    RIGHT_PAD = 15
    AXIS_HEIGHT = 25
    ROW_HEIGHT = 35
    BAR_HEIGHT = 25

    @staticmethod
    def draw(canvas, assignment):
        machines = len(assignment)
        cmax = max((sum(jobs_on_machine) for jobs_on_machine in assignment), default=0)
        max_jobs = max((len(jobs_on_machine) for jobs_on_machine in assignment), default=1)
        width = max(480, GanttChart.LEFT_MARGIN + GanttChart.RIGHT_PAD + 25 * max_jobs)
        height = 10 + GanttChart.ROW_HEIGHT * machines + GanttChart.AXIS_HEIGHT
        canvas.config(width=width, height=height)
        usable = width - GanttChart.LEFT_MARGIN - GanttChart.RIGHT_PAD
        scale = usable / cmax if cmax else 0

        for machine_nr, jobs_on_machine in enumerate(assignment):
            y0 = 10 + machine_nr * GanttChart.ROW_HEIGHT
            canvas.create_text(GanttChart.LEFT_MARGIN - 10, y0 + GanttChart.BAR_HEIGHT / 2, anchor='e', text='Maszyna ' + str(machine_nr + 1))
            if not jobs_on_machine:
                canvas.create_line(GanttChart.LEFT_MARGIN, y0 + GanttChart.BAR_HEIGHT / 2, GanttChart.LEFT_MARGIN + usable, y0 + GanttChart.BAR_HEIGHT / 2, dash=(3, 3), fill='grey')
                canvas.create_text(GanttChart.LEFT_MARGIN + usable / 2, y0 + GanttChart.BAR_HEIGHT / 2, text='brak zadań', fill='grey')
                continue
            offset = 0
            for job in jobs_on_machine:
                x0 = GanttChart.LEFT_MARGIN + offset * scale
                x1 = GanttChart.LEFT_MARGIN + (offset + job) * scale
                color = GanttChart.MACHINE_COLORS[machine_nr % len(GanttChart.MACHINE_COLORS)]
                canvas.create_rectangle(x0, y0, x1, y0 + GanttChart.BAR_HEIGHT, fill=color, outline='black')
                canvas.create_text((x0 + x1) / 2, y0 + GanttChart.BAR_HEIGHT / 2, text=str(job))
                offset += job

        axis_y = 10 + machines * GanttChart.ROW_HEIGHT
        canvas.create_line(GanttChart.LEFT_MARGIN, axis_y, GanttChart.LEFT_MARGIN + usable, axis_y)
        step = max(1, cmax // 10)
        tick = 0
        while tick <= cmax:
            x = GanttChart.LEFT_MARGIN + tick * scale
            canvas.create_line(x, axis_y, x, axis_y + 4)
            canvas.create_text(x, axis_y + 14, text=str(tick))
            tick += step
