from bs4 import BeautifulSoup
import requests
from datetime import date
import csv

def write_to_file(scoreline):
    f = open("scores.csv", "a")
    writer = csv.writer(f)
    tup  = (scoreline,)
    writer.writerow(tup)
    f.close()


def scrape():
    today = date.today()
    html_text =  requests.get('https://www.espncricinfo.com/live-cricket-score').text

    soup = BeautifulSoup(html_text, 'lxml')
    Score_1 = soup.find('div', class_ ="ds-flex ds-flex-col ds-mt-2 ds-mb-2" ).text
    Score_2 = soup.find('p',  class_ ="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo").text
    
    test_list = [Score_1]
    
    res = []
    for i in test_list:
        for j in i:
            if(j.isupper()):
                i = i.replace(j, " "+j)
        res.append(i)
    score= str(res[0]) + "\n" + Score_2 + "\n" + str(today)
    to_store = str(res[0]) + " " + Score_2 + "  " + str(today)
    write_to_file(to_store)
    return(score)
