from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tempfile

data_execucao = datetime.now().date()

CREDENTIALS_FILE = '/opt/airflow/plugins/credentials.json'

default_args = {
    'owner' : 'marcus',
    'start_date' : datetime(2024, 7, 10),
    'depends_on_past' : False,
    'email' : ['marcus.sandi@winker.com.br'],
    'email_on_failure' : True
}

dag = DAG(
    'etl_data_batch',
    default_args=default_args,
    description="Pipeline ETL dos dados derivados da dag *automation_scraping*",
    schedule_interval="0 11 * * 1",
    tags=['etl pipeline', 'data pipeline', 'seg 11h'],
    default_view='graph',
    concurrency=1,
    max_active_runs=1
)

def read_csv_file_apple_comments():
    df = pd.read_csv(f"/opt/airflow/data/api_itunes/comentarios_{data_execucao}.csv", sep=";")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp_file.name, index=False)
    return temp_file.name

def read_csv_file_google_rating():
    df = pd.read_csv(f"/opt/airflow/data/google_rating_{data_execucao}.csv", sep=",")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp_file.name, index=False)
    return temp_file.name

def read_csv_file_google_star():
    df = pd.read_csv(f"/opt/airflow/data/google_star_{data_execucao}.csv", sep=",")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp_file.name, index=False)
    return temp_file.name

def read_csv_file_apple_star():
    df = pd.read_csv(f"/opt/airflow/data/apple_star_{data_execucao}.csv", sep=",")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp_file.name, index=False)
    return temp_file

def append_to_google_sheets(file_path, spreedsheet_name, worksheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    sheet = client.open(spreedsheet_name).worksheet(worksheet_name)
    
    df = pd.read_csv(file_path)
    df = df.fillna('') 

    data = df.values.tolist()

    # útilma linha da coluna A
    last_row = len(sheet.col_values(1)) + 1

    chunk_size = max(1, len(data) // 5) 

    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    for chunk in chunks:
        sheet.append_rows(chunk, value_input_option="RAW", table_range=f"A{last_row}")
        last_row += len(chunk)


def etl_data_apple_comments():
    print("Executando a função *etl_data_apple_comments*!")
    df = read_csv_file_apple_comments()
    append_to_google_sheets(df, "comentarios_apple_google", "apple")

def etl_data_google_rating():
    print("Executando a função *etl_data_google_rating*!")
    df = read_csv_file_google_rating()
    append_to_google_sheets(df, "comentarios_apple_google", "google")

def etl_data_google_star():
    print("Executando a função *etl_data_google_star*!")
    df = read_csv_file_google_star()
    append_to_google_sheets(df, "notas_downloads_apple_google", "google")

def etl_data_apple_star():
    print("Executando a função *etl_data_apple_star*!")
    df = read_csv_file_apple_star()
    append_to_google_sheets(df, "notas_downloads_apple_google", "apple")

task_apple_comments_etl = PythonOperator(
    task_id="task_apple_comments_etl",
    python_callable=etl_data_apple_comments,
    dag=dag
)

task_google_comments_etl = PythonOperator(
    task_id="task_google_comments_etl",
    python_callable=etl_data_google_rating,
    dag=dag
)

task_google_star_etl = PythonOperator(
    task_id="task_google_star_etl",
    python_callable=etl_data_google_star,
    dag=dag
)

task_apple_star_etl = PythonOperator(
    task_id="task_apple_star_etl",
    python_callable=etl_data_apple_star,
    dag=dag
)

send_email_on_start = EmailOperator(
    task_id='send_email_on_start',
    to=['marcus.sandi@winker.com.br', 'junior.freitas@winker.com.br'],
    subject='DAG etl_data_batch has started',
    html_content='<p>The DAG <b>etl_data_batch</b> has started successfully.</p>',
    dag=dag,
)

send_email_on_start >> task_apple_comments_etl >> task_google_comments_etl >> task_google_star_etl >> task_apple_star_etl 