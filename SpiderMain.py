from spider.UrlManager import UrlManager
from spider.HtmlDownloader import HtmlDownloader
from spider.HtmlOutputer import HtmlOutputer
from spider.HtmlParser import HtmlParser


class Spider(object):

    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.htmloutputer = HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.htmloutputer.collect_data(new_data)

                if count == 10:
                    break
                count += 1
            except:
                print 'Craw Failed'

        self.htmloutputer.output_html()

if __name__ == "__main__":
    root_url = "https://en.wikipedia.org/wiki/Python"
    spider = Spider()
    spider.craw(root_url)