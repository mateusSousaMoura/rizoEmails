import pandas as pd
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()

contactFilePath = BASE_DIR /'contatos.xlsx'
input_file_path = BASE_DIR / "input.txt"

df = pd.read_excel(contactFilePath)

with open(input_file_path,'w') as f:
    for index, row in df.iterrows():
        f.write(f"{row.to_string(index=False)}\n")
to = []
with open(input_file_path, "r") as file:
    to = [line.strip() for line in file.readlines()]

print(to)

#print(df)