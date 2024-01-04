# argNorm Tutorial

Video: https://youtu.be/vx8MCQ7gDLs

**argNorm is a tool to normalize antibiotic resistance genes (ARGs) by mapping them to the
[antibiotic resistance ontology (ARO)](https://obofoundry.org/ontology/aro.html) by CARD. It also provides drug categorization of drugs that antibiotic resistance genes confer resistance to.**

## Installation

```bash
pip install argnorm
```

## Help command

```bash
argnorm -h
```
or
```bash
argnorm --help
```

## Example Use Cases

### ARGs-OAP

```bash
# hamronized reads file
argnorm argsoap --mode reads -i examples\hamronized\args-oap.sarg.reads.tsv -o args-oap.sarg.reads.hamronized.normalized.tsv --hamronized
```

```bash
# raw reads file
argnorm argsoap --mode reads -i examples\raw\args-oap.sarg.reads.tsv -o args-oap.sarg.reads.raw.normalized.tsv
```

### ABRicate

```bash
# hamronized resfinder file
argnorm abricate --db resfinder -i examples\hamronized\abricate.resfinder.tsv -o abricate.resfinder.hamronized.normalized.tsv --hamronized
```

```bash
# hamronized megares file
argnorm abricate --db megares -i examples\hamronized\abricate.megares.tsv -o abricate.megares.hamronized.normalized.tsv --hamronized
```

```bash
# raw argannot file
argnorm abricate --db argannot -i examples\raw\abricate.argannot.tsv -o abricate.argannot.raw.normalized.tsv
```

### Resfinder
```bash
# raw resfinder orfs file
argnorm resfinder -i examples\raw\resfinder.resfinder.orfs.tsv -o resfinder.resfinder.raw.normalized.tsv
```

## References

argNorm: https://github.com/BigDataBiology/argNorm

EMBARK: https://antimicrobialresistance.eu/mission/

[CARD](https://card.mcmaster.ca/):
> Alcock, B., Huynh, W., Chalil, R., Smith, K. W., Raphenya, A. R., Wlodarski, M. A., Edalatmand, A., Petkau, A.,
Syed, S. A., Tsang, K. K., Baker, S. J. C., Dave, M., McCarthy, M. C., Mukiri, K. M., Nasir, J. A., Golbon, B., Imtiaz,
H., Jiang, X., Kaur, K., . . . McArthur, A. G. (2022). CARD 2023: expanded curation, support for machine learning, and
resistome prediction at the Comprehensive Antibiotic Resistance Database.
Nucleic Acids Research, 51(D1), D690–D699. https://doi.org/10.1093/nar/gkac920