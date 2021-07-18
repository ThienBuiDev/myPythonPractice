import requests

# download text 
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
len(res.text)
print(res.text[:500])
print(res.status_code)
print(res.raise_for_status())

playFile = open('RomeoAndJuliet.txt,wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

