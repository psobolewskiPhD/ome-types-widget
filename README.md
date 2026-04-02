# ome-types-widget

[![License](https://img.shields.io/github/license/imaging-formats/ome-types-widget)](LICENSE)
[![Version](https://img.shields.io/pypi/v/ome-types-widget.svg)](https://pypi.python.org/pypi/ome-types-widget)
[![CondaVersion](https://img.shields.io/conda/v/conda-forge/ome-types-widget)](https://anaconda.org/conda-forge/ome-types-widget)
[![Python
Version](https://img.shields.io/pypi/pyversions/ome-types-widget.svg)](https://python.org)
<!--
[![Tests](https://github.com/imaging-formats/ome-types-widget/workflows/tests/badge.svg)](https://github.com/imaging-formats/ome-types-widget/actions)
[![codecov](https://codecov.io/gh/imaging-formats/ome-types-widget/branch/main/graph/badge.svg?token=GocY9y8A32)](https://codecov.io/gh/imaging-formats/ome-types-widget)
-->
## A Qt widget that can show OME metadata using ome-types-widget

This widget was originally part of the [`ome-types`](https://github.com/imaging-formats/ome-types) package.
It can be used as a napari plugin or as astand-alone Qt widget.

## Installation

> [!IMPORTANT]
> **A Qt backend is required**  
>
> This package **does not** depend on _any specific Qt backend_, but _a backend_ **is required**.
> We recommend using `PyQt6`, but `PyQt5` or `PySide6` should also work.

### from PyPI

```shell
pip install ome-types-widget
```

### from conda-forge

```shell
conda install -c conda-forge ome-types-widget
```

### from GitHub (bleeding edge dev version)

```shell
pip install git+https://github.com/imaging-formats/ome-types-widget.git
```
