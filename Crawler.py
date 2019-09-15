import requests
import json
import MySQLdb

class Crawler:
    def __init__(self, shopname, shopid, itemid):
        headers = {'user-agent':'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
                           'cookie':'_gcl_au=1.1.254304469.1566737444; _med=refer; SPC_IA=-1; SPC_EC=-; SPC_U=-; _ga=GA1.2.2027192842.1566737445; SPC_F=fp2vjEyCRqz2gB8kS0MurHLdfNh9nMLf; REC_T_ID=f082709c-c736-11e9-9555-b4969130c4b6; __BWfp=c1566737446743x87ac66dee; cto_lwid=cd11e389-9f4b-40fb-bd06-aee0ac449e4e; csrftoken=TtO9rVbtnW1s9GSIOjAyzCi1rQJR9EKB; SPC_SI=wpvmm4458yr03f21cx1xzw3maz4suztx; welcomePkgShown=true; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.223226401.1566835582; SPC_T_IV="Jcsbr3hHr6h+4RuTVpMnBw=="; SPC_T_ID="QKaWNLcauvteKJLoVK9tmlGilDNPw5ZwJOdmkHn0rZZEj+M2cHLFvIKDx5rebBCNbN6NZaIdp+lddnFp27r0g5DweKkoMv8eAdAExM1BQhU="',
                           'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                           'if-none-match':'e5062e839d47ecd0436ebb75790e3611;gzip',
                           'if-none-match-':'55b03-b0ee1233553c8398f6dee11a8119832e'}
        
        url = "https://shopee.tw/api/v2/item/get?itemid="+itemid+"&shopid="+shopid
        
        html = requests.get(url, headers=headers) # 對網站發出請求
        data = json.loads(html.text)
        self.item = data["item"]
        
        host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"

        file = open('C:/Users/m4104/Desktop/ShopeeAnalysis/pwd.txt','r')
        pwd = file.read().rstrip()
        
        self.conn = MySQLdb.connect(host, port=3306, user='rex', passwd=pwd, db="shopee2019")        
        self.cur = self.conn.cursor()
    
    # 檢查資料庫是否已有重複資料
    def check_item(self):
        sql = "SELECT * FROM shopee2019.iteminfo WHERE item_id IN (%s);"
        val = (itemid,)
        self.cur.execute(sql,val)
        return self.cur.fetchall()
    
    # 以MySQL插入使用者蝦皮賣場ID及名字
    def shops(self):
        
        sql = "INSERT INTO shopee2019.shops (shop_id, shop_name) VALUES (%s, %s)"
        val = (shopid, shopname)
        self.cur.execute(sql, val)            
        self.conn.commit()
    
    def iteminfo(self):
        if not self.check_item():
            sql = "INSERT INTO shopee2019.iteminfo (shop_id, item_id, like_count, historical_sold,\
            star5, star4, star3, star2, star1, rating_star, price)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            star_count = self.item["item_rating"]["rating_count"]
            
            # 包括賣場ID、商品ID、喜好次數、歷史銷售量、客戶評分、商品價錢
            val = (shopid, itemid, self.item["liked_count"], self.item["historical_sold"],\
                   star_count[-1], star_count[-2], star_count[-3], star_count[-4], star_count[-5],\
                   self.item["item_rating"]["rating_star"], self.item["price"]//100000)
            self.cur.execute(sql, val)
            self.conn.commit()
        
    def images(self):
        if not self.check_item():
            sql = "INSERT INTO shopee2019.images (item_id, img) VALUES (%s, %s)"
            val = (itemid, "https://cf.shopee.tw/file/"+ self.item["image"] + "_tn")
            self.cur.execute(sql,val)
            self.conn.commit()

    # 關閉MySQL連線
    def close(self):
        self.conn.close()
    
    def run(self):
        self.iteminfo()
        self.images()
        
if __name__ == "__main__":
    url = "https://shopee.tw/%E3%80%90%E9%97%9C%E6%B3%A8%E5%86%8D%E6%8A%9820%E5%85%83%E3%80%91%E8%A7%B8%E6%8E%A7%E5%B0%8F%E5%A4%9C%E7%87%88-%E6%8B%8D%E6%8B%8D%E7%87%88-%E8%BB%8A%E5%BB%82%E7%87%88-%E8%A1%A3%E6%AB%A5%E7%87%88-%E7%B7%8A%E6%80%A5%E7%85%A7%E6%98%8E%E7%87%88-%E5%BE%8C%E8%BB%8A%E5%BB%82%E7%87%88-LED%E7%87%88-%E6%8C%89%E5%A3%93%E7%87%88-%E8%A7%B8%E7%A2%B0%E7%87%88-%E5%90%B8%E9%A0%82%E7%87%88-%E8%BB%8A%E9%A0%82%E7%87%88-i.829655.2793180018"
    url_split = url.split(".")
    shopname = str(input("SHOP NAME : "))
    shopid = url_split[-2]
    itemid = url_split[-1]
    crawler = Crawler(shopname, shopid, itemid)
    crawler.run()
    crawler.close()