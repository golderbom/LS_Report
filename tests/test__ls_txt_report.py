from pathlib import Path

import pytest

from config_ls_model import Model
from ls_txt_report import prepare_label_studio_txt_report


@pytest.mark.parametrize(
    'input_config, expected_output_file', (
            (r'test_config_ls.json', r'tests_data\output\sample_result.txt'),
    )
)
def test__ls_report(input_config: str, expected_output_file: str):
    config = Model.parse_file(input_config)
    assert prepare_label_studio_txt_report(config) == Path(expected_output_file).read_text().split('\n')
