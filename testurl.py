import requests
headers = {'user-agent':'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
                           'cookie':'_gcl_au=1.1.254304469.1566737444; _med=refer; SPC_IA=-1; SPC_EC=-; SPC_U=-; _ga=GA1.2.2027192842.1566737445; SPC_F=fp2vjEyCRqz2gB8kS0MurHLdfNh9nMLf; REC_T_ID=f082709c-c736-11e9-9555-b4969130c4b6; __BWfp=c1566737446743x87ac66dee; cto_lwid=cd11e389-9f4b-40fb-bd06-aee0ac449e4e; csrftoken=TtO9rVbtnW1s9GSIOjAyzCi1rQJR9EKB; SPC_SI=wpvmm4458yr03f21cx1xzw3maz4suztx; welcomePkgShown=true; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.223226401.1566835582; SPC_T_IV="Jcsbr3hHr6h+4RuTVpMnBw=="; SPC_T_ID="QKaWNLcauvteKJLoVK9tmlGilDNPw5ZwJOdmkHn0rZZEj+M2cHLFvIKDx5rebBCNbN6NZaIdp+lddnFp27r0g5DweKkoMv8eAdAExM1BQhU="',
                           'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                           'if-none-match':'e5062e839d47ecd0436ebb75790e3611;gzip',
                           'if-none-match-':'55b03-b0ee1233553c8398f6dee11a8119832e'}
url = "https://shopee.tw/%E3%80%902019%E4%BA%8C%E4%BB%A3%E6%96%B0%E6%AC%BE-%E3%80%91%E6%B0%B4%E5%86%B7%E6%89%87-arctic-air-%E6%B0%B4%E5%86%B7%E7%A9%BA%E8%AA%BF-USB%E6%A1%8C%E6%89%87-%E6%94%9C%E5%B8%B6%E5%9E%8B%E5%86%B7%E6%B0%A3-%E7%A9%BA%E8%AA%BF%E9%A2%A8%E6%89%87-%E6%B0%B4%E9%9C%A7%E9%A2%A8%E6%89%87-i.829655.1310131145"
html = requests.get(url, headers=headers) # 對網站發出請求
data = html.text

print(data)