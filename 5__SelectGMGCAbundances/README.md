# Selecting interesting rows from a very large file with Pandas

This is a general pattern for filtering very large tables with Pandas, but we are motivated by using GMGCv1.

In particular, we will select the abundance for antibiotic resistance genes (ARGs). The high-level process is:

1. get the set of ARGs
2. filter the big abundance table to create a version with only _ARGs_.

This is very trivial conceptually, but because the files are so large, it is not that easy in practice.

## Step 0: Create a conda environment

```bash
mamba create -n gmgc_select_tutorial python=3.9
conda activate gmgc_select_tutorial
mamba install -c conda-forge git git-annex ipython pandas
```

Everything else assumes that you are working in this environment

## Step 1: Getting GMGCv1 (meta)data

[[Previous tutorial using GMGCv1 metadata](../2__GMGCv1MAGs/)]

First, we need to clone the `GMGC10.data` (which is short for _GMGC 1.0_) repository.

```bash
git clone https://git.embl.de/coelho/GMGC10.data.git
cd GMGC10.data
```

This is a [git-annex](https://git-annex.branchable.com/) repository, which builds on top of `git` to add better support for (very) large files.

We will retrieve two files:

1. The unigene ARG annotation file
2. The unigene abundance file (this is very large!!)

```bash
git-annex get GMGC10.card_resfam.tsv.gz # ARG annotation
git-annex get GMGC10.sample-abundance.tsv.xz # sample abundance
```

## Step 2: Get a list of ARGs

We could also have used `pandas`, but it is very easy to do it with standard Python:

```python
import gzip

interesting = set(line.split()[0]
                for line in
                    gzip.open('./GMGC10.data/GMGC10.card_resfam.tsv.gz', 'rt')
                if line[0] != '#')
```

## Step 3: Filter the large table

This would be very easy, except that because the table is so large, _we must process it in chunks_.

```python
import pandas as pd
first_write = True
with gzip.open('selected.tsv.gz', 'wb') as out:
    for ch in pd.read_table('./GMGC10.data/GMGC10.sample-abundance.tsv.xz', index_col=0, chunksize=1_000_000):
        ch = ch[ch.index.map(interesting.__contains__)]
        if len(ch) == 0: continue
        ch.to_csv(out, sep='\t', header=first_write)
        first_write = False
```

Here we used chunks of 100,000. The exact size of the chunk does not matter too much: it should be large enough that the overhead of using Python is amortized but still small enough that it fits in memory, but the exact value is irrelevant.

That's it! Now, the file `selected.tsv.gz` will be small enough that it can be handled using normal pandas functionality.

## References

This is data from the manuscript

> Coelho, L.P., Alves, R., del Río, Á.R. et al. Towards the biogeography of
> prokaryotic genes. Nature 601, 252–256 (2022).
> [https://doi.org/10.1038/s41586-021-04233-4](https://doi.org/10.1038/s41586-021-04233-4)

If you have more questions, feel free to email [luispedro@big-data-biology.org](mailto:luispedro@big-data-biology.org) or join the [GMGC mailing list](https://groups.google.com/forum/#!forum/gmgc-users).

