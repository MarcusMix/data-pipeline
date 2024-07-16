from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.email_operator import EmailOperator
from datetime import datetime
import os
import subprocess

data_execucao = datetime.now().date()

default_args = {
    'owner' : 'marcus',
    'start_date' : datetime(2024, 7, 9),
    'depends_on_past' : False,
    'email' : 'marcus.sandi@winker.com.br',
    'email_on_failure' : True
}

dag = DAG(
    'automation_scraping',
    default_args=default_args,
    description='Pipeline de dados que automatiza o processo de webscraping das lojas de aplicativos e abastece as planilhas necessárias',
    schedule_interval="0 10 * * 1",
    tags=['etl pipeline', 'data pipeline', 'seg 10h'],
    concurrency=1,
    max_active_runs=1 
)

def fetch_API_itunes():
    print("Executando a função *fetch_API_itunes*!")
    data_dir = "/opt/airflow/data/api_itunes"
    os.chdir(data_dir)
    print(f"Diretório atual: {os.getcwd()}")
    
    result = subprocess.run(
        ["python", "api_consumer_itunes.py"],
        capture_output=True,
        text=True
    )
    
    print(f"Return code: {result.returncode}")
    print(f"Standard output: {result.stdout}")
    print(f"Standard error: {result.stderr}")
    
    if result.returncode != 0:
        raise Exception(f"Erro ao executar o run_script_apple_API: {result.stderr}")
    
def fetch_webscraping_google_rating():
    print("Executando a função *fetch_webscraping_google_rating*!")
    data_dir = "/opt/airflow/data/webscraping/googlewebscraping/spiders"
    os.chdir(data_dir)
    print(f"Diretório atual: {os.getcwd()}")

    result = subprocess.run(
        ["scrapy", "crawl", "google_rating", "-o", f"../../../../data/google_rating_{data_execucao}.csv"],
        capture_output=True,
        text=True
    )

    print(f"Return code: {result.returncode}")
    print(f"Standard output: {result.stdout}")
    print(f"Standard error: {result.stderr}")

    if result.returncode != 0:
        raise Exception(f"Erro ao executar o fetch_webscraping_google_rating: {result.stderr}")

def fetch_webscraping_google_star():
    print("Executando a função *fetch_webscraping_google_star*!")
    data_dir = "/opt/airflow/data/webscraping/googlewebscraping/spiders"
    os.chdir(data_dir)
    print(f"Diretório atual: {os.getcwd()}")

    result = subprocess.run(
        ["scrapy", "crawl", "google_star", "-o", f"../../../../data/google_star_{data_execucao}.csv"],
        capture_output=True,
        text=True
    )

    print(f"Return code: {result.returncode}")
    print(f"Standard output: {result.stdout}")
    print(f"Standard error: {result.stderr}")

    if result.returncode != 0:
        raise Exception(f"Erro ao executar o fetch_webscraping_google_star: {result.stderr}")

def fetch_webscraping_apple_star():
    print("Executando a função *fetch_webscraping_apple_star*!")
    data_dir = "/opt/airflow/data/webscraping/googlewebscraping/spiders"
    os.chdir(data_dir)
    print(f"Diretório atual: {os.getcwd()}")

    result = subprocess.run(
        ["scrapy", "crawl", "apple_star", "-o", f"../../../../data/apple_star_{data_execucao}.csv"],
        capture_output=True,
        text=True
    )

    print(f"Return code: {result.returncode}")
    print(f"Standard output: {result.stdout}")
    print(f"Standard error: {result.stderr}")

    if result.returncode != 0:
        raise Exception(f"Erro ao executar o fetch_webscraping_apple_star: {result.stderr}")

check_api = HttpSensor(
    task_id="check_api",
    http_conn_id="API_ITUNES",
    endpoint="/id=1121080703/sortby=mostrecent/json?cc=br",
    poke_interval=5,
    timeout=20,
    dag=dag
)

task_apple_comments = PythonOperator(
    task_id="task_apple_comments",
    python_callable=fetch_API_itunes,
    dag=dag
)

task_google_rating = PythonOperator(
    task_id="task_google_rating",
    python_callable=fetch_webscraping_google_rating,
    dag=dag
)

task_google_star = PythonOperator(
    task_id="task_google_star",
    python_callable=fetch_webscraping_google_star,
    dag=dag
)

task_apple_star = PythonOperator(
    task_id="task_apple_star",
    python_callable=fetch_webscraping_apple_star,
    dag=dag
)

send_email_on_start = EmailOperator(
    task_id='send_email_on_start',
    to=['marcus.sandi@winker.com.br', 'junior.freitas@winker.com.br'],
    subject='DAG automation_scraping has started',
    html_content='<p>The DAG <b>automation_scraping</b> has started successfully.</p>',
    dag=dag,
)

send_email_on_start >> check_api >> task_apple_comments >> task_google_rating >> task_google_star >> task_apple_star