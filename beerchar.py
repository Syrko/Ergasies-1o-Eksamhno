import requests
import json

msg="Give beer characteristics you desire(format: char1, char2, char3, ...): "
print ""
searchChar=raw_input(msg)
msg=msg+searchChar
print len(msg)*"="
searchChar=searchChar.replace(" ","")

par={'key':'3ca87b246314c6f99ee7d95e2b2474dc', 'type':'beer','q':'%s'%searchChar}
r=requests.get('http://api.brewerydb.com/v2/search',params=par)
results=r.json()
if 'totalResults' in results:
    numResults=results['totalResults']
    if numResults>50:
        numResults=50
    results=results['data']
    descList=[]
    ctrList=[]
    nameBeer=[]
    beerNum=-1
    for i in range(numResults):
        temp=results[i]
        if 'description' in temp:
            descList.append(temp['description'])
            nameBeer.append(temp['name'])
    charList=searchChar.split(",")
    for i in range(len(descList)):
        ctr=0
        for j in range(len(charList)):
            charAppear=descList[i].count(charList[j])
            ctr+=charAppear
        ctrList.append(ctr)
    maxCtr=0
    for i in range(len(ctrList)):
        if ctrList[i]>maxCtr:
            maxCtr=ctrList[i]
            beerNum=i
    if beerNum>-1:
        print "The most suitable beer would be:", nameBeer[beerNum]
        print ""
    else:
        print "Could not match desired characteristics with a beer."
        print ""
else:
    print "Could not match desired characteristics with a beer."
    print ""
