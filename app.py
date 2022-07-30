from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(title=title, message=message,
                        app_icon="./images/img.ico", timeout=5)


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        htmlData = getData(
            "https://www.worldometers.info/coronavirus/country/pakistan/")
        soup = BeautifulSoup(htmlData, 'html.parser')
        # print(soup.prettify())
        data = []
        for content in soup.find_all("span"):
            data.append(content.get_text())

        # print(data)

        properData = []

        for d in data:
            if "," in d:
                properData.append(d)

        properData = properData[0:3]
        totalCases = properData[0]
        deaths = properData[1]
        recoveries = properData[2]

        s = f"Total Cases: {totalCases}\nDeaths: {deaths}\nRecoveries: {recoveries}"
        notifyMe("Cases in Pakistan", s)
        # enter your desired time difference between each notification
        time.sleep(10)
