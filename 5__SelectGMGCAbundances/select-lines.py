import pandas as pd
import gzip

interesting = set(line.split()[0]
                for line in
                    gzip.open('./GMGC10.data/GMGC10.card_resfam.tsv.gz', 'rt')
                if line[0] != '#')

first_write = True
with gzip.open('selected.tsv.gz', 'wb') as out:
    for ch in pd.read_table('./GMGC10.data/GMGC10.sample-abundance.tsv.xz', index_col=0, chunksize=1_000_000):
        ch = ch[ch.index.map(interesting.__contains__)]
        if len(ch) == 0: continue
        ch.to_csv(out, sep='\t', header=first_write)
        first_write = False
