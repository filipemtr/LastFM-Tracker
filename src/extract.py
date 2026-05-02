from get_charts import extract_artists, extract_genders, extract_tracks
from get_country_info import country_artists, country_tracks

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






