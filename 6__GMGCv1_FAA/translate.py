from Bio import SeqIO
import gzip

with open('GMGC10.dog-gut.95nr.no-rare.faa.gz', 'wt') \
        as out:
    for s in SeqIO.parse(
                    gzip.open('./GMGC10.dog-gut.95nr.no-rare.fna.gz', 'rt'),
                    format='fasta'):
        sa = s.translate()
        out.write(f'>{s.id}\n{sa.seq}\n')
