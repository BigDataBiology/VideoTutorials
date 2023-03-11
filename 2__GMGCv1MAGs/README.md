# Retrieving MAGs (metagenome-assembled genomes) from GMGCv1 using Python

Video: https://youtu.be/OHrm_uDsIm4

[GMGCv1](https://gmgc.embl.de) (Global Microbial Gene Catalog, version 1) also includes MAGs (metagenome-assembled genomes) for its habitats. Because this work predates [SemiBin](https://semibin.rtfd.io/), this was still done using [MetaBAT2](https://peerj.com/articles/7359/) (which, to be clear, is pretty good, but it's now outperformed by newer alternatives).

In this tutorial, we show how to

1. Get the metadata for the MAGs
2. Select the ones that we want by _(i)_ quality, _(ii)_ habitat, and _(iii)_ taxonomy (as an example, we will select high-quality Fusobacteria MAGs from dog guts)
3. Retrieve their FASTA files


## Step 0: Setup

As usual, we are going to set up a [conda](https://conda.io/) environment for our work

```bash
mamba create -n gmgc_mags_tutorial python=3.9
conda activate gmgc_mags_tutorial
mamba install -c conda-forge git git-annex requests pandas
```

Everything else assumes that you are working in this environment

## Step 1: Getting GMGCv1 (meta)data

We can also go through the [website](https://gmgc.embl.de/download.cgi), but, for this tutorial, we want to get the data tables. First, we need to clone the `GMGC10.data` (which is short for _GMGC 1.0_) repository

```bash
git clone https://git.embl.de/coelho/GMGC10.data.git
cd GMGC10.data
```

This is a [git-annex](https://git-annex.branchable.com/) repository, which builds on top of `git` to add better support for (very) large files.

As with git, `git-annex` is very flexible and powerful, but you can get a lot done if you know 1% of it. In particular, here, we will use the `git-annex get` subcommand which retrieves individual files (and also checks the hash to ensure that they are correct).

We will retrieve two files:

1. The genome bins annotation table
2. The sample metadata

```bash
git-annex get GMBC10.meta.tsv # Genome bins
git-annex get metadata/GMGC10.sample.meta.tsv.gz # Sample metadata
```

GMBC stands for Global Microbial Bins Catalogue. We prefer to call the larger dataset _bins_ as they are unfiltered and reserve the term _MAG_ for those that pass some quality-control standards.

## Step 2: Retrieve the metadata

Now, we will work in Python to select the right bins from the metadata tables. First, we import `pandas` and load the two metadata tables:

```python
import pandas as pd

bins = pd.read_table('./GMBC10.meta.tsv', index_col=0)
meta = pd.read_table('./metadata/GMGC10.sample.meta.tsv.gz',
                index_col='original_name')

```

We need to use `original_name` as the index column. Some samples in GMGCv1 have two names: the European Nucleotide Archive (ENA) sample identifier (which is public) and, in some instances, an internal name (because the project started when the samples were not yet publicly-available).

Bins in GMBC also have two names: (i) a normalized identifier (_e.g._., `GMBC10.003_239`, where the lower numbers correspond to higher quality bins), and (ii) an internal name (_e.g._, `SRS064937.bin.20`, where `SRS064937` is the sample identifier).

So, we can use these two facts to merge the tables together:

```python
bins['sample'] = bins['genome'].str.split('.').str[0]
bins = pd.merge(bins, meta, left_on='sample', right_index=True)
```

Now, we can use standard pandas operations (such as [query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)) to select the MAGs of interest:

```python
dog_bins = bins.query('habitat == "dog gut"') \
            .query('completeness &gt;= 90 & contamination &lt;= 5')
fusos = dog_bins[dog_bins['GTDB_tk'].str.contains('p__Fusobacteriota')]
```

In this case, we were selecting _Fusobacteriota_ at the phylum level (`p__Fusobacteriota`). If you wanted to select, for example, _E. coli_ MAGs (which is a species-level classification), you could use the following:

```python
ecolis = dog_bins[dog_bins['GTDB_tk'].str.contains('s__Escherichia coli')]
```

Now, we retrieve the FASTA files. What you need to know is that individual FASTA failes are available at `https://gmgc.embl.de/api/v1.0/genome_bin/{bin_id}/fasta` (where `{bin_id}` is the identifier for the bin of interest). So, we just need to put everything together and use [requests](https://requests.readthedocs.io/) to retrieve the actual sequences:

```python
import requests
from os import makedirs

URL_PAT = 'https://gmgc.embl.de/api/v1.0/genome_bin/{bin_id}/fasta'

makedirs('dog_fusos', exist_ok=True)
for bin_id in dog_bins.index:
    url = URL_PAT.format(bin_id=bin_id)
    r = requests.get(url)
    with open(f'./dog_fusos/{bin_id}.fna', 'w') as f:
        f.write(r.text)
```

That's it!

## References

This is data from the manuscript

> Coelho, L.P., Alves, R., del Río, Á.R. et al. Towards the biogeography of
> prokaryotic genes. Nature 601, 252–256 (2022).
> [https://doi.org/10.1038/s41586-021-04233-4](https://doi.org/10.1038/s41586-021-04233-4)

If you have more questions, feel free to email [luispedro@big-data-biology.org](mailto:luispedro@big-data-biology.org) or join the [GMGC mailing list](https://groups.google.com/forum/#!forum/gmgc-users).

