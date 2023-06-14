# miiid-schema

Towards a Minimal Information about Intermicrobial Interaction Data schema

## Website

[https://FAIR-MI.github.io/miiid-schema](https://FAIR-MI.github.io/miiid-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [miiid_schema](src/miiid_schema)
    * [schema](src/miiid_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/miiid_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
