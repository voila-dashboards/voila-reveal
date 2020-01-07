# voila-reveal

[![Join the Gitter Chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/QuantStack/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A reveal-based template for [Voilà](https://github.com/voila-dashboards/voila/).

## Installation

`voila-reveal` can be installed from PyPI

```
pip install voila-reveal
```

Or from conda-forge:

```
conda install -c conda-forge voila-reveal
```

## Usage

To use the `reveal` template, pass `--template=reveal` to the `voila` command line:

```
voila --template=reveal notebooks/reveal.ipynb
```

It is possible to overwrite resource defaults by passing additional options. For instance, the default value of transition is "fade". To get the "zoom" behaviour:

```
voila index.ipynb --template=reveal --VoilaConfiguration.resources="{'reveal': {'transition': 'zoom'}}"
```

To configure the template with a configuration file, create `conf.json` under `PREFIX/share/jupyter/voila/templates/reveal/` with the following content:

```json
{
  "traitlet_configuration": {
    "resources": {
      "reveal": {
        "scroll": false,
        "theme": "simple",
        "transition": "zoom"
      }
    }
  }
}
```

## License

We use a shared copyright model that enables all contributors to maintain the
copyright on their contributions.

This software is licensed under the BSD-3-Clause license. See the
[LICENSE](LICENSE) file for details.
