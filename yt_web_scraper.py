from selenium import webdriver
from bs4 import BeautifulSoup

urls = ["https://www.youtube.com/@sharinrehan/shorts"]
# #  We can use this code for multiple yt channels by putting links in the List array

def main():
    driver = webdriver.Firefox()
    driver.get(urls[0])
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')                   # # lxml html parser
    titles = soup.findAll('span', id='video-title')
    # # I got the span tag by inspecting the html of the hyperlink of the yt-short
    # # <span id="video-title" class="style-scope ytd-rich-grid-slim-media">#cute ayzu doing work for mimi#</span>

    views = soup.findAll('span', class_='inline-metadata-item style-scope ytd-video-meta-block')
    # # <span class="inline-metadata-item style-scope ytd-video-meta-block">{} views</span>

    i = 0       # # for views index position because views is a List
    channel_name = soup.select_one(".style-scope ytd-channel-name")
    print(f"Channel name: {channel_name.getText()}")
    for title in titles:
        print('\n{}\t{}\t'.format(title.text, views[i].text))


main()
