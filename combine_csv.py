import pandas as pd
import os

"""
Script to combine multiple csv files into single .xlsx file
"""

base_folder = os.path.abspath(os.path.dirname(__file__))
folder_name = input("Enter directory name to process: ")
full_path = os.path.join(base_folder, folder_name)

print(f'processing the contents of {full_path} ...')
file_names = os.listdir(full_path)
out_name = 'combined.xlsx'
out_file = os.path.join(full_path, out_name)
writer = pd.ExcelWriter(out_file)
for file_name in file_names:
    try:
        data_file = os.path.join(full_path, file_name)
        df = pd.read_csv(data_file, header=None)
        print(f'dumping the content of {file_name}')
        df.to_excel(writer, sheet_name = file_name[:-4])
    except:
        continue
writer.save()