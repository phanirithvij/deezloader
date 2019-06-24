import os
from dotenv import load_dotenv
from pathlib import Path
import deezloader

# MUST have a .env file with contents

# ARL="arl from deezer.com cookies"
# EMAIL="your deezer email"
# PASS="your password"

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

arl = os.getenv('ARL')
email = os.getenv('EMAIL')
passwd = os.getenv('PASS')

# MUST SET HTTP_PROXY AND HTTPS_PROXY as

# export HTTP_PROXY=http://127.0.0.1:9000
# export HTTPS_PROXY=http://127.0.0.1:9000

# Now torrc should have the same port
# Append this line to torrc
# HTTPTunnelPort 9000


def dl_song(dezz, url=""):
    dezz.download_trackspo(
        url,
        output=Path("music"),
        quality="FLAC",
        recursive_quality=True,
        recursive_download=True,
    )


if __name__ == "__main__":
    print(arl)
    print(email)
    print(passwd)
    dezz = deezloader.Login(email, passwd, token=arl)
    dl_song(dezz, url="https://open.spotify.com/track/543bCW2ruMPmxUBWirQ3MR")
