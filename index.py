import requests

BREAKING_CHUTIYA = "https://docs.google.com/spreadsheets/d/1D-O66NYhdJC3OyuOSoIu3-XI8GB54TSSsvrnt9yR8kw/edit?usp=sharing"
GAME_OF_CHUTIYAS = "https://docs.google.com/spreadsheets/d/1CDaEFf0kdokSMHZBmy1ckVAY-p7XlNHfrWwPK3yb5ws/edit?usp=sharing"

resp = requests.get(BREAKING_CHUTIYA)

idx1 = str(resp.text).index('<td class="s3">')
idx2 = str(resp.text).index('<td class="s18">')
vals1 = resp.text[idx1:idx1+30].split('>')[1].split('<')[0]
vals2 = resp.text[idx2:idx2+30].split('>')[1].split('<')[0]

print("Irene", vals1)
print("Prax", vals2)

resp = requests.get(GAME_OF_CHUTIYAS)

idx1 = str(resp.text).index('<td class="s1">')
idx2 = str(resp.text).index('<td class="s10">')
vals1 = resp.text[idx1:idx1+30].split('>')[1].split('<')[0]
vals2 = resp.text[idx2:idx2+30].split('>')[1].split('<')[0]

print("Irene", vals1)
print("Prax", vals2)
