import random

import requests
import time


cook = ' '
cook2 = 'hideShoutbox=1; ' + cook
agent = ' '
uid = ' '


def thank(trid):
    global cook, cook2, agent, uid
    urlthank = "https://www.torrentbd.net/torrent/ajthank.php"
    urlrep = "https://www.torrentbd.net/torrent/ajaddrep.php"
    ref = 'https://www.torrentbd.net/torrent/torrents-details.php?id=' + str(trid)
    cntlen = len(uid) + len(str(trid)) + 5

    headerss = {
        'Host': 'www.torrentbd.net',
        'User-Agent': agent,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': str(cntlen),
        'Origin': 'https://www.torrentbd.net',
        'Connection': 'keep-alive',
        'Referer': ref,
        'Cookie': cook,
        'TE': 'Trailers',
    }

    datas = {
        'u': uid,
        'i': str(trid),
    }

    r = requests.post(urlthank, headers=headerss, data=datas)
    rr  = requests.post(urlrep, headers=headerss, data=datas)



def fetchpage(pageN):
    global cook, cook2, agent, uid
    urlsearch = "https://www.torrentbd.net/torrent/ajsearch.php"
    cntLen = len(str(pageN)) + 168

    headerss = {
            'Host': 'www.torrentbd.net',
            'User-Agent': agent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': str(cntLen),
            'Origin': 'https://www.torrentbd.net',
            'Connection': 'keep-alive',
            'Referer': "https://www.torrentbd.net/torrent/index.php?initK&all",
            'Cookie': cook2,
            'TE': 'Trailers',
        }

    datas = {
        'page': str(pageN),
        'kuddus_searchtype': 'torrents',
        'kuddus_searchkey': '',
        'searchParams[sortBy]':'',
        'searchParams[special_filters]': 'all_torrent',
        'searchParams[secondary_filters_extended]': '',
    }

    sr = requests.post(urlsearch, headers=headerss, data=datas)
    resp = sr.text

    ff = open("wtf.txt", "a+")
    while resp.find("torrents-details.php?id=") != -1:
        resp = resp[resp.find("torrents-details.php?id=")+24:]
        iid = resp[:resp.find("&amp;")]
        ff.write(str(iid) + ' ')

    ff.close()


def fetchAllTorrents(totPage):
    fff = open("wtf.txt", "w+")
    fff.write(" ")
    fff.close()
    for i in range(totPage):
        print('fetching ' + str(i) + "/" + str(totPage) + "\n")
        fetchpage(i)
        time.sleep(.5)

    print("Done fetching")


def startThanking():
    dfl = open("done.txt", "r")
    done = int(dfl.read())
    dfl.close()
    fl = open("wtf.txt" , "r")
    vv = fl.read()
    fl.close()
    trlist = vv.split(' ')


    while done != len(trlist):
        dfl = open("done.txt", "w+")
        print("Thanking " + str(done) + "/" + str(len(trlist)) + "\n")
        tid = int(trlist[done])
        done += 1
        dfl.write(str(done))
        dfl.close()
        thank(tid)
        time.sleep(3)


def Cont():
    global cook, agent, uid
    dt = open("details.txt", "r")
    dtstr = dt.read()
    dtlst = dtstr.split("^")
    cook = dtlst[0]
    agent = dtlst[1]
    uid = dtlst[2]
    print("Continuing with: ")
    print(cook + "\n" + agent + "\n" + uid)



print("Hehehe, Welcome. Ban khaile amar kono dos nai :) ... ")
print("Continue?? (y/n): ")
xx = input()
if xx == 'y' or xx == 'Y':
    Cont()
else:
    print("\nEnter cookie (copy and pase): \n")

    cook = input()

    print("\n Enter user Agent : \n" )

    agent = input()

    print()

    print("\n Enter uid: \n")

    uid = input()

    dt = open("details.txt", "w+")
    dt.write(cook + "^" + agent + "^" + uid)
    dt.close()
    Cont()










