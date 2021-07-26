from requests_html import HTMLSession
import requests

trackID = 'offertenetw03-21'   #trackingID dell'utente affiliato
link = input('inserisci il link che vuoi convertire')   #link del prodotto da convertire


#funzione che recupera il titolo del prodotto

def getTitle(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    title =  r.html.xpath('//*[@id="title"]', first=True).text  
    
    return (title)


#funzione che recupera il prezzo del prodotto

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    price =  r.html.xpath('//*[@id="priceblock_dealprice"]', first=True).text  
    
    return (price)


#funzione che recupera il codice asin del prodotto

def getAsin(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:

        asin =  r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td', first=True).text  
    
    except:
        asin =  r.html.xpath('//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]', first=True).text

    return (asin)


#funzione che genera la stringa del link affiliato

def linkGenerator(ID):
    affiliateLink = 'http://www.amazon.it/dp/' + getAsin(link) + '/?tag=' + ID

    return(affiliateLink)


#funzione che formatta il messaggio da inviare

def writer():
    message =  getTitle(link) + "\n \nDisponibile nuovo a: " + getPrice(link) + "\nSpedizione Gratuita!" + "\n\n\n" + linkGenerator(trackID)
    return(message)


#funzione che invia il messaggio

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1920455240:AAH--6IOaJV_2L8Xk3_D2OP35udgp7WBnVU'
    bot_chatID = '-1001432902351'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def sender():
    
    my_message = writer()   
    telegram_bot_sendtext(my_message)


sender()