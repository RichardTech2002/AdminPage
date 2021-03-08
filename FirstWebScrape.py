"""Called libraries"""
from flask import Flask
import scraper
import tkinter
import requests
from bs4 import BeautifulSoup


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""Scraper section"""
def maincommand(ScrapeSite):
    url = 'https://www.nzdirectory.co.nz/antiques.html'
    page_html = requests.get(url)
    #print(page_html)
    html_soup = BeautifulSoup(page_html.text, 'html.parser')
    items = html_soup.find_all('div', class_="")
    Web_list = []

    for items in Web_list:
        
        title=items.find('div', class_="/html/body/section/div[1]/ul/li[3]/a").text
        address=items.find('div', class_="/html/body/section/div[2]/div/ul/li[2]/div/div[1]").text
        Web_list.append([title,address])
        print(str(title) + str(price))
    return Web_list

    ScrapeSite = ("https://www.nzdirectory.co.nz/antiques-advertising.html")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""Tkinter section. This isn't really necassary"""

window = tkinter.Tk()
window.geometry("220x70")
window.title ("Click the button")
label = tkinter.Label (window, text = "Click the button").pack

mainbutton = tkinter.Button(window, text = "Click to scrape!",font = ('arial', 20), command=maincommand, bg = "powder blue").grid(row = 0,column = 0)

window.mainloop()