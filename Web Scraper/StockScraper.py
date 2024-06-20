import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = ["AAPL","META"]
income_statatement_dict = {}
balance_sheet_dict = {}
cashflow_st_dict = {}

for ticker in tickers:
    #scraping income statement
    url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker,ticker)
    # print(url)
    income_statement = {}
    table_title = {}

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.124 Safari/537.36"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div" , {"class" : "table svelte-1pgoo1f"})
    for t in tabl:

      heading = t.find_all("div" , {"class": "row svelte-1ezv2n5"})
      for top_row in heading:
        #print(top_row)
        table_title[top_row.get_text("|",strip=True).split("|")[0]] = top_row.get_text("|",strip=True).split("|")[1:]
      rows = t.find_all("div" , {"class": "row lv-0 svelte-1xjz32c"})
      for row in rows:
        # Handle potential inconsistencies in row lengths
        values = row.get_text("|",strip=True).split("|")[1:]
        income_statement[row.get_text("|",strip=True).split("|")[0]] = values
    if 'Breakdown' in table_title:
      # Fill missing values to ensure equal column lengths
      temp = pd.DataFrame(income_statement).T
      temp.columns = table_title["Breakdown"]
      income_statatement_dict[ticker] = temp
    #scraping balance sheet statement
    url = "https://finance.yahoo.com/quote/{}/balance-sheet?p={}".format(ticker,ticker)
    balance_sheet = {}
    table_title = {}

    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div" , {"class" : "table svelte-1pgoo1f"})
    for t in tabl:
        heading = t.find_all("div" , {"class": "row svelte-1ezv2n5"})
        for top_row in heading:
            table_title[top_row.get_text("|",strip=True).split("|")[0]] = top_row.get_text("|",strip=True).split("|")[1:]
        rows = t.find_all("div" , {"class": "row lv-0 svelte-1xjz32c"})
        for row in rows:
            # Handle potential inconsistencies in row lengths
            values = row.get_text("|",strip=True).split("|")[1:]
            balance_sheet[row.get_text("|",strip=True).split("|")[0]] = values
    if 'Breakdown' in table_title:
      # Fill missing values to ensure equal column lengths
      temp = pd.DataFrame(balance_sheet).T 
      temp.columns = table_title["Breakdown"]
      balance_sheet_dict[ticker] = temp

    #scraping cashflow statement
    url = "https://finance.yahoo.com/quote/{}/cash-flow?p={}".format(ticker,ticker)
    cashflow_statement = {}
    table_title = {}

    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    tabl = soup.find_all("div" , {"class" : "table svelte-1pgoo1f"})
    for t in tabl:
        heading = t.find_all("div" , {"class": "row svelte-1ezv2n5"})
        for top_row in heading:
            table_title[top_row.get_text("|",strip=True).split("|")[0]] = top_row.get_text("|",strip=True).split("|")[1:]
        rows = t.find_all("div" , {"class": "row lv-0 svelte-1xjz32c"})
        for row in rows:
           values = row.get_text("|",strip=True).split("|")[1:]
           cashflow_statement[row.get_text("|",strip=True).split("|")[0]] = values
    if 'Breakdown' in table_title:
      temp = pd.DataFrame(cashflow_statement).T
      temp.columns = table_title["Breakdown"]
      cashflow_st_dict[ticker] = temp
      #print(temp)

#exporting data to excel
for ticker in tickers:
    with pd.ExcelWriter("{}_Data.xlsx".format(ticker) ,engine='xlsxwriter') as writer:
        income_statatement_dict[ticker].to_excel(writer,sheet_name="income_statement_{}".format(ticker))
        cashflow_st_dict[ticker].to_excel(writer,sheet_name="cashflow_statement_{}".format(ticker))
        balance_sheet_dict[ticker].to_excel(writer,sheet_name="balance_sheet_{}".format(ticker))
        #print(income_statatement_dict[ticker])
print("Done")
