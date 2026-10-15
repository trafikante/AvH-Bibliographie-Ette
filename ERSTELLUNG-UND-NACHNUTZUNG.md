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

## Modelle und dokumentierter Tokenumfang

Ausgewertet wurden lokale Codex-Sitzungsprotokolle. Die folgenden Namen sind die **dort gespeicherten Modellkennungen**, keine nachträglich vermuteten Produktnamen. Ein genauerer Backend-Snapshot lässt sich daraus nicht bestimmen.

| Modellkennung | Einsatz im protokollierten Verlauf | Protokollierte Reasoning-Einstellungen |
|---|---|---|
| `gpt-6-astra` | Redaktionelle Vorarbeiten an der Bibliographie | `high`, `medium` |
| `gpt-6.1-sol` | Redaktionelle Arbeiten sowie Planung und Umsetzung von Datensatz, HTML und Dokumentation | `low`, `medium` |

**Abgrenzung:** Die folgende Teilbilanz beginnt mit dem Auftrag zur bibliographischen Datenbank am **13.10.2026, 14:25:52 Uhr** und endet vor der jetzigen Überarbeitung der Prozessdokumentation am **15.10.2026, 13:39:50 Uhr**, jeweils Europe/Berlin. Sie umfasst auch nachfolgende Inhaltsergänzungen, Rückfragen und Dokumentationsarbeit, nicht nur den eigentlichen Konvertierungslauf. In diesem Abschnitt ist ausschließlich `gpt-6.1-sol` verzeichnet.

| Tokenkategorie | Aufgezeichneter Umfang für dieses Teilprojekt |
|---|---:|
| Eingabe gesamt | 22.027.071 |
| Davon aus dem Cache | 20.908.288 |
| Eingabe ohne Cache | 1.118.783 |
| Ausgabe gesamt | 130.283 |
| Davon Reasoning-Ausgabe | 31.490 |
| **Gesamt: Eingabe + Ausgabe** | **22.157.354** |

Die Teilbilanz beruht auf **131 Antwortdatensätzen**. Sie zählt verarbeitete Tokens über alle Modellaufrufe, nicht unterschiedliche Wörter oder die Länge des fertigen Produkts. Wiederholt mitgesendeter Gesprächskontext kann mehrfach als Eingabe erscheinen. Cache-Tokens sind bereits in der Eingabe enthalten, Reasoning-Tokens bereits in der Ausgabe; beide dürfen nicht nochmals zur Gesamtsumme addiert werden. Diese Teilmengenbeziehung beschreibt auch die [offizielle OpenAI-Dokumentation](https://developers.openai.com/api/docs/guides/agents-api/observability).

Zum Vergleich: Für den gesamten lokal erfassten Verlauf einschließlich redaktioneller Vorarbeiten sind **61.601.085 Tokens** aufgezeichnet: **13.176.291** für `gpt-6-astra` und **48.424.794** für `gpt-6.1-sol`. Die Aufzeichnung mit Tokenangaben beginnt am 12.10.2026. Verbräuche eines zuvor referenzierten ChatGPT-Gesprächs, anderer Sitzungen oder nicht ausgewiesener Dienste sind damit nicht belegt.

**Berechnung:** Je Antwort wurde `usage` aus `token_usage_record` einmal anhand der `response_id` berücksichtigt. Die Modellzuordnung erfolgte über `turn_id` und `turn_context`. Die Summe des vollständigen erfassten Verlaufs stimmt mit dem letzten einbezogenen `thread_token_usage` überein. Daneben auftretende `token_count`-Ereignisse wurden nicht hinzugerechnet. Die Zahlen sind somit protokollbasierte Messwerte mit festem Stichtag, keine Schätzung aus der Textlänge und keine Aussage über Geldkosten oder verbrauchtes Plus-Kontingent.

Die [maschinenlesbare Auswertung](KI-NUTZUNG.json) enthält Abgrenzung, Modellanteile und Rechenmethode, aber keine Gesprächsinhalte. Die jetzige Dokumentationsüberarbeitung und ihre Verbrauchsauswertung sind nicht in den eingefrorenen Summen enthalten.

## Was andere aus dem Vorgehen übernehmen können

Entscheidend war nicht ein einzelner Prompt, sondern eine Folge kleiner, überprüfbarer Aufträge: **prüfen → vorschlagen → entscheiden → umsetzen → kontrollieren**. Fachwissen wurde gezielt dort eingebracht, wo der Agent Informationen nicht sicher erschließen konnte.

Als sinngemäße Arbeitsaufträge für ähnliche Projekte eignen sich:

1. „Untersuche die Word-Bibliographie, dokumentiere Inkonsistenzen und schlage Regeln vor. Ändere noch nichts.“
2. „Erfasse eine repräsentative Probe. Bewahre den vollständigen Nachweis neben strukturierten Feldern und zeige eine Kontrollansicht.“
3. „Verarbeite nach Freigabe die gesamte Quelle. Kennzeichne Unsicherheiten und frage fachliche Entscheidungen einzeln ab.“
4. „Erzeuge Webseite und Exporte aus demselben Datensatz. Prüfe Texttreue und Auswahlmengen; überarbeite die Oberfläche anhand meiner Rückmeldungen.“

Für andere Bibliographien müssen die Erkennungsregeln und Sonderfälle angepasst werden. Die Skripte sind projektspezifische Umsetzungshilfen, kein allgemeiner Word-Konverter. Ziel dieser Dokumentation ist die Nachvollziehbarkeit und Übertragbarkeit des Vorgehens, nicht die identische Wiederholung der ursprünglichen Sitzung.

Felddefinitionen stehen im [Datenmodell](DATENMODELL.md), Bedienung und Exporthinweise in [WEB-NUTZUNG.md](WEB-NUTZUNG.md). Für Daten und redaktionelle Webinhalte gilt CC BY 4.0; der Programmcode ist unter [MIT](LICENSE) lizenziert. Die mehrsprachige Gestaltung der Benutzeroberfläche ist für eine nächste Iteration vorgesehen; die derzeitige Oberfläche ist deutschsprachig, die bibliographischen Originaltitel bleiben mehrsprachig.
