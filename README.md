# Computergestuetzte Visualisierung von Kammermusik
Dieses Programm visualisiert Kammermusik dreidimensional mit einer Ebene und Linien in Python.

## Produktidee
Die Visualisierung ist folgendermassen aufgebaut: 
- Jedes Instrument wird mit einer Linie visualisiert
- Die Tonhöhe wird durch die Höhe der Linie visualisiert. 
- Die Lautstärke wird durch die Dicke der Linien visualisiert. 
- Die Tondauer wird durch die Länge der Linie visualisiert, auf der die Linie auf der gleichen Höhe bleibt.
- Die Harmonien des Musikstückes werden durch die Farbe der Ebene visualisiert. 
- Das Tempo des Musikstückes wird durch die Frequenz der Ebene visualisiert. 

## Benötigte Bibliotheken
Folgende Bibliotheken sind für das Ausführen des Programms nötig:
- matplotlib: https://matplotlib.org/stable/users/installing/index.html
- mido: https://mido.readthedocs.io/en/latest/installing.html
- music21: https://pypi.org/project/music21/ 
- numpy: https://numpy.org/install/

## Ausführung des Programmes: main.py
Das Kammermusik-Stück muss als MIDI-Datei im gleichen Ordner abspeichern, in dem auch das Programm ist. Anschliessend kann in der Zeile 9 der Dateiname des Musikstückes folgendermassen eingegeben werden:
```python
file_path = "file-name.mid"
```

## Ordnerstruktur
Die Ordnerstruktur ist wie folgt aufgebaut:Der Ordner Entwicklung enthält alle Dateien, mit denen das Programm entwickelt worden ist. Dieser Ordner enthält folgende Unterordner
- Dateien zum Erstellen einer Ebene (1_plot-visualization)
- Dateien zum Erstellen einer Linie (2_line-visualization)
- Dateien zur Musikanalyse (3_music-analysis) 
- Dateien zur Visualisierung (4_visualization). 
Das Programm ist unter der Datei [main](main.py) zu finden. 

## Beispiel
Visualisierung des ersten Satzes aus dem Divertimento in F-Dur für 2 Oboen, 2 Hörner und 2 Fagotte von W. A. Mozart:

https://user-images.githubusercontent.com/103033812/205122106-8db08cb5-7209-4d22-af6c-14d9f30b7419.mov
