from django.shortcuts import render
from django.contrib import auth, messages
from ShopeeSite import models
from .Crawler import Crawler

def index(request):
    ItemInfo = models.ItemInfo.objects.all()
    
    return render(request, 'home.html', locals())

# 統計頁面負責呼叫Crawler.py擷取商品資訊
def statistic(request):
    try:
        shopname = request.POST['shopname']
        url = request.POST['url']
    except:
        shopname = ""
        url = ""
    
    if shopname != "" and url != "":
        # 呼叫完整商品統計流程
        url_split = url.split(".")
        shopid = url_split[-2]
        itemid = url_split[-1]
        crawler = Crawler(shopname, shopid, itemid)
        crawler.run()
        crawler.close()
        
        # 將擷取的賣場ID、商品ID存於Django資料庫
        post = models.ItemInfo.objects.create(shopname = shopname,
                                              url = url)
        post.save()
        
        message = 'Successful statistics !!'
    
    else:
        message = "Please enter the Shopee shop name & item's url if you want to analyze."
        
    return render(request, 'statistic.html', locals())
