# Examples of use of miiid_schema

This folder contains example data conforming to miiid_schema

The source for these is in [src/data](../src/data/examples)

```
cd miiid_schema
poetry shell
# Convert the example to a table
linkml-convert -o example.tsv -s src/miiid_schema/schema/miiid_schema.yaml IntermicrobialInteraction-001.yaml 
```

```
id	participants	evidence_type	reference
example:IntermicrobialInteraction001	[{'name': 'Acidobacteria', 'tax_id': 57723}|{'name': 'Gammaproteobacteria', 'tax_id': 1236}]	high throughput evidence used in automatic assertion	https://doi.org/10.1038/ismej.2011.119
```
