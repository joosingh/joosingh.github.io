from pybtex.database.input import bibtex
from collections import defaultdict
import html

def escape(s):
    return html.escape(s, quote=True)

def generate_publications_by_year(bib_data):
    years = defaultdict(list)
    for entry_key, entry in bib_data.entries.items():
        year = entry.fields.get('year', 'Unknown')
        years[year].append((entry_key, entry))
    return dict(sorted(years.items(), reverse=True))  # Sort newest first

def generate_html(bib_data):
    years = generate_publications_by_year(bib_data)

    output = ['''
<div class="pub-container">
  <style>
    .pub-container {
        font-family: "Segoe UI", sans-serif;
        max-width: 900px;
        margin: auto;
        padding: 1rem;
    }
    .year-block summary {
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
        cursor: pointer;
    }
    .pub-entry {
        margin-bottom: 1rem;
        padding: 1rem;
        background: #f9f9f9;
        border-left: 4px solid #007acc;
        border-radius: 6px;
    }
    .pub-entry summary {
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
    }
    .pub-entry pre {
        background: #eee;
        padding: 0.5rem;
        overflow-x: auto;
        font-size: 0.9rem;
        position: relative;
    }
    .copy-button {
        position: absolute;
        top: 0.3rem;
        right: 0.5rem;
        background: #007acc;
        color: white;
        border: none;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        cursor: pointer;
    }
    .copy-button:active {
        background: #005f99;
    }
    .copy-feedback {
        font-size: 0.8rem;
        color: green;
        margin-top: 0.3rem;
        display: none;
    }
    .pub-entry a {
        color: #007acc;
        text-decoration: none;
    }
    .pub-entry a:hover {
        text-decoration: underline;
    }
  </style>
  <script>
    function copyBibtex(id) {
    const textarea = document.getElementById(id);
    textarea.select();
    document.execCommand('copy');

    const feedback = document.getElementById(id + '-copied');
    feedback.style.display = 'inline';
    setTimeout(() => {
        feedback.style.display = 'none';
    }, 1500);
    }
  </script>
''']

    for year, entries in years.items():
        output.append(f'<details class="year-block" open>')
        output.append(f'<summary>{year}</summary>')
        output.append('<div>')

        for i, (key, entry) in enumerate(entries):
            fields = entry.fields
            title = escape(fields.get('title', 'No Title'))
            #authors = ', '.join(str(person) for person in entry.persons.get('author', []))
                        # Authors, bolding your name
            
            authors = []
            for person in entry.persons.get('author', []):
                name_str = str(person)
                if 'Juhi Singh' in name_str or 'Singh, Juhi' in name_str:
                    name_str = f'<em style="color:blue;">{escape(name_str)}</em>'
                else:
                    name_str = escape(name_str)
                authors.append(name_str)
            authors = ', '.join(authors)
            
            abstract = escape(fields.get('abstract', fields.get('abstract', '')))
            url = fields.get('url', '')
            bibtex_id = f'bibtex_{year}_{i}'
            bibtex_str = escape(entry.to_string('bibtex'))

            venue = escape(fields.get('journal', fields.get('conference', '')))
            venue = f'<b style="color:#32a87b;">{venue}</b>'

            output.append('<details class="pub-entry">')
            output.append(f' <summary>{title}<br>{venue}<br>{authors}</summary>')
            output.append('  <div>')

            if abstract:
                output.append(f'<p><strong>Abstract:</strong> {abstract}</p>')
            if url:
                output.append(f'<p><a href="{url}" target="_blank">🔗 View Paper</a></p>')

            output.append(f'<p><strong>BibTeX:</strong></p>')
            output.append(f'''
<div style="position: relative;">
  <button class="copy-button" onclick="copyBibtex('{bibtex_id}')">Copy</button>
  <pre><code>{bibtex_str}</code></pre>
  <textarea id="{bibtex_id}" style="position:absolute; left:-9999px;">{entry.to_string('bibtex')}</textarea>
  <span class="copy-feedback" id="{bibtex_id}-copied">✔ Copied!</span>
</div>
''')


            output.append('  </div>')
            output.append('</details>')

        output.append('</div>')
        output.append('</details>')

    output.append('</div>')
    return '\n'.join(output)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bibtex_to_html.py publications.bib")
        sys.exit(1)

    parser = bibtex.Parser()
    bib_data = parser.parse_file(sys.argv[1])
    print(generate_html(bib_data))