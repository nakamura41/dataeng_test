from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import pandas as pd

args = {"owner": "airflow"}

with DAG(
    dag_id="etl_job",
    default_args=args,
    schedule_interval="0 13 * * *",
    start_date=days_ago(2),
    tags=["etl"],
) as dag:
    # [START howto_operator_bash]

    def process_data(df: pd.DataFrame) -> pd.DataFrame:
        df = df[(df["name"].notna())]
        df["price"] = df["price"].astype("float64")
        df["name"] = df["name"].str.split(" ")
        df["first_name"] = df["name"].str[0]
        df["last_name"] = df["name"].str[1]
        df["above_100"] = df["price"] > 100
        del df["name"]
        return df[["first_name", "last_name", "price", "above_100"]]

    def process_data_files():
        dfs = []
        airflow_base_folder = "/opt/airflow/dags"

        df = pd.read_csv(f"{airflow_base_folder}/data/dataset1.csv", encoding="utf-8")
        df = process_data(df)
        dfs.append(df)

        df = pd.read_csv(f"{airflow_base_folder}/data/dataset2.csv", encoding="utf-8")
        df = process_data(df)
        dfs.append(df)

        final_df = pd.concat(dfs).reset_index(drop=True)
        print(final_df)

        s3_output_path = f"{airflow_base_folder}/data/output.csv"
        print(f"Write output to {s3_output_path}")
        final_df.to_csv(s3_output_path, index=False, encoding="utf-8")

    run_this = PythonOperator(task_id="task1", python_callable=process_data_files)
