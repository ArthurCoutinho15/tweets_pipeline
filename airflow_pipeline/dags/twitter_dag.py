import sys
sys.path.append('airflow_pipeline')

from operators.twitter_operator import TwitterOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.models import DAG
from airflow.utils.dates import days_ago
from os.path import join
from pathlib import Path
    
with DAG(dag_id = "TwitterDAG", start_date=days_ago(2), schedule_interval="@daily") as dag:
    BASEFOLDER = join(
        str(Path('~/home').expanduser()),
        "pipeline_tweets/datalake/{stage}/twitter_datascience/{partition}"
    )
    PARTITION_FOLDER_EXTRACT = "extract_date={{ data_interval_start.strftime('%Y-%m-%d') }}"
    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
    query = "datascience"
    
    twitter_operator = TwitterOperator(file_path=join(BASEFOLDER.format(stage='bronze', partition=PARTITION_FOLDER_EXTRACT),
                                        "datascience_{{ ds_nodash }}.json"),
                                        query=query, 
                                        start_time="{{ data_interval_start.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}", 
                                        end_time="{{ data_interval_end.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}", 
                                        task_id="twitter_datascience")
    
    twitter_transform = SparkSubmitOperator(task_id="transform_twitter_datascience",
                                            application="/home/arthur/pipeline_tweets/src/spark/transformation.py",
                                            name="twitter_transformation",
                                            application_args=["--src", BASEFOLDER.format(stage='bronze', partition=PARTITION_FOLDER_EXTRACT), 
                                                              "--dest", BASEFOLDER.format(stage='silver', partition=""),
                                                              "--process_date", "{{ ds }}"])
    
    twitter_operator >> twitter_transform
    