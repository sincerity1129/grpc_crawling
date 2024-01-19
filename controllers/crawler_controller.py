import requests
from bs4 import BeautifulSoup


def crawl_naver_site(url):
    try:
        # 네이버 사이트에 HTTP 요청을 보냅니다.
        response = requests.get(url)

        # 요청이 성공적인지 확인합니다 (상태 코드 200).
        if response.status_code == 200:
            # BeautifulSoup을 사용하여 HTML을 파싱합니다.
            soup = BeautifulSoup(response.text, 'html.parser')
            
            news_links = soup.select('.Nlist_item a')
            
            
            for link in news_links:
                response = requests.get(link['href'])
                detail_soup = BeautifulSoup(response.text, 'html.parser')
                articles = detail_soup.select('.sh_text a')
                for article in articles:
                    if 'sh_head_more' in article.get('class'):
                        continue
                    article_response = requests.get(article['href'])
                    article_soup = BeautifulSoup(article_response.text, 'html.parser')
                    title = article_soup.title.string
                    cotent = article_soup.article.text.replace("\n", "").replace("\".")
                    ariticle_dict=dict(
                        title=title,
                        content=cotent
                    )
                    print(ariticle_dict)
        else:
            print(f'Error: {response.status_code}')

    except Exception as e:
        print(f'Error: {e}')

# 크롤링하고자 하는 네이버 특정 사이트의 URL을 지정합니다.
naver_site_url = 'https://news.naver.com'

# 크롤링 함수 호출
crawl_naver_site(naver_site_url)