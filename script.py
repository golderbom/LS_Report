from pathlib import Path

from config_ls_model import Model


def ls_report(config):
    path_list = config.sourse_path.glob('*.txt')  # create list of txt files
    result_list = []
    for path in path_list:
        path_number = path.stem.split('_')[0]
        result_list.append(f'frames_{path_number}')
        for frame in path.read_text().split('\n'):
            result_list.extend(Path(frame).stem)
    print(result_list)
    output_path = Path('result.txt')
    output_path.write_text('\n'.join(result_list))


if __name__ == '__main__':
    config = Model.parse_file("config_ls.json")
    ls_report(config)