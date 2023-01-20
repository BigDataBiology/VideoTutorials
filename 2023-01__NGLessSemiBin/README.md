# Metagenomics tutorial

Full script:

```bash

# Get the data
bash get-data.sh

# Create conda environment:

mamba create -n metagenomics_tutorial python=3.9
conda activate metagenomics_tutorial
mamba install -c conda-forge -c bioconda ngless SemiBin

# Run NGLess
ngless -j8 process.ngl

# Run SemiBin2
SemiBin2 single_easy_bin -i contig.fa -b output.sorted.bam --environment human_gut -p4 --output semibin.out

```

## Step -1: Get Data

You can run `get-data.sh` command to retrieve the data, which will be put into a directory called `data/`

## Step 0: Create conda environment and install NGLess/SemiBin:

You can use [conda](https://docs.conda.io/) or its faster replacement,
[mamba](https://mamba.readthedocs.io/) to install NGLess and SemiBin (on Linux
or Mac OS X):

```bash
mamba create -n metagenomics_tutorial python=3.9
conda activate metagenomics_tutorial
mamba install -c conda-forge -c bioconda ngless SemiBin
```

## Step 1: Run NGLess

The file `process.ngl` is used to process the data.

## Step 2: Run SemiBin2

The full command is

```bash
SemiBin2 \
    single_easy_bin \
    -i contig.fa \
    -b output.sorted.bam \
    --environment human_gut \
    --output semibin.out \
    -p4
```

Breaking it down:

0. `SemiBin2`: we are using the newer SemiBin2 interface
1. `single_easy_bin`: use the all in one pipeline for single sample binning
2. `-i contig.fa`: input FASTA file
3. `-b output.sorted.bam`: input BAM file
4. `--environment human_gut`: use the prebuilt model for the human gut
5. `--output semibin.out`: set the output directory
6. `-p4`: use 4 threads
```

## References

For [NGLess](https://ngless.embl.de):

> _NG-meta-profiler: fast processing of metagenomes using NGLess, a
> domain-specific language_ by Luis Pedro Coelho, Renato Alves, Paulo Monteiro,
> Jaime Huerta-Cepas, Ana Teresa Freitas, Peer Bork. Microbiome (2019)
> [https://doi.org/10.1186/s40168-019-0684-8](https://doi.org/10.1186/s40168-019-0684-8)

For [SemiBin](https://semibin.rtfd.io/):

> _A deep siamese neural network improves metagenome-assembled genomes in
> microbiome datasets across different environments_ by Shaojun Pan, Chengkai
> Zhu, Xing-Ming Zhao, and Luis Pedro Coelho. Nature Communications (2022)
> [https://doi.org/10.1038/s41467-022-29843-y](https://doi.org/10.1038/s41467-022-29843-y)

