# Model card for "Erstes exemplarisches neuronales Netz für Use-Case 2"

## Model details

Es wurde ein Feed Forward Neuronales Netz verwendet. Es besitzt drei Schichten.

- Eingabeschicht: 100 Neuronen, Aktivierung "relu"
- Versteckte Schicht 10 Neuronen, Aktivierung "relu"
- Ausgabeschicht: 1 Neuron, Aktivierung "sigmoid"

## Intended use

Das Modell ist zum Klassifizieren von Zeitreihen aus der BBG-Anlage.

## Metrics

Das Modell wurde über Loss und Accuracy evaluiert. Die Accuracy ist im Training auf 100% gestiegen.

### Model performance measures

### Decision thresholds

Es wird ein Decision thresholds von 0.9 bzw. 0.1 empfohlen.

### Approaches to uncertainty and variability

## Evaluation data

Die Evaluation data enthält Sample aus der gleichen Messung wie die Trainingsdaten.

### Datasets

Es gibt ein gut-Datensatz (~120 Trainingsdatenelemente) und einen schlecht-Datensatz (~60 Trainingsdatenelemente)

### Preprocessing
Das Preprocessing ist im Datasheet genauer beschrieben.

## Quantitative analyses
Das Modell konnte bisher nur auf wenig Daten trainiert werden. Es müssen mehr Daten bereitgestellt und fürs Training und die Evaluation genutzt werden, um das Modell tatsächlich für die Praxis Einsatzfähig zu bekommen und um es abschließend zu evaluieren.
