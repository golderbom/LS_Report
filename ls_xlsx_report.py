from pathlib import Path

import pandas as pd

from config_ls_model import Model
from ls_common_report import get_frame_dict


def prepare_label_studio_xlsx_report(config: Model):
    frame_dict = get_frame_dict(config)

    # convert dict to pd.DataFrame for unequal column length:https://stackoverflow.com/a/43866426
    df = pd.DataFrame.from_dict(frame_dict, orient='index').T
    df.to_excel(config.target_file_path.with_suffix('.xlsx'), index=False)
    return frame_dict


if __name__ == '__main__':
    config_work = Model.parse_file("config_ls_xlsx.json")
    filenames = prepare_label_studio_xlsx_report(config_work)
    print(filenames)