# Datenmodell und Erfassungsregeln

## Inhalt

- [Aufbau des Datensatzes](#aufbau-des-datensatzes)
- [Felder eines Eintrags](#felder-eines-eintrags)
- [Redaktionelle Kategorien](#redaktionelle-kategorien)
- [Bibliographische Typen und Personenrollen](#bibliographische-typen-und-personenrollen)
- [Sprachen, Jahre und weitere Ausgaben](#sprachen-jahre-und-weitere-ausgaben)
- [Quellen, Seiten und Online-Verweise](#quellen-seiten-und-online-verweise)
- [Export und Webansicht](#export-und-webansicht)
- [Freigabe und Pflege](#freigabe-und-pflege)

Diese Spezifikation beschreibt den veröffentlichten JSON-Projektdatensatz mit 262 Einträgen. Maßgeblich sind `data/bibliographie.json` und das zugehörige Projektschema `schema/bibliographie.schema.json`. Die CSV-Datei ist eine tabellarische Ableitung; CSL-JSON und RIS sind Austauschformate.

## Aufbau des Datensatzes

| Feld | Bedeutung |
|---|---|
| `schema_version` | Version des Projektformats, derzeit `0.2.0`. |
| `dataset` | Titel, Erfassungsdatum, Umfang, Quellenbezug, Lizenz und Publikationsfreigabe. |
| `categories` | Kontrollierte Kategorien mit stabilen IDs, sichtbaren Bezeichnungen und Untergruppen. |
| `records` | Bibliographische Erfassungseinträge. |

`dataset.status: complete-transcription` bezeichnet die vollständige Übertragung, `dataset.publication_status: released` die Publikationsfreigabe. `dataset.review_note` erläutert deren Grundlage: redaktionelle Kontrolle zahlreicher Einträge und Importtests, keine behauptete Einzelprüfung sämtlicher Felder. `created` bezeichnet das Datum der Datensatzerstellung, nicht das Erscheinungsjahr einer Publikation.

## Felder eines Eintrags

| Feld | Erfassungsregel |
|---|---|
| `id` | Dauerhafte ID im Muster `ette-000001`. Nicht aus Jahr oder Absatznummer berechnet; nicht umnummerieren oder wiederverwenden. |
| `source_order` | Position in der übernommenen Quellenreihenfolge, beginnend mit 1. |
| `category_id` | Eine Hauptkategorie aus dem kontrollierten Vokabular. |
| `subcategory_id` | Eine akademische Untergruppe oder `null`, wenn nicht anwendbar. |
| `languages` | Liste der Publikationssprachen. Leere Liste bedeutet ungeklärt, nicht sprachlos. |
| `language_assessment` | Status und Begründung der Sprachzuordnung: ausdrücklich belegt/bestätigt (`explicit`), erschlossen (`inferred`) oder ungeklärt (`undetermined`). |
| `publication_year` | Jahr der beschriebenen Hauptausgabe, bei Portalen das Startjahr. |
| `year_basis` | `publication` oder `online-start`. |
| `publication_medium` | `text`, `audio`, `video` oder `website`, unabhängig von Kategorie und CSL-Typ. |
| `bibliographic` | Bibliographische Standardfelder mit identischer ID; fehlende optionale Angaben werden ausgelassen. |
| `parallel_titles` | Vorhandene Paralleltitel beziehungsweise Übersetzungen mit Sprache und Status. |
| `container_contributors` | Personenrollen des übergeordneten Werkes, getrennt von Rollen des Einzelbeitrags. |
| `contributors` | Zusätzliche Medienrollen, falls vorhanden: `participant`, `interviewer`, `moderator`, jeweils mit Namensobjekt. |
| `related_editions` | Weitere Auflagen oder Ausgaben mit eigenem Jahr, Quellenangabe und gegebenenfalls URL. |
| `relations` | Beziehungen zu vorhandenen IDs: `part-of` oder `same-publication`. |
| `online_resources` | Online-Verweise der vollständigen Quellenangabe in ihrer Reihenfolge; `basis: current-source`. |
| `notes` | Erschließungs- und Quellenhinweise; keine automatisch öffentlich angezeigten Kommentare. |
| `review_status` | `reviewed`: vom Bearbeiter für die Veröffentlichung freigegebener Datenbestand. Keine Zusicherung, dass jedes Feld einzeln verifiziert wurde. |
| `source` | Dateiname, SHA256, Absatznummern, Absatztexte, vollständige Literaturangabe und deren HTML-Fassung. |

Leere Listen bedeuten keine erfassten Listenelemente; `null` bezeichnet bei der Untergruppe „nicht anwendbar“. Unbekannte optionale Einzelangaben werden nicht durch erfundene Werte ersetzt. Die Dokumentation einer Datenfelddefinition ist keine Behauptung, dass das Feld in jedem Eintrag befüllt ist.

## Redaktionelle Kategorien

| Stabile ID | Sichtbare Bezeichnung |
|---|---|
| `literarisches` | Literarisches |
| `akademische-buchpublikationen` | Akademische Publikationen |
| `internet-praesentationen` | Internet-Präsentationen |
| `aufsaetze` | Aufsätze |
| `vorworte-lexikonartikel-bibliographien` | Vorworte, Lexikonartikel und Bibliographien |
| `debatten` | Wissenschaftskommunikation |
| `uebersetzungen` | Übersetzungen |

Nur „Akademische Publikationen“ hat Untergruppen: `monographien`, `editionen`, `sammelbaende`, `didaktische-materialien` und `hoerbuecher`. Technische IDs bleiben auch bei geänderten sichtbaren Bezeichnungen stabil.

## Bibliographische Typen und Personenrollen

Die Feldnamen orientieren sich an CSL-JSON. Im veröffentlichten Bestand werden `book`, `chapter`, `article-journal`, `article-magazine`, `article-newspaper`, `broadcast` und `webpage` verwendet.

- Editionen, Monographien, didaktische Bücher und Sammelbände: `book`, mit den jeweils belegten Rollen.
- Zeitschriftendossiers: auf redaktionelle Festlegung wie Sammelbände als `book`; Zeitschriftenkontext, Band und Heft bleiben erhalten.
- Hörbücher: `book` mit Audio-Medium; im RIS-Export `SOUND`.
- Audio-/Videobeiträge: `broadcast`; RIS-Typ `SOUND` beziehungsweise `VIDEO`.
- Vorworte/Einleitungen: Typ der publizierten Einheit, etwa `chapter` in einem Buch oder `article-journal` in einer Zeitschrift.
- Übersetzungen: Typ der übersetzten publizierten Einheit. Ette wird nicht pauschal als Autor eines Humboldt-Buches gesetzt.

Namen werden, soweit sicher, in `family`, `given` und gegebenenfalls `non-dropping-particle` getrennt. `Humboldt, Alexander von` entspricht Familie `Humboldt`, Vorname `Alexander`, Partikel `von`. Nicht sicher zerlegbare Namen bleiben als `literal` erhalten.

Autoren, Herausgeber, Übersetzer, Sprecher und weitere Mitwirkende bleiben unterscheidbar. Rollen eines übergeordneten Werkes werden einem Einzelbeitrag nicht automatisch zugeschrieben.

## Sprachen, Jahre und weitere Ausgaben

Publikationssprache und Sprache eines Klammertitels sind verschiedene Angaben. Ein chinesischer oder russischer Beitrag mit englischem Paralleltitel wird dadurch nicht englischsprachig. Mehrsprachige Publikationen erhalten mehrere Codes: `de`, `en`, `es`, `fr`, `pt`, `zh`, `ru`, `gl` sind im Bestand vertreten. CSL `language` wird nur bei genau einer zugeordneten Sprache gesetzt.

Das Hauptjahr steht konsistent in `publication_year` und `bibliographic.issued.date-parts[0][0]`. Ein belegter Tag wird als `[Jahr, Monat, Tag]` erfasst. Titeljahreszahlen sowie abweichende Aufzeichnungs-/Wiederholungsdaten ersetzen nicht das Publikationsdatum.

Ein redaktioneller Haupteintrag bleibt ein Datensatz. Weitere Auflagen stehen in `related_editions` mit `publication_year`, `label`, `source_paragraph`, `citation_text` und gegebenenfalls `url`. Bei mehreren zugehörigen Jahren kann `publication_years` ergänzen. Ausgabenbezogene Links bleiben dieser Ausgabe zugeordnet. Jahresregister und Jahres-Gruppenexports verwenden das Hauptjahr; zusätzliche Ausgaben haben ein eigenes Register.

## Quellen, Seiten und Online-Verweise

`source.paragraphs` bewahrt die unveränderten Quellenabsätze, `source.citation_text` verbindet sie mit Zeilenumbrüchen. `source.citation_html` enthält escapten Text, Kursivierung mit `<em>` und Hyperlinks. Absatznummern dienen nur als Fundstellen in der durch SHA256 bestimmten Word-Fassung, nicht als dauerhafte IDs.

Historische Schreibungen, chinesische Schriftzeichen und Transliteration bleiben erhalten. Das russische Transliterationzeichen `ʹ` ist U+02B9, kein typographisch zu ersetzender Apostroph.

Römische, nicht zusammenhängende und besonders erläuterte Paginierungen werden nicht zu vermeintlich fortlaufenden Seitenbereichen vereinfacht. Bedeutungsvolle Mehrfachnachweise werden nicht automatisch dedupliziert.

DOI steht in `bibliographic.DOI` ohne Resolverpräfix; die Ansicht verwendet die vollständige DOI-URL. CSL `URL` enthält höchstens die primäre Adresse. `online_resources` bewahrt auch weitere Verweise; deren genaue Zuordnung ergibt sich aus dem vollständigen Nachweis und gegebenenfalls `related_editions`.

## Export und Webansicht

Der Projektdatensatz ist das informationsreichere Format. CSV bildet seine Felder tabellarisch ab; verschachtelte Inhalte können als JSON-Zeichenfolgen in Zellen stehen. CSL-JSON und RIS ersetzen nicht sämtliche Projektfelder.

CSL-JSON erhält den vollständigen Originalnachweis zusätzlich als `note`. RIS verwendet für den Originalnachweis und ergänzende Erläuterungen ein einziges mehrzeiliges `N1`-Feld, beginnend mit „Vollständige Literaturangabe:“. Spezifische Rollen und besondere Seitenangaben bleiben nötigenfalls dort erhalten.

Die HTML-Ansicht zeigt `source.citation_html`, nicht einen aus Einzelfeldern neu zusammengesetzten Nachweis. Sprachregister und Sprach-Gruppenexports sind nach Hauptjahr aufsteigend sortiert; bei gleichem Jahr bleibt die Quellenreihenfolge maßgeblich. Kategorien zeigen die Quellenreihenfolge. Webtitel und Auswahlprinzipien stehen in `data/web-konfiguration.json`; sie sind Webmetadaten, keine zusätzlichen bibliographischen Einträge.

## Freigabe und Pflege

Der Bestand ist für die Datenpublikation freigegeben. Es liegen redaktionelle Kontrollen zahlreicher Einträge sowie RIS-Importtests in Zotero und Citavi vor. Dies bedeutet keine lückenlose Einzelverifikation aller Felder. Sprachzuordnungen behalten ihre jeweilige Begründung auch nach der Publikationsfreigabe.

Korrekturen sollen stabile IDs und Quellenbezüge bewahren und in Daten, Exporte und HTML übernommen werden. Hinweise können als [GitHub Issue](https://github.com/trafikante/AvH-Bibliographie-Ette/issues) eingereicht werden. Datenlizenz: CC BY 4.0; Programmcode: [MIT](LICENSE).
