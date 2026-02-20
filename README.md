# Analisi Eventi LED — Arduino + Python + DearPyGui

In collaborazione con jaupi Enrico.

Questo progetto permette di **registrare eventi generati da un sistema Arduino** (pressioni di pulsanti, cambi di stato LED, ecc.) e di **analizzarli tramite uno script Python** che produce:

- statistiche sugli eventi
- conteggio per LED
- primo e ultimo timestamp
- tempo totale di utilizzo
- una dashboard grafica interattiva realizzata con **DearPyGui**

---

## Python — Analisi dei dati

Lo script `analisi.py`:

- legge il file CSV
- calcola:
  - conteggio eventi per LED
  - primo timestamp
  - ultimo timestamp
  - durata totale
- mostra una **dashboard grafica** con:
  - testo riepilogativo
  - grafico a barre aggiornabile

---

## Dashboard DearPyGui

La GUI include:

- **Statistiche temporali**
- **Grafico a barre** con il numero di eventi per LED
- **Pulsante "Aggiorna"** per ricaricare il CSV
- Aggiornamento automatico al primo frame
