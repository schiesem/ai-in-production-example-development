# Model card for "U-Net für die Segmentierung von Primerfehlstellen"

- [Modelldetails](#model-details)
- [Verwendungszweck](#intended-use)
- [Faktoren](#factors)
- [Metriken](#metrics)
- [Evaluationsdaten](#evaluation-data)
- [Trainingsdaten](#training-data)
- [Quantitative Analysen](#quantitative-analyses)
- [Ethische Überlegungen](#ethical-considerations)
- [Vorbehalte und Empfehlungen](#caveats-and-recommendations)

## Modelldetails

_Grundlegende Informationen über das Modell._
Review section 4.1 of the [model cards paper](https://arxiv.org/abs/1810.03993).

- Entwickler: Interne Entwicklungsabteilung eines Unternehmens.
- Datum des Modells: August 2024.
- Version des Modells: Version 1.0.
- Modell-Typ: UNet-basiertes Convolutional Neural Network (CNN) zur Bildsegmentierung.
- Trainingsalgorithmen und Parameter:
    - Algorithmus: Adam-Optimizer mit Learning Rate Scheduling.
    - Parameter: Learning Rate: 0.001, Batch Size: 16, Epochen: 50.
    - Verwendete Bibliotheken: PyTorch, Albumentations für Datenaugmentation.
- Lizenz: MIT.
- Kontakt: Fragen oder Kommentare können an die interne Entwicklungsabteilung des Unternehmens gesendet werden.

### Modellarchitektur
Das entwickelte Modell basiert auf der UNet-Architektur, einer weit verbreiteten Architektur für Bildsegmentierungsaufgaben. Die UNet-Architektur zeichnet sich durch ihre Encoder-Decoder-Struktur aus, die es dem Modell ermöglicht, sowohl lokale als auch globale Merkmale aus den Eingabebildern zu extrahieren und zu verarbeiten.
Details zur Modellarchitektur:
- Encoder (Downsampling-Pfad):
  Der Encoder besteht aus einer Abfolge von ConvBlock- und Downscaling-Schichten. Jede dieser Schichten reduziert schrittweise die räumliche Auflösung der Eingabebilder, während sie die Anzahl der Merkmalskanäle erhöht.
  Der ConvBlock führt eine doppelte 3x3-Faltung mit einer ReLU-Aktivierung durch, gefolgt von einer Batch-Normalisierung. Der Downscaling-Block verwendet zusätzlich ein Max-Pooling, um die räumliche Größe zu halbieren.

- Bottleneck:
  In der Mitte des Netzwerks befindet sich das Bottleneck, das den tiefsten Punkt der UNet-Struktur darstellt. Hier werden die komplexesten und abstraktesten Merkmale extrahiert.

- Decoder (Upsampling-Pfad):
  Der Decoder besteht aus einer Reihe von Upscaling-Schichten. Jede dieser Schichten erhöht die räumliche Auflösung der Merkmalskarten durch eine transponierte Faltung (auch als ConvTranspose2d bekannt).
  Die Upscaling-Blöcke kombinieren die hochaufgelösten Merkmalskarten mit den entsprechenden Merkmalskarten aus dem Encoder über sogenannte Skip Connections. Diese Skip Connections stellen sicher, dass Detailinformationen, die während des Downsampling verloren gehen könnten, in die Rekonstruktion des Ausgabebildes einfließen.

- Ausgabeschicht (Output Layer):
  Die finale Ausgabeschicht (OutConv) ist eine 1x1-Faltung, die die Anzahl der Merkmalskarten auf die Anzahl der gewünschten Ausgabeklassen reduziert (in diesem Fall eine Klasse: Fehlstellen oder kein Fehlstellen).
  Die Ausgabe ist eine binäre Segmentierungsmaske, die angibt, welche Bildbereiche als Fehlstellen klassifiziert werden.

Genaue Modellarchitektur:
- Encoder (Downsampling-Pfad):
    -Eingang: Das Modell nimmt Bilder mit einem Kanal als Eingabe.
    - Stem Layer:
      - Convolution 1: 3x3-Faltung, 64 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
      - Convolution 2: 3x3-Faltung, 64 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
    - Downscaling 1:
      - Max-Pooling: 2x2, Stride 2.
      - Convolution 1: 3x3-Faltung, 128 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
      - Convolution 2: 3x3-Faltung, 128 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
    - Downscaling 2:
      - Max-Pooling: 2x2, Stride 2.
      - Convolution 1: 3x3-Faltung, 256 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
      - Convolution 2: 3x3-Faltung, 256 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
    - Downscaling 3:
      - Max-Pooling: 2x2, Stride 2.
      - Convolution 1: 3x3-Faltung, 512 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.
      - Convolution 2: 3x3-Faltung, 512 Filter, Stride 1, Padding 1.
      - Batch-Normalisierung und ReLU.

- Bottleneck: Hier werden die tiefsten Merkmale mit 512 Kanälen und einer reduzierten räumlichen Auflösung extrahiert.

- Decoder (Upsampling-Pfad):
  - Upscaling 1:
    - Transponierte Faltung: 2x2-Kernel, 256 Filter, Stride 2.
    - Convolution 1: 3x3-Faltung, 256 Filter, Stride 1, Padding 1.
    - Batch-Normalisierung und ReLU.
    - Convolution 2: 3x3-Faltung, 256 Filter, Stride 1, Padding 1.
    - Batch-Normalisierung und ReLU.
  - Upscaling 2:
    - Transponierte Faltung: 2x2-Kernel, 128 Filter, Stride 2.
    - Convolution 1: 3x3-Faltung, 128 Filter, Stride 1, Padding 1.
    - Batch-Normalisierung und ReLU.
    - Convolution 2: 3x3-Faltung, 128 Filter, Stride 1, Padding 1.
    - Batch-Normalisierung und ReLU.
  - Upscaling 3:
    - Transponierte Faltung: 2x2-Kernel, 64 Filter, Stride 2.
    - Convolution 1: 3x3-Faltung, 64 Filter, Stride 1, Padding 1.
    - Batch-Normalisierung und ReLU.
    - Convolution 2: 3x3-Faltung, 64 Filter, Stride 1, Padding 1.
    - Batch-Normalisierung und ReLU.

- Ausgabeschicht (Output Layer):
  - OutConv: 1x1-Faltung, 64 Eingangsfilter, 1 Ausgangsfilter, Stride 1.
  - Die Ausgabe ist eine binäre Segmentierungsmaske mit einer räumlichen Auflösung, die der Eingabe entspricht.

## Verwendungszweck
Review section 4.2 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Hauptverwendungszweck
Das Modell wurde entwickelt, um Fehlstellen im Primerauftrag auf Glasscheiben in einem industriellen Produktionsprozess zu erkennen und zu segmentieren. Ziel ist es, die manuelle visuelle Inspektion durch eine automatisierte, KI-gestützte Lösung zu ersetzen.

### Vorrangig vorgesehene Nutzer
Der primäre Einsatzbereich des Modells ist die automatisierte visuelle Inspektion von Glasscheiben in der Produktionslinie. Das Modell segmentiert die Bilddaten und markiert potenzielle Fehlstellen, die dann für weitere Prozessschritte verwendet werden.
Das Modell unterstützt ebenfalls die lückenlose Dokumentation der erkannten Fehlstellen. Die Segmentierungsergebnisse werden zusammen mit den spezifischen Bilddaten gespeichert und sind mit den zugehörigen Scheiben verknüpft, wodurch eine Rückverfolgbarkeit und Nachweisbarkeit der Produktqualität gewährleistet wird.

### Out-of-scope Use Cases

## Faktoren
Review section 4.3 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Relevante Faktoren
???
- Umgebungslicht: Variationen in den Lichtverhältnissen können die Leistung des Modells beeinträchtigen.
- Glasoberflächen: Unterschiedliche Glasarten oder Oberflächenbeschaffenheiten könnten das Modell beeinflussen.
- Kamerawinkel: Leichte Abweichungen im Kamerawinkel könnten die Bildqualität und somit die Modellleistung beeinträchtigen.

### Evaluationsfaktoren
?

## Metriken
Welche Metriken für eine Modellkarte geeignet sind, hängt von der Art des zu prüfenden Modells ab. Beispielsweise unterscheiden sich Klassifizierungssysteme, bei denen die primäre Ausgabe eine Klassenbezeichnung ist, erheblich von Systemen, deren primäre Ausgabe eine Punktzahl ist. In jedem Fall sollten die berichteten Metriken auf der Grundlage der Struktur und des Verwendungszwecks des Modells bestimmt werden.

Review section 4.4 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Modellleistungskennzahlen
- Dice Score: Bewertung der Überlappung zwischen vorhergesagten und tatsächlichen Segmenten.
- Jaccard Index: Ein Maß für die Ähnlichkeit zwischen den vorhergesagten und tatsächlichen Segmenten.

### Schwellenwerte für Entscheidungen
- Schwellenwert für Binärsegmentierung: 0.5.

### Ansätze für Unsicherheit und Variabilität
?

## Evaluationsdaten

Alle referenzierten Datensätze sollten idealerweise auf eine Reihe von Dokumenten verweisen, die Aufschluss über die Quelle und die Zusammensetzung des Datensatzes geben. Zu den Evaluierungsdatensätzen sollten Datensätze gehören, die für die Nutzung durch Dritte öffentlich zugänglich sind. Dabei kann es sich um bestehende Datensätze oder um neue Datensätze handeln, die zusammen mit den Modellkartenanalysen bereitgestellt werden, um ein weiteres Benchmarking zu ermöglichen.

Review section 4.5 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Datensätze
- Primärer Evaluierungsdatensatz: Interner Datensatz bestehend aus Produktionsbildern der Glasscheiben.

### Motivation
- Evaluationsziel: Sicherstellung, dass das Modell unter realen Produktionsbedingungen funktioniert.

### Vorverarbeitung
- Transformationen: Resize, Rotation, horizontale/vertikale Flip, Normalisierung.

## Trainingsdaten
Der Trainingsdatensatz besteht aus Bildern von Glasscheiben mit aufgetragenem Primer, die mit Fehlerannotationen versehen sind. Die Daten stammen aus derselben Produktionsumgebung wie die Evaluationsdaten.

## Quantitative Analysen
Quantitative Analysen sollten disaggregiert, d.h. nach den gewählten Faktoren aufgeschlüsselt werden. Die quantitativen Analysen sollten die Ergebnisse der Bewertung des Modells nach den gewählten Metriken liefern und, wenn möglich Konfidenzintervallwerte, wenn möglich.

Review section 4.7 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Einheitliche Ergebnisse
- Durchschnittlicher Dice Score auf Testdaten: ...
- Durchschnittlicher Jaccard Index auf Testdaten: ...

### Intersektionelles Ergebnis
?

## Ethische Überlegungen

Dieser Abschnitt soll die ethischen Überlegungen aufzeigen, die in die Modellentwicklung eingeflossen sind, und den Beteiligten ethische Herausforderungen und Lösungen aufzeigen. Die ethische Analyse führt nicht immer zu präzisen Lösungen, aber der Prozess der ethischen Betrachtung ist lohnenswert, um über verantwortungsvolle Praktiken und die nächsten Schritte in der zukünftigen Arbeit zu informieren.

Review section 4.8 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Daten
- Keine personenbezogenen Daten: Es wurden keine sensiblen oder personenbezogenen Daten verwendet.

### Menschliches Leben
- Keine direkten Auswirkungen: Das Modell beeinflusst keine Entscheidungen, die direkt das menschliche Leben betreffen.

### Abhilfemaßnahmen
- Kontinuierliche Überwachung: Fortlaufende Modellaktualisierungen und -verbesserungen basierend auf neuen Daten.

### Risiken und Schäden
- False Negative: Mögliche unentdeckte Fehlstellen könnten zu Qualitätsproblemen führen.

### Use Cases
- Hauptanwendung: Einsatz in der Qualitätssicherung während des Produktionsprozesses.

## Vorbehalte und Empfehlungen
Das Modell ist spezifisch für den Anwendungsfall der Primerfehlstellen-Erkennung auf Glasscheiben entwickelt worden. Es wird empfohlen, das Modell nur innerhalb dieses Anwendungsbereichs einzusetzen und bei Veränderungen in der Produktionsumgebung regelmäßig zu aktualisieren. Externe Verwendung sollte aufgrund möglicher Leistungseinbußen unter anderen Bedingungen vermieden werden.

Review section 4.9 of the [model cards paper](https://arxiv.org/abs/1810.03993).


