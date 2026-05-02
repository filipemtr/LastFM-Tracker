from get_charts import extract_artists, extract_genders, extract_tracks
from get_country_info import country_artists, country_tracks
from dotenv import load_dotenv
import os
import boto3

load_dotenv()

# Charts data extraction 
artists_charts = extract_artists()
genders_charts = extract_genders()
tracks_charts = extract_tracks()


# Country based artists and tracks extraction
countries = [ 
    "brazil", "united states", "argentina", "mexico", "china",
    "japan", "united kingdom", "canada", "india", "australia"
]

country_artist_info = {}
for country in countries:
    country_artist_info[country] = country_artists(country)

country_track_info = {}
for country in countries:
    country_track_info[country] = country_tracks(country)

AWS_KEY = os.getenv("AWS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")

s3 = boto3.client(
    's3',
    aws_access_key_id=f'{AWS_KEY}',
    aws_secret_access_key=f'{AWS_SECRET}',
    region_name='us-east-1'
)

# conexão feita, só falta converter os dicts pra dataframe do jeito certo, converter pra parquet e dar
# upload no bronze/data/ do lastfm-tracker





