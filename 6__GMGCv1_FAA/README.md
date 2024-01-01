# How to obtain amino acids version of GMGCv1 subcatalogs

Video: [https://youtu.be/xjYBFphJ0bk](https://youtu.be/xjYBFphJ0bk)

A subscriber question about GMGCv1, namely how to get amino acid versions of
the subcatalogs (_e.g._, the _human gut subcatalog_). We only provide
nucleotide versions for disk space reasons, but it's pretty easy to generate
amino acid ones and here we show how.

## Step 0: install software & get data

As usual, we are going to set up a [conda](https://conda.io/) environment for our work

```bash
mamba create -n gmgc_faa_tutorial python=3.9
conda activate gmgc_faa_tutorial
mamba install -c conda-forge git git-annex biopython
```

Everything else assumes that you are working in this environment

## Step 1: Getting GMGCv1 (meta)data

We can also go through the [website](https://gmgc.embl.de/download.cgi), but, for this tutorial, we want to get the data tables. First, we need to clone the `GMGC10.data` (which is short for _GMGC 1.0_) repository

```bash
git clone https://git.embl.de/coelho/GMGC10.data.git
cd GMGC10.data/subcatalogs
```

This is a [git-annex](https://git-annex.branchable.com/) repository, which builds on top of `git` to add better support for (very) large files.

```bash
git-annex get GMGC10.dog-gut.95nr.no-rare.faa.gz
```

### Translate from nucleotides to amino acids

```python
from Bio import SeqIO
import gzip

with open('GMGC10.dog-gut.95nr.no-rare.faa.gz', 'wt') \
        as out:
    for s in SeqIO.parse(
                    gzip.open('./GMGC10.dog-gut.95nr.no-rare.fna.gz', 'rt'),
                    format='fasta'):
        sa = s.translate()
        out.write(f'>{s.id}\n{sa.seq}\n')
```
