from datetime import datetime
from bs4 import BeautifulSoup

import requests

def getTime():
    now = datetime.now()
    return str(now.hour).rjust(2, "0") + ":" + str(now.minute).rjust(2, "0")


def getDateTime():
    now = datetime.now()
    return str(now.year).rjust(4, "0") + str(now.month).rjust(2, "0") + str(now.day).rjust(2, "0") + str(
        now.hour).rjust(2, "0") + str(now.minute).rjust(2, "0")


def getJson(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}
    request = requests.get(url, headers=header)
    return request.json()


def getHTML(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}
    request = requests.get(url, headers=header)
    return str(request.content)


def getBandInfo(band):
    name = band[0].split('>')[1].replace('</a', '')
    idBand = band[0].split('"')[1].split('/')[-1]
    return [name, idBand]


def getLinks(htmlString):
    soup = BeautifulSoup(htmlString, 'html.parser')
    return soup.find_all('td')


def searchLinks(bandName, genre, country, yearCreationFrom, yearCreationTo, bandNotes, status, themes, location,
                bandLabelName):
    iDisplayStart = 0
    response = getJson(
        "https://www.metal-archives.com/search/ajax-advanced/searching/bands/?bandName=" + bandName + "&genre=" + genre
        + "&country=" + country + "&yearCreationFrom=" + yearCreationFrom + "&yearCreationTo=" + yearCreationTo +
        "&bandNotes=" + bandNotes + "&status=" + status + "&themes=" + themes + "&location=" + location +
        "&bandLabelName=" + bandLabelName + "&sEcho=2&iColumns=3&sColumns=&iDisplayStart=" + str(
            iDisplayStart) + "&iDisplayLength=200&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&_=1590665381828")
    iTotalRecords = response["iTotalRecords"]

    results = list()

    while iDisplayStart < iTotalRecords:
        bands = []
        for band in response["aaData"]:
            bands.append(getBandInfo(band))

        for band in bands:
            links = getLinks(getHTML("https://www.metal-archives.com/link/ajax-list/type/band/id/" + band[1]))

            for link in links:
                if link.get_text() == "Spotify":
                    spotifyLink = (str(link).split('"')[1])
                    results.append([str(band[0]), spotifyLink])
        iDisplayStart += 200
        url = "https://www.metal-archives.com/search/ajax-advanced/searching/bands/?bandName=" + bandName + "&genre=" + genre + "&country=" + country + "&yearCreationFrom=" + yearCreationFrom + "&yearCreationTo=" + yearCreationTo + "&bandNotes=" + bandNotes + "&status=" + status + "&themes=" + themes + "&location=" + location + "&bandLabelName=" + bandLabelName + "&sEcho=2&iColumns=3&sColumns=&iDisplayStart=" + str(
            iDisplayStart) + "&iDisplayLength=200&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&_=1590665381828"
        response = getJson(url)
    return results


def saveToHTML(linkList, bandName, genre, country, yearCreationFrom, yearCreationTo, bandNotes, status, themes,
               location, bandLabelName):
    fileName = str(getDateTime() + " " +
                   (bandName.capitalize() + "-" if len(bandName) > 0 else "") +
                   (genre.capitalize() + "-" if len(genre) > 0 else "") +
                   (country.capitalize() + "-" if len(country) > 0 else "") +
                   (yearCreationFrom.capitalize() + "-" if len(yearCreationFrom) > 0 else "") +
                   (yearCreationTo.capitalize() + "-" if len(yearCreationTo) > 0 else "") +
                   (bandNotes.capitalize() + "-" if len(bandNotes) > 0 else "") +
                   (status.capitalize() + "-" if len(status) > 0 else "") +
                   (themes.capitalize() + "-" if len(themes) > 0 else "") +
                   (location.capitalize() + "-" if len(location) > 0 else "") +
                   (bandLabelName.capitalize() if len(bandLabelName) > 0 else ""))
    file = open(fileName + ".html", "w")
    for link in linkList:
        try:
            file.write('<a href="' + link[1] + '">' + link[0] + "</a><br>")
        except:
            continue
    file.close()
    return file
