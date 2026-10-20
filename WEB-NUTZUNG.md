# Webseite und Datenexporte

## Inhalt

- [Öffnen](#öffnen)
- [Navigation](#navigation)
- [Suche](#suche)
- [Downloads](#downloads)
  - [Smartphone und direkte Dateilinks](#smartphone-und-direkte-dateilinks)
  - [Formate und Notizen](#formate-und-notizen)
- [Prüfung und beobachtete Browserunterschiede](#prüfung-und-beobachtete-browserunterschiede)
- [Barrierefreiheit](#barrierefreiheit)
- [Lokale Neuerstellung](#lokale-neuerstellung)
- [Lizenz](#lizenz)

## Öffnen

Die [veröffentlichte Bibliographie](https://trafikante.github.io/AvH-Bibliographie-Ette/) ist eine eigenständige Datenpublikation mit 262 Einträgen. Die HTML-Datei `index.html` enthält sämtliche Einträge, die Gestaltung und eingebettete Exportdaten. Sie lässt sich auch einzeln offline öffnen. Externe Publikationen, GitHub-Links und separat bereitgestellte Online-Dateien benötigen Internet.

## Navigation

Kategorien und Untergruppen führen zu den Einträgen; Sprach- und Jahresregister erschließen die Titel. „Zurück zur Navigation“ springt an den Seitenanfang.

- **Sprachregister:** Einträge chronologisch aufsteigend, ältere zuerst. Mehrsprachige Publikationen erscheinen in jeder zutreffenden Sprache.
- **Jahresregister:** maßgeblich sind das Erscheinungsjahr der Hauptausgabe beziehungsweise das Startjahr eines Portals.
- **Weitere Ausgaben:** separates Register für Neuauflagen und digitale Ausgaben mit Rückverweis zum Haupteintrag.
- **Suche:** „Bibliographie durchsuchen“ öffnet das Suchfeld mit kombinierbarem Suchbereich und Kategoriefilter. Die Browser-Textsuche bleibt über Strg+F, auf dem Mac ⌘F erreichbar; für die Suche in allen Einträgen zuvor eine aktive Filterung zurücksetzen.
- Registerbereiche und der Reiter „Dokumentation“ lassen sich mit den aufklappbaren Überschriften öffnen. Die Dokumentation zeigt die Auswahlregeln gegliedert und verlinkt Prozessbeschreibung, Datenmodell und Repository. Eine mehrsprachige Benutzeroberfläche ist für die nächste Iteration vorgesehen.

## Suche

Die Suche läuft lokal im Browser mit eingebettetem JavaScript, auch beim Öffnen der einzelnen HTML-Datei ohne Internet. Ohne JavaScript werden die Suchbedienelemente ausgeblendet; sämtliche Einträge, Register und Downloads bleiben verfügbar.

- **Suchen in:** gesamte Literaturangabe, Publikationstitel oder Verlag. Titel und Verlag stammen aus den entsprechenden strukturierten Datenfeldern; die Gesamtsuche verwendet den sichtbaren vollständigen Nachweis.
- **Kategorie:** alle Kategorien oder eine redaktionelle Hauptkategorie. Die Kategorie lässt sich auch ohne Suchtext auswählen.
- **Suchverhalten:** Teilzeichenfolgen werden gefunden; mehrere durch Leerzeichen getrennte Wörter müssen alle im gewählten Suchbereich vorkommen. Groß-/Kleinschreibung, Akzente und `ß`/`ss` werden beim Vergleich angeglichen. Es gibt keine Lemmatisierung, Übersetzung oder allgemeine Erkennung historischer Schreibvarianten. Originaltexte bleiben unverändert.
- **Treffer:** Die Anzeige aktualisiert sich während der Eingabe und behält die bestehende Reihenfolge der Kategorien und Einträge bei. Die Trefferzahl steht am Suchfeld und in den sichtbaren Kategorieüberschriften; bei null Treffern erscheint ein Hinweis.
- **Zurücksetzen:** Die Schaltfläche und die Escape-Taste im Suchfeld löschen Suchtext, Suchbereichsauswahl und Kategorieauswahl. Interne Navigations- und Registerlinks setzen die Auswahl ebenfalls zurück; die Links zum Suchfeld und zum Seitenanfang erhalten sie.

Beispiel: `Insel` findet derzeit 17 vollständige Nachweise, 6 Publikationstitel oder 9 Verlagsangaben. Die Kombination **Publikationstitel + Aufsätze** liefert 4 Treffer. `Weltbewusstsein` findet auch `Weltbewußtsein`.

Die Suche verändert keine Exporte. Kategorie- und Untergruppen-Downloads werden bei aktiver Auswahl ausgeblendet; Einzelexporte bleiben nutzbar. Downloads in Sprach- und Jahresregistern sowie unter „Datensets“ beziehen sich weiterhin auf ihre vollständige Auswahl. Einen Export nur der Suchtreffer gibt es nicht.

## Downloads

Jeder Eintrag bietet RIS und CSL-JSON für genau diesen Haupteintrag. Gruppenexporte stehen bei Kategorien, akademischen Untergruppen, Sprachen und Hauptjahren: insgesamt 56 Gruppen mit 112 Exportlinks. In Sprachgruppen ist die Reihenfolge chronologisch aufsteigend. Zusätzliche Auflagen werden nicht als eigenständige Datensätze in diese Exporte eingeschoben.

Der Abschnitt „Datensets“ bietet alle Einträge als RIS, CSL-JSON, CSV und vollständigen JSON-Projektdatensatz. CSV ist UTF-8 mit BOM kodiert; auch die anderen Dateien verwenden UTF-8.

### Smartphone und direkte Dateilinks

Zusätzlich zu den eingebetteten Downloads gibt es unter „Datensets“ **echte Dateilinks** und ein **ZIP-Paket** mit allen vier Gesamtformaten sowie dem Lizenzhinweis. Das umgeht die Abhängigkeit von eingebetteten Data-URL-Downloads. Ein mobiler Browser kann eine Datei anzeigen, statt sie sofort zu speichern; dann sein Teilen-/Speichermenü nutzen, auf dem iPhone etwa „In Dateien sichern“.

Diese Links funktionieren auf GitHub Pages oder zusammen mit den lokalen Ordnern `data` und `exports`. Beim alleinigen Kopieren von `index.html` bleiben die eingebetteten Downloads erhalten; die externen Dateilinks stehen dann nicht automatisch offline zur Verfügung. Einzel- und Gruppenexports bleiben eingebettete Downloads und können denselben mobilen Einschränkungen unterliegen.

### Formate und Notizen

Der Projektdatensatz bewahrt Kategorien, Sprachzuordnungen und Quellenbezüge. CSL-JSON bildet die bibliographischen Standardfelder ab und enthält den vollständigen Nachweis als `note`.

RIS bildet Hörbücher und Audiobeiträge als `SOUND`, Videos als `VIDEO`, Sammelbände einschließlich Zeitschriftendossiers als `BOOK` ab. Zusätzliche Personenrollen und komplexe Angaben bleiben bei Bedarf in der Notiz erhalten. Der Originalnachweis wird in **einem einzigen RIS-Notizfeld** ausgegeben: zuerst „Vollständige Literaturangabe:“, danach der ursprüngliche Volltext und gegebenenfalls weitere Erläuterungen. Frühere Exporte mit zwei getrennten Notizen werden dadurch nicht nachträglich in einer Literaturverwaltung geändert.

## Prüfung und beobachtete Browserunterschiede

Der Bearbeiter hat zahlreiche Datensätze kontrolliert und die Bibliographie zur Publikation freigegeben. RIS-Importe in **Citavi und Zotero** wurden geprüft; bisher wurden abgesehen von der jetzt korrigierten Aufteilung des Originalnachweises in zwei Notizen keine Fehler beobachtet. EndNote wurde nicht getestet. Die neu erzeugten RIS-Dateien sollten zur Bestätigung der Notizdarstellung nochmals importiert werden.

Die eingebetteten Gesamtdownloads funktionierten in den Tests des Bearbeiters in **Chrome auf dem Laptop**. Auf dem **iPhone mit aktuellem iOS und der Firefox-App** funktionierten sie dagegen nicht. Die ergänzten direkten Dateien und das ZIP-Paket sind ein alternativer Downloadweg; ihre tatsächliche Bedienung auf diesem iPhone muss nach Veröffentlichung nochmals geprüft werden. Eine erfolgreiche lokale Struktur-/Dateiprüfung ersetzt diesen Gerätetest nicht.

Automatisch geprüft werden erhaltene Literaturangaben, interne Sprungziele, Exportinhalte, chronologische Sprachregister und das ZIP-Paket. Die direkten Dateilinks wurden lokal über HTTP geprüft und das ZIP im lokalen Browser erfolgreich heruntergeladen. Der offizielle Zotero-RISReader hat bei allen 262 Einträgen ein einziges Notizfeld mit der gewünschten Reihenfolge erkannt. Das ist ein Parser-Test, kein erneuter Import in die vollständige Zotero-Anwendung. Korrekturhinweise sind über [GitHub Issues](https://github.com/trafikante/AvH-Bibliographie-Ette/issues) willkommen.

Die Suche wurde lokal in Edge mit Suchbereich/Kategorie, mehreren Suchwörtern, Schreibvarianten, leeren Ergebnissen, Zurücksetzen und Registerwechsel geprüft. Browseransichten mit 390 und 325 CSS-Pixeln sowie die vollständige Ansicht ohne JavaScript wurden kontrolliert. Diese Prüfung ersetzt keinen Test auf einem echten Smartphone oder mit einem Screenreader.

## Barrierefreiheit

Die deutschsprachige HTML-Seite bleibt über semantische Bereiche, sichtbare Überschriften, normale Links und verständliche Exportbeschriftungen auslesbar. Zusätzlich eingefügte unsichtbare Titelüberschriften und besondere Bereichsmarkierungen wurden auf Wunsch des Bearbeiters entfernt; die normale Tastaturbedienung und browserseitige Fokusdarstellung bleiben erhalten. Vergrößerbare Schrift, größere Bedienelemente und eine einspaltige schmale Ansicht unterstützen die Nutzung. Dekorative Icons bleiben für Screenreader verborgen. Suchfeld und Auswahlfelder besitzen sichtbare Beschriftungen und Fokusmarkierungen; die Trefferzahl wird über eine Live-Region bereitgestellt. Ein Praxistest mit Screenreader steht noch aus; eine vollständige WCAG-Konformität wird nicht behauptet.

## Lokale Neuerstellung

Die veröffentlichte HTML-Datei enthält Titel und Auswahlprinzipien bereits fest. Für die Neuerstellung liest `scripts/build_site.py` diese Angaben aus `data/web-konfiguration.json` sowie Daten aus JSON und CSV. Der Generator bettet zusätzlich Suchoberfläche, JavaScript und einen aus Titel, Verlag und Kategorie abgeleiteten Suchindex ein. Die Word-Datei ist dafür nicht mehr erforderlich.

Bei vorhandener Python-Installation mit `lxml` erzeugt `py scripts/build_site.py` HTML, Gesamtexporte und ZIP neu; `py scripts/build_site.py --check` prüft die gespeicherten Ergebnisse. Zum bloßen Lesen und Herunterladen ist Python nicht nötig. Die Word-Erfassung ist ein davon getrennter, projektspezifischer Arbeitsschritt; siehe [Prozessdokumentation](ERSTELLUNG-UND-NACHNUTZUNG.md).

## Lizenz

Daten und redaktionelle Webinhalte: CC BY 4.0. Programmcode: [MIT](LICENSE). Verlinkte Inhalte Dritter sind davon nicht erfasst; siehe [LIZENZ.md](LIZENZ.md).
