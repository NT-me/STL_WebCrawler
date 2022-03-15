from retriveWeb import getURLsFromHtml
from createCSV import createTwoCSV, createdomName
import random

if __name__ == "__main__":
    startPoint = 'https://fr.wikipedia.org/'

    oldUrls = []
    ret = dict()
    ret[startPoint] = getURLsFromHtml(startPoint, oldUrls)
    lastUrl = startPoint

    for i in range(0, 30):
        if ret[lastUrl]:
            currentUrl = random.choice(ret[lastUrl])

        try:
            ret[currentUrl] = getURLsFromHtml(currentUrl, oldUrls)
            if ret[currentUrl] != []:
                lastUrl = currentUrl
            # oldUrls = ret[lastUrl]
        except:
            ret[lastUrl].remove(currentUrl)
    createTwoCSV(ret)
