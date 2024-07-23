import requests
from urllib.parse import quote
from time import sleep
from config import aiir_id, aiir_password, file_path
while True:
        try:
                with open(file_path,encoding='utf-8-sig') as file:
                        lines = file.readlines()
                        for line in lines:
                                if '-' in line:
                                        artist, song = line.strip().split(' - ')
                                        data = {'type': "song", 'artist': artist, 'title': song}
                                        response = requests.post(f"https://api.aiir.net/v1/services/{aiir_id}/now-playing?artist={quote(artist)}&title={quote(song)}&type=song&password={quote(aiir_password)}", data=data)
        except:
                print('File mid update')
        sleep(15)

