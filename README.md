# System that generates music based on user preferences (Not finished)

## Project for 11th edition of the Konferencja Projektów Zespołowych (KPZ) ##

### Description:
Upon receiving a Spotify playlist link from the user, the system will utilize the **Spotify API - Spotipy** (https://spotipy.readthedocs.io/en/2.22.1/) to fetch the artists and genres of all songs on the playlist. Subsequently, using the **OpenAI API** (https://openai.com/blog/openai-api), an input will be generated and then fed into the **MusicGEN music generator** (https://ai.honu.io/papers/musicgen/). After generating the sample, it will be uploaded to SoundCloud using **Soundcloud API** (https://pypi.org/project/soundcloud-lib/), and a link will be provided for downloading purposes.
