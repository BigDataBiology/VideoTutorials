import gzip
import pandas as pd
active = set()
for line in gzip.open('subcatalogs/GMGC10.dog-gut.95nr.no-rare.fna.gz', 'rt'):
    if line[0] == '>':
        active.add(line[1:-1])

with open('./GMGC10.dog-dog.no-rare.emapper2.tsv', 'wt') as out:
    for ch in pd.read_table('GMGC10.emapper2.annotations.tsv.gz', header=None, comment='#', index_col=0, chunksize=100_000):
        ch = ch[ch.index.map(active.__contains__)]
        ch.to_csv(out, sep='\t', header=None)
