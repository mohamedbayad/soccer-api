from bs4 import BeautifulSoup
import requests
import uuid

class FootBall:

    def __init__(self, url) -> str:
        self.url = url

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cookie' : 'sw_l10m=ar; sw_l10org=MA; _pbjs_userid_consent_data=3524755945110770; undefined=7afcc204-4d81-4ba7-99c3-29e2d3295cfd; _ga=GA1.3.112269125.1688600249; _gid=GA1.3.1398223591.1688600249; __qca=P0-2000407547-1688600248404; _sharedid=9218ca2f-ff8d-4fd8-8b38-2777d36116e2; pbjs-unifiedid=%7B%22TDID%22%3A%220e70bfb1-9199-4cd8-af09-a6a9433aa8b4%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-06-05T23%3A37%3A35%22%7D; panoramaId_expiry=1689205055491; _cc_id=809c2e66b528d0db8d996af10350b04b; panoramaId=e4d0f4c514dc82d96a46707a84ee4945a7023c4914f0634e616b00f375eb9430; lngtd-sdp=18; nol_fpid=uaw4ndit7r6e5us1m7fvuyeowemx91688600249|1688600249827|1688601657773|1688601658844; cto_bundle=p7CogF9CY0ExaGN4JTJCTDkwR0NxQXhZa3d0M0hoUThVJTJGSiUyQlozZzg5TlVaalhsZ3NYZ0s5cG42b25ycVlTckVVVyUyRmJkUldRJTJGZ2Z6b2xIbnBxUnclMkYwU1FZbXVEQzEwT0pzTnYxQ01zTXRycjN1M2ttQm1SM1V6QmZCM215ZDJycTN3UW5pNDU4YlNsNVJZOFNROTFsM04wZDV2V2clM0QlM0Q; cto_bidid=PXwAa19YNUF2SENFWDVPUmR4MjdQV1dSWklyOEdpd0dlYW1aTGxEWVR0MFdjWU9SVVptQkdBQk5WZ1E3aUJxR3VzRGp2RmNuZEJNbDZkaHlyM0tuaEV6c2pSdGFzeklCTG5tTFlOUEhmblZ4N1hpTSUzRA; cto_bundle=TtKIzF9CY0ExaGN4JTJCTDkwR0NxQXhZa3d0M0FwbUs0dUF6QUo1UWI0TXdocG1UWlM3JTJGRkdtSUI4QWJkeEJUbUVrYTZHVEM1VVpQUGF4VkNUYW9LZjUwZlM5SnRvblBKdHBpc3Z5TVZISVJKaXZSVk5EUnZpWlZqeUJlTE40M29tMnptRndONFJVOW9wZU1mNSUyRlZNc0pmNCUyQlB4QSUzRCUzRA; cto_bundle=TtKIzF9CY0ExaGN4JTJCTDkwR0NxQXhZa3d0M0FwbUs0dUF6QUo1UWI0TXdocG1UWlM3JTJGRkdtSUI4QWJkeEJUbUVrYTZHVEM1VVpQUGF4VkNUYW9LZjUwZlM5SnRvblBKdHBpc3Z5TVZISVJKaXZSVk5EUnZpWlZqeUJlTE40M29tMnptRndONFJVOW9wZU1mNSUyRlZNc0pmNCUyQlB4QSUzRCUzRA; cto_bidid=lXTpmV9YNUF2SENFWDVPUmR4MjdQV1dSWklyOEdpd0dlYW1aTGxEWVR0MFdjWU9SVVptQkdBQk5WZ1E3aUJxR3VzRGp2RmNuZEJNbDZkaHlyM0tuaEV6c2pSaVphM3kxeTlBTFNrYVNNTzBwbXBkQSUzRA; cto_bidid=lXTpmV9YNUF2SENFWDVPUmR4MjdQV1dSWklyOEdpd0dlYW1aTGxEWVR0MFdjWU9SVVptQkdBQk5WZ1E3aUJxR3VzRGp2RmNuZEJNbDZkaHlyM0tuaEV6c2pSaVphM3kxeTlBTFNrYVNNTzBwbXBkQSUzRA'
    }


    finishData = {} # This dictionary contains all data
    def getData(self):

        respons = requests.get(self.url, headers=self.header)

        if respons.status_code == 200:

            soup =  BeautifulSoup(respons.content, "lxml") # Code organization with bs4

            container = soup.find_all("div", {'id' : 'bd'}) 

            title = container[0].contents[0].find_next("h1").text.strip() # get title of the league

            header = container[0].contents[3].find_all("th") # get header from table

            dataHeader = { # header data 
                "rank" : header[0].text,
                "team" : header[2].text,
                "mp" : header[3].text,
                "total_won" : header[4].text,
                "total_drawn" : header[5].text,
                "total_lost" : header[6].text,
                "total_gf" : header[7].text,
                "total_ga" : header[8].text,
                "gd" : header[9].text,
                "points" : header[10].text,
            }

            body = container[0].contents[3].find_all("tr", {"class" : "team_rank"})
            cleanList = list()
            # clean data from spaces 
            for i in body:
                listItem = list()
                [listItem.append(item) for item in i.contents if item != "\n"]
                cleanList.append(listItem)
            
            dataBodyList = list()
            id_team = 0
            for item in cleanList:
                id_team += 1
                dataBody = { # body data 
                    "id" : id_team,
                    "rank" : int(item[0].text),
                    "team" : item[2].text,
                    "mp" : int(item[3].text),
                    "total_won" : int(item[4].text),
                    "total_drawn" : int(item[5].text),
                    "total_lost" : int(item[6].text),
                    "total_gf" : int(item[7].text),
                    "total_ga" : int(item[8].text),
                    "gd" : int(item[9].text),
                    "points" : int(item[10].text),
                }
                dataBodyList.append(dataBody) # append body data to list dataBodyList
            
            
            # add all data to dictionary dataJson 
            id_table = str(uuid.uuid4().int)
            id_table = id_table[:10]
            self.finishData.update({title : {
                "id" : int(id_table),
                "title" : title,
                "header" : dataHeader,
                "body" : dataBodyList
            }})

            return self.finishData

        

