from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser():
    def __init__(self):
        pass

    def __get_new_urls(self, page_url, soup):

        new_urls = set()
        links = soup.find_all('a', href=re.compile('/wiki/\w+'))

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def __get_new_data(self, page_url, soup):
        res_data = {'url': page_url}
        title_node = soup.find(id="firstHeading").get_text()
        res_data['title'] = title_node
        return res_data

    def parse(self, pageUrl, htmlContent):
        if pageUrl is None or htmlContent is None:
            return

        soup = BeautifulSoup(htmlContent, 'html.parser', from_encoding='utf-8')
        new_urls = self.__get_new_urls(pageUrl, soup)
        new_data = self.__get_new_data(pageUrl, soup)
        return new_urls, new_data
