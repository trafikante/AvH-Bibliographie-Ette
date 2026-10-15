# Offline-Webseite und Exporte

## Öffnen

`index.html` mit einem aktuellen Browser öffnen. Die Datei enthält sämtliche 262 Einträge, die Gestaltung und die Downloadinhalte. Sie kann allein kopiert oder auf Zenodo bereitgestellt werden; kein Server, keine Installation, keine JavaScript-Ausführung und keine Internetverbindung zum Lesen nötig. Nur die externen Publikations-/Medienlinks und die Lizenzseite benötigen Internet.

Die vorhandene `probe.html` bleibt unveränderte historische Erfassungsprobe. Maßgeblich für die neue Gesamtansicht ist `index.html`.

## Navigation

Der vollständige Titel folgt dem Titel der Word-Datei. Der aufklappbare Reiter „Prinzipien zur Auswahl“ im Seitenkopf enthält die Auswahlgrundsätze ohne Kategorienaufzählung. „Zurück zur Navigation“ springt jetzt über `#seitenanfang` an den Dokumentanfang, statt die sticky Seitenleiste als Sprungziel zu verwenden. Der Hinweis auf die parallele Veröffentlichung in HiN im Dezember 2026 folgt der redaktionellen Nutzerangabe und verlinkt die Zeitschriftenhomepage.

- Kategorien und die fünf Untergruppen von „Akademische Publikationen“ führen direkt zu den Einträgen.
- Sprach- und Jahreslinks führen zu aufklappbaren Titelregistern. Dort den jeweiligen Registerbereich öffnen und einen Titel auswählen. Mehrsprachige Publikationen stehen in mehreren Sprachregistern.
- Das Jahresregister zeigt das Hauptjahr bzw. das Startjahr von Portalen. „Weitere Ausgaben“ erschließt zusätzliche Auflagen und digitale Ausgaben gesondert.
- Jeder Eintrag bietet „Zurück zur Navigation“. Ein angesprungener Eintrag wird hervorgehoben.
- Volltextsuche: Strg+F, unter macOS ⌘F. Die Register sind keine frei kombinierbaren dynamischen Filter; alle bibliographischen Einträge bleiben im Dokument vorhanden.
- Druckansicht blendet Navigation und Exportaktionen aus. Kleine flache SVG-Symbole sind eingebettet, dekorativ und für Screenreader verborgen. Bedienung per Tastatur und responsive Gestaltung sind im HTML/CSS vorgesehen.

## Downloads

Gruppen-Downloads: Jede der sieben Kategorien, jede der fünf akademischen Untergruppen, jede Sprache und jedes Hauptjahr bietet eigene RIS-/CSL-JSON-Downloads. Kategorien-Downloads stehen unmittelbar unter der Abschnittsüberschrift; Sprach- und Jahresdownloads im geöffneten Registerbereich. Insgesamt 56 Gruppen mit 112 Exportlinks. Mehrsprachige Einträge gehören zu jeder zutreffenden Sprachgruppe; innerhalb einer Gruppe wird jeder Eintrag nur einmal exportiert. Jahresgruppen richten sich ausschließlich nach dem Hauptjahr, nicht nach zusätzlichen Auflagen. Alle Gruppen-Exportdaten sind direkt im HTML eingebettet und funktionieren ohne JavaScript oder weitere Dateien.

Der Kopfbereich wurde mit zurückhaltender grüner Farbfläche, deutlicherer typographischer Hierarchie, kompaktem Statusfeld und direkten Register-/Downloadlinks neu gestaltet. Word-Titel, Auswahlprinzipien und Veröffentlichungshinweis bleiben erhalten.

Jeder Eintrag enthält zwei Downloadlinks für genau diesen Eintrag: RIS und CSL-JSON. Im Abschnitt „Gesamtdaten“ stehen alle Einträge als RIS, CSL-JSON, CSV sowie als vollständiger Projektdatensatz JSON zur Verfügung. Die Downloads sind UTF-8-kodiert in der HTML-Datei eingebettet; die CSV enthält eine UTF-8-BOM für Tabellenprogramme.

Zusätzlich liegen Gesamt-RIS und Gesamt-CSL-JSON im Ordner `exports`, JSON/CSV im Ordner `data`. Diese Dateien sind als alternative Importwege nutzbar, falls ein Browser eingebettete Downloads einschränkt.

Die RIS-Abbildung orientiert sich an der [offiziellen Zotero-RIS-Implementierung](https://github.com/zotero/translators/blob/master/RIS.js): Hörbücher und Audiobeiträge als `SOUND`, Videos als `VIDEO`, Sammelbände einschließlich Zeitschriftendossiers als `BOOK`. Die unterschiedlichen Importrollen der Medienformate erlauben keine pauschale Gleichsetzung von Autor, Regisseur und Komponist; die bibliographisch benannten Personen stehen bei Medien deshalb mit ihren Rollen in Notizen. Übersetzungs-/Sprecherrollen, besondere Paginierungen und vollständige Literaturangaben bleiben dort ebenfalls erhalten. Dies ist eine dokumentierte Austauschabbildung, keine Zusage identischer Darstellung in allen Literaturverwaltungen.

CSL-JSON enthält die strukturierten bibliographischen Felder und zur Bewahrung zusätzlicher Angaben die vollständige Literaturangabe als `note`. Die eigenen Kategorie-, Sprach- und Quellenfelder bleiben im Projektdatensatz; CSL-JSON ersetzt ihn nicht. Einzel-Exporte enthalten den jeweiligen Haupteintrag, keine zusätzlich selbständig angelegten Neuauflagen.

## Prüfung und Grenzen

Automatisch geprüft: 262 quellentreu dargestellte Einträge, 524 Einzel-Exporte, vier Gesamt-Exporte, dekodierbare Downloadinhalte, eindeutige Sprungmarken und gültige interne Links. Keine Skripte oder extern geladenen Gestaltungsmittel. Neuaufbau und gespeicherte Ergebnisse werden mit `scripts/build_site.py --check` verglichen.

Die Browserautomatisierung erlaubt hier keine `file:`-Navigation. Daher wurden weder visuelle Browserdarstellung noch tatsächliches Speichern über die Downloadlinks in dieser Umgebung bestätigt. Bitte beim ersten manuellen Öffnen insbesondere ein RIS- und ein CSL-JSON-Download sowie die schmale/mobile Darstellung prüfen. Ein praktischer Import in Zotero, EndNote oder Citavi steht noch aus; diese Programme müssen Medienrollen gegebenenfalls unterschiedlich zuordnen.

Der lokale Prüfer ist kein vollständiger W3C-HTML-Validator. Er prüft die projektrelevante Struktur und die eingebetteten Inhalte. Der bibliographische Datensatz bleibt fachlich als Entwurf gekennzeichnet, ohne interne Erfassungsentscheidungen in den Einzeltiteln anzuzeigen.

## Lokale Erstellung

Die Erstellungsreihenfolge ist: aktuelle Word-Quelle mit `scripts/migrate_v2.py` erfassen und prüfen, danach `scripts/build_site.py` ausführen. Die Word-Datei wird nicht verändert. Python wird nur zur Neuerstellung gebraucht, nicht zum Öffnen der Webseite. Es werden keine Git-Operationen, Netzwerkzugriffe oder Veröffentlichungen ausgeführt.

Lizenz: CC BY 4.0 für Daten und projektspezifische Webinhalte; keine Lizenzübertragung für verlinkte Inhalte Dritter. Genauer Umfang in `LIZENZ.md`.
