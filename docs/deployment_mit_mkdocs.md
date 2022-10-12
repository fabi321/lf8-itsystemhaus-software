# Docs deployment auf Github-Pages mit mkdocs

## MkDocs installieren

```
pip install mkdocs mkdocs-material
```

!!! note "Verwendung des proxy"
	In der schule muss python die verwendung des Proxy mittgeteilt werden. Dies geschieht durch die Option --proxy. Der resultierende Befehl sieht also wie folgt aus:
	```
	pip --proxy http://kjs-03.lan.dd-schulen.de:3128  install mkdocs mkdocs-material
	```

## Mit mkdocs anfangen

Zuerst muss man eine mkdocs.yml Datei anlegen, die die Struktur und das Aussehen der Dokumentation beschreibt. Ein Beispiel könnte wie folgt aussehen:
```
site_name: Projektname
nav:
  - index.md
theme: material
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

Dazu benötigt man eine Verzeichnisstruktur wie folgt:
```
Projektverzeichnis
 |- mkdocs.yml
 \- docs
  \- index.md
```

## Dokumentation lokal ansehen

Dazu führt man mkdocs mit dem Unterbefehl serve wie folgt aus
```
mkdocs serve
```

!!! note "Befehl konnte nicht gefunden werden"
	Falls ihr mkdocs installiert habt, es aber fon der git bahsh nicht gefunden werden kann, ist es wahrscheinlich nicht im Pfad enthalten. Für diesen Fall müsst ihr den Befehl `mkdocs` in diesem und weiteren Aufrufen ersetzen durch:
	```
	~/AppData/Roaming/Python/Python310/Scripts/mkdocs.exe
	```

Anschließend kann man sich die Dokumentation unter [localhost:8000](http://localhost:8000) ansehen.
Der Webserver kann durch drücken von Strg+C beendet werden.

## Auf Github-Pages deployen

Github-Pages ist für jedes Repository auf Github verfügbar.
Um eine MkDocs-Seite über Github-Pages verfügbar zu machen, muss man zuerst den Subbefehl gh-deploy von MkDocs ausführen:
```
mkdocs gh-deploy
```

Anschließend sollte Github automatisch ein Github-Pages Environment hinzufügen, welches die Seite unter `https://<username>.github.io/<repositoryName>` verfügbar machen.

