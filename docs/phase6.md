# Phase 6

## Identifizierte Nutzer

Schreibrechte implizieren Leserechte

| Nutzer | Leserechte | Schreibrechte |
|--------|------------|---------------|
| Einkauf | Übersicht der zu installierenden Hardware |  |
| Verkauf | Raumplan, Übersicht der zu installierenden Hardware, Platzierung der zu installierenden Hardware |  |
| Innendienst |  | Raumplan, Übersicht der zu installierenden Hardware, Platzierung der zu installierenden Hardware | 
| Außendienst | bereitgestellter Grundriss | Raumplan |
| Administrator |  | Raumplan, Übersicht der zu installierenden Hardware, Platzierung der zu installierenden Hardware, bereitgestellter Grundriss |

## Praktische Umsetzung

Implementierung des Rollen- und Berechtigungskonzeptes mit SQLite, grafische Oberfläche wird über SQLite Browser realisiert.
Die Schnittstelle findet über C Aufrufe statt.

