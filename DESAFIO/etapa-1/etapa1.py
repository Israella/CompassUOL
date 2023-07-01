import boto3
import os
from datetime import datetime

aws_access_key_id = 'AKIA5DRNIVCFBDOHOFFZ'
aws_secret_access_key = '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'
aws_region = 'us-east-1'

bucket_name = 'data-lake-israella'

s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=aws_region)

current_date = datetime.now().strftime('%Y/%m/%d')

data_to_upload = [
    {
        'local_path': os.path.join('filmes.csv'),
        's3_key': f'Raw/Local/CSV/Movies/{current_date}/filmes.csv'
    },
    {
        'local_path': os.path.join('series.csv'),
        's3_key': f'Raw/Local/CSV/Series/{current_date}/series.csv'
    }
]

for data in data_to_upload:
    local_path = data['local_path']
    s3_key = data['s3_key']

    s3_client.upload_file(local_path, bucket_name, s3_key)

    print(f'Arquivo {local_path} enviado para o bucket {bucket_name} com sucesso! Caminho no S3: {s3_key}')