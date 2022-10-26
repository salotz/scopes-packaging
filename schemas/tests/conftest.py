from pathlib import Path
import json
import shutil as sh

import pytest

CURDIR = Path('.')

TESTS_DIR = CURDIR / 'tests'
DUMP_DIR = TESTS_DIR / '_dump'
DATA_DIR = TESTS_DIR / 'data'

SLN_DATA_DIR = DATA_DIR / 'sln'
SCOPES_PKG_DATA_DIR = DATA_DIR / 'scopes_pkg'


SLN_SUFFIX = '.slon'

JSON_SCHEMAS_DIR = CURDIR / 'json-schemas'

SCHEMA_FILENAME_SUFFIX = '.schema.json'

@pytest.fixture
def common_paths():
    return {
        'curdir' : CURDIR,
        'tests_dir' : TESTS_DIR,
        'data_dir' : DATA_DIR,
        'sln_suffix' : SLN_SUFFIX,
        'json_schemas_dir' : JSON_SCHEMAS_DIR,
        'sln_data_dir' : SLN_DATA_DIR,
        'scopes_pkg_data_dir' : SCOPES_PKG_DATA_DIR
    }

@pytest.fixture
def sln_json_schema():
    return json.loads(
        (JSON_SCHEMAS_DIR / f'sln{SCHEMA_FILENAME_SUFFIX}'
         ).read_text(
         ).strip()
    )

@pytest.fixture
def scopes_pkg_json_schema():
    return json.loads(
        (JSON_SCHEMAS_DIR / f'scopes-pkg{SCHEMA_FILENAME_SUFFIX}'
         ).read_text(
         ).strip()
    )

@pytest.fixture(scope='session')
def dump_dir():
    sh.rmtree(DUMP_DIR, ignore_errors=True)
    DUMP_DIR.mkdir(parents=True, exist_ok=True)
    return DUMP_DIR
