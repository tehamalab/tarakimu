import pytest


@pytest.fixture(scope="module")
def numwords():
    return {
        'sw': {
            '88': 'themanini na nane',
            '-88': 'hasi themanini na nane',
            '1001.1': 'elfu moja na moja nukta moja',
            100: 'mia moja',
            4000000000: 'bilioni nne',
            1111111111111111111111111111111111: (
                'desilioni moja, nonilioni mia moja na kumi na moja, '
                'oktilioni mia moja na kumi na moja, septilioni mia moja na '
                'kumi na moja, seksitilioni mia moja na kumi na moja, '
                'kuintilioni mia moja na kumi na moja, kuadrilioni mia moja '
                'na kumi na moja, trilioni mia moja na kumi na moja, bilioni '
                'mia moja na kumi na moja, milioni mia moja na kumi na moja, '
                'mia moja na kumi na moja elfu, mia moja na kumi na moja')
        },
        'en': {
            '88': 'eighty eight',
            '-88': 'negative eighty eight',
            '1001.1': 'one thousand and one point one',
            100: 'one hundred',
            2012: 'two thousand and twelve',
            100103: 'one hundred thousand, one hundred and three',
            3000000000: 'three billion'
        }
    }


@pytest.fixture(scope="module")
def invalid_nums():
    return ['88a', '108,000']
