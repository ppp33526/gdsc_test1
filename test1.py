# 先導入後面會用到的套件
import requests # 請求工具
from bs4 import BeautifulSoup # 解析工具
import time # 用來暫停程式

# 爬取的股票
stock = ["1101", "2330"]
for i in range(len(stock)): # 迴圈依序股票
    # 現在處理的股票
    stockid = stock[1]
    # 網址塞入股票編號
    url = "https://tw.stock.yahoo.com/quote/"+stockid+".tw"
    # 發送請求
    r = requests.get(url)
    # 解析回來的 HTML
    soup = BeautifulSoup(r.text, 'html.parser')
    # 定位股價
    price = soup.find('span',class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)", "Fz(32px) Fw(b```python
# 回報的訊息 (可自訂)
message = "股票 "+stockid+" 即時股價為 "+price
# 用 telegram bot 回報股價
# bot token
token = "6718510325:AAF1by3LnmV2nPit9NBTxkDExhUK1MEOISY"
# 使用名 id
