from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import selenium
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time 
import random

# Return 
def _getData(data, url):
    options = webdriver.ChromeOptions()
    print(url)
    driver = webdriver.Chrome(executable_path=r""+ data)
    driver.get(url)
    # driver.implicitly_wait()
    content = driver.page_source.encode('utf-8').strip()
    soup_pages = soup(content, 'lxml')

    timeData = []
    titles = soup_pages.findAll('a', id='video-title')
    video_urls = soup_pages.findAll('a',id='video-title')
    channelData = []

    title = []
    videoUrls = []

    i = 0
    for item in titles:
        title.append(item.text)
        videoUrls.append(video_urls[i].get('href'))
        i+=1

    driver.quit()

    df = pd.DataFrame()

    df['title'] = title
    df['vidUrl'] = videoUrls

    return df

# --------------> Child-Functions
# Get Single Page Data views
def transformViews(string):
    View = ''
    k = 0
    hold = []
    numberHold = ['0','1','2','3','4','5','6','7','8','9']
    toFloat = ''
    for i in string:
        for j in numberHold:
            if i == j:
                hold.append(i)
    for i in hold:
        toFloat = toFloat + i

    transformView = float(toFloat)
    return transformView

#Transforms string to float
def transformLikes(string):
    if string == 'No likes':
        return 0
    else:
        View = ''
        hold = []
        numberHold = ['0','1','2','3','4','5','6','7','8','9']
        toFloat = ''
        for i in string:
            for j in numberHold:
                if i == j:
                    hold.append(i)
        for i in hold:
            toFloat = toFloat + i
        transformLike = float(toFloat)
        return transformLike

#Transforms string to float
def transformDislikes(string):
    if string == 'No dislikes':
        return 0
    else:
        View = ''
        hold = []
        numberHold = ['0','1','2','3','4','5','6','7','8','9']
        toFloat = ''
        for i in string:
            for j in numberHold:
                if i == j:
                    hold.append(i)
        for i in hold:
            toFloat = toFloat + i
        transformDislikes = float(toFloat)
        return transformDislikes

# Returns Single Page Data
def getSPD(driver, url):
    transformedUrl = 'http://www.youtube.com' + url

    driver = webdriver.Chrome(executable_path=r"" + driver)
    driver.get(transformedUrl)
    driver.implicitly_wait(10)
    views = driver.find_element_by_css_selector('span.view-count').text
    title = driver.find_element_by_css_selector('h1.title').text
    likes = driver.find_element_by_id('top-level-buttons').find_element_by_id('text').get_attribute('aria-label')
    dislikes = driver.find_element_by_id('top-level-buttons').find_elements_by_id('text')
    date = driver.find_element_by_id('date').find_element_by_css_selector('yt-formatted-string.style-scope').text
    j = 0
    for i in dislikes:
        dislikes = i.get_attribute('aria-label')
        if j == 1: break
        j+=1

    view = transformViews(views)
    likes = transformLikes(likes)
    dislikes = transformDislikes(dislikes)
    driver.quit()
    return view, title, likes, dislikes, date

# <--------

# Init timer
def _getVideoData(driver, min, max, data):
    views = []
    titles = []
    likes = []
    dislikes = []
    dates = []

    k = 0
    t = random.randint(min, max)
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    if t == 0:
        view, title, like, dislike, date = getSPD(driver, data)
        views.append(view)
        titles.append(title)
        likes.append(like)
        dislikes.append(dislike)
        dates.append(date)
  
    df = pd.DataFrame()

    df['date'] = dates
    df['titles'] = titles
    df['views'] = views
    df['likes'] = likes
    df['dislikes'] = dislikes

    return df


