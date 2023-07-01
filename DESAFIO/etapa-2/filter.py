import pandas as pd
import json
import requests
import boto3
from datetime import datetime
import time

API_KEY = 'bbcc8408d943c83e88693080f4943110'  # Enter your API key here
AWS_ACCESS_KEY_ID = 'AKIA5DRNIVCFBDOHOFFZ'  # Enter your AWS access key ID here
AWS_SECRET_ACCESS_KEY = 'FZPZspux4SYM++kL2dtRoUi4f2rvva/GUFyh1mDX'  # Enter your AWS secret access key here
BUCKET_NAME = 'data-lake-israella'
STORAGE_LAYER = 'Raw'
DATA_SOURCE = 'TMDB'
DATA_FORMAT = 'JSON'
CHUNK_SIZE = 100

def get_movie_popularity(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        popularity = data['popularity']
        return popularity

    time.sleep(0.02)
    return None

def save_popularity_to_s3(data, bucket, key):
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name='us-east-1')

    # Transform the data dictionary into a list of dictionaries with desired key-value pairs
    transformed_data = [{"id": movie_id, "popularidade": popularity} for movie_id, popularity in data.items()]

    json_data = json.dumps(transformed_data, ensure_ascii=False)
    s3.put_object(Body=json_data, Bucket=bucket, Key=key)

def lambda_handler(event, context):
    current_date = datetime.now().strftime('%Y/%m/%d')
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name='us-east-1')

    # Read CSV data from S3
    key = 'Raw/Local/CSV/Movies/2023/06/22/filmes.csv'
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    selected_columns = ['id', 'genero']
    df = pd.read_csv(response['Body'], delimiter='|', usecols=selected_columns, dtype={'id': str})

    # Filter movies by genre
    genre_principal = ['Horror']
    filtered_df = df[df['genero'].isin(genre_principal)]
    unique_movie_ids = filtered_df['id'].unique()
    filtered_df = pd.DataFrame(unique_movie_ids, columns=['id'])
    filtered_df.reset_index(drop=True, inplace=True)

    df_chunks = [filtered_df[i:i + CHUNK_SIZE] for i in range(0, filtered_df.shape[0], CHUNK_SIZE)]
    num_lotes = len(df_chunks)

    for i in range(num_lotes):
        popularity_data = {}

        chunk = df_chunks[i]

        for _, row in chunk.iterrows():
            movie_id = row['id']
            popularity = get_movie_popularity(movie_id)

            if popularity is not None:
                popularity_data[movie_id] = popularity

        # Store popularity data in S3
        data_specification_popularity = 'Popularidade'
        file_name_popularity = f'{data_specification_popularity}_{str(i).zfill(3)}.json'
        save_popularity_to_s3(popularity_data, BUCKET_NAME,
                               f'{STORAGE_LAYER}/{DATA_SOURCE}/{DATA_FORMAT}/{current_date}/{data_specification_popularity}/{file_name_popularity}')

    return {
        'statusCode': 200,
        'body': 'Os dados foram salvos no bucket S3 com sucesso!'
    }