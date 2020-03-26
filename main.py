from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
	notification.notify(
		title=title,
		message=message,
		app_icon="Your icon location",
		timeout=15
	)


def getData(url):
	r=requests.get(url)
	return r.txt

if __name__ == '__main__':
	while True:

		notifyMe("Covid-19 Updates","Warning")
		myHtmlData=getData('https://www.mohfw.gov.in/')

		#print(myHtmlData)
		soup=BeautifulSoup(myHtmlData,'html.parser')
		#print(soup.preetify())

		myDataStr=""

		for tr in soup.find_all('tbody')[1].find_all('tr'):
			#print(tr.get_text())
			myDataStr+= tr.get_text()
		myDataStr=myDataStr[1:]
		itemList= myDataStr.split("\n\n")


		states=['Chandigarh', 'Chandigarh', 'Punjab', 'Uttar Pradesh', 'Kerala', 'Delhi']

		for item in itemList[0:21]:
			dataList=item.split('\n')
			if dataList[1] in states:
				print(dataList)
				nTitle='Cases of COVID-19'
				nText=f"STATE {dataList[1]} Indian:{dataList[2]}  Foreign: {dataList[3]}\n Deaths: {dataList[4]}\n Cured: {dataList[5]}"
				notifyMe(nTitle,nText)
				time.sleep(2)

		time.sleep(3600)











