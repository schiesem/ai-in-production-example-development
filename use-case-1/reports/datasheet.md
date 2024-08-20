# Datasheet for dataset "BBG: Primererkennung"

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation
Die Fragen in diesem Abschnitt sollen die Ersteller von Datensätzen in erster Linie dazu ermutigen, ihre Gründe für die Erstellung des Datensatzes klar darzulegen und die Transparenz hinsichtlich der Finanzierungsinteressen zu fördern.


### Zu welchem Zweck wurde der Datensatz erstellt? 
Der primäre Zweck des Datensatzes besteht darin, ein KI-Modell zu trainieren, das Fehlstellen im Primerauftrag auf Autoscheiben erkennt und lokalisiert. Dies ermöglicht die Automatisierung der visuellen Qualitätskontrolle in der Produktionslinie.


### Wer hat den Datensatz erstellt (z. B. welches Team, welche Forschungsgruppe) und im Namen welcher Einrichtung (z. B. Unternehmen, Institution, Organisation)?
BBG: Automatisierungsteam


### Wer hat die Erstellung des Datensatzes finanziert?
BBG hat die Erstellung des Datensatzes finanziert. Es gab keine Zuschussgeber.


### Sonstige Anmerkungen?
-


## Zusammensetzung
_Die meisten dieser Fragen sollen den Nutzern des Datensatzes die Informationen liefern
Informationen liefern, die sie benötigen, um fundierte Entscheidungen über die Verwendung des Datensatzes für bestimmte Aufgaben zu treffen. Die Antworten auf einige dieser Fragen geben Aufschluss über die Einhaltung der EU-Datenschutzgrundverordnung (GDPR) oder vergleichbarer Vorschriften in anderen Rechtsordnungen._


### Was stellen die Instanzen dar, aus denen der Datensatz besteht (z. B. Dokumente, Fotos, Personen, Länder)?
Die Instanzen, aus denen der Datensatz besteht, sind Fotos (Bilder) von Glasscheiben, die während des Primer-Auftrags in einer industriellen Umgebung aufgenommen wurden. Jedes Bild erfasst den Zustand des Primers, der auf die Ränder der Glasscheiben aufgetragen wurde, wobei der Schwerpunkt auf der Identifizierung und Dokumentation von Fehlstellen liegt (Bereiche, in denen der Primer nicht richtig aufgetragen wurde).


### Wie viele Instanzen gibt es insgesamt (ggf. von jedem Typ)?
1950 in Train, 209 in Val, 420 in Test 


### Enthält der Datensatz alle möglichen Instanzen oder handelt es sich um eine Stichprobe (nicht unbedingt zufällig) von Instanzen aus einer größeren Menge?
Der Datensatz stellt eine Stichprobe von Instanzen aus einer größeren Menge dar, nämlich aus der Gesamtproduktion von Glasscheiben, auf die Primer aufgetragen wird. Diese zusammengestellte Stichprobe besteht aus zwei möglichen Variationen von Scheiben, die im Laufe des Forschungsprojektes EKI umschäumt werden. Um die Repräsentativität der Stichprobe zu gewährleisten enthalten die Aufnahmen verschiedene Ausprägungen von Fehlstellen und wurden unter unterschiedlichen Bedingungen, die während des Produktionsprozesses auftreten können, aufgenommen. Diese Auswahl ermöglicht es die Vielfalt und Komplexität der potenziellen Fehler abzudecken, sodass das Modell auf eine breite Palette von Situationen, die in der tatsächlichen Produktionsumgebung auftreten können, trainiert wurde. Die Validierung erfolgte durch die Überprüfung der Modellleistung auf Testdaten, die eine ähnliche Vielfalt aufweisen wie die Trainingsdaten.
Dennoch besteht die Gefahr, dass die Stichprobe möglicherweise nicht vollständig repräsentativ für alle denkbaren Fälle ist, da bestimmte Szenarien, die selten auftreten, möglicherweise nicht im Datensatz enthalten sind. 

Insgesamt wurde die Stichprobe so gewählt, dass sie eine robuste Grundlage für das Training und die Evaluierung des Modells bietet, auch wenn nicht alle möglichen Szenarien abgedeckt sind.



### Aus welchen Daten besteht die jeweilige Instanz? 
Jede Instanz des Datensatzes besteht aus folgenden Daten:
- Bilder: Die Kernkomponente jeder Instanz ist ein Bild, das während des Produktionsprozesses aufgenommen wurde. Diese Bilder zeigen den auf die Glasscheiben aufgetragenen Primer und enthalten sowohl korrekte Bereiche als auch Fehlstellen (Bereiche, in denen der Primer nicht ordnungsgemäß aufgetragen wurde). Die Bilder sind in einem unkomprimierten oder verlustfreien Format gespeichert, um eine hohe Qualität für die Bildverarbeitung zu gewährleisten.
- Metadaten zu den Bildern:
    - Segmentinformationen: Jedes Bild ist einem bestimmten Segment des Pfades zugeordnet, den der Roboter während des Primerauftragsprozesses zurückgelegt hat. Diese Segmentinformationen helfen dabei, die genaue Position der Glasscheibe während der Bildaufnahme zu rekonstruieren.
    - RFID-Tag: Jedem Bild ist eine eindeutige Identifikationsnummer (RFID-Tag) zugeordnet, die es ermöglicht, das Bild mit einer spezifischen Glasscheibe zu verknüpfen und die Rückverfolgbarkeit zu gewährleisten.


### Gibt es für jede Instanz ein Label oder ein Ziel?
Jedes Bild ist mit einer sogenannten Segmentierungsmaske (Fehlstellenannotation) versehen, die das Ziel oder Label darstellt. Diese Maske ordnet jedem Pixel im Bild eine Kategorie zu, entweder „Primer vorhanden“ oder „Fehlstelle“.
Die Segmentierungsmaske ist eine binäre Maske, bei der Fehlstellen als „1“ (oder eine spezifische Farbe) und korrekt geprimerte Bereiche als „0“ (oder eine andere Farbe) markiert sind.
Diese Masken werden entweder manuell annotiert, basierend auf bestehenden Qualitätskontrollen, die Fehlstellen markieren.

    Zusätzliche Metadaten:
        In manchen Fällen können zusätzliche Labels vorhanden sein, die spezifische Eigenschaften der Fehlstellen beschreiben, wie z. B. die Größe, Form oder Position auf der Glasscheibe. Diese Metadaten können zur Verfeinerung der Modellvorhersagen genutzt werden.

Die Labels dienen als „Ground Truth“ (Referenzwerte), gegen die das Modell während des Trainings und der Evaluierung bewertet wird. Sie sind entscheidend, um dem Modell beizubringen, zwischen korrekt und fehlerhaft geprimerte Bereiche zu unterscheiden und diese Fehlstellen genau zu lokalisieren.


### Fehlen Informationen aus einzelnen Instanzen?
Nein.


### Werden Beziehungen zwischen einzelnen Instanzen explizit gemacht (z. B. Filmbewertungen der Nutzer, Links zu sozialen Netzwerken)?
Nein, in diesem Datensatz werden keine expliziten Beziehungen zwischen den einzelnen Instanzen hergestellt. Jede Instanz, also jedes Bild mit den zugehörigen Labels und Metadaten, wird als eigenständige Einheit behandelt.
Die einzige indirekte Verbindung zwischen den Instanzen könnte durch die RFID-Tag-Information bestehen, die einzelne Bilder einer bestimmten Glasscheibe zuordnet. Diese Information dient jedoch primär der Rückverfolgbarkeit und nicht zur Analyse von Beziehungen zwischen den Bildern.


### Gibt es eine empfohlene Aufteilung der Daten (z. B. Training, Entwicklung/Validierung, Test)? 
Die Daten wurden im Verhältnis 70% für das Training, 15% für die Validierung und 15% für den Test aufgeteilt. Diese Aufteilung wurde vorgenommen, um sicherzustellen, dass das Modell auf einer ausreichend großen Menge von Daten trainiert wird, während gleichzeitig genügend Daten für die Evaluierung und Validierung bereitgestellt werden.


### Gibt es Fehler, Störquellen oder Redundanzen im Datensatz?
_If so, please provide a description._


### Ist der Datensatz in sich geschlossen oder verweist er auf externe Ressourcen (z. B. Websites, Tweets, andere Datensätze) oder greift er auf diese zurück?
Der Datensatz ist in sich geschlossen und enthält alle notwendigen Informationen und Daten, die für das Training und die Evaluierung des KI-Modells erforderlich sind. Er verweist nicht auf externe Ressourcen wie Websites, Tweets oder andere Datensätze und greift auch nicht auf solche zurück.
Alle Daten, die für das Modelltraining und die Evaluierung benötigt werden, befinden sich direkt im Datensatz. 


### Enthält der Datensatz Daten, die als vertraulich eingestuft werden könnten (z. B. Daten, die durch das Anwaltsgeheimnis oder die ärztliche Schweigepflicht geschützt sind, Daten, die den Inhalt nichtöffentlicher Mitteilungen von Einzelpersonen enthalten)?
Nein, der Datensatz enthält keine Daten, die als vertraulich eingestuft werden könnten. Es handelt sich ausschließlich um technische Daten, nämlich Bilder von Glasscheiben und deren Primerauftrag, sowie zugehörige technische Metadaten (z. B. Segmentinformationen, Fehlstellenannotationsdaten).
Es gibt keine personenbezogenen Daten, keine Daten, die durch das Anwaltsgeheimnis, die ärztliche Schweigepflicht oder andere Schutzmechanismen abgedeckt wären, und keine nichtöffentlichen Mitteilungen von Einzelpersonen. Alle Daten im Datensatz beziehen sich auf industrielle Prozesse und sind rein technischer Natur.


### Enthält der Datensatz Daten, die bei direkter Betrachtung anstößig, beleidigend, bedrohlich oder anderweitig beunruhigend sein könnten?
Nein, der Datensatz enthält keine Daten, die bei direkter Betrachtung anstößig, beleidigend, bedrohlich oder anderweitig beunruhigend sein könnten. 


### Bezieht sich der Datensatz auf Personen? 
Nein, der Datensatz bezieht sich nicht auf Personen.


### Weist der Datensatz irgendwelche Untergruppen aus (z. B. nach Alter, Geschlecht)?
Nein, der Datensatz weist keine Untergruppen im Sinne von demografischen Merkmalen wie Alter, Geschlecht oder ähnlichem auf. Da es sich um einen technischen Datensatz handelt, der sich auf den industriellen Prozess der Qualitätskontrolle von Glasscheiben und deren Primerauftrag konzentriert, gibt es keine menschlichen oder demografischen Daten, die typischerweise zur Bildung solcher Untergruppen führen würden.
Die Instanzen im Datensatz könnten nach technischen Kriterien wie der Art der Fehlstellen, dem Scheibentyp, den Produktionschargen, den verwendeten Kamerakonfigurationen oder ähnlichen Aspekten kategorisiert werden. Diese Kategorien würden jedoch nicht als klassische Untergruppen im sozialen oder demografischen Sinne gelten und sind rein technischer Natur.
Daher gibt es keine spezifischen Untergruppen und somit auch keine Verteilungen dieser innerhalb des Datensatzes, die beschrieben werden könnten.


### Ist es möglich, Einzelpersonen (d. h. eine oder mehrere natürliche Personen) entweder direkt oder indirekt (d. h. in Kombination mit anderen Daten) anhand des Datensatzes zu identifizieren?
Nein.


### Enthält der Datensatz Daten, die in irgendeiner Weise als sensibel angesehen werden könnten (z. B. Daten, die Aufschluss über die rassische oder ethnische Herkunft, die sexuelle Orientierung, religiöse Überzeugungen, politische Meinungen oder Gewerkschaftszugehörigkeit oder den Standort geben; Finanz- oder Gesundheitsdaten; biometrische oder genetische Daten; Formen der staatlichen Identifizierung, wie Sozialversicherungsnummern; Vorstrafen)?
Nein


### Sonstige Anmerkungen?
-


## Erhebungsprozess
Die Antworten auf diese Fragen können Informationen liefern, die es anderen ermöglichen den Datensatz zu rekonstruieren, ohne Zugang zu ihm zu haben.


### Wie wurden die Daten zu den einzelnen Instanzen erfasst?
Die Daten zu den einzelnen Instanzen im Datensatz wurden direkt beobachtbar erfasst. Die Bilder wurden direkt während des Primerauftragsprozesses aufgenommen. Eine Kamera, die in der Produktionszelle hinter der Auftragseinheit positioniert ist, erfasst die Glasscheiben entlang der Bewegung des Roboters. Die Bildaufnahmen erfolgen automatisch, synchronisiert mit der Bewegungsgeschwindigkeit des Roboters und dem Produktionsprozess. Die Bilder werden in regelmäßigen Abständen entlang der Roboterpfade aufgenommen.


### Welche Mechanismen oder Verfahren wurden für die Datenerhebung verwendet (z. B. Hardware-Geräte oder Sensoren, manuelle Pflege durch Menschen, Softwareprogramme, Software-API)?
Folgende Mechanismen und Verfahren wurden zur Datenerhebung verwendet:
- Kamera: Die Datenerfassung erfolgt mit der Wenglor B50M012 Smart Camera. Diese Kamera wurde im Vorfeld umfangreich getestet, um sicherzustellen, dass sie unter den verschiedenen Bedingungen der Produktionsumgebung, einschließlich variabler Lichtverhältnisse und Oberflächenreflexionen, konsistent hochwertige Bilder liefert.
- Roboter: Ein Roboter, der die Glasscheiben entlang einer definierten Trajektorie führt, koordiniert die Bewegung der Scheiben an der Auftragseinheit vorbei und synchronisiert die Bildaufnahme mit der Kameraposition. Das Triggern der Kamera von der Robotersteuerung wurde getestet, um sicherzustellen, dass die Kamera die erforderlichen Bildausschnitte in Abhängigkeit der Position der Glasscheiben präzise erfasst. Zudem wurden die Bewegungstrajektorien und die Positionierungsgenauigkeit des Roboters validiert, um sicherzustellen, dass die Glasscheiben präzise entlang des gewünschten Pfades geführt werden und die Kamera die relevanten Bildausschnitte erfasst
- RFID-Reader: Ein RFID-Reader erfasst die eindeutige Identifikationsnummer jeder Glasscheibe, um die Rückverfolgbarkeit sicherzustellen und die Bilder den entsprechenden Scheiben zuzuordnen.
- Edge-Gerät und Cloud-Anbindung: Ein Edge-Steuergerät verarbeitet die aufgenommenen Bilder vor, bevor sie zur weiteren Analyse und Modelltraining in die Cloud übertragen werden. Die Vorverarbeitung umfasst grundlegende Schritte wie Bildnormalisierung und das Filtern von unerwünschtem Rauschen. Dieser Prozess wurde überprüft, um eine verlustfreie und korrekte Verarbeitung der Bilddaten sicherzustellen.
- API und Kommunikationsprotokoll: Die Kamera verwendet das LIMA-Protokoll zur Kommunikation und Steuerung. Das LIMA-Protokoll ermöglicht eine zuverlässige und präzise Steuerung der Kamera sowie die Übertragung der Bilddaten an das Edge-Gerät. Es wurde auf zuverlässige Datenübertragung und präzise Steuerung der Kamerafunktionen getestet. Hierbei wurde sichergestellt, dass alle Steuerbefehle und Daten korrekt und ohne Verzögerung übertragen werden.
Die gewählten Mechanismen und Validierungsmaßnahmen gewährleisten, dass die Wenglor B50M012 Smart Camera und das LIMA-Protokoll optimal für diesen industriellen Anwendungsfall geeinet und konfiguriert sind, dass sie eine zuverlässige Datenbasis für das KI-Modell bereitstellen.


### Wenn es sich bei dem Datensatz um eine Stichprobe aus einer größeren Menge handelt, welche Stichprobenstrategie wurde verwendet (z. B. deterministisch, probabilistisch mit bestimmten Stichprobenwahrscheinlichkeiten)?
Da es sich bei dem Datensatz um eine Stichprobe aus einer größeren Menge von Glasscheiben handelt, wurde eine gezielte deterministische Stichprobenstrategie verwendet. Diese Strategie wurde gewählt, um sicherzustellen, dass die Stichprobe eine breite Vielfalt an möglichen Szenarien und Fehlerarten abdeckt, die während des Primerauftragsprozesses auftreten können. Ziel war es, sicherzustellen, dass die Stichprobe repräsentativ für die häufigsten und kritischsten Fehlerszenarien ist, die in der Praxis auftreten könnten.
Es wurde darauf geachtet, dass die Stichprobe Bilder enthält, die aus verschiedenen Produktionschargen, mit unterschiedlichen Glasscheiben und bei variierenden Umgebungsbedingungen aufgenommen wurden. Dies soll sicherstellen, dass das Modell robust gegenüber unterschiedlichen Produktionsbedingungen ist. Zudem wurde beachtet, dass eine Vielzahl von Fehlstellenarten im Primerauftrag umfasst, einschließlich unterschiedlicher Größen und Formen der Fehlstellen.


### Wer war an der Datenerhebung beteiligt (z. B. Studenten, Crowdworker, Auftragnehmer) und wie wurden sie entlohnt (z. B. wie viel erhielten die Crowdworker)?
Die Datenerhebung in diesem Anwendungsfall erfolgte durch ein Team von Fachleuten aus verschiedenen Bereichen (Produktion, Automatisierung und KI). Die Techniker und Produktionsmitarbeiter sind verantwortlich für die Einrichtung und Überwachung der Produktionslinie, einschließlich der Konfiguration der Wenglor B50M012 Smart Camera und des Robotersystems. Sie sorgten dafür, dass die Kamera korrekt positioniert und kalibriert wurde, um qualitativ hochwertige Bilder zu erfassen. Zudem führten sie aufgrund ihres Domänenwissens die Annotation der Daten durch. Die Automatisierungsingenieure waren zuständig für die Integration und Synchronisation der Kamera- und Robotersysteme, einschließlich der Implementierung und Validierung des LIMA-Protokolls. KI-Experten waren verantwortlich für die Auswahl und Vorbereitung der Daten für das Modelltraining. Sie führten die Datenvalidierung durch, um sicherzustellen, dass die erfassten Bilder und Metadaten von ausreichender Qualität und Relevanz für das Training des KI-Modells sind.


### In welchem Zeitrahmen wurden die Daten erhoben?
Die Datenerhebung erfolgte über einen Zeitraum von drei Wochen. Dieser Zeitrahmen war erforderlich, um sicherzustellen, dass die Daten eine ausreichende Vielfalt an Produktionsbedingungen, Fehlertypen und Umgebungsvariablen abdecken.


### Wurden ethische Überprüfungsverfahren durchgeführt (z. B. durch einen institutionellen Prüfungsausschuss)?
Da der Datensatz rein technischer Natur ist und keine ethisch sensiblen Daten umfasst, wurden keine ethischen Überprüfungsverfahren durch einen institutionellen Prüfungsausschuss durchgeführt. Der Fokus lag auf der technischen Validierung und der Sicherstellung der Qualität der erhobenen Daten für die beabsichtigte Anwendung.


### Bezieht sich der Datensatz auf Personen?
Nein.


### Wurden die Daten direkt bei den betroffenen Personen erhoben oder wurden sie über Dritte oder andere Quellen (z. B. Websites) erhalten?
Da keine betroffenen Personen in die Datenerhebung involviert waren und die Daten direkt aus dem Produktionsprozess stammen, erübrigen sich typische Datenschutz- oder ethische Fragestellungen, die bei personenbezogenen Daten relevant wären.


### Wurden die betroffenen Personen über die Datenerhebung informiert?
Da keine Menschen von der Datenerhebung betroffen waren, war es nicht notwendig, Personen über die Datenerhebung zu informieren. Alle erhobenen Daten beziehen sich ausschließlich auf technische Prozesse und beinhalten keine persönlichen oder sensiblen Informationen.


### Haben die betroffenen Personen der Erhebung und Verwendung ihrer Daten zugestimmt?
Es waren keine betroffenen Personen vorhanden, daher war keine Zustimmung zur Datenerhebung und -nutzung notwendig. Der gesamte Prozess bezieht sich rein auf industrielle und technische Daten ohne Bezug zu natürlichen Personen.


### Wenn eine Einwilligung eingeholt wurde, wurde den einwilligenden Personen ein Verfahren zur Verfügung gestellt, mit dem sie ihre Einwilligung für die Zukunft oder für bestimmte Verwendungszwecke widerrufen können?
-


### Wurde eine Analyse der möglichen Auswirkungen des Datensatzes und seiner Verwendung auf die betroffenen Personen (z. B. eine Datenschutz-Folgenabschätzung) durchgeführt?
-


### Sonstige Anmerkungen?
-


## Vorverarbeitung/Bereinigung/Labeling
Die Fragen in diesem Abschnitt sollen den Nutzern von Datensätzen die Informationen liefern, die sie benötigen, um festzustellen, ob die „Rohdaten“ auf eine Weise verarbeitet wurden, die mit den von ihnen gewählten Aufgaben vereinbar ist.


### Wurde eine Vorverarbeitung/Bereinigung/Labeling der Daten vorgenommen (z. B. Diskretisierung oder Bucketing, Tokenisierung, Part-of-Speech-Tagging, SIFT-Merkmalextraktion, Entfernung von Instanzen, Verarbeitung fehlender Werte)?
Ja, es wurde eine umfangreiche Vorverarbeitung, Bereinigung und Labeling der Daten durchgeführt, um die Daten für das Training des KI-Modells vorzubereiten. Diese Schritte waren entscheidend, um die Qualität der Daten sicherzustellen und optimale Ergebnisse beim Modelltraining zu erzielen.
Details zu den durchgeführten Schritten:

Vorverarbeitung der Daten:
- Bildnormalisierung: Die Bilder wurden normalisiert, um sicherzustellen, dass die Pixelwerte über den gesamten Datensatz hinweg konsistent sind. Dies verbessert die Trainingsstabilität des Modells. 
- Größenanpassung: Alle Bilder wurden auf eine einheitliche Größe skaliert, um sicherzustellen, dass sie für das Modelltraining geeignet sind und die Rechenanforderungen reduziert werden.
- Bildaugmentation: Um die Robustheit des Modells zu erhöhen, wurden folgende Augmentationstechniken angewendet:
    - Rotation: Die Bilder wurden zufällig um bis zu 35 Grad gedreht.
    - Horizontales und vertikales Spiegeln: Es wurden zufällig horizontale (p=0.5) und vertikale Spiegelungen (p=0.1) durchgeführt.
    - Nach der Anwendung dieser Transformationen wurden die Bilder in Tensoren konvertiert, um für das Modelltraining genutzt zu werden.

Bereinigung der Daten:
- Entfernung von fehlerhaften oder unbrauchbaren Bildern: Bilder, die aufgrund von schlechten Lichtverhältnissen, Unschärfe oder anderen Problemen die Qualität der Daten beeinträchtigen könnten, wurden entfernt.
- Überprüfung und Korrektur von Anomalien: Es wurden Anomalien und Inkonsistenzen in den Metadaten oder den Bildern selbst identifiziert und korrigiert, um sicherzustellen, dass die Daten konsistent und verlässlich sind.

Labeling der Daten:
- Fehlstellenannotation: Jede Instanz bzw. Bild wurde manuell annotiert, um die Fehlstellen im Primerauftrag zu markieren. Diese Annotationen wurden als Segmentierungsmasken gespeichert, die jedem Pixel im Bild eine Kategorie zuweisen („Primer vorhanden“ oder „Fehlstelle“).


### Wurden die „Rohdaten“ zusätzlich zu den vorverarbeiteten/bereinigten/beschrifteten Daten gespeichert (z. B. zur Unterstützung unvorhergesehener zukünftiger Verwendungen)?
Ja, die Rohdaten wurden zusätzlich zu den vorverarbeiteten, bereinigten und beschrifteten Daten gespeichert. Diese Entscheidung wurde getroffen, um eine flexible Dateninfrastruktur zu gewährleisten, die auch unvorhergesehene zukünftige Verwendungen oder erneute Analysen unterstützt. 


### Ist die Software, die zur Vorverarbeitung/Reinigung/Etikettierung der Instanzen verwendet wird, verfügbar?
Ja, die Software, die zur Vorverarbeitung verwendet wurde, ist verfügbar. 


### Sonstige Anmerkungen?
-


## Verwendungen
Diese Fragen sollen die Ersteller von Datensätzen dazu anregen, über die Aufgaben nachzudenken, für die der Datensatz verwendet werden sollte und für die er nicht verwendet werden sollte. Durch die ausdrückliche Hervorhebung dieser Aufgaben können die Ersteller von Datensätzen den Nutzern von Datensätzen helfen, fundierte Entscheidungen zu treffen und so mögliche Risiken oder Schäden zu vermeiden.

### Wurde der Datensatz bereits für irgendwelche Aufgaben verwendet?
Nein.


### Gibt es ein Repository, das Links zu allen Arbeiten oder Systemen enthält, die den Datensatz verwenden?
Ja.


### Für welche (anderen) Aufgaben könnte der Datensatz verwendet werden?
Der Datensatz, der Bilder von Glasscheiben mit aufgetragenem Primer und annotierten Fehlstellen enthält, könnte für andere Aufgaben verwendet werden. Die Daten könnten zur Optimierung von Robotersystemen verwendet werden, die Defekte erkennen und automatisch korrigieren. Dies könnte eine Erweiterung der aktuellen Anwendung sein oder in anderen Branchen eingesetzt werden.


### Gibt es irgendetwas an der Zusammensetzung des Datensatzes oder an der Art und Weise, wie er gesammelt und vorverarbeitet/bereinigt/etikettiert wurde, das sich auf die künftige Nutzung auswirken könnte?
Ja, es gibt einige Aspekte in Bezug auf die Zusammensetzung des Datensatzes sowie die Art und Weise, wie er gesammelt, vorverarbeitet, bereinigt und etikettiert wurde, die sich auf die künftige Nutzung auswirken könnten:
- Der Datensatz wurde für einen sehr spezifischen Anwendungsfall erstellt: die Erkennung von Fehlstellen im Primerauftrag auf Glasscheiben. Die Bilder und Annotationen sind stark auf diese Aufgabe ausgerichtet. Dies könnte die Übertragbarkeit des Datensatzes auf andere Aufgaben oder Industrien einschränken.
- Da eine deterministische Stichprobenstrategie verwendet wurde, könnte der Datensatz bestimmte seltene Fehlstellen oder extreme Bedingungen unterrepräsentieren. Für zukünftige Anwendungen, die eine breitere Abdeckung oder eine zufälligere Stichprobe erfordern, könnte dies zu einem Bias führen.
- Die Bildauflösung und Qualität wurden für die spezifischen Anforderungen des Anwendungsfalls optimiert. Dies könnte sich auf die Nutzung in Szenarien auswirken, die eine andere Bildauflösung oder spezifische visuelle Details erfordern, die möglicherweise nicht vollständig erfasst wurden.


### Gibt es Aufgaben, für die der Datensatz nicht verwendet werden sollte?
Nein.


### Sonstige Anmerkungen?
-


## Verteilung
### Wird der Datensatz an Dritte außerhalb der Einrichtung (z. B. Unternehmen, Institution, Organisation) weitergegeben, in deren Auftrag der Datensatz erstellt wurde? 
Der Datensatz wurde für interne Zwecke entwickelt. Im Zuge des Forschungsprojektes EKI wird der Datensatz (ausschließlich Bilder und Annotationen) der breiteren Gemeinschaft durch Veröffentlichung auf GitHub zur Verfügung gestellt. 


### Wie wird der Datensatz verbreitet (z. B. Tarball auf der Website, API, GitHub)?
Siehe oeben.


### Wann wird der Datensatz verteilt?
-


### Wird der Datensatz unter einer Urheberrechts- oder einer anderen Lizenz für geistiges Eigentum (IP) und/oder unter geltenden Nutzungsbedingungen (ToU) verbreitet?
-


### Haben Dritte IP-basierte oder andere Beschränkungen für die mit den Instanzen verbundenen Daten eingeführt?
-


### Gelten für den Datensatz oder einzelne Instanzen Exportkontrollen oder andere gesetzliche Beschränkungen?
-


### Sonstige Anmerkungen?
-


## Wartung
Diese Fragen sollen die Ersteller von Datensätzen dazu ermutigen, die Pflege des Datensatzes zu planen und diesen Plan den Nutzern des Datensatzes mitzuteilen.

### Wer unterstützt/hostet/pflegt den Datensatz?
-


### Wie kann der Eigentümer/Kurator/Manager des Datensatzes kontaktiert werden (z. B. E-Mail-Adresse)?
-


### Gibt es ein Erratum?
-


### Wird der Datensatz aktualisiert (z. B. um Labelingfehler zu korrigieren, neue Instanzen hinzuzufügen oder Instanzen zu löschen)?
Ja, der Datensatz wird für interne Zwecke regelmäßig aktualisiert. Während des laufenden Produktionsprozesses werden kontinuierlich neue Bilder aufgenommen. Diese neuen Bilddaten werden in regelmäßigen Abständen annotiert/gelabelt und in den bestehenden Datensatz integriert. Anschließend wird das KI-Modell mit den aktualisierten Daten erneut trainiert.


### Wenn sich der Datensatz auf Personen bezieht, gibt es Grenzen für die Aufbewahrung der mit den Instanzen verbundenen Daten (z. B. wurde den betroffenen Personen mitgeteilt, dass ihre Daten für einen bestimmten Zeitraum aufbewahrt und dann gelöscht werden)?
-


### Werden ältere Versionen des Datensatzes weiterhin unterstützt/gehostet/gepflegt?
- 


### Wenn andere den Datensatz erweitern/verbessern/auf ihm aufbauen/einen Beitrag dazu leisten wollen, gibt es dann einen Mechanismus, um dies zu tun?
Nein.


### Sonstige Anmerkungen?
-