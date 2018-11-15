import bs4
import requests

def getFollowersAndFollowees():
  url_data = requests.get('https://twitter.com/baseballmarc_mm')

  html_data = url_data.text

  soup = bs4.BeautifulSoup(html_data, "html.parser")

  followers = soup.select('span.ProfileNav-value')[1].text
  followees = soup.select('span.ProfileNav-value')[2].text

  return f'【Twitterの現在のフォロワー数】{followers}人 \n【Twitterの現在のフォロー数】{followees}人'
