# Examples of use of `miiid_schema`

This folder contains example data conforming to `miiid_schema`

The source for these is in [src/data](../src/data/examples)

```bash
cd miiid_schema
poetry shell
# if examples were ran previously
# rm -Rf examples/output
make test-examples
```

This would execute:

```bash
mkdir -p examples/output
poetry run linkml-run-examples \
	--output-formats json \
	--output-formats yaml \
	--counter-example-input-directory src/data/examples/invalid \
	--input-directory src/data/examples/valid \
	--output-directory examples/output \
	--schema src/miiid_schema/schema/miiid_schema.yaml > examples/output/README.md 
```
