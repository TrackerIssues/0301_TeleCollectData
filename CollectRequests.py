import requests, json
from bs4 import BeautifulSoup as bs


# lstNateKeyword = []
# lstGoogleKeyword = []
# lstRank = []
# lstZumKeyword = []
# lstSignalKeyword = []

# Nate 실시간 검색어 크롤러
def nate_crawler( sDate ):
#   now = datetime.now().strftime('%Y%m%d%H%M')
#   url = 'https://www.nate.com/js/data/jsonLiveKeywordDataV1.js?v=' + dtKorea.strftime('%Y%m%d%H%M')
  url = 'https://www.nate.com/js/data/jsonLiveKeywordDataV1.js?v=' + sDate
  r = requests.get(url).content
  keyword_list = json.loads(r.decode('euc-kr'))
  result = []
  # print(dtKorea.strftime('%Y%m%d%H%M'))
  print("\n< 네이트 실시간 검색어 >")
  for i in keyword_list:
    result.append(i[1])
    # lstNateKeyword.append( i[1] )
  return result


# Google Trend 최근 인기 검색어 크롤러
def google_crawler():
  url = 'https://trends.google.com/trends/api/topdailytrends?hl=ko&tz=-540&geo=KR'
  html = requests.get(url).text
  data = json.loads(str(html).split('\n')[1])
  result = []
  print("\n< 구글 실시간 검색어 >")
  for i in range(10):
    sTemp = (data['default']['trendingSearches'][i]['title'])
    result.append( sTemp )
    # lstGoogleKeyword.append( result[i] )
    # lstRank.append( i +1 )
  return result


# Zum 실시간 검색어 크롤러
def zum_crawler(): 
    url = 'https://m.search.zum.com/search.zum?method=uni&option=accu&qm=f_typing.top&query='
    html = requests.get(url).content
    soup = bs(html, 'html.parser')
    keyword_list = soup.find('div', {'class' : 'list_wrap animate'}).find_all('span', {'class' : 'keyword'})
    result = []
    print("\n< Zum 실시간 검색어 >") 
    for k in keyword_list:
        sTemp = k.text.strip()
        result.append(sTemp)
        # lstZumKeyword.append( sTemp )
    return result

