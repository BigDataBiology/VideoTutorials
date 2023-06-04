# How to eggnog-mapper annotations for genes in the GMGC

This is building on the [previous tutorial](../6__GMGCv1_FAA/README.md) and the
first two steps are repeated.

## Step 0 (as before): install software & get data

As usual, we are going to set up a [conda](https://conda.io/) environment for our work

```bash
mamba create -n gmgc_faa_tutorial python=3.9
conda activate gmgc_faa_tutorial
mamba install -c conda-forge git git-annex biopython
```

Everything else assumes that you are working in this environment

## Step 1 (as before): Getting GMGCv1 (meta)data

We can also go through the [website](https://gmgc.embl.de/download.cgi), but, for this tutorial, we want to get the data tables. First, we need to clone the `GMGC10.data` (which is short for _GMGC 1.0_) repository

```bash
git clone https://git.embl.de/coelho/GMGC10.data.git
cd GMGC10.data/subcatalogs
```

This is a [git-annex](https://git-annex.branchable.com/) repository, which builds on top of `git` to add better support for (very) large files.

```bash
git-annex get GMGC10.dog-gut.95nr.no-rare.faa.gz
```

### Step 2: Retrieve the eggnog-mapper annotations

In technical terms, this is just an application of the techniques we saw on how
to [retrieve rows from large tables](../5__SelectGMGCAbundances/README.md) using pandas.

#### Step 2.1: build a set of identifiers of interest

```python
import gzip
import pandas as pd
active = set()
for line in gzip.open('subcatalogs/GMGC10.dog-gut.95nr.no-rare.fna.gz', 'rt'):
    if line[0] == '>':
        active.add(line[1:-1])
```

#### Step 2.2: iterate in chunks to select the rows


```python
with open('./GMGC10.dog-dog.no-rare.emapper2.tsv', 'wt') as out:
    for ch in pd.read_table('GMGC10.emapper2.annotations.tsv.gz', header=None, comment='#', index_col=0, chunksize=100_000):
        ch = ch[ch.index.map(active.__contains__)]
        ch.to_csv(out, sep='\t', header=None)
```
