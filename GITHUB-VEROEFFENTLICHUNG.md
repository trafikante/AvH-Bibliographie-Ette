# Veröffentlichung auf GitHub und GitHub Pages

## Inhalt

- [1. Was du veröffentlichst](#1-was-du-veröffentlichst)
- [2. Empfohlen: GitHub Desktop](#2-empfohlen-github-desktop)
- [3. Alternative: nur im Browser](#3-alternative-nur-im-browser)
- [4. GitHub Pages aktivieren – für beide Varianten](#4-github-pages-aktivieren--für-beide-varianten)
- [5. Einmal vollständig kontrollieren](#5-einmal-vollständig-kontrollieren)
- [6. Später pflegen – Desktop und VS Code kombinieren](#6-später-pflegen--desktop-und-vs-code-kombinieren)
- [7. Optional: eine zitierbare Version markieren](#7-optional-eine-zitierbare-version-markieren)

Diese Anleitung veröffentlicht das vorhandene Projekt als öffentliches Repository **AvH-Bibliographie-Ette** und stellt die fertige HTML-Datei als Webseite bereit. Sie benötigt weder Python noch eine JavaScript-Anwendung. Es wurden hier keine Git-Operationen und keine Uploads ausgeführt.

## 1. Was du veröffentlichst

Verwende ausschließlich den Inhalt dieses Unterordners, nicht den gesamten übergeordneten Projektordner:

```text
C:\Users\kraft\Nextcloud\26 HiN Ette (TK + UP)\Beiträge\bibliographie_oe\Projektordner\AvH-Bibliographie-Ette
```

Die Struktur im neuen Repository soll so aussehen:

```text
AvH-Bibliographie-Ette/
├── index.html
├── README.md
├── LIZENZ.md
├── .nojekyll
├── .gitignore
├── GITHUB-VEROEFFENTLICHUNG.md
├── DATENMODELL.md
├── PRUEFPROTOKOLL.md
├── UI-ENTSCHEIDUNGEN.md
├── WEB-NUTZUNG.md
├── Debatten-Medien-Recherche.md
├── data/
├── exports/
├── schema/
└── scripts/
```

`index.html` muss direkt auf der obersten Ebene liegen, nicht nochmals in einem Unterordner gleichen Namens. Die README beschreibt die Ressource; GitHub Pages zeigt dagegen `index.html` als Startseite.

**Aktuelle Daten:** `data/bibliographie.json`, `data/bibliographie.csv`, `exports/bibliographie.csl.json`, `exports/bibliographie.ris`, aktuelles Schema und redaktionelle Festlegungen.

**Nachvollziehbarkeit:** Die Prozessdokumentation, Felddefinitionen und vorhandenen Skripte erläutern das Vorgehen. Historische Probedaten werden für die veröffentlichte Ressource nicht benötigt.

**Nicht hochladen:** `scripts/__pycache__/`, `*.pyc`, Word-Sperrdateien, private Sicherungen, Zugangsdaten oder den übergeordneten Projektordner. `.gitignore` schützt beim Desktop-/Git-Workflow vor einigen temporären Dateien; beim Browserupload musst du sie selbst weglassen.

Die Word-Quelldateien liegen außerhalb dieses Unterordners und werden nicht automatisch veröffentlicht. Sie sind zum Lesen der Webseite und für die vorhandenen Downloads nicht erforderlich. Die Erfassungsskripte benötigen sie jedoch zur Neuerstellung; darauf weist die README hin. Über eine zusätzliche Veröffentlichung der Quellenfassung solltest du gesondert entscheiden.

## 2. Empfohlen: GitHub Desktop

Ich empfehle ein neues Repository außerhalb von Nextcloud, damit keine Git-Verwaltungsdateien synchronisiert werden. Der bisherige Projektordner bleibt dabei unangetastet.

1. Melde dich in GitHub Desktop bei deinem GitHub-Konto an.
2. Wähle **File → New repository**. Name: `AvH-Bibliographie-Ette`. Als Beschreibung eignet sich: `Publikationen von Ottmar Ette zu Alexander von Humboldt – Datensatz und Offline-Webansicht`.
3. Wähle als **Local path** beispielsweise `C:\Users\kraft\Documents\GitHub`. Desktop legt darunter den gleichnamigen Repositoryordner an. Zusätzliche README, Lizenz und Git-ignore-Vorlage sind nicht nötig: Diese Dateien bringen wir mit.
4. Erstelle das Repository. Öffne seinen Ordner im Explorer und kopiere den **Inhalt** des vorbereiteten Projekt-Unterordners hinein, einschließlich `.gitignore` und `.nojekyll`. Nicht den äußeren Ordner hineinkopieren.
5. Prüfe unter **Changes** die Dateiliste. Keine privaten oder temporären Dateien auswählen. Als Commit-Nachricht eignet sich `Bibliographie und Offline-Webseite hinzufügen`. Committe auf den aktuellen Hauptbranch; notiere dessen Namen, üblicherweise `main`.
6. Wähle **Publish repository**. Name kontrollieren; **Keep this code private** deaktivieren, damit das Repository öffentlich wird. Veröffentliche unter deinem persönlichen Konto, sofern du keine Organisation verwenden möchtest.
7. Öffne über **Repository → View on GitHub** die Repositoryseite. Kontrolliere die Dateien und die angezeigte README.

Dieser Ablauf folgt der [GitHub-Desktop-Anleitung](https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop). „Publish repository“ erstellt das Repository online; spätere Uploads erfolgen mit „Push origin“.

Falls der Name bereits existiert, nicht überschreiben oder löschen. Verwende dann das vorhandene Repository bewusst oder kläre den Namenskonflikt zuerst.

## 3. Alternative: nur im Browser

1. Melde dich bei GitHub an und öffne [New repository](https://github.com/new).
2. Wähle dein Konto als Eigentümer, Name `AvH-Bibliographie-Ette`, Sichtbarkeit **Public**. Keine zusätzliche README, `.gitignore` oder Lizenz initialisieren; sie liegen bereits vor. Repository erstellen.
3. Nutze den angebotenen Link zum Hochladen bestehender Dateien, später **Add file → Upload files**.
4. Ziehe die Dateien und Unterordner aus dem vorbereiteten Projekt in die Uploadfläche. Die äußere Ordnerebene darf nicht zusätzlich entstehen. `scripts/__pycache__` und andere temporäre Dateien nicht hochladen. Prüfe auch `.gitignore` und die leere `.nojekyll`.
5. Schreibe eine Commit-Nachricht und bestätige die Änderungen auf dem Hauptbranch. Kontrolliere danach `index.html`, README und Unterordner auf GitHub.

Browseruploads sind auf 100 Dateien pro Upload und 25 MiB pro Datei begrenzt. Unsere HTML-Datei ist derzeit ungefähr 4,7 MB groß und liegt darunter. Die Dateizahl dieses Projekts passt ebenfalls in einen Upload, wenn temporäre Dateien ausgeschlossen sind. [GitHub: Dateien hinzufügen](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

Falls dein Browser die leere `.nojekyll` nicht übernimmt, erstelle sie anschließend über **Add file → Create new file**, Dateiname `.nojekyll`, und committe sie. Danach wie bei der Desktop-Variante mit dem nächsten Abschnitt fortfahren.

## 4. GitHub Pages aktivieren – für beide Varianten

1. Öffne auf GitHub das neue Repository und wähle **Settings → Pages**.
2. Unter **Build and deployment** als **Source** die Option **Deploy from a branch** wählen.
3. Den Hauptbranch auswählen, normalerweise `main`. Bei abweichendem Namen den tatsächlich vorhandenen Branch nehmen.
4. Als Ordner **/(root)** wählen und **Save** klicken.
5. Warte auf die Bereitstellung. Die Pages-Einstellungen zeigen anschließend die tatsächliche Websiteadresse. Unter **Actions** kannst du den Fortschritt beziehungsweise Fehler des Pages-Deployments sehen.

`index.html` ist bereits fertig. `.nojekyll` deaktiviert die zusätzliche Jekyll-Verarbeitung; kein eigener Build-Workflow und kein Python-Lauf auf GitHub sind erforderlich. Öffentliche Repositories können GitHub Pages mit GitHub Free verwenden. [GitHub: Pages erstellen](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

Wenn du unter dem Konto `trafikante` und dem vorgesehenen Namen veröffentlichst, sind die erwarteten Adressen:

- Repository: [github.com/trafikante/AvH-Bibliographie-Ette](https://github.com/trafikante/AvH-Bibliographie-Ette)
- Webseite: [trafikante.github.io/AvH-Bibliographie-Ette/](https://trafikante.github.io/AvH-Bibliographie-Ette/)

Das sind erwartete Zieladressen, keine Bestätigung einer bereits erfolgten Veröffentlichung. Bei einem anderen Konto ändert sich der Benutzername in beiden Adressen.

## 5. Einmal vollständig kontrollieren

- Die Pages-Startseite zeigt den Word-Titel, nicht die README oder einen Ordnerindex.
- Kategorien-, Sprach- und Jahresregister funktionieren.
- „Zurück zur Navigation“ springt an den Seitenanfang.
- Je einen Einzel- und Gruppenexport als RIS und CSL-JSON herunterladen; die Auswahl und die enthaltenen Umlaute beziehungsweise chinesischen Zeichen kontrollieren.
- Die vier Gesamtdownloads testen. Die tatsächlichen Importe in Zotero, EndNote oder Citavi sind bislang nicht praktisch geprüft.
- Bei gewünschter Kontrolle ohne Internet die `index.html` herunterladen und lokal öffnen.
- Lizenzumfang in `LIZENZ.md` beachten: CC BY 4.0 für Daten und redaktionelle Webinhalte, MIT für den Programmcode; fremde verlinkte Medien behalten ihre eigenen Rechte.

Wenn Pages 404 zeigt: Branch, `/(root)`, genaue Schreibweise `index.html`, erfolgreiche Bereitstellung und fehlende zusätzliche Ordnerebene prüfen. Die Anzeige kann nach dem Speichern noch etwas Zeit benötigen.

## 6. Später pflegen – Desktop und VS Code kombinieren

Für spätere Arbeit nutze die Kopie im neuen Repository, nicht gleichzeitig zwei unabhängige Arbeitsstände.

1. Öffne das Repository aus GitHub Desktop in VS Code oder öffne den Repositoryordner direkt in VS Code.
2. Änderungen speichern und die betroffenen Dateien prüfen. Datensatzänderungen müssen auch in HTML und Exporten nachvollzogen werden; eine Änderung nur an einer Kopie aktualisiert die anderen Dateien nicht automatisch.
3. Zurück in GitHub Desktop: Änderungen prüfen, Commit-Nachricht schreiben und committen.
4. **Push origin** anklicken. Bei Updates über den Browser vorher den aktuellen Remote-Stand abrufen und übernehmen.
5. GitHub Pages übernimmt die veröffentlichte neue `index.html` nach erfolgreicher Bereitstellung.

Python brauchst du nur zur Neuerstellung. Der Seitengenerator liest JSON, CSV und `data/web-konfiguration.json` und benötigt Python mit `lxml`, keine Word-Datei. Die ursprünglichen Word-Erfassungsskripte sind davon getrennte projektspezifische Werkzeuge. Für einen Upload der fertigen Dateien musst du keines der Skripte ausführen.

## 7. Optional: eine zitierbare Version markieren

Nach erfolgreicher Kontrolle kannst du über die Repositoryseite eine Release-Version anlegen, etwa `v1.0.0`, und den veröffentlichten Datenstand beschreiben. Das ist ein zusätzlicher Schritt und wird nicht durch diese Anleitung automatisch ausgeführt. Eine spätere Zenodo-Veröffentlichung lässt sich getrennt vorbereiten; eine GitHub-Pages-Adresse ist noch keine DOI.
