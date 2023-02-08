# Metagenomics tutorial using NGLess & SemiBin (multiple samples)

## Videos

- Full playlist: https://www.youtube.com/playlist?list=PLn-ZqA9cHNdSsmVTojYL1lEcfh-J3Hdff

1. [Assembly with NGLess (single sample)](https://youtu.be/EIkmZ8kN6j0)
2. [Binning with SemiBin (single sample)](https://youtu.be/W5_-tjUWbCY)
3. [Assembly with NGLess (multiple samples)](https://youtu.be/b6l48ETb-6k)
4. [Binning with SemiBin (multiple samples)](https://youtu.be/-77jy-ShEVk)

## Scripts

Full script:

Unlike in the video, we create a single conda environment with both [NGLess](https://ngless.embl.de) and [SemiBin](https://semibin.rtfd.io/).

```bash

# Get the data
bash get-data.sh

# Create conda environment:

mamba create -n metagenomics_tutorial python=3.9
conda activate metagenomics_tutorial
mamba install -c conda-forge -c bioconda ngless SemiBin

# Run NGLess 3 times
ngless -j8 process.ngl
ngless -j8 process.ngl
ngless -j8 process.ngl

SemiBin concatenate_fasta  -i *fa -o semibin.out.multi

# Map to the concatenated FASTA

ngless -j8 map-to-concatenated.ngl

# Run SemiBin2
SemiBin2 multi_ -i contig.fa -b output.sorted.bam --environment human_gut -p4 --output semibin.out
SemiBin2 multi_easy_bin \
    -i semibin.out.multi/concatenated.fa \
    -b concat_output_SAMEA481789* \
    -o semibin.out.multi

```

Note that running everything may take many hours if you are running on a single computer.

## Step -1: Get data

You can run `get-data.sh` command to retrieve the data, which will be put into
a directory called `data.multi/` with subdirectories per sample:

```bash
bash get-data.sh
```

Let's just make sure that things look okay:

```bash
find data.multi/
data.multi/
data.multi/SAMEA4817893
data.multi/SAMEA4817893/ERR2726404_1.fastq.gz
data.multi/SAMEA4817893/ERR2726404_2.fastq.gz
data.multi/SAMEA4817894
data.multi/SAMEA4817894/ERR2726405_1.fastq.gz
data.multi/SAMEA4817894/ERR2726405_2.fastq.gz
data.multi/SAMEA4817895
data.multi/SAMEA4817895/ERR2726406_1.fastq.gz
data.multi/SAMEA4817895/ERR2726406_2.fastq.gz
```

## Step 0: Create conda environment


You can use [conda](https://docs.conda.io/) or its faster replacement,
[mamba](https://mamba.readthedocs.io/) to install NGLess and SemiBin (on Linux
or Mac OS X):

```bash
mamba create -n metagenomics_tutorial python=3.9
conda activate metagenomics_tutorial
mamba install -c conda-forge -c bioconda ngless SemiBin
```

## Step 1: Run NGLess

We adapted the file `process.ngl` from the first tutorial to use the data structure that is inside the `samples.yaml` file.

Because there are three samples, you need to run it 3 times!

## Step 2: Create a the concatenated FASTA file

```bash
SemiBin2 concatenate_fasta  -i *fa -o semibin.out.multi
```

### Step 3: Map to the concatenated FASTA

```bash
ngless -j8 map-to-concatenated.ngl
```

### Step 4: Run multi step binning

```bash
SemiBin2 multi_easy_bin \
    -i semibin.out.multi/concatenated.fa \
    -b concat_output_SAMEA481789* \
    -p4 \
    --output semibin.out.multi
```

Breaking it down:

0. `SemiBin2`: we are using the newer SemiBin2 interface
1. `multi_easy_bin`: use the all in one pipeline for single sample binning
2. `-i semibin.out.multi/concatenated.fa`: input FASTA file
3. `-b concat_output_SAMEA481789*`: input BAM file
4. `--output semibin.out.multi`: set the output directory
5. `-p4`: use 4 threads

Note that unlinke the case for the single sample, we cannot use a pretrained model and a new model will be trained. This will be slow, but result in better bins.

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

