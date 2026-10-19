from pathlib import Path
from collections import Counter
from copy import deepcopy
import base64
import csv
import html
import io
import json
import re
import sys
import zipfile
from lxml import html as html_parser

PROJECT = Path(__file__).resolve().parents[1]
LANGUAGES = {'de': 'Deutsch', 'en': 'Englisch', 'es': 'Spanisch', 'fr': 'Französisch',
             'pt': 'Portugiesisch', 'zh': 'Chinesisch', 'ru': 'Russisch', 'gl': 'Galicisch'}
ICONS = {
    'literarisches': '<path d="m5 19 3-7L18 2l4 4L12 16Zm3-7 4 4M5 19l-2 2"/>',
    'akademische-buchpublikationen': '<path d="M12 5C8 2 4 3 2 4v15c4-2 7-1 10 1 3-2 6-3 10-1V4c-2-1-6-2-10 1Zm0 0v15"/>',
    'internet-praesentationen': '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
    'aufsaetze': '<path d="M6 2h9l4 4v16H6ZM14 2v5h5M9 11h7M9 15h7M9 19h4"/>',
    'vorworte-lexikonartikel-bibliographien': '<path d="M5 3h14v18H5ZM8 7h8M8 11h8M8 15h5"/>',
    'debatten': '<path d="M21 12a9 9 0 0 1-9 9H3l2-4a9 9 0 1 1 16-5ZM8 10h8M8 14h5"/>',
    'uebersetzungen': '<path d="M3 5h12M9 2v3M6 5c0 5 3 8 7 10M12 5c0 5-3 8-7 10m10 6 4-11 4 11m-7-3h6"/>',
    'hoerbuecher': '<path d="M3 14v-2a9 9 0 0 1 18 0v2M3 13h4v8H3Zm14 0h4v8h-4Z"/>',
}
CSS = '''
:root{color-scheme:light;--ink:#203633;--muted:#536662;--paper:#f7f6f1;--line:#d9dfd8;--accent:#246654;--pale:#e9f0e8}
*{box-sizing:border-box}html{scroll-padding-top:1rem}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}a{color:var(--accent);text-underline-offset:.2em}a:hover{color:#123e31}header,footer,.layout{max-width:1240px;margin:auto;padding:0 32px}header{padding-top:52px;padding-bottom:30px;border-bottom:1px solid var(--line)}.eyebrow{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700}h1{font:600 clamp(2rem,4vw,3.1rem)/1.1 Georgia,"Times New Roman",serif;margin:.45em 0}header .intro{max-width:760px;font-size:1.05rem}.status,.hint{color:var(--muted);font-size:.86rem}.layout{display:grid;grid-template-columns:270px minmax(0,1fr);gap:38px;padding-top:30px}.navigation{position:sticky;top:20px;max-height:calc(100vh - 40px);overflow:auto;align-self:start;padding:0 12px 18px 0}.navigation h2{font-size:.85rem;letter-spacing:.08em;text-transform:uppercase;margin:0 0 14px}.category-list{list-style:none;padding:0;margin:0}.category-list li{margin:0 0 5px}.category-list a{display:flex;gap:9px;align-items:start;text-decoration:none;padding:8px 9px;border-radius:5px}.category-list a:hover{background:var(--pale)}.count{margin-left:auto;color:var(--muted);font-size:.78rem;font-variant-numeric:tabular-nums}.subnav{list-style:none;margin:0 0 8px 33px;padding:0;font-size:.83rem}.subnav a{padding:3px 5px}.icon{width:19px;height:19px;flex-shrink:0;vertical-align:-.2em;margin-top:3px}.navigation details{border-top:1px solid var(--line);margin-top:18px;padding-top:12px}summary{cursor:pointer;font-weight:600}.register-list{list-style:none;padding:0 0 0 10px;margin:9px 0}.register-list li{padding:5px 0}.register-list a{font-size:.88rem;text-decoration:none;display:flex;gap:12px}.register-details{margin-top:24px;border:1px solid var(--line);border-radius:7px;padding:12px 16px;background:#fff}.register-details h2{font-size:1.2rem;margin:0 0 12px}.register-details details{padding:7px 0;border-top:1px solid var(--line)}.index-links{list-style:none;padding:0;margin:9px 0;font-size:.87rem}.index-links li{display:grid;grid-template-columns:4ch minmax(0,1fr);column-gap:1rem;align-items:start;margin:10px 0;line-height:1.45}.index-links .index-year{color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}main{min-width:0}.section-heading{display:flex;gap:10px;align-items:baseline;border-bottom:2px solid var(--accent);padding-bottom:10px;margin:0 0 16px;font:600 1.55rem/1.3 Georgia,"Times New Roman",serif}.section-heading .count{font:400 .85rem system-ui,sans-serif}.category-section{margin-bottom:48px}.subheading{font-size:1.04rem;margin:24px 0 12px;color:var(--accent)}article{background:white;border:1px solid var(--line);border-radius:7px;margin:12px 0;padding:18px 20px;scroll-margin-top:16px}.entry-meta{display:flex;gap:9px;flex-wrap:wrap;align-items:center;font-size:.75rem;color:var(--muted);margin-bottom:10px}.entry-meta .icon{width:16px;height:16px;margin:0}.entry-year{font-weight:700;color:var(--accent)}.tag{background:var(--pale);padding:1px 7px;border-radius:3px}.citation{margin:0;font:1rem/1.75 Georgia,"Times New Roman",serif;overflow-wrap:anywhere}.entry-actions{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:14px;font-size:.74rem}.download{border:1px solid var(--line);border-radius:4px;padding:4px 9px;text-decoration:none;display:inline-block;background:white}.download:hover{background:var(--pale)}.back{margin-left:auto}.download-group{display:flex;flex-wrap:wrap;gap:8px;margin:13px 0}.skip{position:absolute;left:12px;top:-100px;background:white;padding:8px;z-index:2}.skip:focus{top:12px}footer{padding-top:28px;padding-bottom:40px;border-top:1px solid var(--line);margin-top:35px;font-size:.8rem;color:var(--muted)}.footer-links{display:flex;gap:14px;flex-wrap:wrap}
@media(max-width:850px){header,footer,.layout{padding-left:20px;padding-right:20px}.layout{grid-template-columns:1fr;gap:20px}.navigation{position:static;max-height:none;padding:0 0 20px;border-bottom:1px solid var(--line)}.category-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:5px}.navigation h2{margin-top:0}.subnav{margin-left:12px}header{padding-top:28px}.section-heading{font-size:1.35rem}.back{margin-left:0}}
@media(max-width:470px){.category-list{grid-template-columns:1fr}article{padding:15px}.entry-meta{gap:6px}.back{flex-basis:100%}}
@media print{body{background:white;color:black;font-size:11pt}header,footer,.layout{padding:0;max-width:none}.layout{display:block}.navigation,.register-details,.entry-actions,.download-group,.skip,.hint{display:none}header{padding-bottom:15px}h1{font-size:22pt}article{border:0;border-bottom:1px solid #ddd;border-radius:0;padding:10px 0;break-inside:avoid;box-shadow:none!important}.category-section{margin-bottom:20px}.citation{font-size:10pt}a{color:inherit;text-decoration:none}.section-heading{font-size:16pt}footer{margin-top:15px}}
'''

CSS += '.selection{margin:18px 0;max-width:850px}.selection>summary{display:list-item;width:fit-content;border:1px solid var(--line);border-radius:5px;padding:6px 12px;background:white;font-size:.85rem}.selection-content{padding:6px 16px;border-left:2px solid var(--accent);margin-top:12px;font-size:.9rem}.publication{max-width:850px;font-size:.9rem}body{scroll-margin-top:0}'
CSS += '''
header{position:relative;background:linear-gradient(125deg,#e9efe5 0%,#f7f6f1 78%);border-top:6px solid var(--accent);padding-top:42px;padding-bottom:32px}header h1{max-width:1000px;font-weight:500;letter-spacing:-.025em;line-height:1.17;margin:18px 0 20px}header .eyebrow{display:inline-block;border-bottom:1px solid #9fb6a5;padding-bottom:8px;margin:0}header .intro{font-size:.95rem;margin-bottom:14px}header .status{display:inline-block;background:#fff9;border:1px solid #c9d6c6;border-radius:25px;padding:5px 13px;font-size:.78rem;margin:0 0 14px}.header-actions{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0 18px}.header-actions a{padding:7px 13px;border:1px solid var(--accent);border-radius:5px;text-decoration:none;font-size:.82rem}.header-actions a:first-child{background:var(--accent);color:white}.header-actions a:hover{background:#dce8da;color:var(--ink)}header .publication{border-left:3px solid #9fb6a5;padding:7px 15px;max-width:840px;background:#ffffff70;font-size:.83rem}header .selection{margin:12px 0}.bulk-downloads{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:10px 0 18px;font-size:.75rem;color:var(--muted)}.bulk-downloads .download{padding:3px 8px}.subheading+.bulk-downloads{margin-top:-5px}.register-details details>.bulk-downloads{margin-bottom:10px}
@media(max-width:850px){header{padding-top:26px}header h1{font-size:2rem}.header-actions{gap:7px}}
@media print{header{background:none;border-top:0;padding-top:0}.header-actions,.bulk-downloads,.selection{display:none}header .status,header .publication{background:none;border:0;padding:0}}
'''

CSS += '''
body{font-size:17px}h1,.index-links a,.selection-content{overflow-wrap:anywhere}.entry-meta,.entry-actions,.bulk-downloads,.hint,.status{font-size:.9rem}footer{font-size:.9rem}.download{min-height:36px;padding:6px 10px}.section-heading{flex-wrap:wrap}.index-year{margin-right:.5em}.direct-files{padding:14px;border:2px solid var(--accent);border-radius:6px;background:var(--pale)}.direct-files ul{padding-left:1.4em}.direct-files li{margin:8px 0}.skip{top:auto;transform:translateY(-200%)}.skip:focus{top:8px;transform:none}
.section-heading{overflow-wrap:anywhere}.category-list a>span:not(.count){min-width:0;overflow-wrap:anywhere}
@media(pointer:coarse){a.download,.header-actions a,summary{min-height:44px;display:inline-flex;align-items:center}.entry-actions{gap:12px}.direct-files a{display:inline-block;padding:8px 0}}
@media print{.direct-files{display:none}}
'''


CSS += '''
.selection-content{border-left:0;background:#fff;border:1px solid var(--line);border-radius:7px;padding:18px 22px;line-height:1.75;max-width:72ch}.selection-content h2{font-size:1.05rem;margin:0 0 12px;color:var(--accent)}.selection-content h2:not(:first-child){margin-top:24px;padding-top:16px;border-top:1px solid var(--line)}.selection-content p{margin:10px 0}.selection-rules{margin:16px 0}.selection-rules dt{font-weight:650;margin-top:16px;overflow-wrap:anywhere}.selection-rules dd{margin:5px 0 12px;padding-left:14px;border-left:2px solid var(--line)}.footer-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:30px}.footer-grid>*{min-width:0}.footer-grid h2{font-size:1rem;color:var(--ink);margin:0 0 14px}.footer-grid ul{list-style:none;padding:0;margin:8px 0}.footer-grid li{margin:8px 0}.footer-grid p{margin:8px 0}.footer-grid a{overflow-wrap:anywhere}.github-link{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600}.github-mark{width:22px;height:22px;flex-shrink:0;fill:var(--ink)}
@media(max-width:700px){.footer-grid{grid-template-columns:1fr;gap:22px}.footer-grid>*+*{border-top:1px solid var(--line);padding-top:18px}.selection-content{padding:16px}}
@media print{.footer-grid{display:block}.footer-grid>*{margin-top:14px}}
'''


def escape(value):
    return html.escape(str(value), quote=True)


def icon(identifier):
    return '<svg class="icon" aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">' + ICONS[identifier] + '</svg>'


def github_mark():
    return (PROJECT / 'assets/mark-github.svg').read_text(encoding='utf-8').replace('<svg ', '<svg class="github-mark" aria-hidden="true" focusable="false" fill="currentColor" ', 1)


def display_name(person):
    if 'literal' in person:
        return person['literal']
    family = ' '.join(filter(None, [person.get('non-dropping-particle'), person['family']]))
    return family + ', ' + person.get('given', '')


def csl_record(record):
    metadata = deepcopy(record['bibliographic'])
    notes = [metadata.get('note', ''), record['source']['citation_text']]
    for contributor in record.get('contributors', []):
        notes.append(contributor['role'] + ': ' + display_name(contributor['name']))
    metadata['note'] = '\n'.join(filter(None, notes))
    return metadata


def ris_record(record, category_labels, subgroup_labels):
    metadata = record['bibliographic']
    audio = record['publication_medium'] == 'audio'
    video = record['publication_medium'] == 'video'
    type_map = {'book': 'BOOK', 'chapter': 'CHAP', 'article-journal': 'JOUR',
                'article-magazine': 'MGZN', 'article-newspaper': 'NEWS', 'webpage': 'ELEC'}
    kind = 'SOUND' if audio else 'VIDEO' if video else type_map[metadata['type']]
    lines = []
    notes = ['Vollständige Literaturangabe:\n' + record['source']['citation_text']]

    def field(tag, value):
        if value:
            if tag == 'N1':
                notes.append(str(value))
                return
            for part in str(value).splitlines():
                lines.append(tag + '  - ' + part)

    field('TY', kind)
    field('ID', record['id'])
    field('TI', metadata['title'])
    for person in metadata.get('author', []):
        field('N1' if audio or video else 'AU', ('Autor: ' if audio or video else '') + display_name(person))
    for person in metadata.get('editor', []):
        field('A3' if kind == 'BOOK' else 'N1' if audio or video else 'A2', display_name(person))
    for person in record['container_contributors'].get('editor', []):
        field('A2' if kind in ['CHAP', 'JOUR', 'MGZN', 'NEWS'] else 'N1', display_name(person))
    for person in metadata.get('translator', []):
        field('N1' if audio or video else 'A4', ('Übersetzer: ' if audio or video else '') + display_name(person))
    for person in metadata.get('narrator', []):
        field('N1', 'Sprecher: ' + display_name(person))
    for contributor in record.get('contributors', []):
        field('N1', contributor['role'] + ': ' + display_name(contributor['name']))
    issued = metadata['issued']['date-parts'][0]
    field('PY', issued[0])
    if len(issued) == 3:
        field('DA', '/'.join(str(part).zfill(2) for part in issued))
    for code in record['languages']:
        field('LA', code)
    for tag, key in [('T2', 'container-title'), ('T3', 'collection-title'), ('PB', 'publisher'),
                     ('CY', 'publisher-place'), ('VL', 'volume'), ('IS', 'issue'), ('DO', 'DOI')]:
        field(tag, metadata.get(key))
    pages = metadata.get('page', '')
    simple = re.fullmatch(r'([\dIVXLCDMivxlcdm]+)[–-]([\dIVXLCDMivxlcdm]+)', pages)
    if simple:
        field('SP', simple.group(1))
        field('EP', simple.group(2))
    elif pages and re.fullmatch(r'[\dIVXLCDMivxlcdm]+', pages):
        field('SP', pages)
    elif pages:
        field('N1', 'Seiten: ' + pages)
    field('UR', metadata.get('URL'))
    for resource in record.get('online_resources', []):
        if resource['url'] != metadata.get('URL'):
            field('N1', 'Weiterer Online-Verweis (Zuordnung siehe Literaturangabe): ' + resource['url'])
    field('KW', category_labels[record['category_id']])
    field('KW', subgroup_labels.get(record['subcategory_id']))
    field('N1', 'Medium: ' + metadata['medium'] if metadata.get('medium') else '')
    note_lines = '\n\n'.join(notes).splitlines()
    lines.append('N1  - ' + note_lines[0])
    lines.extend('      ' + line if line else '' for line in note_lines[1:])
    lines.append('ER  - ')
    return '\r\n'.join(lines) + '\r\n\r\n'


def download(label, filename, content, mime, context=None):
    payload = base64.b64encode(content.encode('utf-8')).decode('ascii')
    return '<a class="download" aria-label="' + escape(label + ' herunterladen: ' + (context or filename)) + '" download="' + escape(filename) + '" href="data:' + mime + ';charset=utf-8;base64,' + payload + '">' + escape(label) + '</a>'


def linked_citation(record):
    fragment = html_parser.fragment_fromstring(record['source']['citation_html'], create_parent='div')
    urls = sorted({resource['url'] for resource in record.get('online_resources', [])
                   if resource['url'].startswith(('https://', 'http://'))}, key=len, reverse=True)
    if not urls:
        return record['source']['citation_html']
    pattern = re.compile('|'.join(re.escape(url) for url in urls))
    changed = False
    # Link only text outside existing anchors; punctuation and inline markup stay intact.
    for node in fragment.xpath('.//text()[not(ancestor::a)]'):
        matches = list(pattern.finditer(str(node)))
        if not matches:
            continue
        changed = True
        owner = node.getparent()
        if node.is_tail:
            parent = owner.getparent()
            position = parent.index(owner) + 1
            owner.tail = str(node)[:matches[0].start()]
        else:
            parent = owner
            position = 0
            owner.text = str(node)[:matches[0].start()]
        for index, match in enumerate(matches):
            link = html_parser.Element('a', href=match.group())
            link.text = match.group()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(node)
            link.tail = str(node)[match.end():end]
            parent.insert(position + index, link)
    if not changed:
        return record['source']['citation_html']
    return escape(fragment.text or '') + ''.join(html_parser.tostring(child, encoding='unicode') for child in fragment)


def index_link(record, edition=None):
    metadata = record['bibliographic']
    title = metadata['title']
    label = title if edition is None else title + ' — ' + edition['label']
    return '<li><span class="index-year">' + str(record['publication_year'] if edition is None else edition['publication_year']) + '</span><a href="#' + record['id'] + '">' + escape(label) + '</a></li>'


def bulk_downloads(records, group, category_labels, subgroup_labels):
    ris = ''.join(ris_record(record, category_labels, subgroup_labels) for record in records)
    csl = json.dumps([csl_record(record) for record in records], ensure_ascii=False, indent=2) + '\n'
    if group.startswith('kategorie-'):
        context = category_labels[group.removeprefix('kategorie-')]
    elif group.startswith('untergruppe-'):
        context = subgroup_labels[group.removeprefix('untergruppe-')]
    elif group.startswith('sprache-'):
        context = 'Sprache ' + LANGUAGES[group.removeprefix('sprache-')]
    else:
        context = 'Jahr ' + group.removeprefix('jahr-')
    context += ', ' + str(len(records)) + ' Einträge'
    links = download('RIS', group + '.ris', ris, 'application/x-research-info-systems', context)
    links += download('CSL-JSON', group + '.json', csl, 'application/json', context)
    return '<div class="bulk-downloads" data-export-group="' + escape(group) + '"><span>' + str(len(records)) + ' Einträge herunterladen:</span>' + links + '</div>'


def build_page(dataset):
    config = json.loads((PROJECT / 'data/web-konfiguration.json').read_text(encoding='utf-8'))
    title = config['title']
    principles = config['selection_principles']
    repository = config['repository_url']
    zenodo = config['zenodo']
    doi_url = 'https://doi.org/' + zenodo['doi']
    concept_doi_url = 'https://doi.org/' + zenodo['concept_doi']
    explanation = []
    rules = []
    for text in principles:
        if ': ' in text:
            label, body = text.split(': ', 1)
            rules.append('<dt>' + escape(label) + '</dt><dd>' + escape(body) + '</dd>')
        else:
            explanation.append('<p>' + escape(text) + '</p>')
    documentation = '<h2>Grundlage und Auswahl</h2>' + ''.join(explanation) + '<dl class="selection-rules">' + ''.join(rules) + '</dl>'
    documentation += '<h2>Ausführliche Dokumentation</h2><p>Wie aus der Word-Bibliographie in Zusammenarbeit mit einem KI-Agenten diese Webseite und strukturierte Daten entstanden sind, beschreibt die <a href="' + escape(repository + '/blob/main/ERSTELLUNG-UND-NACHNUTZUNG.md') + '">Prozessdokumentation</a>. Das <a href="' + escape(repository + '/blob/main/DATENMODELL.md') + '">Datenmodell</a> erläutert die Erfassungsregeln. Dokumentation, Rohdatensatz und Programmcode sind im <a href="' + escape(repository) + '">GitHub-Repository</a> verfügbar.</p>'
    documentation += '<h2>Zitieren und Archivierung</h2><p>Kraft, Tobias; Päßler, Ulrich (2026): <em>' + escape(title) + '</em>. Version ' + escape(zenodo['version']) + '. Zenodo. <a href="' + escape(doi_url) + '">' + escape(doi_url) + '</a>.</p><p>Diese DOI bezeichnet den archivierten Stand. Die laufende Webseite kann spätere Änderungen enthalten. Für die Ressource über alle Versionen hinweg steht die <a href="' + escape(concept_doi_url) + '">versionsübergreifende DOI</a> bereit. <a href="' + escape(repository + '/blob/main/CITATION.cff') + '">Maschinenlesbare Zitierangaben</a>.</p>'
    citation = '<section class="register-details" id="zitierhinweis"><h2>Zitierhinweis</h2>'
    citation += '<h3>HTML-Webseite</h3><p>Kraft, Tobias; Päßler, Ulrich (2026): <em>' + escape(title) + '</em>. HTML-Webseite. <a href="https://trafikante.github.io/AvH-Bibliographie-Ette/">https://trafikante.github.io/AvH-Bibliographie-Ette/</a> (abgerufen am [TT.MM.JJJJ]).</p>'
    citation += '<h3>GitHub-Repository</h3><p>Kraft, Tobias; Päßler, Ulrich (2026): <em>' + escape(title) + '</em>. GitHub-Repository. <a href="' + escape(repository) + '">' + escape(repository) + '</a> (abgerufen am [TT.MM.JJJJ]).</p>'
    citation += '<h3>Archivierte Fassung (Zenodo)</h3><p>Kraft, Tobias; Päßler, Ulrich (2026): <em>' + escape(title) + '</em>. Version ' + escape(zenodo['version']) + '. Zenodo. <a href="' + escape(doi_url) + '">' + escape(doi_url) + '</a>.</p><p>Diese DOI bezeichnet den archivierten Stand. Die laufende Webseite und das Repository können spätere Änderungen enthalten. Für die Ressource über alle Versionen hinweg steht die <a href="' + escape(concept_doi_url) + '">versionsübergreifende DOI</a> bereit. <a href="' + escape(repository + '/blob/main/CITATION.cff') + '">Maschinenlesbare Zitierangaben zur archivierten Fassung</a>.</p></section>'
    selection = '<details class="selection"><summary>Dokumentation</summary><div class="selection-content">' + documentation + '</div></details>'
    records = dataset['records']
    chronological_records = sorted(records, key=lambda record: (record['publication_year'], record['source_order']))
    categories = dataset['categories']
    category_labels = {category['id']: category['label'] for category in categories}
    subgroup_labels = {subgroup['id']: subgroup['label'] for category in categories for subgroup in category['subcategories']}
    counts = Counter(record['category_id'] for record in records)
    category_nav = []
    for category in categories:
        identifier = category['id']
        subnav = ''.join('<li><a href="#' + subgroup['id'] + '">' + escape(subgroup['label']) + '</a></li>' for subgroup in category['subcategories'])
        category_nav.append('<li><a href="#' + identifier + '">' + icon(identifier) + '<span>' + escape(category['label']) + '</span><span class="count">' + str(counts[identifier]) + '</span></a>' + ('<ul class="subnav">' + subnav + '</ul>' if subnav else '') + '</li>')
    language_codes = sorted({code for record in records for code in record['languages']}, key=lambda code: LANGUAGES[code])
    years = sorted({record['publication_year'] for record in records}, reverse=True)
    languages_nav = ''.join('<li><a href="#sprache-' + code + '">' + LANGUAGES[code] + '<span class="count">' + str(sum(code in record['languages'] for record in records)) + '</span></a></li>' for code in language_codes)
    years_nav = ''.join('<li><a href="#jahr-' + str(year) + '">' + str(year) + '<span class="count">' + str(sum(record['publication_year'] == year for record in records)) + '</span></a></li>' for year in years)
    navigation = '<aside class="navigation" id="navigation"><nav aria-label="Bibliographie erschließen"><h2>Navigation</h2><ul class="category-list">' + ''.join(category_nav) + '</ul><details open><summary>Sprachen</summary><ul class="register-list">' + languages_nav + '</ul></details><details><summary>Jahre</summary><ul class="register-list">' + years_nav + '</ul></details><p class="hint">Register öffnen und einen Titel wählen. Volltextsuche: Strg+F, am Mac ⌘F. Die Register ersetzen keine kombinierbaren Filter.</p><p><a href="#downloads">Datensets</a></p></nav></aside>'
    sections = []
    for category in categories:
        content = []
        current_subgroup = None
        for record in records:
            if record['category_id'] != category['id']:
                continue
            subgroup = record['subcategory_id']
            if subgroup and subgroup != current_subgroup:
                content.append('<h3 class="subheading" id="' + subgroup + '">' + escape(subgroup_labels[subgroup]) + '</h3>')
                content.append(bulk_downloads([item for item in records if item['subcategory_id'] == subgroup], 'untergruppe-' + subgroup, category_labels, subgroup_labels))
                current_subgroup = subgroup
            label = subgroup_labels.get(subgroup, category['label'])
            entry_icon = icon('hoerbuecher' if subgroup == 'hoerbuecher' else category['id'])
            languages = ', '.join(LANGUAGES[code] for code in record['languages'])
            meta = entry_icon + '<span>' + escape(label) + '</span><span class="entry-year">' + str(record['publication_year']) + '</span><span class="tag">' + escape(languages) + '</span>'
            ris = ris_record(record, category_labels, subgroup_labels)
            csl = json.dumps([csl_record(record)], ensure_ascii=False, indent=2) + '\n'
            actions = download('RIS', record['id'] + '.ris', ris, 'application/x-research-info-systems', record['bibliographic']['title']) + download('CSL-JSON', record['id'] + '.json', csl, 'application/json', record['bibliographic']['title']) + '<a class="back" href="#seitenanfang">Zurück zur Navigation ↑</a>'
            content.append('<article id="' + record['id'] + '" aria-label="' + escape(record['bibliographic']['title']) + '"><div class="entry-meta">' + meta + '</div><p class="citation">' + linked_citation(record) + '</p><div class="entry-actions">' + actions + '</div></article>')
        category_exports = bulk_downloads([record for record in records if record['category_id'] == category['id']], 'kategorie-' + category['id'], category_labels, subgroup_labels)
        sections.append('<section class="category-section" id="' + category['id'] + '"><h2 class="section-heading">' + escape(category['label']) + '<span class="count">' + str(counts[category['id']]) + ' Einträge</span></h2>' + category_exports + ''.join(content) + '</section>')
    language_register = ''.join('<details id="sprache-' + code + '"><summary>' + LANGUAGES[code] + ' · ' + str(sum(code in record['languages'] for record in records)) + ' Einträge</summary>' + bulk_downloads([record for record in chronological_records if code in record['languages']], 'sprache-' + code, category_labels, subgroup_labels) + '<ul class="index-links">' + ''.join(index_link(record) for record in chronological_records if code in record['languages']) + '</ul></details>' for code in language_codes)
    year_register = ''.join('<details id="jahr-' + str(year) + '"><summary>' + str(year) + ' · ' + str(sum(record['publication_year'] == year for record in records)) + ' Einträge</summary>' + bulk_downloads([record for record in records if record['publication_year'] == year], 'jahr-' + str(year), category_labels, subgroup_labels) + '<ul class="index-links">' + ''.join(index_link(record) for record in records if record['publication_year'] == year) + '</ul></details>' for year in years)
    editions = {}
    for record in records:
        for edition in record['related_editions']:
            for year in edition.get('publication_years', [edition['publication_year']]):
                editions.setdefault(year, []).append((record, edition))
    editions_register = ''.join('<details><summary>' + str(year) + '</summary><ul class="index-links">' + ''.join(index_link(record, {**edition, 'publication_year': year}) for record, edition in editions[year]) + '</ul></details>' for year in sorted(editions, reverse=True))
    registers = '<section class="register-details" id="sprachregister"><h2>Sprachregister</h2><p class="hint">Mehrsprachige Publikationen erscheinen in jedem zutreffenden Register.</p>' + language_register + '</section><section class="register-details" id="jahresregister"><h2>Jahresregister</h2><p class="hint">Erscheinungsjahr der Hauptausgabe, bei Portalen das Startjahr.</p>' + year_register + '</section><section class="register-details" id="weitere-ausgaben"><h2>Weitere Ausgaben</h2><p class="hint">Neuauflagen und digitale Ausgaben führen zum zugehörigen Haupteintrag; die Ausgabenangabe steht dort in der Literaturangabe.</p>' + editions_register + '</section>'
    all_csl = json.dumps([csl_record(record) for record in records], ensure_ascii=False, indent=2) + '\n'
    all_ris = ''.join(ris_record(record, category_labels, subgroup_labels) for record in records)
    dataset_json = json.dumps(dataset, ensure_ascii=False, indent=2) + '\n'
    csv_content = (PROJECT / 'data/bibliographie.csv').read_text(encoding='utf-8-sig')
    downloads = '<section class="register-details" id="downloads"><h2>Gesamtdaten</h2><div class="download-group">' + download('CSL-JSON', 'bibliographie.csl.json', all_csl, 'application/json') + download('RIS', 'bibliographie.ris', all_ris, 'application/x-research-info-systems') + download('CSV', 'bibliographie.csv', '\ufeff' + csv_content, 'text/csv') + download('Projektdatensatz JSON', 'bibliographie.json', dataset_json, 'application/json') + '</div><p class="hint">RIS und CSL-JSON für Literaturverwaltung. Der Projektdatensatz bewahrt zusätzlich Kategorien und Quellenbezüge. RIS bildet komplexe Medienrollen und Seitenangaben teilweise als Notizen ab. Importe in Zotero, EndNote und Citavi sind noch nicht praktisch geprüft.</p></section>'
    header = '<header><p class="eyebrow">Alexander von Humboldt · Bibliographie</p><h1>' + escape(title) + '</h1><p class="intro">Zusammengestellt von Tobias Kraft und Ulrich Päßler (BBAW).</p><p class="status">262 Einträge · 7 Kategorien · Stand 13.10.2026</p>' + selection
    header += '<div class="header-actions"><a href="#bibliographie">Zur Bibliographie ↓</a><a href="#sprachregister">Sprachen</a><a href="#jahresregister">Jahre</a><a href="#downloads">Datensets</a><a href="#zitierhinweis">Zitierhinweis</a></div>'
    header += '<p class="publication">Die Bibliographie wurde parallel als Teil der Sondernummer der <em>HiN</em> zum 70. Geburtstag von Ottmar Ette im Dezember 2026 online veröffentlicht (<a href="https://www.hin-online.de/">www.hin-online.de</a>). Die zugehörigen <a href="#downloads">Datensets</a> stehen in verschiedenen Formaten zum Herunterladen bereit.</p>'
    header += '<p class="hint">Offline nutzbar, ohne JavaScript. Eingebettete Downloads können auf Smartphones eingeschränkt sein; dafür stehen im Abschnitt „Datensets“ direkte Dateilinks und ein ZIP-Paket bereit.</p></header>'
    footer_navigation = '<nav aria-label="Navigation im Seitenfuß"><h2>Bibliographie</h2><ul><li><a href="#seitenanfang">Zurück zur Navigation ↑</a></li><li><a href="#sprachregister">Sprachregister</a></li><li><a href="#jahresregister">Jahresregister</a></li><li><a href="#weitere-ausgaben">Weitere Ausgaben</a></li><li><a href="#downloads">Datensets</a></li></ul></nav>'
    footer_project = '<section><h2>Projekt und Dokumentation</h2><a class="github-link" href="' + escape(repository) + '">' + github_mark() + '<span>GitHub-Repository</span></a><ul><li><a href="' + escape(repository + '/blob/main/ERSTELLUNG-UND-NACHNUTZUNG.md') + '">Entstehung und Zusammenarbeit</a></li><li><a href="' + escape(repository + '/blob/main/DATENMODELL.md') + '">Datenmodell und Erfassungsregeln</a></li><li><a href="' + escape(repository + '/tree/main/data') + '">Rohdatensatz</a></li></ul></section>'
    footer_project = footer_project.replace('</ul>', '<li><a href="' + escape(doi_url) + '">Zenodo: archivierte Version ' + escape(zenodo['version']) + '</a></li><li><a href="' + escape(repository + '/blob/main/CITATION.cff') + '">Zitierangaben</a></li></ul>')
    footer_license = '<section><h2>Lizenz und Nachnutzung</h2><p>Daten und redaktionelle Webinhalte: <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.</p><p>Programmcode: <a href="' + escape(repository + '/blob/main/LICENSE') + '">MIT-Lizenz</a>. Verlinkte Inhalte Dritter behalten ihre eigenen Rechte.</p><p><a href="' + escape(repository + '/blob/main/LIZENZ.md') + '">Lizenz- und Bildnachweise</a></p></section>'
    footer = '<footer><div class="footer-grid">' + footer_navigation + footer_project + footer_license + '</div></footer>'
    direct_files = '<div class="direct-files"><h3>Dateien für Smartphone und Desktop</h3><p>Falls eingebettete Downloads nicht funktionieren: Datei öffnen und über das Browsermenü speichern oder teilen. Auf dem iPhone gegebenenfalls „In Dateien sichern“ wählen.</p><ul><li><a href="exports/bibliographie-downloads.zip" download>ZIP-Paket mit allen vier Gesamtformaten herunterladen</a></li><li><a href="exports/bibliographie.csl.json">CSL-JSON-Datei öffnen</a></li><li><a href="exports/bibliographie.ris">RIS-Datei öffnen</a></li><li><a href="data/bibliographie.csv">CSV-Datei öffnen</a></li><li><a href="data/bibliographie.json">JSON-Projektdatensatz öffnen</a></li></ul><p class="hint">Diese Dateilinks benötigen die veröffentlichte Webseite oder die zugehörigen lokalen Ordner. Die eingebetteten Downloads funktionieren auch in der allein gespeicherten HTML-Datei, soweit der Browser sie unterstützt.</p></div>'
    downloads = downloads.replace('<div class="download-group">', direct_files + '<h3>Eingebettete Offline-Downloads</h3><div class="download-group">', 1)
    downloads = downloads.replace('Importe in Zotero, EndNote und Citavi sind noch nicht praktisch geprüft.', 'Der Bearbeiter hat RIS-Importe in Zotero und Citavi geprüft; abgesehen von der inzwischen korrigierten Notizaufteilung wurden dabei keine Fehler beobachtet. EndNote wurde nicht getestet.')
    downloads = downloads.replace('<h2>Gesamtdaten</h2>', '<h2>Datensets</h2>')
    return '<!doctype html>\n<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Bibliographie der Publikationen von Ottmar Ette zu Alexander von Humboldt mit Kategorien-, Sprach- und Jahresregistern sowie RIS- und CSL-JSON-Export."><title>' + escape(title) + '</title><style>' + CSS + '</style></head><body id="seitenanfang" tabindex="-1"><a class="skip" href="#bibliographie">Zur Bibliographie</a>' + header + '<div class="layout">' + navigation + '<main id="bibliographie" tabindex="-1">' + ''.join(sections) + registers + downloads + citation + '</main></div>' + footer + '</body></html>\n'


def validate(page, dataset):
    tree = html_parser.fromstring(page)
    identifiers = tree.xpath('//*[@id]/@id')
    assert len(identifiers) == len(set(identifiers))
    assert tree.get_element_by_id('seitenanfang').tag == 'body'
    assert tree.xpath('//title/text()')[0] == tree.xpath('//h1/text()')[0]
    assert all(link.get('href') == '#seitenanfang' for link in tree.xpath('//a[contains(text(), "Zurück zur Navigation")]'))
    assert 'Sie unterscheidet die Kategorien' not in ''.join(tree.xpath('//details[@class="selection"]')[0].itertext())
    assert tree.xpath('//details[@class="selection"]/summary/text()') == ['Dokumentation']
    assert not tree.xpath('//article//h3|//article//h4|//*[@class="sr-only"]')
    assert not tree.xpath('//article[@aria-labelledby]')
    assert len(tree.xpath('//footer//div[@class="footer-grid"]/*')) == 3
    assert len(tree.xpath('//footer//svg[@class="github-mark"]')) == 1
    assert not tree.xpath('//script|//iframe|//link[@rel="stylesheet"]|//img|//audio|//video')
    assert not re.search(r'\son\w+\s*=', page, re.I)
    assert not re.search(r'@import|url\(', CSS)
    records = dataset['records']
    assert len(tree.xpath('//article')) == len(records)
    for href in tree.xpath('//a/@href'):
        if href.startswith('#'):
            assert href[1:] in identifiers, href
    for record in records:
        article = tree.get_element_by_id(record['id'])
        citation = article.xpath('./p[@class="citation"]')[0]
        assert ''.join(citation.itertext()) == ''.join(record['source']['paragraphs'])
        links = article.xpath('.//a[@download]')
        assert len(links) == 2
        payloads = {link.get('download'): base64.b64decode(link.get('href').split(',', 1)[1]).decode('utf-8') for link in links}
        csl = json.loads(payloads[record['id'] + '.json'])
        assert csl == [csl_record(record)]
        ris = payloads[record['id'] + '.ris']
        assert ris.count('TY  - ') == ris.count('ER  - ') == 1
        assert ris.count('\r\nN1  - ') == 1
        assert '\r\nN1  - Vollständige Literaturangabe:\r\n      ' in ris
        assert 'ID  - ' + record['id'] + '\r\n' in ris
        assert all(resource['url'] in ris for resource in record.get('online_resources', []))
        assert not article.xpath('.//details')
    downloads = tree.get_element_by_id('downloads').xpath('.//a[@download and starts-with(@href, "data:")]')
    payloads = {link.get('download'): base64.b64decode(link.get('href').split(',', 1)[1]).decode('utf-8') for link in downloads}
    assert len(json.loads(payloads['bibliographie.csl.json'])) == len(records)
    assert payloads['bibliographie.ris'].count('TY  - ') == len(records)
    assert json.loads(payloads['bibliographie.json']) == dataset
    assert len(list(csv.DictReader(io.StringIO(payloads['bibliographie.csv'].lstrip('\ufeff'))))) == len(records)
    category_labels = {category['id']: category['label'] for category in dataset['categories']}
    subgroup_labels = {subgroup['id']: subgroup['label'] for category in dataset['categories'] for subgroup in category['subcategories']}
    expected_groups = {}
    for record in records:
        groups = ['kategorie-' + record['category_id'], 'jahr-' + str(record['publication_year'])]
        groups += ['sprache-' + code for code in record['languages']]
        if record['subcategory_id']:
            groups.append('untergruppe-' + record['subcategory_id'])
        for group in groups:
            expected_groups.setdefault(group, []).append(record)
    group_elements = tree.xpath('//*[@data-export-group]')
    assert {element.get('data-export-group') for element in group_elements} == set(expected_groups)
    assert len(group_elements) == len(expected_groups)
    for element in group_elements:
        group = element.get('data-export-group')
        links = element.xpath('./a[@download]')
        assert len(links) == 2
        expected_records = expected_groups[group]
        if group.startswith('sprache-'):
            expected_records = sorted(expected_records, key=lambda record: (record['publication_year'], record['source_order']))
            register_links = tree.get_element_by_id(group).xpath('./ul/li/a/@href')
            assert register_links == ['#' + record['id'] for record in expected_records]
        group_payloads = {link.get('download'): base64.b64decode(link.get('href').split(',', 1)[1]).decode('utf-8') for link in links}
        assert json.loads(group_payloads[group + '.json']) == [csl_record(record) for record in expected_records]
        assert group_payloads[group + '.ris'] == ''.join(ris_record(record, category_labels, subgroup_labels) for record in expected_records)
    return {'records': len(records), 'single_exports': len(records) * 2, 'complete_exports': len(downloads),
            'bulk_groups': len(group_elements), 'bulk_exports': len(group_elements) * 2,
            'javascript': False, 'external_assets': False, 'source_text_preserved': True,
            'internal_links_valid': True, 'download_payloads_checked': True, 'language_registers_chronological': True, 'single_ris_note': True, 'bytes_utf8': len(page.encode('utf-8'))}


def main():
    dataset = json.loads((PROJECT / 'data/bibliographie.json').read_text(encoding='utf-8'))
    page = build_page(dataset)
    page = page.replace('262 Einträge · 7 Kategorien · Stand 13.10.2026', str(len(dataset['records'])) + ' Einträge · ' + str(len(dataset['categories'])) + ' Kategorien · Stand ' + '.'.join(reversed(dataset['dataset']['created'].split('-'))))
    report = validate(page, dataset)
    target = PROJECT / 'index.html'
    labels = {category['id']: category['label'] for category in dataset['categories']}
    sublabels = {subgroup['id']: subgroup['label'] for category in dataset['categories'] for subgroup in category['subcategories']}
    expected_csl = json.dumps([csl_record(record) for record in dataset['records']], ensure_ascii=False, indent=2) + '\n'
    expected_ris = ''.join(ris_record(record, labels, sublabels) for record in dataset['records'])
    if '--check' in sys.argv:
        assert target.read_text(encoding='utf-8') == page
        assert (PROJECT / 'exports/bibliographie.csl.json').read_text(encoding='utf-8') == expected_csl
        with (PROJECT / 'exports/bibliographie.ris').open(encoding='utf-8', newline='') as handle:
            assert handle.read() == expected_ris
    else:
        target.write_text(page, encoding='utf-8')
        exports = PROJECT / 'exports'
        exports.mkdir(exist_ok=True)
        labels = {category['id']: category['label'] for category in dataset['categories']}
        sublabels = {subgroup['id']: subgroup['label'] for category in dataset['categories'] for subgroup in category['subcategories']}
        (exports / 'bibliographie.csl.json').write_text(json.dumps([csl_record(record) for record in dataset['records']], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        with (exports / 'bibliographie.ris').open('w', encoding='utf-8', newline='') as handle:
            handle.write(''.join(ris_record(record, labels, sublabels) for record in dataset['records']))
        with zipfile.ZipFile(exports / 'bibliographie-downloads.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
            for filename in ['exports/bibliographie.csl.json', 'exports/bibliographie.ris', 'data/bibliographie.csv', 'data/bibliographie.json', 'LIZENZ.md', 'LICENSE']:
                archive.write(PROJECT / filename, Path(filename).name)
        (PROJECT / 'data/web-pruefung.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with zipfile.ZipFile(PROJECT / 'exports/bibliographie-downloads.zip') as archive:
        assert archive.testzip() is None
        for filename in ['exports/bibliographie.csl.json', 'exports/bibliographie.ris', 'data/bibliographie.csv', 'data/bibliographie.json', 'LIZENZ.md', 'LICENSE']:
            assert archive.read(Path(filename).name) == (PROJECT / filename).read_bytes()
    for href in html_parser.fromstring(page).xpath('//a/@href'):
        if not href.startswith(('#', 'https://', 'http://', 'data:')):
            assert (PROJECT / href).is_file(), href
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
