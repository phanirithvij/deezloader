import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
sys.path.append(str(Path('.').absolute().parent))

from deezloader import Deezer

load_dotenv(find_dotenv('.env'))

email=os.getenv('EMAIL')
arl=os.getenv('ARL')
passw=os.getenv('PASS')

deez = Deezer(
    email,
    passw,
    arl
)

# Search song on spotify
deez.download_name("League of Legends", "Rise")

# Download track from spotify
deez.download_trackspo(
    "https://open.spotify.com/track/2P8MOT07PrPiTjqNPKWVsp")

# Not avavile on deezer (error test)
try:
    deez.download_trackspo(
        "https://open.spotify.com/track/3HO2PCDfVutyscQs6jGXbd")
except Exception as e:
    print(str(e))
try:
    deez.download_trackspo(
        "https://open.spotify.com/track/1qDaWdzDhrmGu12Thqultf")
except Exception as e:
    print(str(e))


# Download album on spotify
deez.download_albumspo(
    "https://open.spotify.com/album/6ZvDJs17O3woQirttKRYCG")

# Spotify playlist with less than 100
deez.download_playlistspo(
    "https://open.spotify.com/playlist/37i9dQZEVXcIpKpMGiO4CH")

# Download track from deezer
deez.download_trackdee("https://www.deezer.com/en/track/520422862")
deez.download_trackdee("https://www.deezer.com/track/546578/")

# Download album from deezer
deez.download_albumdee("https://www.deezer.com/us/album/13616177")

# Download track from deezer (FLAC)
# deez.quality = "FLAC"
deez.download_trackdee(
    "https://www.deezer.com/track/696042592", quality="FLAC")

# Download playlist from deezer (FLAC)
deez.download_playlistdee(
    "https://www.deezer.com/en/playlist/6117941304", quality="FLAC")
