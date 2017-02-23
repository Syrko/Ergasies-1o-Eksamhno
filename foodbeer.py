import requests
import json
alpha=raw_input("Specify food to eat(e.g chicken): ")
print ""
print "Recipe for %s dish:"%alpha
print ""
par={'key':'42b8a95086c39020c81d18dd3f257c61','q':'%s'%alpha}
r=requests.get("http://food2fork.com/api/search",params=par)
recipes=r.json()
top=recipes['recipes']
if top:
    frecipe=top[0]
    for i in frecipe:
        print i,"-->",frecipe[i]
else:
    print "Could not find recipe."
print ""

print "Suitable beer:"
print ""
par2={'food':'%s'%alpha}
r2=requests.get("https://api.punkapi.com/v2/beers",verify=False,params=par2)
beers=r2.json()
if beers:
    fbeer=beers[0]
    print "Name: ",fbeer['name']
    print "Description: ",fbeer['description']
else:
    print "Could not match current food with beer."
print ""
