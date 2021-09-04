import pandas as pd


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['name'].notna()]
    df['name'] = df['name'].str.split(' ')
    df['first_name'] = df['name'].str[0]
    df['last_name'] = df['name'].str[1]
    df['above_100'] = df['price'] > 100
    del df['name']
    return df[['first_name', 'last_name', 'price', 'above_100']]


if __name__ == '__main__':
    df = pd.read_csv("data/dataset1.csv", encoding="utf-8")
    df = process_data(df)
    print(df)
