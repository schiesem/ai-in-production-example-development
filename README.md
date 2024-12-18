# KI in der Produktion - Leitfaden und Beispielentwicklung
Dieses Repo stellt einen Leitfaden und zwei Fallbeispiele für die Entwicklung von KI in Produktionssystemen bereit.

> [!CAUTION]
> This project is still in very early stages of development. Use at your own risk.

## Leitfaden und Nutzung
Zur Entwicklung von KI-Anwendungen in der Produktion wird zunächst das folgende [Projekt Folder Template](templates/folder-structure)[^1] für die Ordnerstruktur empfohlen. Für den Entwicklungsprozess empfielt das Prozessmodell aus Abb.1 einzelne Schritte die in Abb. 3 genauer spezifiziert werden. Der Ist-Stand der Anlage und die KI-Anwendung sollten mit dem [grafischen Beschreibungsmittel](https://github.com/schiesem/GML-AIAAS)[^2] modelliert werden. Die Informationen über die verwendeten Daten sollten mit einem [Data Sheet Template](templates/datasheets/datasheet-for-dataset-template.md)[^3] und die Infomrationen über das verwendete Modell mit einem [Model Card Template](templates/modelcards/model-card-template.md)[^4] festgehalten werden.

Zwei Fallbeispiele für die Umsetzung einer Exemplarischen Entwicklung finden sich hier
- [Project-Folder Fallbeispiel 1](use-case-1)
- [Project-Folder Fallbeispiel 2](use-case-2)

| <img src="/templates/figures/figures-DMME.png" width="450"/>|
|:--:|
| <p>Abb.1: Data mining methodology for engineering  <br> applications (DMME) Entwicklungprozesses nach Huber et. al[^5] </p>|

| <img src="/templates/figures/process-steps.png" width="450"/>|
|:--:|
| Abb.2: Details zu den einzelnen DMME Schritten|

## Fallbeispiel 1
Im ersten Fallbeispiel wird Computer Vision eingesetzt, um die Qualität von Bauteilen innerhalb einer Produktionslinie zu überwachen.
- [README Fallbeispiel 1](use-case-1/README.md)
- [Code-Übersicht Jupyter Notebook](tbd.)
- [Datasheet](use-case-1/reports/datasheet.md)
- [Modelcard](use-case-1/reports/model-card.md)

## Fallbeispiel 2
Im zweiten Fallbeispiel werden Zeitreihenanalysen eingesetzt, um den Zustand einer Produktionsanlage zu überwachen.
- [README Fallbeispiel 2](use-case-2/README.md)
- [Code-Übersicht Jupyter Notebook](use-case-2/notebooks/project.ipynb)
- [Datasheet](use-case-2/reports/datasheet.md)
- [Modelcard](use-case-2/reports/model-card.md)

# How to cite

This guideline and its use-cases were published as a conference paper. In case you want to use the presented use-cases, the guidline or the repo, please cite as:
```
M. Schieseck, P. Topalis, T. Zech, R. Ortloff, A. Fay: KI in der Produktion: KI vom Konzept zur Realisierung mit Fallbeispielen aus der Qualitäts- und Zustandsüberwachung. In: 25. VDI Automation, Baden-Baden, DE, 2024.
```
If you are using a BiBTex-file, you can copy the following:
```
@inproceedings{schieseck2024,
  title = {{KI in der Produktion: KI vom Konzept zur Realisierung mit Fallbeispielen aus der Qualitäts- und Zustandsüberwachung}},
  booktitle = {Automation 25.},
  author = {Schieseck, Marvin and Topalis, Philip and Zech, Tom and Ortloff, Richard and Fay, Alexander},
  year = {2024},
  pages = {303–-306},
  publisher = {{VDI Verlag}},
  doi={10.51202/9783181024379} 
}
```

[^1]: https://github.com/cookiecutter/cookiecutter. 
[^2]: Schieseck, M.; Topalis, P.; Fay, A.: A Graphical Modeling Language for Artificial Intelligence Applications in Automation Systems. In: 2023 IEEE 21st International Conference on Industrial Informatics (INDIN). Lemgo, DE, 2023.
[^3]: Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Iii, H. D., & Crawford, K. (2021). Datasheets for datasets. Communications of the ACM, 64(12), 86-92.
[^4]: Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., ... & Gebru, T. (2019, January). Model cards for model reporting. In Proceedings of the conference on fairness, accountability, and transparency (pp. 220-229).
[^5]: Huber, S.; Wiemer, H.; Schneider, D.; Ihlenfeldt, S.: DMME: Data mining methodology for engineering applications–a holistic extension to the CRISP-DM model. Procedia CIRP 79/, S. 403–408, 2019.
