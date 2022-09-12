from pathlib import Path

input_path = r'C:\Users\emenshikova\Desktop\Trash'
if __name__ == '__main__':
   path_list = Path(input_path).glob('*.txt')  # create list of txt files
   result_list = []
   for path in path_list:
      path_number = path.stem.split('_')[0]
      result_list.append(f'frames_{path_number}')
      for frame in path.read_text().split('\n'):
         result_list.extend(Path(frame).stem)
   print(result_list)
   output_path = Path('result.txt')
   output_path.write_text('\n'.join(result_list))