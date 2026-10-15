# Von der Word-Bibliographie zu Daten und HTML: Zusammenarbeit mit einem KI-Agenten

## Inhalt

- [Arbeitsteilung](#arbeitsteilung)
- [Vorgehen in sechs Schritten](#vorgehen-in-sechs-schritten)
  - [1. Erst prüfen, dann Regeln vereinbaren](#1-erst-prüfen-dann-regeln-vereinbaren)
  - [2. Ziel und Datenmodell gemeinsam festlegen](#2-ziel-und-datenmodell-gemeinsam-festlegen)
  - [3. Mit einer kleinen Probe beginnen](#3-mit-einer-kleinen-probe-beginnen)
  - [4. Gesamterfassung mit fachlichen Rückkopplungen](#4-gesamterfassung-mit-fachlichen-rückkopplungen)
  - [5. Daten, Webseite und Exporte technisch erzeugen](#5-daten-webseite-und-exporte-technisch-erzeugen)
  - [6. Automatisch prüfen und manuell nachbessern](#6-automatisch-prüfen-und-manuell-nachbessern)
- [Archivierung und Zitierbarkeit](#archivierung-und-zitierbarkeit)
- [Modelle und dokumentierter Tokenumfang](#modelle-und-dokumentierter-tokenumfang)
- [Was andere aus dem Vorgehen übernehmen können](#was-andere-aus-dem-vorgehen-übernehmen-können)

Diese Dokumentation beschreibt das Vorgehen bei AvH-Bibliographie-Ette: Ein fachlich verantwortlicher Bearbeiter (Tobias Kraft, BBAW) entwickelte gemeinsam mit einem KI-Agenten aus einer Word-Bibliographie eine strukturierte Datensammlung und eine offline nutzbare Webseite. Übertragbar ist die **Arbeitsweise**, nicht die unveränderte Ausführung aller projektspezifischen Skripte.

## Arbeitsteilung

| Fachlich verantwortlicher Bearbeiter | KI-Agent in Codex Desktop |
|---|---|
| Legte Auswahl, bibliographische Regeln und Veröffentlichungsziele fest. | Prüfte Dateien, machte Vorschläge und setzte freigegebene Regeln durch Skripte um. |
| Kontrollierte und korrigierte die Word-Fassung, entschied über Zweifelsfälle und bestätigte Publikationssprachen. | Recherchierte bibliographische Angaben und Online-Nachweise; stellte nicht sicher lösbare Fragen gezielt zurück. |
| Erprobte die Webansicht und gab Rückmeldungen zu Navigation, Gestaltung und Exportwünschen. | Erzeugte Daten, HTML und Exportformate, implementierte Prüfungen und überarbeitete die Oberfläche. |
| Veröffentlichte das Repository und aktivierte GitHub Pages selbst. | Bereitete Dateien und Veröffentlichungsanleitung vor; führte keinen Commit oder Push aus. |

Der Agent arbeitete nicht nur als Dialogpartner, sondern las lokale Dateien, schrieb und führte Python-Skripte aus und prüfte deren Ergebnisse. Fachliche Entscheidungen und technische Automatisierung wurden dabei bewusst getrennt.

## Vorgehen in sechs Schritten

### 1. Erst prüfen, dann Regeln vereinbaren

Zunächst wurde die Bibliographie auf Namen, Titel, Erscheinungsangaben, Zeichensetzung, Kursivierung und Links untersucht. Der Bearbeiter verlangte Befund und Änderungsvorschläge **vor** der Bearbeitung. Freigegebene Anpassungen erfolgten in neuen Word-Fassungen; das Original blieb erhalten. Unklare Angaben wurden recherchiert oder zur Entscheidung vorgelegt.

### 2. Ziel und Datenmodell gemeinsam festlegen

Für die digitale Ressource wurden Kategorien-, Sprach- und Jahreszugänge, Literaturverwaltungsexporte und eine ohne JavaScript nutzbare HTML-Datei vereinbart. Die Kategorien der Word-Datei sollten die Webseite prägen, aber von bibliographischen Standardtypen getrennt bleiben.

Die zentrale Entscheidung war, zwei Darstellungen parallel zu bewahren: die **vollständige, formatierte Literaturangabe** für die Anzeige und **strukturierte Metadaten** für Erschließung und Export. Ein standardisiertes Feld sollte keine wissenschaftlich bedeutsame Quelleninformation verdrängen.

### 3. Mit einer kleinen Probe beginnen

Der Agent erfasste zunächst 20 repräsentative Einträge und erzeugte eine HTML-Kontrollansicht. Der Bearbeiter prüfte das Ergebnis, bevor die vollständige Bibliographie verarbeitet wurde. Dabei wurden unter anderem Einzel-Exporte, Rücklinks zur Navigation, kleine Kategorie-Icons und das Ausblenden interner Erfassungsentscheidungen für die öffentliche Ansicht festgelegt.

Die Probe diente nicht nur als technischer Test: An konkreten Einträgen ließ sich besprechen, welche Informationen das Modell bewahren und wie die Webseite sie darstellen sollte.

### 4. Gesamterfassung mit fachlichen Rückkopplungen

Die Skripte wurden auf alle Einträge angewandt. Währenddessen ergänzte und korrigierte der Bearbeiter die Quellenfassung erneut, unter anderem bei Interviews und Podcasts. Der Agent glich den aktualisierten Stand ab, statt eine ältere Auswahl weiterzuführen. Bestehende IDs blieben erhalten.

Zweifelsfälle wurden nicht pauschal automatisch entschieden. Ein konkretes Beispiel sind die Publikationssprachen der Sammelbände: Der Agent fragte sie **einzeln** ab; der Bearbeiter antwortete aus seiner Fachkenntnis. Die bestätigten Angaben gingen anschließend in die Daten ein. Erschlossene und ausdrücklich bestätigte Sprachzuordnungen bleiben im Modell unterscheidbar.

### 5. Daten, Webseite und Exporte technisch erzeugen

Die Verarbeitung erfolgte mit Python, `python-docx` zum Lesen der DOCX sowie `lxml` für XML-/HTML-Verarbeitung und Kontrollen:

- Überschriften und Eintragsanfänge bestimmten Kategorien und Eintragsgrenzen; Fortsetzungen wurden etwa als weitere Ausgaben zugeordnet.
- Der Wortlaut der Literaturangaben blieb gespeichert. Kursivierungen wurden in HTML als `<em>`, Hyperlinks als `<a>` erhalten; Text und Attribute wurden escaped.
- Regeln erschlossen Titel, Personenrollen, Erscheinungsjahre, Seiten und Online-Verweise. Projektspezifische Sonderfälle wurden gesondert behandelt.
- Der JSON-Projektdatensatz bewahrt Kategorien, Sprachen, Beziehungen und Quellenbezüge neben den bibliographischen Feldern. CSV bietet eine tabellarische Ansicht.
- `scripts/build_site.py` erzeugt daraus die HTML-Ansicht und die Gesamtexporte als CSL-JSON und RIS. Titel und Auswahlprinzipien stehen heute in `data/web-konfiguration.json`. Beim Generieren werden sie in die HTML-Datei geschrieben; zum Neuerzeugen der Seite ist keine Word-Datei mehr nötig. Die ursprüngliche Datenerschließung aus Word ist davon zu unterscheiden.

Die Webseite zeigt die gespeicherten Literaturangaben, statt sie neu aus Einzelfeldern zusammenzusetzen. Gestaltung, Icons und Offline-Downloadinhalte sind eingebettet. Ergänzend stehen echte Dateilinks und ein ZIP-Paket für mobile Browser bereit, die eingebettete Data-URL-Downloads einschränken können. Einzel- und Gruppendownloads werden vorab erzeugt; JavaScript ist nicht erforderlich.

### 6. Automatisch prüfen und manuell nachbessern

Der Agent implementierte Kontrollen für erhaltene Quellenabsätze, eindeutige IDs, Jahreswerte, Beziehungen, CSV-Rücklesung, interne Sprungziele und die Inhalte aller Exportauswahlen. Der Bearbeiter kontrollierte zahlreiche, nicht sämtliche Datensätze sowie die tatsächliche Webansicht. Seine Rückmeldungen führten beispielsweise zur Korrektur des Rücksprungankers und zur Ergänzung der Gruppen-Exporte.

Der Bearbeiter hat die Datensätze geprüft und als eigenständige Datenpublikation freigegeben. RIS-Importe in Zotero und Citavi wurden erprobt; abgesehen von einer inzwischen korrigierten Notizaufteilung wurden bisher keine Fehler beobachtet. Der Originalnachweis wird nun mit dem vorangestellten Hinweis „Vollständige Literaturangabe:“ in einem einzigen RIS-Notizfeld ausgegeben. Die Tests sind keine behauptete Einzelkontrolle aller Metadaten oder aller Programme. Korrekturhinweise können als [GitHub Issue](https://github.com/trafikante/AvH-Bibliographie-Ette/issues) eingereicht werden.

## Archivierung und Zitierbarkeit

Der Bearbeiter veröffentlichte die Ressource auf GitHub und GitHub Pages und verband das Repository mit Zenodo. Ein GitHub-Release löst die Archivierung aus. Die Datei `.zenodo.json` legt dafür Titel, Ressourcentyp Dataset, die Bearbeiter Tobias Kraft und Ulrich Päßler mit ORCID/GND, Beschreibung und Lizenz fest. Der Agent bereitete diese Angaben vor und half bei der Fehleranalyse: Zwei fehlende Kommas verhinderten zunächst das Einlesen der Metadaten. Der syntaktisch korrigierte Stand wurde anschließend als `v1.0.2` erfolgreich archiviert.

Der [Zenodo-Eintrag](https://doi.org/10.5281/zenodo.23400543) wurde über die öffentliche API kontrolliert: Version `v1.0.2`, Publikationsdatum 15.10.2026, Dataset, beide Bearbeiter samt Kennungen und CC BY 4.0. Die DOI `10.5281/zenodo.23400543` bezeichnet diese konkrete Fassung; `10.5281/zenodo.23400542` ist die versionsübergreifende DOI. Eine spätere Änderung im GitHub-Repository aktualisiert das archivierte Release nicht automatisch.

README und HTML-Webansicht verweisen auf die archivierte Fassung. `CITATION.cff` stellt die Zitierangaben einschließlich ORCID für GitHubs Zitierfunktion bereit; GND-Kennungen stehen in `.zenodo.json`. Sind beide Dateien vorhanden, übernimmt Zenodo die Metadaten aus [`.zenodo.json`](https://help.zenodo.org/docs/github/describe-software/zenodo-json/). Für ein künftiges Release müssen Zitierangaben und Versionsbezüge erneut geprüft werden. Die hier ergänzten DOI-Hinweise und die folgende aktualisierte Tokenauswertung sind Nacharbeiten am laufenden Repository, noch keine nachträgliche Änderung des archivierten Releases.

## Modelle und dokumentierter Tokenumfang

Ausgewertet wurden lokale Codex-Sitzungsprotokolle. Die folgenden Namen sind die **dort gespeicherten Modellkennungen**, keine nachträglich vermuteten Produktnamen. Ein genauerer Backend-Snapshot lässt sich daraus nicht bestimmen.

| Modellkennung | Einsatz im protokollierten Verlauf | Protokollierte Reasoning-Einstellungen |
|---|---|---|
| `gpt-6-astra` | Redaktionelle Vorarbeiten sowie spätere Unterstützung der Zenodo-Veröffentlichung | `high`, `medium` |
| `gpt-6.1-sol` | Redaktionelle Arbeiten sowie Planung und Umsetzung von Datensatz, HTML, Dokumentation und Veröffentlichung | `low`, `medium` |

**Abgrenzung:** Die folgende Teilbilanz beginnt mit dem Auftrag zur bibliographischen Datenbank am **13.10.2026, 14:25:52 Uhr** und erfasst die vor **15.10.2026, 18:16:09 Uhr** protokollierten Modellaufrufe, jeweils Europe/Berlin. Sie umfasst nachfolgende Inhaltsergänzungen, Rückfragen, Oberflächen- und Dokumentationsarbeit sowie die Unterstützung der GitHub-/Zenodo-Veröffentlichung. Ausgewertet wurden die ursprüngliche Sitzung, deren Fortsetzung in einem abgezweigten Chat und der gesonderte Zenodo-Troubleshoot-Chat. Die laufende DOI-/Dokumentationsüberarbeitung ist nur insoweit enthalten, wie Verbrauchswerte bereits vor diesem Stichtag aufgezeichnet waren; ihr Abschluss und die Schlussantwort sind nicht enthalten.

| Tokenkategorie | Aufgezeichneter Umfang für dieses Teilprojekt |
|---|---:|
| Eingabe gesamt | 48.243.255 |
| Davon aus dem Cache | 46.431.232 |
| Eingabe ohne Cache | 1.812.023 |
| Ausgabe gesamt | 203.398 |
| Davon Reasoning-Ausgabe | 55.523 |
| **Gesamt: Eingabe + Ausgabe** | **48.446.653** |

Die Teilbilanz beruht auf **251 Antwortdatensätzen**: **3.875.641 Tokens** entfallen auf `gpt-6-astra`, **44.571.012** auf `gpt-6.1-sol`. Sie zählt verarbeitete Tokens über alle Modellaufrufe, nicht unterschiedliche Wörter oder die Länge des fertigen Produkts. Wiederholt mitgesendeter Gesprächskontext kann mehrfach als Eingabe erscheinen. Cache-Tokens sind bereits in der Eingabe enthalten, Reasoning-Tokens bereits in der Ausgabe; beide dürfen nicht nochmals zur Gesamtsumme addiert werden. Diese Teilmengenbeziehung beschreibt auch die [offizielle OpenAI-Dokumentation](https://developers.openai.com/api/docs/guides/agents-api/observability).

Zum Vergleich: Für den gesamten lokal erfassten Verlauf einschließlich redaktioneller Vorarbeiten sind über die drei ausgewerteten Sitzungen **87.890.384 Tokens** in **484 Antwortdatensätzen** aufgezeichnet: **17.051.932** für `gpt-6-astra` und **70.838.452** für `gpt-6.1-sol`. Die Aufzeichnung mit Tokenangaben beginnt am 12.10.2026. Verbräuche eines zuvor referenzierten ChatGPT-Gesprächs, weiterer Sitzungen oder nicht ausgewiesener Dienste sind damit nicht belegt; gesonderte automatische Sicherheitsprüfungen wurden nicht einbezogen.

**Berechnung:** Je Antwort wurde `usage` aus `token_usage_record` einmal anhand der `response_id` berücksichtigt, über alle drei ausgewerteten Sitzungen hinweg. Die Modellzuordnung erfolgte über `turn_id` und einen vollständigen Index der `turn_context`-Einträge. Die Fortsetzung übernimmt im kumulativen Zähler bereits **81.860.014 Tokens** aus der Ursprungssitzung; diese wurden nicht erneut addiert. Die Summe der Einzelverbräuche aus Ursprung und Fortsetzung stimmt mit deren letztem einbezogenen `thread_token_usage` überein; der gesonderte Troubleshoot-Chat steuert **33.881 Tokens** bei. Die frühere Bilanz von 61.601.085 Tokens zum alten Stichtag wurde zur Gegenprüfung exakt reproduziert. Daneben auftretende `token_count`-Ereignisse wurden nicht hinzugerechnet. Die Zahlen sind protokollbasierte Messwerte mit festem Stichtag, keine Schätzung aus der Textlänge und keine Aussage über Geldkosten oder verbrauchtes Plus-Kontingent.

Die [maschinenlesbare Auswertung](KI-NUTZUNG.json) enthält die drei Sitzungskennungen, Abgrenzung, Modellanteile, Rechenmethode und Gegenprüfungen, aber keine Gesprächsinhalte. Die verwendete Erfassungsgrenze ist als UTC-Zeit gespeichert. Künftige Arbeiten, insbesondere die geplante Mehrsprachigkeit, erfordern eine neue Auswertung.

## Was andere aus dem Vorgehen übernehmen können

Entscheidend war nicht ein einzelner Prompt, sondern eine Folge kleiner, überprüfbarer Aufträge: **prüfen → vorschlagen → entscheiden → umsetzen → kontrollieren**. Fachwissen wurde gezielt dort eingebracht, wo der Agent Informationen nicht sicher erschließen konnte.

Als sinngemäße Arbeitsaufträge für ähnliche Projekte eignen sich:

1. „Untersuche die Word-Bibliographie, dokumentiere Inkonsistenzen und schlage Regeln vor. Ändere noch nichts.“
2. „Erfasse eine repräsentative Probe. Bewahre den vollständigen Nachweis neben strukturierten Feldern und zeige eine Kontrollansicht.“
3. „Verarbeite nach Freigabe die gesamte Quelle. Kennzeichne Unsicherheiten und frage fachliche Entscheidungen einzeln ab.“
4. „Erzeuge Webseite und Exporte aus demselben Datensatz. Prüfe Texttreue und Auswahlmengen; überarbeite die Oberfläche anhand meiner Rückmeldungen.“

Für andere Bibliographien müssen die Erkennungsregeln und Sonderfälle angepasst werden. Die Skripte sind projektspezifische Umsetzungshilfen, kein allgemeiner Word-Konverter. Ziel dieser Dokumentation ist die Nachvollziehbarkeit und Übertragbarkeit des Vorgehens, nicht die identische Wiederholung der ursprünglichen Sitzung.

Felddefinitionen stehen im [Datenmodell](DATENMODELL.md), Bedienung und Exporthinweise in [WEB-NUTZUNG.md](WEB-NUTZUNG.md). Für Daten und redaktionelle Webinhalte gilt CC BY 4.0; der Programmcode ist unter [MIT](LICENSE) lizenziert. Die mehrsprachige Gestaltung der Benutzeroberfläche ist für eine nächste Iteration vorgesehen; die derzeitige Oberfläche ist deutschsprachig, die bibliographischen Originaltitel bleiben mehrsprachig.
