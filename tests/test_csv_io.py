from io_utils.csv_util import CsvUtil
import pytest

csv_util = CsvUtil("")

headers = ['id', 'name', 'type', 'dimension']
filters_valid = ['dimension', 'name', 'type', 'id']
filters_invalid = ['dimension2', 'name2', 'type', 'id']

def test_valid_filters():
    csv_util._validate_columns(filters_valid, headers)

def test_invalid_filters():
    with pytest.raises(ValueError) as exception_info:
        csv_util._validate_columns(filters_invalid, headers)
    
    error_message = str(exception_info.value)
    assert 'dimension2' in error_message
    assert 'name2' in error_message
