from get_charts import extract_artists, extract_genders, extract_tracks
from get_country_info import country_artists, country_tracks
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import os
import boto3

load_dotenv()

# Receives an list / dict and the names of the columns if its necessary and convert it into a object!

def convertIntoDF(object: dict | list, column: list = None):
    dataframe = pd.DataFrame(data=object, columns=column)
    dataframe.insert(0, "ID", range(1, len(dataframe) + 1))

    return dataframe

# Global charts data extraction 
artists_charts = extract_artists()
genders_charts = extract_genders()
tracks_charts = extract_tracks()

# Country based artists charts and tracks charts extraction
countries = [ 
    "brazil", "united states", "argentina", "mexico", "china",
    "japan", "united kingdom", "canada", "india", "australia"
]

# Converting dicts and lists to dataframes

# Global artists charts
df_artists = convertIntoDF(artists_charts, ["Artist Name", "Listeners", "Playcount"])

# Global genders charts
df_genders = convertIntoDF(genders_charts, ["Gender"])

# Global tracks chartscountry_artist_info
df_tracks = convertIntoDF(tracks_charts, ["Music Name", "Playcount", "Artist"])

# Country based artists charts
artists = [country_artists(ctr) for ctr in countries]
flat_artists = [item for country in artists for item in country]
df_country_artists = convertIntoDF(flat_artists, ["Artist", "Country"])

# Country based tracks charts
tracks = [country_tracks(ctr) for ctr in countries]
flat_tracks = [item for country in tracks for item in country]

df_country_tracks = convertIntoDF(flat_tracks, ["Music Name", "Artist", "Country"])

# Saving locally 
BASE_DIR = Path(__file__).parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

df_artists.to_parquet(RAW_DIR / "global_artists" / "artists.parquet", index=False)
df_genders.to_parquet(RAW_DIR / "global_genders" / "genders.parquet", index=False)
df_tracks.to_parquet(RAW_DIR / "global_tracks" /  "tracks.parquet", index=False)
df_country_artists.to_parquet(RAW_DIR / "country_data" / "artists_charts" / "c_artists.parquet", index=False)
df_country_tracks.to_parquet(RAW_DIR / "country_data" / "tracks_charts" / "c_tracks.parquet", index=False)

# S3 Bucket Conn
AWS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    's3',
    aws_access_key_id=f'{AWS_KEY}',
    aws_secret_access_key=f'{AWS_SECRET}',
    region_name='us-east-1'
)

# Uploading parquet files in S3

for item in RAW_DIR.rglob("*.parquet"):
    if "global_tracks" in str(item):
        s3.upload_file(
            Filename=str(item),
            Bucket="lastfm-tracker",
            Key="bronze/data/global_tracks/tracks.parquet"
        )
    elif "global_genders" in str(item):
        s3.upload_file(
            Filename=str(item),
            Bucket="lastfm-tracker",
            Key="bronze/data/global_genders/genders.parquet"
        )
    elif "global_artists" in str(item):
        s3.upload_file(
            Filename=str(item),
            Bucket="lastfm-tracker",
            Key="bronze/data/global_artists/artists.parquet"
        )
    elif "c_artists" in str(item):
        s3.upload_file(
            Filename=str(item),
            Bucket="lastfm-tracker",
            Key="bronze/data/country_data/artists_charts/c_artists.parquet"
        )
    elif "c_tracks" in str(item):
        s3.upload_file(
            Filename=str(item),
            Bucket="lastfm-tracker",
            Key="bronze/data/country_data/tracks_charts/c_tracks.parquet"
        )

