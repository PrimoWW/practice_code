from bs4 import BeautifulSoup
import requests
import time

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST"
urls = ["https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST"
            .format(str(i)) for i in range(30, 930, 30)]


def get_attractions(url, data=None):
    wb_data = requests.get(url)

    time.sleep(2)

    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.listing_title > a[target:"_blank"]')
    imgs = soup.select('a.photo_link > img[height="180"]')
    cates = soup.select('span[class="matchedTag noTagImg"]')


    for title, img, cate in zip(titles, imgs, cates):
        data = {'title':title.get_text(),
                'img':img.get('src'),
                'cate':list(cate.stripped_strings),
                }
        print(data)

'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Cookie':'TAUnique=%1%enc%3A2YLmNxB4JhwDK30unz5zzdZb1hEB2783pru72qAGIxg2jHwltRJPGQ%3D%3D; TASSK=enc%3AAMk53ymLGMrqeUVZLnRkWa8p4v0BkKyINqZkA4tSsnRAE05p%2FhBQa4mj%2F59sfBI5SWcNyhu%2Bn%2FP5Mf9i4%2By%2BhvvBtqZ9JCMmDG4jlu%2BNsnc6h7j7G4J3YZ0XAVgL1kWA%2Fg%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1505805394532; _jzqy=1.1505200690.1505200690.1.jzqsr=baidu|jzqct=tripadvisor.-; __gads=ID=3dce500e45053be9:T=1505200600:S=ALNI_MZXRCW1ZyJ9d2MUO_FBUNqGrowfvg; ServerPool=C; TAPD=tripadvisor.cn; _jzqckmp=1; CommercePopunder=SuppressAll*1505375172735; _smt_uid=59b78a31.4a97f8ec; SecureLogin2=3.4%3AAGmeCJaQIERLmcBqzTnYGATTG97xaaNf46E5iuCOfeXED2VtLwhaAarDtvFjJY%2BpKuL%2BwQQMCjoVzeoHCYQum0nLLRlRDaA72ZF2YFNpwJQjEw7iQct4VFGkmAsom21SZjuJ42c10eX3hq9bnEgwSH7w5bILA6ha%2BdubDEGDVRD0%2BHOAtbaIjEtDNq0oO8IgcYPLQRuIl0s4CRDryezFLzE%3D; TAAuth3=3%3A3994debad0122cfcbafefb769ecfcf3f%3AABd6h%2BssM9m3EyxGilmefpTG3MiF2a%2BVqy4lWlbY4oA3lnFSZH5cSACoWHL3IG0D4dmccELY4dQ7PeAyY4CZJLOpIiDgigfs2PUyPNIOkc1WoSYOelVF4Nu9dpdpvWTuiCjs70gfpoFJGnIrHh9Kdvnw8OTDKUsxiToLdhEHaQQ8Xp7bzjLkCzSHaeEjXphLUw%3D%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_257l1687489_257l294226_257l2_257l294232_257l298184_257l105127_257*RS.1; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C5%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; ki_t=1505200691356%3B1505375151770%3B1505389880505%3B2%3B40; ki_r=; roybatty=TNI1625!AIGUxBXCz8sxF6ssl8Dr5Lu9xQmMBQiiSPOJyxkLoVBOKPt9V0Mo7A2yzoYF8jw1cPaoMDwuPEUO%2BTmkSN65QD5fMG95UdCYKN64ahgd8bzlJqfirhFG1ptF%2BEjUNQ14JmXaA1yywvZpWO1OtTpC7uO9d3kVxb8Kkm5xXRpxA9ok%2C1; _ga=GA1.2.385852342.1505200690; _gid=GA1.2.1092742304.1505375146; _gat_UA-79743238-4=1; TASession=%1%V2ID.E5A0A53C3C23A019680E0AE950891E23*SQ.192*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Den_US%26pool%3DC%26returnTo%3D%252F*PR.1434%7CUserReview*LS.DemandLoadAjax*GR.70*TCPAR.52*TBR.14*EXEX.13*ABTR.42*PHTB.0*FS.8*CPU.61*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.EBE3BF14A1E86EDD5E49CCFAAA833321*LF.zhCN*FA.1*DF.0*IR.3*OD.en_US*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1505200594490-1*RDD-1-2017_09_12*LG-192760242-2.1.F.*LD-192760243-.....; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1505200690,1505375151; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1505393447; _jzqa=1.3284512371922838000.1505200690.1505388633.1505393447.4; _jzqc=1; _jzqx=1.1505388633.1505393447.2.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.jzqsr=tripadvisor%2Ecn|jzqct=/tourism-g298184-tokyo_tokyo_prefecture_kanto-vacations%2Ehtml; _qzja=1.1456271944.1505200690473.1505388633540.1505393447045.1505389880521.1505393447045..0.0.41.4; _qzjb=1.1505393447045.1.0.0.0; _qzjc=1; _qzjto=38.3.0; _jzqb=1.1.10.1505393447.1',
}
'''
