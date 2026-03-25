import requests

URL = "https://dummyjson.com/posts"
r = requests.get(URL)
data = r.json()
posts = data["posts"]

def reaktsioonide_summa(p):
    return p["reactions"]["likes"] + p["reactions"]["dislikes"]

print("Pealkirjad:")
for p in posts:
    print(p["title"])

maksim_post = posts[0]
for p in posts:
    if reaktsioonide_summa(p) > reaktsioonide_summa(maksim_post):
        maksim_post = p

print("\nKõige rohkem reaktsioone:")
print(maksim_post["title"], "-", reaktsioonide_summa(maksim_post))

vaatamiste_arv = 0
for p in posts:
    vaatamiste_arv += p["views"]
print("\nVaatamiste kogusumma:", vaatamiste_arv)

reaktsioonid_kokku = 0
for p in posts:
    reaktsioonid_kokku += reaktsioonide_summa(p)

keskmine = reaktsioonid_kokku / len(posts)
print("\nKeskmine reaktsioonide arv:", keskmine)