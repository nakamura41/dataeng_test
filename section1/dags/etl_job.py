from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow'
}

with DAG(
        dag_id='etl_job',
        default_args=args,
        schedule_interval=None,
        start_date=days_ago(2),
        tags=['etl']
) as dag:
    pass
