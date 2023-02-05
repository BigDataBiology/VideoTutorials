#!/usr/bin/env bash

set -ev

mkdir -p data.multi
cd data.multi/

mkdir SAMEA4817893	
cd SAMEA4817893	
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR272/004/ERR2726404/ERR2726404_1.fastq.gz
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR272/004/ERR2726404/ERR2726404_2.fastq.gz
cd ..

mkdir SAMEA4817894	
cd SAMEA4817894	
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR272/005/ERR2726405/ERR2726405_1.fastq.gz
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR272/005/ERR2726405/ERR2726405_2.fastq.gz
cd ..

mkdir SAMEA4817895	
cd SAMEA4817895	
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR272/006/ERR2726406/ERR2726406_1.fastq.gz
wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR272/006/ERR2726406/ERR2726406_2.fastq.gz
cd ..

