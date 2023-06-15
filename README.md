# miiid-schema

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

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

The metadata schema is based on the metadata suggested in Pacheco, A. R., Pauvert, C., Kishore, D., & Segrè, D. (2022). Toward FAIR Representations of Microbial Interactions. *MSystems, 7*(5). <https://doi.org/10.1128/msystems.00659-22>.
The schema is implemented using [LinkML](https://linkml.io) and the [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
