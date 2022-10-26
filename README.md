
# Scopes Packaging

## Package Metadata File

A Scopes package contains a metadata file `scopes-pkg.slon` that
provides a human and machine readable description of the package at a
high level.

The file itself is written in [Scopes List
Notation](https://scopes.readthedocs.io/en/latest/dataformat/) (SLN),
which is what Scopes itself is written in and is most similar to
S-Expressions from Lisps.

Herein, we currently recognize the file extension `.slon` (Scopes List
Optimized Notation) to disambiguate against the other relatively
common `.sln` extensions. However, this should be subject to change as
of now.

There is a codified schema for the file format to allow for
validation, since there is no, and likely/hopefully will never, be a
Scopes language specific package manager that serves as a de facto
schema reference.

This is written as a [JSON Schema](http://json-schema.org/) in the
file `schemas/json-schemas/scopes-pkg.schema.json`.

An example of this file can be found in
`examples/wumpus/scopes-pkg.slon`.

As an example of an external tool parsing this format check out the
[python-sln](https://github.com/salotz/python-sln) Python library &
CLI.

It can be used to dump SLN files
