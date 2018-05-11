import pytest


@pytest.fixture(scope="module")
def numwords():
    return {
        '88': 'themanini na nane',
        '-88': 'hasi themanini na nane',
        '1001.1': 'elfu moja na moja nukta moja',
        100: 'mia moja'
    }


@pytest.fixture(scope="module")
def invalid_nums():
    return ['88a', '108,000']
