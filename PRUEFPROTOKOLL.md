# Prüfprotokoll der Erfassungsprobe

## Vollständige Offline-Webansicht

Erweiterung nach Nutzerwunsch: Kopfbereich mit grüner Farbfläche, ruhigerer Titelgestaltung, Statusfeld und Schnellnavigation überarbeitet. Eingebettete RIS-/CSL-JSON-Gruppenexports für sieben Hauptkategorien, fünf akademische Untergruppen, acht Sprachen und 36 Hauptjahre hinzugefügt: 56 Gruppen, 112 Downloads. Prüfung vergleicht für jede Gruppe sämtliche Datensätze, IDs, Reihenfolge und Inhalte mit der entsprechenden Auswahl im Quelldatensatz, nicht nur die Trefferzahl. Mehrsprachige Einträge in jeder zutreffenden Sprachgruppe; Jahresgruppen ausschließlich nach Hauptjahr. Keine Änderung bibliographischer Daten, der Word-Datei oder der GitHub-Anbindung. Browserdarstellung und tatsächliche Browserdownloads bleiben mangels erlaubter lokaler Browserautomation manuell zu prüfen.

Nach Nutzerprüfung angepasst: Alle „Zurück zur Navigation“-Links zeigen auf `#seitenanfang` am `body`, nicht mehr auf die sticky Seitenleiste. Der bisherige Anker war vorhanden, aber nicht am Seitenanfang positioniert. Seitentitel und H1 übernehmen den Wortlaut „Schriftenverzeichnis: Publikationen von Ottmar Ette zu Alexander von Humboldt“ aus der unveränderten Word-Quelle. Ein kleiner aufklappbarer Reiter „Prinzipien zur Auswahl“ enthält die Auswahlprinzipien aus Word, ohne Kategorienaufzählung. Der vom Nutzer vorgegebene Hinweis auf die parallele HiN-Veröffentlichung im Dezember 2026 wurde mit Link zur Zeitschriftenhomepage aufgenommen; das ist eine redaktionelle Vorgabe, keine unabhängig geprüfte Veröffentlichungsaussage. Erneuter Aufbau und Vergleichsprüfung erfolgreich; Browserkontrolle weiterhin nicht möglich.

`index.html` auf Grundlage der aktuellen 262 Datensätze erzeugt. Redaktionelle Kategorien einschließlich „Akademische Publikationen“ und „Wissenschaftskommunikation“ stehen im Vordergrund; Untergruppen, flache eingebettete Icons und Rücklinks umgesetzt. Interne Erfassungsentscheidungen und Quellenlocatoren erscheinen nicht in den Einzeltiteln.

Sprach-, Hauptjahres- und gesondertes Auflagenregister ohne JavaScript. 524 eingebettete Einzel-Downloads (RIS/CSL-JSON) und vier Gesamt-Downloads (RIS/CSL-JSON/CSV/Projekt-JSON). Gesamt-RIS und -CSL zusätzlich als Dateien in `exports`.

Automatische Prüfung: vollständige Darstellung und Zeichenidentität der Quellenabsätze, eindeutige IDs, auflösbare interne Sprungziele, UTF-8-Inhalte aller Downloadlinks, genau ein Datensatz je Einzelexport, vollständige Gesamtdateien, keine JavaScript-/Iframe-/externen Asset-Abhängigkeiten. Technischer Bericht: `data/web-pruefung.json`. Anleitung und RIS-Abbildungsgrenzen: `WEB-NUTZUNG.md`.

Browserautomatisierung blockiert `file:`-Navigation. Keine Umgehung versucht; Browserdarstellung, tatsächliches Downloadverhalten und Import in Literaturverwaltungsprogramme sind daher noch manuell zu prüfen. Die Webseite selbst benötigt keinen Server. GitHub/Zenodo weder verbunden noch verändert; keine Commits oder Pushes.

## Bestätigte redaktionelle Festlegungen

Sprachabfrage abgeschlossen: `ette-000050`, „avhumboldt.de – Alexander von Humboldt Informationen online“ (seit 2009): Deutsch, Englisch, Spanisch und Französisch vom Nutzer bestätigt und in JSON/CSV übernommen. Alle elf zuvor ungeklärten Sprachzuordnungen sind beantwortet; erschlossene Sprachzuordnungen anderer Einträge bleiben weiterhin als solche gekennzeichnet. Frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000048`, „Alexander von Humboldt. die ganze Welt, der ganze Mensch“ (2024): Deutsch, Spanisch und Englisch vom Nutzer bestätigt und in JSON/CSV übernommen. Alle zehn zuvor ungeklärten Sammelband-/Heftzuordnungen sind damit beantwortet. Noch offen ist die Sprachzuordnung des Portals `ette-000050`; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000046`, „Alexander von Humboldt-Handbuch. Leben – Werk – Wirkung“ (2018): Deutsch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch zwei ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000045`, „Landschaften und Kartographien der Humboldt’schen Wissenschaft“ (2017): Deutsch, Englisch und Französisch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch drei ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000044`, „Forster – Humboldt – Chamisso. Weltreisende im Spannungsfeld der Kulturen“ (2017): Deutsch, Englisch und Französisch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch vier ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000043`, „Horizonte der Humboldt-Forschung. Natur, Kultur, Schreiben“ (2016): Deutsch und Französisch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch fünf ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000042`, „Alexander von Humboldt and the Americas“ (2012): Englisch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch sechs ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000041`, „Humboldt und Hispanoamerika / Humboldt e Hispano-América“, Bd. 2 (2010): Spanisch und Deutsch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch sieben ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000040`, „Humboldt und Hispanoamerika / Humboldt e Hispano-América“, Bd. 1 (2009): Deutsch und Spanisch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch acht ungeklärte Sprachzuordnungen; frühere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000039`, „Alexander von Humboldt – Aufbruch in die Moderne“ (2001): ausschließlich Deutsch vom Nutzer bestätigt und in JSON/CSV übernommen. Noch neun ungeklärte Sprachzuordnungen; ältere Zahlen dokumentieren vorausgehende Stände.

Sprachabfrage: `ette-000005`, „Ansichten Amerikas“ (2001): Deutsch, Englisch, Spanisch vom Nutzer bestätigt und in JSON/CSV übernommen. Damit verbleiben zehn ungeklärte Sprachzuordnungen. Die ältere Angabe von elf offenen Zuordnungen unten beschreibt den vorherigen Stand.

Neuauflagen bleiben verbundene Ausgaben; Paralleltitel und Titelerläuterungen bleiben quellentreu (Fragen 2 und 3 bestätigt). Hörbücher bilden die eigene Untergruppe „Hörbücher“ unter „Akademische Publikationen“; CSL-Typ `book` mit Audio-Medium. Vier Zeitschriftendossiers werden auf Nutzerwunsch wie Sammelbände als `book` geführt; Zeitschriftenkontext, Band und Heft bleiben erhalten. Die Hauptkategorie heißt in Daten und Webansicht „Akademische Publikationen“; ihre stabile ID ändert sich nicht. Die DOCX bleibt unangetastet.

HTML/CSS ohne JavaScript und CC BY 4.0 für Daten/projektspezifische Webinhalte bestätigt. Softwarelizenz und endgültige Zitierempfehlung bleiben vor Veröffentlichung zu klären. Die Sprachen werden einzeln beim Nutzer abgefragt und reproduzierbar in `data/redaktionelle-festlegungen.json` gespeichert; noch keine Sprachantwort vorweggenommen.

## Aktuelle Gesamterfassung aus v2 (13.10.2026)

Quelle: `bibliographie_ette_final_v2.docx`, SHA256 `6b9ca6cc0be1c4254736211d4b642a346fa51202b62d68c6825771e1a768de92`, 592 Absätze. Die Word-Datei wurde ausschließlich gelesen und bleibt unverändert.

- 262 Einträge: Literarisches 1; Akademische Buchpublikationen 36; Internet-Präsentationen 2; Aufsätze 173; Vorworte, Lexikonartikel und Bibliographien 30; Wissenschaftskommunikation 17; Übersetzungen 3.
- Gegenüber dem früheren Gesamtdatensatz: 241 unveränderte Literaturangaben, sechs aktualisierte bzw. verschobene Nachweise, 15 neue Einträge. Alle 247 bisherigen IDs einschließlich der 20 Probe-IDs erhalten. Der SWR-Beitrag wechselte von „Aufsätze“ nach „Wissenschaftskommunikation“ und behält `ette-000083`; keine Doppelanlage.
- Die vom Nutzer gestrichenen Mediennachweise wurden nicht erneut eingefügt. Die zusammengeführte radioeins-/Kulturradio-Angabe und die neue L.I.S.A.-Podcast-URL wurden quellentreu übernommen; keine erneute Netzprüfung in diesem Schritt.
- Manuelle Korrekturen außerhalb der Medienrubrik übernommen: Giorleny D. Altamirano Rayo, „in the Net“, zwei Zeitschriftentitel „Humboldt“ ohne „port.“ und die versionierte Adresse des digitalen Insel-Textes. Vergleich vollständig in `data/v2-abgleich.json`.
- Kategorien und Untergruppen bleiben von CSL-Typen getrennt. Die neue Rubrikbezeichnung wird angezeigt, der technische Kategorie-Schlüssel `debatten` bleibt stabil.
- Frühere Parserfehler korrigiert: keine aus Sendungs-/Artikelangaben abgeleiteten falschen Verlagsangaben; „Northeastern Naturalist“ 8 als Band, nicht als Heft. Alle drei SWR-MP3-Adressen stehen zusätzlich strukturiert in `online_resources`.
- Technische Prüfungen: Projektschema, vollständige und einmalige Übernahme der Erfassungsabsätze, eindeutige IDs, konsistente Jahresfelder, gültige vollständige Kalenderdaten, CSV-Rücklesung ohne Textverlust und reproduzierbarer Neuaufbau. Literarische Quelltexte, historische Schreibungen und Kursivierung bleiben erhalten.
- Noch offen: Publikationssprachen bei elf Einträgen (zehn Sammelbände/Heftnachweise und das viersprachige Portal); erschlossene Sprachangaben sind nicht extern verifiziert. Weitere konkrete Metadatenfragen stehen in `data/erfassungsfragen.json`. Erläuternde Quellenhinweise werden nicht pauschal als Fehler gezählt.

Die HTML-Probe bleibt der historische 20-Einträge-Stand. Neue Oberfläche und Standardexporte sind noch nicht erstellt. Keine GitHub-/Zenodo-Veröffentlichung. Die nachfolgenden Abschnitte dokumentieren die ursprüngliche Probe.

## Quelle und Status

- Erfasst am 13.10.2026 aus `bibliographie_ette_final.docx`.
- SHA256: `d403b5c6d2811644a64e0473778780232961c709d6515118d4b913d982495fd3`.
- 20 Erfassungseinträge; Entwurf, noch keine fachliche Freigabe.
- Die Quelle hat 560 Absätze und 284 Absätze mit Text. Diese Zahlen sind keine Anzahl bibliographischer Datensätze: Überschriften, Erläuterungen und Fortsetzungsabsätze sind darin enthalten.
- Keine Änderung an der DOCX, keine Wiederaufnahme des abgeschlossenen Korrekturlaufs.

## Abdeckung

| Hauptkategorie | Einträge in der Probe |
|---|---:|
| Literarisches | 1 |
| Akademische Buchpublikationen | 7 |
| Internet-Präsentationen | 1 |
| Aufsätze | 6 |
| Vorworte, Lexikonartikel und Bibliographien | 2 |
| Debatten | 1 |
| Übersetzungen | 2 |

Alle fünf Untergruppen der akademischen Buchpublikationen sind vertreten: Monographien (2), Editionen (1), Sammelbände (2), didaktische Materialien (1), Hörbücher (1).

## Fachlich relevante Fälle

| ID | Beispiel | Erfassungsentscheidung |
|---|---|---|
| ette-000001 | Roman-Auszug | Kategorie Literarisches, Typ Zeitschriftenbeitrag. |
| ette-000002 | Literatura de viaje | Spanischer Titel, deutsche Rollenangabe; Übersetzer getrennt vom Autor. |
| ette-000003 | Weltbewußtsein | Hauptjahr 2002; Ausgaben 2005/2020 als verbundene Ausgaben. Digitale URL ausschließlich bei 2005. |
| ette-000004 | Reise in die Äquinoktial-Gegenden | Humboldt als Autor, Ette als Herausgeber; Fortsetzungen 1999/2004 erhalten. |
| ette-000005 | Ansichten Amerikas | Herausgeberband; Sprache des gesamten Bandes noch ungeklärt. |
| ette-000006 | Chinesisches Dossier | Redaktionell Sammelbände, CSL-Typ periodical; deutsche Erläuterung kein Sprachbeleg für Deutsch. |
| ette-000007 | Didaktische Materialien | Buchtyp und didaktische Funktion als separate Angaben. |
| ette-000008 | KOSMOS als Hörbuch | Buchtyp mit Audio-CD als Medium; spätere RIS-Zuordnung noch zu prüfen. |
| ette-000009 | Humboldt im Netz | Drei explizit beschriebene Sprachen; 1998 als Startjahr, nicht ein erfundenes Publikationsdatum des gesamten Portals. |
| ette-000010 | Unterwegs zum Weltbewußtsein | Deutscher Zeitschriftenbeitrag; DOI als reine Kennung gespeichert. |
| ette-000011 | Kosmos: indexing it | Englischer Beitrag mit zwei Autoren. |
| ette-000012 | Zentralamerika-Einführung | Deutscher Einzelbeitrag im zweisprachigen Buch; römisch-arabische und diskontinuierliche Seiten erhalten. Buchübersetzerin nicht als Übersetzerin des deutschen Beitrags gesetzt. |
| ette-000013 | Russische Umschrift | Sprache ru; englischer Paralleltitel separat; Primezeichen erhalten. |
| ette-000014 | Chinesischer Inselaufsatz | Sprache zh; englischer Klammertitel separat; Ren Haiyan als Übersetzerin. |
| ette-000015 | Chinesische Einleitung | Sprache zh; Fan Ni als Übersetzerin; Beziehung zum Dossier ette-000006. |
| ette-000016 | Apresentação / Einführung | Zwei Beitragssprachen pt/de, nicht automatisch Englisch wegen eines englischen Buchanhangs. |
| ette-000017 | 寄语 | Chinesischer Beitrag mit deutscher Titelerläuterung; Dossier-Landingpage als Quellen-URL, nicht als eigener Artikel-DOI ausgegeben. |
| ette-000018 | Universitätszeitung PUTZ | Kategorie Debatten, CSL-Typ article-newspaper. |
| ette-000019 | Reise – Übersetzungsnachweis | Getrennter Kategorieeintrag, mit Bezug auf dieselbe Ausgabe wie ette-000004; keine automatische Deduplikation. |
| ette-000020 | Buch der Begegnungen | Humboldt als Autor, Ette als Herausgeber und Übersetzer. |

## Technische Prüfungen

Erfolgreich geprüft durch `scripts/build_probe.py`:

- 20 eindeutige IDs, gleichlautende IDs im CSL-Unterdatensatz.
- Abdeckung der sieben Hauptkategorien und fünf Untergruppen.
- Jahreswerte stimmen zwischen Projektmetadaten und CSL-Datum überein.
- Beziehungen zeigen ausschließlich auf bestehende Probe-IDs.
- Zuordnung der Fortsetzungsabsätze zu den Haupteinträgen.
- Originaltexte sämtlicher ausgewählter Absätze stimmen zeichengetreu mit der DOCX überein.
- HTML-Text entspricht den Quellenabsätzen; Kursivierungen und echte Hyperlinks werden übernommen.
- CSV lässt sich verlustfrei wieder einlesen, einschließlich mehrzeiliger Literaturangaben und Unicode.
- Kein JavaScript, keine nachzuladenden Stylesheets, Schriften oder Daten in `probe.html`.
- SHA256 der finalen DOCX vor und nach der Erstellung identisch.

Das beigefügte JSON-Schema verwendet Draft 2020-12. Der lokale Prüfer prüft den tatsächlich verwendeten Schema-Ausschnitt (Typen, Pflichtfelder, zusätzliche Felder, Muster, Wertebereiche, Listen und Kategoriebedingungen). Er ist kein universeller JSON-Schema-Validator. Zusätzliche Erfassungsregeln werden mit fachlich motivierten Assertions geprüft. Eine Prüfung mit einem unabhängigen vollständigen Schema-Validator und Imports in Literaturverwaltungsprogramme gehören zur nächsten Ausbaustufe.

Nachprüfung mit dem gebündelten Python-Laufzeitpfad:

```powershell
& 'C:\Users\kraft\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 'C:\Users\kraft\Nextcloud\26 HiN Ette (TK + UP)\Beiträge\bibliographie_oe\Projektordner\AvH-Bibliographie-Ette\scripts\build_probe.py' --check
```

Das Skript schreibt bei `--check` keine Dateien. Für Anwender genügt es, `probe.html` im Browser oder `data/probe.csv` in einer Tabellenkalkulation zu öffnen. Python ist für diese Nutzung nicht erforderlich.

## Noch fachlich zu prüfen

1. Sprachzuordnungen: 18 anhand von Titeln erschlossen, 1 explizit aus der Quellenbeschreibung, 1 ungeklärt. Insbesondere die Sprachen der Sammelbände benötigen Inhaltsverzeichnis/Volltext. Diese Unterscheidung ist Bestandteil der Daten.
2. Die Probe behandelt Neuauflagen als verbundene Ausgaben unter einem redaktionellen Haupteintrag. Die spätere Jahresnavigation muss diesen Unterschied sichtbar machen.
3. Veröffentlichte englische Paralleltitel und deutsche Erläuterungen bleiben in der Form der finalen DOCX. Sie werden nicht pauschal als neue Übersetzungen umgeschrieben.
4. Hörbücher und Zeitschriftendossiers benötigen beim RIS-Export programmabhängige Abbildung und Importkontrolle.
5. Die Kategorieüberschrift „Akademische Buchpublikationen“ folgt der endgültigen Quelle, obwohl ihre vorangestellte Übersicht die kürzere Form „Akademische Publikationen“ verwendet.
6. Kategorien-, Sprach- und Jahresregister können ohne JavaScript umgesetzt werden. Frei kombinierbare dynamische Filter sind mit der Vorgabe einer einzelnen, statischen HTML-Datei ohne JavaScript nicht enthalten. Die vorliegende Probe ist eine Kontrollansicht, noch keine fertige Filteroberfläche.
7. Lizenz für Daten/Code und genaue Veröffentlichungsmetadaten stehen vor einem Upload festzulegen.

## GitHub

Authentifiziertes Connector-Konto: `trafikante`. `trafikante/AvH-Bibliographie-Ette` lieferte beim Metadatenabruf eine 404-Antwort. Der Connector bietet keine Repository-Erstellung; die vorhandene GitHub CLI meldet keine Anmeldung. Das gewünschte Repository wurde deshalb in diesen beiden lokalen Arbeitsschritten noch nicht erstellt. Es wurden weder Git-Commits noch Uploads vorgenommen.
