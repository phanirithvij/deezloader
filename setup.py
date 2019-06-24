from setuptools import setup

setup(
    name="deezloader",
    version="5.4.1",
    description="Downloads songs, albums or playlists from deezer",
    license="Apache-2.0",
    author="Phani Rithvij",
    author_email="phanirithvij2000@gmail.com",
    url="https://github.com/phanirithvij/deezloader",
    packages=["deezloader"],
    install_requires=['mutagen', 'requests', 'spotipy', 'tqdm']
)
