import csv
from datetime import datetime
import dearpygui.dearpygui as dpg

file_csv = "eventi_led.csv"

def leggi_dati():
    conteggio_led = {}
    primo_ts = None
    ultimo_ts = None

    with open(file_csv, "r") as file:
        reader = csv.reader(file)

        for riga in reader:
            if len(riga) != 3:
                continue

            timestamp_str, evento, led = riga

            conteggio_led[led] = conteggio_led.get(led, 0) + 1

            ts = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            if primo_ts is None:
                primo_ts = ts
            ultimo_ts = ts

    tempo_totale = None
    if primo_ts and ultimo_ts:
        tempo_totale = ultimo_ts - primo_ts

    return conteggio_led, primo_ts, ultimo_ts, tempo_totale


def aggiorna_gui():
    conteggio_led, primo_ts, ultimo_ts, tempo_totale = leggi_dati()

    dpg.set_value("txt_primo", str(primo_ts))
    dpg.set_value("txt_ultimo", str(ultimo_ts))
    dpg.set_value("txt_totale", str(tempo_totale))

    label = list(conteggio_led.keys())
    valori = list(conteggio_led.values())

    x = list(range(len(label)))

    dpg.configure_item("bar_series", x=x, y=valori)

    ticks = [(i, label[i]) for i in range(len(label))]
    dpg.set_axis_ticks("x_axis", ticks)

dpg.create_context()

with dpg.window(label="Statistiche LED", width=600, height=700):

    dpg.add_text("Primo evento:")
    dpg.add_text("", tag="txt_primo")

    dpg.add_text("Ultimo evento:")
    dpg.add_text("", tag="txt_ultimo")

    dpg.add_text("Tempo totale:")
    dpg.add_text("", tag="txt_totale")

    with dpg.plot(label="Conteggio LED", height=300, width=400):
        dpg.add_plot_axis(dpg.mvXAxis, label="LED", tag="x_axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="Conteggio", tag="y_axis")

        dpg.add_bar_series([], [], parent="y_axis", tag="bar_series")

    dpg.add_button(label="Aggiorna", callback=lambda: aggiorna_gui())


dpg.create_viewport(title="Dashboard LED", width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
