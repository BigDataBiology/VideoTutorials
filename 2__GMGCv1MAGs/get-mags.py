# This is a slightly more robust version of the script presented as it adds a
# bit more error checking and reorganized the code (e.g., imports at the top)
import pandas as pd
import requests
from os import path, makedirs

if not path.exists('GMGC10.meta.tsv'):
    import sys
    if not path.islink('GMGC10.meta.tsv'):
        sys.stderr.write('GMGC10.meta.tsv not found. Make sure you are running in the correct directory.\n')
    else:
        sys.stderr.write('GMGC10.meta.tsv is a dangling symlink. You should probably run\n\n')
        sys.stderr.write('  git-annex get GMBC10.meta.tsv # Genome bins\n')
        sys.stderr.write('  git-annex get metadata/GMGC10.sample.meta.tsv.gz # Sample metadata\n')
    sys.exit(1)

URL_PAT = 'https://gmgc.embl.de/api/v1.0/genome_bin/{bin_id}/fasta'
bins = pd.read_table('./GMBC10.meta.tsv', index_col=0)
meta = pd.read_table('./metadata/GMGC10.sample.meta.tsv.gz', index_col='original_name')

bins['sample'] = bins['genome'].str.split('.').str[0]
bins = pd.merge(bins, meta, left_on='sample', right_index=True)
dog_bins = bins.query('habitat == "dog gut" & completeness >= 90 & contamination <= 5')
fusos = dog_bins[dog_bins['GTDB_tk'].str.contains('p__Fusobacteriota')]


makedirs('dog_fusos', exist_ok=True)
for bin_id in fusos.index:
    url = URL_PAT.format(bin_id=bin_id)
    r = requests.get(url)
    with open(f'dog_fusos/{bin_id}.fna', 'w') as f:
        f.write(r.text)

