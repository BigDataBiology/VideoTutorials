# Metagenomics tutorial

Do everything at once

```bash

# Get the data
bash get-data.sh

# Run NGLess
ngless -j8 process.ngl

# Run SemiBin2
SemiBin2 single_easy_bin -i contig.fa -b output.sorted.bam --environment human_gut -p4 --output semibin.out

```

## Step 0: Get Data

You can run `get-data.sh` command to retrieve the data, which will be put into a directory called `data/`

## Step 1: Run NGLess

The file `process.ngl` is used to process the data.
