from pathlib import Path

import pandas as pd

from config_ls_model import Model


def ls_xlsx_report(config):
    path_list = config.source_path.glob('*.txt')  # create list of txt files
    result = {}
    for path in path_list:
        path_number = path.stem.split('_')[0]
        temp = []
        for frame in path.read_text().split('\n'):
            temp.append(Path(frame).stem)
        result[path_number] = temp
    print(result)

    # df = pd.DataFrame.from_dict(result)
    # convert dict to pd.DataFrame for unequal column length:https://stackoverflow.com/a/43866426
    df = pd.DataFrame.from_dict(result, orient='index').T
    df.to_excel(config.target_path.with_suffix('.xlsx'), index=False)

    # output_path = Path(config.target_path)
    # output_path.write_text('\n'.join(result))
if __name__ == '__main__':
    config = Model.parse_file("config_ls.json")
    ls_xlsx_report(config)