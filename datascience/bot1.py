#pip install pandas openpyxl


from dputils import scrape
import pandas as pd

def get_news_headlines(url = "https://www.ndtv.com/latest"):
    
    soup = scrape.get_webpage_data(url)
    if soup:

        t = {'tag' : 'div','attrs': {'class' : 'lisingNews'}}
        items = {'tag' : 'div','attrs': {'class' : 'news_Itm'}}
        title = {'tag' : 'h2','attrs': {'class' : 'newsHdng'}}
        deet = {'tag' : 'span', 'attrs': {'class':'posted-by'}}
        summary = {'tag' : 'p', 'attrs': {'class':'newsCont'}}

        result = scrape.extract_many(soup, target = t ,items = items, title = title, details = deet, summary = summary)

        return result
    else:
        print ("Soup is None")


all_data = []
page = 1
while True:
    url = f'https://www.ndtv.com/latest/page-{page}'
    print("LOG : ",url)
    data = get_news_headlines(url)
    if isinstance(data, list):      #The isinstance() function returns True if the specified object is of the specified type, otherwise False. Here it checks  if data is list or not.
        if len(data) > 0:
            page += 1
            all_data.extend(data)
        else:
            break
    else:
        break

pd.DataFrame(all_data).to_excel('headlines.xlsx')       #save your data as excel files