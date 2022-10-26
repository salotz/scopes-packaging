import json

import pytest

import jsonschema

from sln.json import parse_to_json

def test_examples(
        common_paths,
        dump_dir,
        sln_json_schema,
):

    # load the examples from the data folder
    instances = {}
    for instance_path in [path
                         for path
                         in common_paths['sln_data_dir'].iterdir()
                         if (not path.is_dir() and
                             path.suffix == '.slon')
                         ]:

        instance_name = instance_path.stem

        instances[instance_name] = instance_path.read_text()

    sln_dump_dir = dump_dir / 'sln'

    sln_dump_dir.mkdir(parents=True)


    # then generate the json version
    instance_jsons = {}
    for name, sln_text in instances.items():

        instance_jsons[name] = parse_to_json(sln_text)

        # then dump them for debugging
        (sln_dump_dir / f"{name}.json").write_text(
            instance_jsons[name]
        )

    # then check these against the schema
    for name, json_text in instance_jsons.items():

        # load the data into a python object "instance"
        instance = json.loads(json_text)

        assert jsonschema.validate(instance, sln_json_schema) is None
