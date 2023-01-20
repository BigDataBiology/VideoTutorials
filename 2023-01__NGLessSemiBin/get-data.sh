#!/usr/bin/env bash

set -ev

echo "Retrieving data and placing it in data/ directory"
mkdir -p data
cd data

wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR478/ERR478958/ERR478958_1.fastq.gz
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR478/ERR478958/ERR478958_2.fastq.gz
