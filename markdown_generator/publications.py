import subprocess
from bs4 import BeautifulSoup



# Generate the publications HTML file
print("generating the publications.html file ...")
subprocess.run(['bibtex2html', 
    '--no-abstract',
    '--no-keywords',
    '--quiet',
    #'--reverse-sort',
    #'--sort-by-date',
    '-o', 'publications',
    'publications.bib'
])

print("generating the index.html file ...")
# Load the source HTML file
with open('publications.html', 'r') as f:
    source_soup = BeautifulSoup(f, 'html.parser')

# Find the table in the source file
table = source_soup.find('table')

lines = [
    "---",
    "layout: archive",
    "title: Publications",
    "permalink: /publications/",
    "author_profile: true",
    "---",
    "{% if author.googlescholar %}",
    "{% endif %}",
    "{% include base_path %}",
]

# append table to the end '../pages/publications.md'
with open('../_pages/publications.md', 'w') as f:
    for line in lines:
        f.write(line + '\n')

    f.write(str(table) + '\n')

lines = [
    "---",
    "layout: archive",
    "title: Bibtex",
    "permalink: /publications/publications_bib",
    "author_profile: true",
    "---",
    "{% include base_path %}",
]

with open('publications_bib.html', 'r') as f:
    source_soup = BeautifulSoup(f, 'html.parser')

body = source_soup.find('body')
body_str = str(body)
body_str = body_str.replace('publications.html', '')

with open('../_pages/publications_bib.md', 'w') as f:
    for line in lines:
        f.write(line + '\n')

    f.write(body_str + '\n')

# table_str = str(table)
# table_str = table_str.replace(static_site_dir + '/', "")
# table = BeautifulSoup(table_str, 'html.parser')