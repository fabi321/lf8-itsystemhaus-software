# Phase 5

## Notwendige Daten

 - Raumplan
 - Übersicht der zu installierenden Hardware
 - Platzierung der zu installierenden Hardware

## Analysieren Sie die Datenquellen hinsichtlich der Bereitsteller/Orte und möglicher Datenformate in denen diese bereitgestellt werden können.

 - __Vom Architekten__: IFC
 - __Vom Gebäudetechniker__: Revit
 - __Vom Außendienst__: X3D

## Untersuchen Sie die Datenformate:
| Datenformat | Welche Daten <br>werden dargestellt                                                | Wie werden Daten in <br>den Datenquellen dargestellt                                                                                                                                                                    | Wie können diese importiert und <br>sinnvoll weiterverarbeitet werden                                            | Welche Metainformationen sind <br>zur Datenquelle vorhanden |
|-------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| .ifc        | - logische Bauwerkstrukturen<br>- zugehörige Eigenschaften<br>- optische Geometrie | - IfcObjectDefinition beinhaltet die Entitäten<br>- IfcRelationship beinhaltet die <br>beziehungen zwischen Entitäten<br>- IfcPropertyDefinition beinhaltet die Eigenschaften,<br>die mit den Entitäten verbunden sind | IFC-Dateien werden z.B. von Autodesk, Adobe Acrobat, <br>FME Desktop, CYPECAD, SketchUp und ARCHICAD unterstützt |                                                             |
| .rvt        | - 2D- und 3D-Modellierung für <br>bauteilorientierte Gebäudemodelle                |                                                                                                                                                                                                                         |                                                                                                                  |                                                             |
| .x3d        | - Koordinaten <br>vom Bauteil<br>- Material<br>- Networking und Animationen        |                                                                                                                                                                                                                         |                                                                                                                  |                                                             |


## Entscheiden Sie, wer die Daten innerhalb der ITSystemHausDD GmbH nutzen und verarbeiten darf.

 - Der __Außendienst__, um Raumpläne anzufertigen
 - Der __Innendienst__, um die eigentliche Planung vorzunehmen
 - Der __Verkauf__, um das Angebot erstellen zu können

## Entscheiden Sie sich für ein Datenformat für das Angebot.

PDF

