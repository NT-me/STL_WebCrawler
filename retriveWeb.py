import csv
import requests as r
import re


def cleanString(raw):
    if '"' in raw:
        raw = raw.replace('"', "")

    if '<' in raw:
        raw = raw.replace('<', "")

    if '>' in raw:
        raw = raw.split('>')[0]
    return raw



def getURLsFromHtml(source, oldUrls):
    page = r.get(source).text
    urlsInPage = re.findall(r'(https?://[^\s]+)', page)
    urlsInPage = list(set(urlsInPage) - set(oldUrls))
    urlsInPage = [cleanString(item) for item in urlsInPage]
    return urlsInPage
