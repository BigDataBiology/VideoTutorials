# Using Macrel on the command line for metagenomics

This is quite a trivial one-step tutorial: install the software and run the one-step tool.

## Step 0: install macrel using mamba

```bash
mamba create -n macrel_tutorial python=3.9
conda activate macrel_tutorial
mamba install -c bioconda macrel
```

## Step 1: Run macrel

```bash
macrel contigs \
    -f contig.fa \
    -o macrel_out
```

## References


>   Santos-Júnior CD, Pan S, Zhao X, Coelho LP. 2020.
>   Macrel: antimicrobial peptide screening in genomes and metagenomes.
>   PeerJ 8:e10555. DOI: [10.7717/peerj.10555](https://doi.org/10.7717/peerj.10555)

Run Macrel online: [https://big-data-biology.org/software/macrel](https://big-data-biology.org/software/macrel)
