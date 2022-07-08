from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.govcagecodes.com/?code=&company=TESLA#results"

try:
    tableHeaders = []

    source = requests.get(url).text

    soup = BeautifulSoup(source, "lxml")
    table = soup.find("table", id="rt")

    # iterate over thead in table to extract all td in thead and append its text to array tableHeaders
    for td in table.thead.tr.find_all("td"):
        tableHeaders.append(td.text)

    df = pd.DataFrame(columns=tableHeaders)

    #iterate over tbody in table to extract all tr in tbody and append its text to array tableRows 
    for tr in table.tbody.find_all("tr"):
        data = tr.find_all("td")
        tableRows = [td.text for td in data]
        length = len(df)
        df.loc[length] = tableRows

    df.to_json("./tableData.json")
except Exception as err:
    print(err)