# Datasheet for dataset "BBG Formenträger Positionierdaten"

## Motivation

Die Daten wurden aufgezeichnet um den Verschleiß des Formenträgers bei BBG zu ermitteln.

### For what purpose was the dataset created?

Die Daten sollen einen Rückschluss auf den Verschleißzustand des Antriebsriemens der Positioniereinheit ermöglichen.

### Who created the dataset?
Die Daten werden von BBG in Mindelheim an der "HSU-Anlage" aufgezeichnet. Die Aufnahmen wurden von einem Mitarbeiter von BBG durchgeführt.

### Who funded the creation of the dataset?

Das Projekt indem die Daten aufgezeichnet werden wird vom Zentrum für Digitalisierungs- und Technologieforschung der Bundeswehr gefördert.

## Composition

Der Datensatz besteht aus:
- 60 Aufnahmen, bei denen der Riemen verschlissen ist -> [Daten Verschlissen](/data/raw/60Hz_WZ1710kg)
- 128 Aufnahmen, bei denen der Riemen heile ist -> [Daten Gut](/data/raw/60Hz_WZ1710kg)

### What do the instances that comprise the dataset represent?

Die Daten bestehen aus Zeitreihen von mehreren Aufnahmekanälen. Darunter zählen wichtige Datenkanäle wie:
- Positionsdaten
- Relativer Schlupf des Antriebsmotors
- Antrieb Gestartet(1)/nicht Gestartet(0)

### Are there any errors, sources of noise, or redundancies in the dataset?

Teilweise werden einzelne Kanäle nicht mit Daten befüllt beim Aufnahmeprozess. Dieser Fehler muss in der Vorverarbeitung abgefangen werden.

## Collection process

### What mechanisms or procedures were used to collect the data?

Die Daten werden bei jeden Verfahrprozess der Anlage aufgezeichnet. Sowohl beim Schließen der Maschine als auch beim öffnen. Anschließend werden die Daten automatisiert mit einem zufälligen Namen ergänzt um das aktuelle Datum im JSON-Format abgelegt. Das Label wird über den überordner gekennzeichnet. Die dafür erforderliche Spannung / Schwingfrequenz des Riemens wird manuell in abständen von ca. 50 Fahrten ermittelt.


### Over what timeframe was the data collected?

Die Daten wurden über mehrere Fahrten an zwei Tagen aufgezeichnet.

## Preprocessing/cleaning/labeling

### Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

_If so, please provide a description. If not, you may skip the remainder of the questions in
this section._

### Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?

Die rohen Daten befinden sich in [Daten-Gut](/data/raw/60Hz_WZ1710kg) und [60Hz_WZ1710kg](Daten-Verschlissen/data/raw/). Die Daten werden durch ein Skript und entsprechende Funktionen aus data.utils vorverarbeitet. Dies geschieht wie folgt:
- Einlesen der rohen Daten
- Zuschneiden auf die Länge in der der Bewegungsprozess über den Prozesskanal Antrieb Gestartet(1) aktiv ist.
- Anschließend werden die Daten von ca. 1000 Messwerte für 5 Sekunden auf exakt 100 Messwerte resampled
- Dann werden die Daten in  [Daten-Vorverarbeitet](/data/processed) gespeichert als .pickle File.

Die Struktur der Daten in den .pickle-Files sieht wie folgt aus:

```JSON
  {
  	"file_nr_1": {
  		"FILE_PATH": "path",
  		"FILE_TYPE": "type",
  		"FILE_FOLDER": "folder",
  		"MOVE_LABEL": "up",
  		"FREQUENCY_LABEL": "freq",
  		"WEIGHT_LABEL": "weight",
  		"FILE_DEVICES": {
  			"device_nr_1": {
  				"SAMPLE_TIME": "sample_time",
  				"CHANNEL_DESCRIBTIONS": [
  					{
  						"name": "describtion_1",
  						"index": "index_1",
  						"subindex": "subindex_1",
  						"offset": "0",
  						"type": "Int32",
  						"unit": "1/min"
  					}
  				],
  				"SAMPLES": [
  					{
  						"EC_SYSTEM_TIMESTAMP": "timestamp",
  						"CHANNEL_DATA": [
  							0,
  							0,
  							0,
  							0,
  							0,
  							0,
  							0,
  							0
  						],
  						"SCALED_CHANNEL_DATA": [
  							0,
  							0,
  							0,
  							0,
  							0,
  							0,
  							0,
  							0
  						]
  					}
  				]
  			}
  		}
  	},
  	"file_nr_2": {
  		"FILE_PATH": "path",
  		"FILE_TYPE": "type",
  		"FILE_FOLDER": "folder",
  		"MOVE_LABEL": "up",
  		"FREQUENCY_LABEL": "freq",
  		"WEIGHT_LABEL": "weight",
  		"FILE_DEVICES": {
  			"device_nr_1": {
  				"SAMPLE_TIME": "sample_time",
  				"CHANNEL_DESCRIBTIONS": [
  					{
                          ...
  					},
  					{
                          ...
  					}
  				],
  				"SAMPLES": [
  					{
  						"EC_SYSTEM_TIMESTAMP": "timestamp",
  						"CHANNEL_DATA": [
                              ...
  						],
  						"SCALED_CHANNEL_DATA": [
                              ...
  						]
  					}
  				]
  			},
  			"device_nr_2": {
  				"SAMPLE_TIME": "sample_time",
  				"CHANNEL_DESCRIBTIONS": [
  					{
                          ...
  					},
  					{
                          ...
  					},
  					{
                          ...
  					},
  					{
                          ...
  					}
  				],
  				"SAMPLES": [
  					{
  						"EC_SYSTEM_TIMESTAMP": "timestamp",
  						"CHANNEL_DATA": [
                              ...
  						],
  						"SCALED_CHANNEL_DATA": [
                              ...
  						]
  					}
  				]
  			}
  		}
  	}
  }
```

### Is the software used to preprocess/clean/label the instances available?

Ja, der Code für die Vorverarbeitung kann im Jupyter Notebook unter [Jupyter-Notebook](notebooks/project.ipynb) nachgelesen werden.
