from scholarly import scholarly
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import re

def clean_id(title, i):
    """Cleans and truncates the title to create a valid BibTeX ID."""
    base = re.sub(r'\W+', '_', title.lower())
    return base[:40] + f"_{i}"

def generate_bib():
    try:
        author = scholarly.search_author_id('ikDZzswAAAAJ')  # Juhi's ID
        author_filled = scholarly.fill(author, sections=['publications'])

        entries = []
        for i, pub in enumerate(author_filled['publications']):
            pub_filled = scholarly.fill(pub)
            bib = pub_filled.get('bib', {})
            if not bib.get('title'):
                continue  # Skip entries without a title

            entry = {
                'ENTRYTYPE': bib.get('pub_type', 'article'),
                'ID': clean_id(bib['title'], i),
            }

            # Add standard fields
            for key in ['author', 'title', 'journal', 'conference', 'volume', 'number', 'pages', 'publisher']:
                if key in bib:
                    entry[key] = bib[key]

            # Year: from bib if available, else from publication_date
            year = bib.get('pub_year')
            if year:
                entry['year'] = str(year)

            # Add URL if available
            if 'eprint_url' in pub_filled:
                entry['url'] = pub_filled['eprint_url']
            elif 'pub_url' in pub_filled:
                entry['url'] = pub_filled['pub_url']

            # Add abstract if available
            abstract = bib.get('abstract')
            if abstract:
                entry['abstract'] = abstract

            entries.append(entry)

        # Write to BibTeX file
        bib_database = BibDatabase()
        bib_database.entries = entries

        writer = BibTexWriter()
        writer.indent = '    '
        writer.order_entries_by = ('year', 'ID')

        with open('assets/data/publications.bib', 'w') as bibfile:
            bibfile.write(writer.write(bib_database))

        print("✅ publications.bib generated successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    generate_bib()
