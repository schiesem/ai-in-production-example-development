# KI in der Produktion - Leitfaden für eine Beispielentwicklung
Dieses Repo stellt einen Leitfaden und zwei Fallbeispiele für die Entwicklung von KI in Produktionssystemen bereit.

> [!CAUTION]
> This project is still in very early stages of development. Use at your own risk.

## Leitfaden und Nutzung
Zur Entwicklung von KI-Anwendungen in der Produktion wird zunächst das folgende [Projekt Folder Template](templates/folder-structure)[^1] für die Ordnerstruktur empfohlen. Für den Entwicklungsprozess empfielt das Prozessmodell aus Abb.1 einzelne Schritte die in Abb. 3 genauer spezifiziert werden. Der Ist-Stand der Anlage und die KI-Anwendung sollten mit dem [grafischen Beschreibungsmittel](https://github.com/schiesem/GML-AIAAS)[^5] modelliert werden. Die Informationen über die verwendeten Daten sollten mit einem [Data Sheet Template](templates/datasheets/datasheet-for-dataset-template.md)[^3] und die Infomrationen über das verwendete Modell mit einem [Model Card Template](templates/modelcards/model-card-template.md)[^4] festgehalten werden.

Zwei Fallbeispiele für die Umsetzung einer Exemplarischen Entwicklung finden sich hier
- [Fallbeispiel 1](use-case-1)
- [Fallbeispiel 2](use-case-2)

| <img src="/templates/figures/figures-DMME.png" width="450"/>|
|:--:|
| Abb.1: des Data mining methodology for engineering applications (DMME) Entwicklungprozesses nach Huber et. al[^2] |

| <img src="/templates/figures/process-steps.png" width="450"/>|
|:--:|
| Abb.2: Details zu den einzelnen DMME Schritten|

## Fallbeispiel 1
Kurzbeschreibung des Fallbeispiels (tbd.)

- [Jupyter Notebook](tbd.)
- [Datasheet](use-case-1/reports/datasheet.md)
- [Modelcard](use-case-1/reports/model-card.md)

## Fallbeispiel 2
Kurzbeschreibung des Fallbeispiels (tbd.)

- [Jupyter Notebook](use-case-2/notebooks/project.ipynb)
- [Datasheet](use-case-2/reports/datasheet.md)
- [Modelcard](use-case-2/reports/model-card.md)

# How to cite

This guideline is currently in a publishing process as a conference paper.
In case you want to use the presented use-cases, the guidline or the repo, please cite as:
```
tbd.
```
If you are using a BiBTex-file, you can copy the following:
```
@inProceedings{tbd.}
}
```

[^1]: https://github.com/cookiecutter/cookiecutter. 
[^2]: Quelle B.
[^3]: Quelle C.
[^4]: Quelle D.
