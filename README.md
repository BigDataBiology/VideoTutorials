# BDB-Lab Video Tutorials

This is a support repository for our video tutorials, which you can find on our [YouTube channel](https://youtube.com/@BigDataBiology).

## 0. How to install software with mamba

Almost all our tutorials start by installing software with `mamba`

[[More information](tree/main/0__HowToInstallSoftwareWithMamba)]

## 1. NGLess/SemiBin

Shows how to use [NGLess](https://ngless.embl.de) and [SemiBin](https://semibin.rtfd.io/) to build MAGs from a metagenome.

Available in 4 languages.

[[More information](tree/main/1__NGLessSemiBin)]

## 2. GMGCv1 MAGs

How to retrieve MAGs from the [GMGCv1](https://gmgc.embl.de) (Global Microbial Gene Catalog, version 1) dataset.

[[More information](tree/main/2__GMGCv1MAGs)]

## 3. Macrel

How to run [macrel](https://macrel.readthedocs.io/en/latest/) on a metagenome.

[[More information](tree/main/3__Macrel)]

## 4. Metagenomics tutorial using NGLess & SemiBin (multiple samples)

Shows how to use [NGLess](https://ngless.embl.de) and
[SemiBin](https://semibin.rtfd.io/) to build MAGs using multiple metagenomes.
This likely makes the most sense if you've seen the first tutorial.

[[More information](tree/main/4__NGLessSemiBinMultiple)]

## 5. Selecting interesting rows from a very large file with Pandas

Motivated by a subscriber question about GMGCv1, this is actually a general
question about using pandas and Python to deal with very huge tables.

[[More information](tree/main/5__SelectGMGCAbundances)]

### 6. How to obtain amino acids version of GMGCv1 subcatalogs

Another subscriber question about GMGCv1, namely how to get amino acid versions
of the subcatalogs. We only provide nucleotide versions for disk space reasons,
but it's pretty easy to generate amino acid ones and here we show how.

[[More information](tree/main/6__GMGCv1_FAA)]

### 7. How to eggnog-mapper annotations for genes in the GMGC

All the unigenes in GMGCv1 come with [eggnog-mapper](https://eggnog-mapper.embl.de/) annotations. Here, we show how to retrieve them.

[[More information](tree/main/7__GMGCv1_Emapper)]
