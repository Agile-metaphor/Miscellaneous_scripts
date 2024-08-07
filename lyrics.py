import requests
import colorama 
from colorama import Fore
from bs4 import BeautifulSoup

colorama.init(autoreset=True)

print(Fore.CYAN + '''

 ██▓   ▓██   ██▓ ██▀███    ██▓  ▄████▄   ██████ 
▓██▒    ▒██  ██▒▓██ ▒ ██▒▒▓██▒ ▒██▀ ▀█ ▒██    ▒ 
▒██░     ▒██ ██░▓██ ░▄█ ▒▒▒██▒ ▒▓█    ▄░ ▓██▄   
▒██░     ░ ▐██▓░▒██▀▀█▄  ░░██░▒▒▓▓▄ ▄██  ▒   ██▒
░██████  ░ ██▒▓░░██▓ ▒██▒░░██░░▒ ▓███▀ ▒██████▒▒
░ ▒░▓     ██▒▒▒ ░ ▒▓ ░▒▓░ ░▓  ░░ ░▒ ▒  ▒ ▒▓▒ ▒ ░
░ ░ ▒   ▓██ ░▒░   ░▒ ░ ▒ ░ ▒ ░   ░  ▒  ░ ░▒  ░ ░
  ░ ░   ▒ ▒ ░░    ░░   ░ ░ ▒ ░ ░       ░  ░  ░  
    ░   ░ ░        ░       ░   ░ ░           ░  
''')

artist_input = input("Enter the name of the artist: ")
stripped_input = artist_input.strip()
artist_name = stripped_input.replace(" ", "-")

song_input = input("Enter the name of the song: ")
stripped_input = song_input.strip()
song_name = stripped_input.replace(" ", "-")

url = f"https://genius.com/{artist_name}-{song_name}-lyrics"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
lyrics_div = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-6 YYrds")

for br in soup.find_all("br"):
    br.replace_with("\n")

if lyrics_div is not None:
    lyrics = lyrics_div.get_text().strip()
    lyrics = lyrics.replace("<br>", "\n")
    print("\n" + Fore.GREEN + "LYRICS:")
    print("\n" + lyrics)
else:
    print(Fore.RED + "Check the spelling of the artist and try again.")