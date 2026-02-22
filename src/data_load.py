import pandas as pd
import os

def load_nuclear_data(file_path):
    if not os.path.exists(file_path):
        print(f"Помилка: Файл {file_path} не знайдено.")
        return None

    df = pd.read_excel(file_path)

    numeric_cols = df.columns.drop(['year', 'quarter', 'station'])

    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(',', '.').str.strip()
        df.loc[df[col].str.contains('<', na=False), col] = '0'
        df[col] = pd.to_numeric(df[col], errors='coerce')

    #print(f"Дані успішно завантажені. Розмірність: {df.shape}")
    return df


if __name__ == "__main__":
    DATA_PATH = "../data/raw/nuclear_safety.xlsx"
    data = load_nuclear_data(DATA_PATH)
