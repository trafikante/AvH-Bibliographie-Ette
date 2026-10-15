# Datenmodell und Erfassungsregeln

Aktuelle Nutzerfestlegung: Hauptgruppe „Akademische Publikationen“, stabile ID `akademische-buchpublikationen`. Hörbücher bleiben eigenständige Untergruppe `hoerbuecher`, bibliographisch `book` mit Audio-Medium. Zeitschriftendossiers unter `sammelbaende` werden im Export ebenfalls als `book` behandelt, ohne ihren Zeitschriftenkontext zu entfernen. Die nachfolgenden älteren Angaben zum Typ `periodical` dokumentieren den vorausgehenden Entwurfsstand. Nutzerbestätigte Sprachen werden nach stabiler ID mit Zuordnungsstatus `explicit` gespeichert.

Entwurf 0.1.0, 13.10.2026. Ziel ist eine quellentreue Bibliographie mit getrennten redaktionellen Kategorien und standardisierten bibliographischen Typen.

## Drei Ebenen

Aktuelle Erweiterung für v2 (13.10.2026): Die frühere Kategorie „Debatten“ heißt jetzt „Wissenschaftskommunikation“; ihre stabile ID bleibt `debatten`. Medien erhalten CSL-Typ `broadcast` und Projektmedium `audio` oder `video`. Belegte vollständige Erscheinungsdaten stehen in `issued.date-parts`; Aufzeichnungs- und Wiederholungsdaten bleiben im vollständigen Quellnachweis unterscheidbar.

`online_resources` bewahrt sämtliche Online-Verweise der Quellenangabe in ihrer Reihenfolge. Ausgabenbezogene Links bleiben zusätzlich in `related_editions` zugeordnet. CSL `URL` enthält höchstens die primäre Adresse. Bei Medien beschreibt `contributors` zusätzliche Rollen `participant`, `interviewer` und `moderator`; ausdrücklich genannte Mitwirkung wird nicht pauschal als Autorschaft ausgegeben. Namen ohne sichere Zerlegung bleiben `literal`.

Der vollständige v2-Datensatz umfasst 262 Einträge und bleibt fachlich `draft`. Die folgenden Probeangaben dokumentieren den ursprünglichen Entwurfsstand.

1. Quellenfassung: vollständige Literaturangabe, exakte Textabsätze und übernommene Kursivierung.
2. Projektmetadaten: stabile ID, Kategorie, Untergruppe, Publikationssprachen, Jahreszuordnung, Beziehungen und Erfassungsstatus.
3. Bibliographische Metadaten: CSL-JSON-kompatible Titel, Personen mit Rollen, Erscheinungsangaben, Seiten und Identifikatoren.

Die Webseite zeigt die redaktionellen Kategorien. CSL-Typen dienen der bibliographischen Nachnutzung, nicht als Ersatz der Kategoriennavigation.

## Hauptfelder je Eintrag

| Feld | Bedeutung |
|---|---|
| `id` | Dauerhafte ID `ette-000001` usw.; nicht aus Jahr, Titel oder Absatznummer berechnet. Bereits vergebene IDs nicht umnummerieren oder wiederverwenden. |
| `category_id` | Hauptkategorie aus dem kontrollierten Vokabular. |
| `subcategory_id` | Untergruppe der akademischen Buchpublikationen; sonst `null`. |
| `languages` | Liste der Publikationssprachen als Sprachcodes, z. B. `de`, `en`, `es`, `pt`, `fr`, `ru`, `zh`. Eine leere Liste bedeutet noch nicht bestimmt. |
| `language_assessment` | Explizit aus der Quelle, anhand des Titels erschlossen oder noch ungeklärt; jeweils mit Begründung. Erschlossen ist nicht gleich extern verifiziert. |
| `publication_year` | Erscheinungsjahr der beschriebenen Hauptausgabe; bei Portalen dokumentiertes Startjahr. |
| `year_basis` | `publication` oder `online-start`; bei fehlendem Jahr künftig `null` und eigener Prüfhinweis. |
| `bibliographic` | CSL-JSON-kompatibler Datensatz mit identischer ID und standardisiertem Typ. Fehlende optionale Felder werden ausgelassen. |
| `parallel_titles` | In der Quelle vorhandene Übersetzungen bzw. Paralleltitel mit Sprache und Status; nicht als Publikationssprache interpretieren. |
| `publication_medium` | Text, Hörbuch oder Website; unabhängig vom CSL-Typ. |
| `related_editions` | In Fortsetzungsabsätzen genannte weitere Ausgaben mit eigenem Jahr, eigener Literaturangabe und ausgabenbezogenen Links. |
| `relations` | Explizite Verbindung zu anderen Erfassungseinträgen, etwa Teil eines Dossiers oder dieselbe Publikation in einer anderen redaktionellen Kategorie. |
| `notes` | Besonderheiten ohne Verlust wissenschaftlicher Information. |
| `review_status` | In dieser Probe `draft`; technische Prüfung ist keine fachliche Freigabe. |
| `source` | Dateiname, SHA256, interne Absatznummern, Absatztexte, vollständige Literaturangabe und HTML-Darstellung. |

## Kategorien aus der finalen Word-Datei

| ID | Bezeichnung | Untergruppen |
|---|---|---|
| `literarisches` | Literarisches | keine |
| `akademische-buchpublikationen` | Akademische Buchpublikationen | Monographien, Editionen, Sammelbände, Didaktische Materialien, Hörbücher |
| `internet-praesentationen` | Internet-Präsentationen | keine |
| `aufsaetze` | Aufsätze | keine |
| `vorworte-lexikonartikel-bibliographien` | Vorworte, Lexikonartikel und Bibliographien | keine |
| `debatten` | Debatten | keine |
| `uebersetzungen` | Übersetzungen | keine |

Die Bezeichnung „Akademische Buchpublikationen“ folgt der tatsächlichen Abschnittsüberschrift der aktuellen DOCX. Keine frühere Änderungsempfehlung wird nachträglich in die abgeschlossene Quelle eingetragen. Die Kategorienliste im JSON enthält auch die unveränderten Unterüberschriften `a.` bis `e.` als Quellenbezeichnungen.

## Bibliographischer Standard

CSL-JSON ist Grundlage der Feldbenennung. Verwendete Typen in der Probe: `article-journal`, `article-newspaper`, `book`, `chapter`, `periodical`, `webpage`.

- Eine Edition und ein Sammelband sind bibliographisch `book`, mit unterschiedlicher Personenrollenbelegung und redaktioneller Untergruppe.
- Ein Zeitschriftendossier ist `periodical`, nicht pauschal `book`, auch wenn es redaktionell unter Sammelbänden steht.
- Ein Hörbuch wird als `book` mit `medium: Audio-CD` und Projektmedium `audio` beschrieben. Diese Modellentscheidung muss beim späteren RIS-Export auf das im Zielprogramm verfügbare Hörbuchformat abgebildet werden.
- Ein didaktisches Buch bleibt `book`; die didaktische Funktion steht in der Untergruppe.
- Vorworte und Einleitungen in Büchern sind `chapter`, Einleitungen in Zeitschriften `article-journal`.
- Ein Roman-Auszug in einer Zeitschrift bleibt bibliographisch `article-journal` und redaktionell „Literarisches“.
- Übersetzungen erhalten den Typ der publizierten Einheit und die in der Quelle belegten Rollen. Ette wird nicht pauschal als Autor eines Humboldt-Buches gesetzt.

Schemaquelle: [CSL-JSON-Schema](https://github.com/citation-style-language/schema/blob/master/schemas/input/csl-data.json). Die ausgewählte Typmenge und die benutzten Felder wurden anhand des offiziellen Schemas geprüft. Das projektspezifische Schema ist ein dokumentierter Ausschnitt, kein vollständiger Ersatz des CSL-Schemas.

## Sprachen

Publikationssprache und Sprache eines Klammertitels sind verschiedene Angaben. Russische Umschrift mit englischem Paralleltitel bleibt ein russischer Beitrag; ein chinesischer Aufsatz mit englischem Klammertitel bleibt ein chinesischer Beitrag. Zweisprachige Beiträge erhalten zwei Sprachcodes. Sprache des übergeordneten Buches und Sprache des einzelnen Beitrags nicht vermischen.

Ein deutsches Titelblatt eines Sammelbandes beweist nicht, dass alle Beiträge deutsch sind. Beim Sammelband „Ansichten Amerikas“ bleibt die Sprache deshalb in der Probe ungeklärt. Andere plausible Titelzuordnungen werden ausdrücklich als erschlossen gekennzeichnet. Eine spätere Filteroberfläche muss eine Gruppe „Sprache noch ungeklärt“ anzeigen.

CSL `language` wird nur für Einträge mit genau einer zugeordneten Publikationssprache gesetzt. Mehrsprachigkeit bleibt verlustfrei in `languages`; eine Liste wird nicht in ein einzelnes CSL-Sprachfeld gezwungen.

## Jahre und Ausgaben

Es wird das Erscheinungsjahr der beschriebenen Ausgabe erfasst, nicht eine beliebige Jahreszahl im Titel, ein Archivdatum oder das Jahr der Erfassung.

Die Grundregel für die Probe ist ein Datensatz pro redaktionellem Haupteintrag. Neuauflagen aus Fortsetzungsabsätzen werden unter `related_editions` mit eigenem Jahr dokumentiert. Beispiel: „Weltbewußtsein“ hat 2002 als Hauptjahr und Ausgaben von 2005 und 2020. Der Link von 2005 bleibt an der digitalen Ausgabe und wird nicht als Link der Druckausgabe von 2002 ausgegeben.

Für die spätere Jahresnavigation: Hauptjahr als Voreinstellung; optionale Registeransicht „einschließlich weiterer Ausgaben“ mit deutlicher Ausgabenkennzeichnung. Werden Ausgaben später eigenständig erfasst, erhalten sie neue IDs und Beziehungen zum Haupteintrag; der bisherige Eintrag bleibt adressierbar.

## Personen, Seiten und Beziehungen

- Namen stehen getrennt nach Familienname, Vorname und gegebenenfalls Namenspartikel. Die angezeigte Literaturangabe bleibt unverändert. `Humboldt, Alexander von` wird als Familie `Humboldt`, Vorname `Alexander`, Partikel `von` modelliert.
- Herausgeber und Übersetzer des Beitrags werden von Herausgebern und Übersetzern des übergeordneten Buches unterschieden. Containerrollen stehen in den projektspezifischen `container_contributors` und werden nicht fälschlich dem Beitrag zugeschrieben.
- Bei „Die Humboldtsche Wissenschaft …“ wird Silvia Kruse als Übersetzerin des Buches, nicht ohne Beleg als Übersetzerin des deutschen Einleitungsbeitrags geführt.
- Römische Seiten, nicht zusammenhängende Paginierung und Hinweise wie „nur gerade Seiten“ bleiben erhalten. Ein spezieller Seitenbereich wird nicht zu einem vermeintlich fortlaufenden Bereich vereinfacht.
- Erfassungseinträge verschiedener Kategorien werden nicht stillschweigend dedupliziert. Edition und Übersetzungsleistung zu derselben Ausgabe können getrennte Einträge mit einer Beziehung bleiben.
- DOI wird als Kennung ohne Resolverpräfix in CSL gespeichert, als vollständige DOI-URL in der Ansicht dargestellt. Eine Dossier-URL wird nicht automatisch als Artikel-URL anderer Beiträge übernommen.

## Quellenbezug und Kontrolle

`source.paragraphs` enthält unveränderte Absätze. `source.citation_text` verbindet zugehörige Absätze mit Zeilenumbrüchen. `source.citation_html` enthält ausschließlich escapten Text, `<em>` und Links; es wird kein aktiver Inhalt aus Word übernommen. Absatznummern dienen nur der Wiederauffindbarkeit innerhalb der durch SHA256 identifizierten Quelle, nicht als permanente Datensatz-ID.

Nachprüfbar sind: 20 verschiedene IDs, Abdeckung aller sieben Kategorien und aller fünf akademischen Untergruppen, Quellenidentität, Verlustfreiheit der übernommenen Absatztexte, richtige Verknüpfung der Fortsetzungen und Schema-Konformität. Fachliche Freigabe der Erschließung steht anschließend an.
