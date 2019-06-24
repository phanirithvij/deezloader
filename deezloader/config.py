from pathlib import Path

localdir = Path('.') / 'Songs'

header = {
    "Accept-Language": "en-US,en;q=0.5",
    'accept-encoding': 'application/json'
}


qualities = {
    "FLAC": {
        "quality": "9",
        "extension": ".flac",
        "qualit": "FLAC"
    },
    "MP3_320": {
        "quality": "3",
        "extension": ".mp3",
        "qualit": "320"
    },
    "MP3_256": {
        "quality": "5",
        "extension": ".mp3",
        "qualit": "256"
    },
    "MP3_128": {
        "quality": "1",
        "extension": ".mp3",
        "qualit": "128"
    }
}
