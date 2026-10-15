# AvH-Bibliographie-Ette

**Schriftenverzeichnis: Publikationen von Ottmar Ette zu Alexander von Humboldt**

Zusammengestellt von Tobias Kraft und Ulrich Päßler (BBAW). Aktuelle Ressource: **262 Einträge**, redaktionell nach sieben Hauptkategorien und fünf akademischen Untergruppen gegliedert. Statische HTML-Webansicht mit Registern und eingebetteten Einzel-, Gruppen- und Gesamtexporten; offline nutzbar, ohne JavaScript.

- [Webansicht](index.html)
- [Projektdatensatz JSON](data/bibliographie.json) und [CSV](data/bibliographie.csv)
- [CSL-JSON](exports/bibliographie.csl.json) und [RIS](exports/bibliographie.ris)
- [Anleitung zur Veröffentlichung auf GitHub und GitHub Pages](GITHUB-VEROEFFENTLICHUNG.md)
- [Nutzung und Exportgrenzen](WEB-NUTZUNG.md), [Datenmodell](DATENMODELL.md), [Lizenzumfang](LIZENZ.md)

Die GitHub-Pages-Startseite ist `index.html` im Repository-Hauptverzeichnis. `.nojekyll` ist vorbereitet. Daten und eigene Webinhalte stehen unter **CC BY 4.0**; verlinkte Inhalte Dritter sind nicht erfasst. Noch keine gesonderte Softwarelizenz festgelegt. Fachlicher Erschließungsstatus und praktische Importgrenzen sind im Prüfprotokoll dokumentiert.

## Aktuelle und historische Dateien

Maßgeblich sind `data/bibliographie.*`, `exports/bibliographie.*` und `schema/bibliographie.schema.json`. `probe.html`, `data/probe.*` und `schema/dataset.schema.json` dokumentieren die ursprüngliche 20-Einträge-Probe. `data/erfassungsstand_vor_v2.json` bewahrt den früheren Stand für die ID-stabile Migration. Recherche- und Vergleichsdateien dienen der Nachvollziehbarkeit, nicht als weitere aktuelle Bibliographien.

Die folgenden Abschnitte enthalten auch die Entwicklungsgeschichte; ältere Quellen- und Umfangsangaben sind nicht mit dem aktuellen Stand zu verwechseln.

Aktuelle redaktionelle Festlegungen stehen in `data/redaktionelle-festlegungen.json`: „Akademische Publikationen“ als Hauptgruppenlabel, eigene Untergruppe „Hörbücher“, Zeitschriftendossiers wie Sammelbände, Datenlizenz CC BY 4.0. Sie werden vom v2-Erfassungsskript angewendet. Lizenzumfang: `LIZENZ.md`; frühere Aussagen zur noch offenen Datenlizenz sind damit überholt. Sprachangaben werden einzeln bestätigt. Die Oberfläche bleibt ohne JavaScript.

Bibliographie der Publikationen von Ottmar Ette zu Alexander von Humboldt. Grundlage ist das von Tobias Kraft und Ulrich Päßler zusammengestellte Schriftenverzeichnis.

## Stand

Neu: überarbeiteter Kopfbereich und eingebettete RIS-/CSL-JSON-Gruppenexports für jede Kategorie, Sprache und jedes Hauptjahr sowie die akademischen Untergruppen (56 Gruppen, 112 Links). Die Einzel- und Gesamtexporte bleiben erhalten. Gruppeninhalte sind vollständig gegen den Datensatz geprüft; weiterhin ohne JavaScript und ohne GitHub-Zugriffe.

Die vollständige Offline-Webseite liegt in `index.html`: 262 Einträge mit Kategorien-, Sprach- und Jahresregistern, eingebetteten RIS-/CSL-JSON-Einzelexporten und vier Gesamt-Downloads. Alle elf zuvor offenen Sprachzuordnungen sind vom Nutzer bestätigt. Verwendung, Prüfungen und noch ausstehende Browser-/Importkontrolle: `WEB-NUTZUNG.md`. Erstellung: `scripts/build_site.py`; Vergleichsprüfung: `scripts/build_site.py --check`. Gesamt-RIS und Gesamt-CSL-JSON liegen zusätzlich in `exports`. Keine direkte GitHub-Anbindung, kein Commit und kein Push.

Aktive redaktionelle Quelle ist seit 13.10.2026 `bibliographie_ette_final_v2.docx`. Die Rubrik „Debatten“ wurde darin um 23 Mediennachweise ergänzt; ein vorhandener SWR-Nachweis wurde aktualisiert. Recherche und Auswahlgrenzen dokumentiert `Debatten-Medien-Recherche.md`; die Einzelangaben stehen in `data/debatten-medien-v2.json`.

Schritt 3 wurde nach deiner manuellen Überarbeitung der v2-Datei wieder aufgenommen: `data/bibliographie.json` und `data/bibliographie.csv` enthalten 262 Einträge aus der aktuellen Quelle, darunter 17 unter der nun „Wissenschaftskommunikation“ genannten Rubrik. Die stabile Kategorie-ID `debatten` bleibt erhalten. `data/v2-abgleich.json` dokumentiert den Quellenvergleich. Die älteren Probe-Dateien und `probe.html` bleiben historische Erfassungsprobe, nicht aktuelle Gesamtansicht.

Reproduzierbare Aktualisierung und Prüfung: `scripts/migrate_v2.py` bzw. `scripts/migrate_v2.py --check`. Das Skript verwendet den gesicherten früheren Erfassungsstand `data/erfassungsstand_vor_v2.json`; vorhandene IDs bleiben erhalten. Die älteren Skripte bleiben an ihre frühere Quelle gebunden. Die neue Weboberfläche ist lokal erstellt; fachliche Metadatenprüfung und praktische Importkontrolle sind noch nicht abgeschlossen.

Historischer Stand der Schritte 1 und 2: Erfassungsprobe mit 20 Einträgen, Stand 13.10.2026. Diese Probe war noch kein vollständiger Datensatz. Sie bleibt als Vergleichsstand erhalten.

- `DATENMODELL.md`: Felder, Kategorien und Erfassungsregeln.
- `data/probe.json`: maßgebliche strukturierte Erfassungsprobe.
- `data/probe.csv`: tabellarische Kontrollansicht; verschachtelte Felder stehen vollständig in JSON.
- `schema/dataset.schema.json`: überprüfbares JSON-Schema.
- `probe.html`: statische Kontrollansicht mit vollständigen Literaturangaben, offline nutzbar, ohne JavaScript oder externe Ressourcen.
- `PRUEFPROTOKOLL.md`: Prüfungen, Zuordnungen und noch offene Fragen.
- `scripts/build_probe.py`: reproduzierbare Erstellung der Probe aus der finalen DOCX und den expliziten Erfassungsentscheidungen im Skript.

Bei der Datensatzerfassung wird die Word-Datei ausschließlich gelesen. Die gesondert beauftragte redaktionelle Ergänzung betrifft nur die v2-Datei; die ältere finale Fassung bleibt unverändert. Die Probe bewahrt Literaturangaben und Kursivierungen aus dem Dokument. Schriftzeichen und historische Titelorthographie bleiben erhalten.

## Veröffentlichung

Geplant: öffentliches GitHub-Repository `AvH-Bibliographie-Ette`, statische Webseite auf GitHub Pages und ein Zenodo-Datensatz mit denselben Daten sowie einer eigenständig nutzbaren HTML-Datei. Das GitHub-Konto `trafikante` wurde über den verbundenen Connector bestätigt. Für das gewünschte Repository lieferte der Connector am 13.10.2026 eine 404-Antwort. Eine Repository-Erstellungsfunktion steht im verbundenen Connector nicht zur Verfügung; die lokale GitHub CLI ist nicht angemeldet. Die Dateien sind lokal vorbereitet; es wurde noch kein Repository erstellt und nichts hochgeladen.

Ohne JavaScript erhält die Webseite Kategorien-, Sprach- und Jahresregister, Sprungmarken und die Suchfunktion des Browsers. Frei kombinierbare Auswahlfilter mit dynamischer Trefferzahl lassen sich mit einer rein statischen, einzelnen HTML-Datei ohne JavaScript nicht wie im ursprünglichen Vorschlag umsetzen. Für die Schritte 1 und 2 ist diese spätere Oberflächenentscheidung nicht erforderlich. Die Probe bietet Kategoriennavigation und aufklappbare Angaben.

Die Daten werden unabhängig von der Oberfläche strukturiert, sodass Sprache, Kategorie, Untergruppe und Jahr in nachnutzenden Programmen filterbar sind.

## Pflege und Nachnutzung

JSON ist die maßgebliche Erfassungsdatei. CSV, HTML und spätere Standardexporte werden daraus erzeugt. Nach der vollständigen Erfassung erfolgen Änderungen am Datensatz mit dokumentierter Version; die abgeschlossene DOCX bleibt die Quellenfassung.

Standardisierte bibliographische Felder folgen CSL-JSON. Redaktionelle Kategorien bleiben eigene Projektfelder. Ein späterer RIS-Export kann daraus abgeleitet werden; diese Probe enthält noch keinen RIS-Export und wurde noch nicht in Zotero, EndNote oder Citavi importiert.

Die Datenlizenz ist inzwischen als CC BY 4.0 festgelegt. Eine gesonderte Softwarelizenz und das endgültige Versionszitat bleiben vor einer Release-Veröffentlichung zu klären. Quelldokument und private Arbeitsdateien gehören nicht automatisch in das öffentliche Repository. Die lokale Word-Quelle wird von den Erfassungsskripten im übergeordneten Ordner erwartet; das vorhandene HTML und die bereitgestellten Exporte funktionieren ohne sie. Ein GitHub-Upload führt keines dieser Skripte automatisch aus.
