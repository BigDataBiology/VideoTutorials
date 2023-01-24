#!/usr/bin/env bash

set -ev

if ! which git-annex; then
    echo "git-annex not found"
    exit 1
fi

echo "Retrieving GMGC10.data"

git clone https://git.embl.de/coelho/GMGC10.data.git
cd GMGC10.data
git-annex get GMBC10.meta.tsv # Genome bins
git-annex get metadata/GMGC10.sample.meta.tsv.gz # sample metadata
