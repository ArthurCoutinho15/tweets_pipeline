import sys
sys.path.append('airflow_pipeline')

from datetime import datetime, timedelta
from operators.twitter_operator import TwitterOperator
from airflow.models import DAG
from airflow.utils.dates import days_ago
from os.path import join
    
with DAG(dag_id = "TwitterDAG", start_date=days_ago(2), schedule_interval="@daily") as dag:

    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
    query = "datascience"

    to = TwitterOperator(file_path=join("datalake/twitter_datascience",
                                        "extract_data={{ ds }}",
                                        "datascience_{{ ds_nodash }}.json"),
                                        query=query, 
                                        start_time="{{ data_interval_start.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}", 
                                        end_time="{{ data_interval_end.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}", 
                                        task_id="twitter_datascience")
    