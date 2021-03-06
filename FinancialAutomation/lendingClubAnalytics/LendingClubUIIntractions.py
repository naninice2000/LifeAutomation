import selenium 
from selenium import webdriver

import sys 
import glob, os
import shutil
import os.path 


class LendingClub:
	username=""
	password=""
	currentDirectory=os.getcwd()
	currentInputDirectory = "inputdir"

	#FirefoxProfile profile = webdriver.FirefoxProfile();
	profile = webdriver.FirefoxProfile()
	profile.set_preference('browser.download.manager.showWhenStarting', False )
	profile.set_preference('browser.download.folderList', 2) # option 2 means custom location
	profile.set_preference('browser.download.useDownloadDir', True)
	download_dir = currentDirectory+"/"
	profile.set_preference('browser.download.dir',download_dir)
	profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
	profile.update_preferences()
	browser=webdriver.Firefox(profile)
	
	def __init__(self,username,password):
		self.username=username
		self.password=password
		self.currentDirectory=os.getcwd()
		self.currentInputDirectory = self.currentDirectory+"/inputdir/"
		if not os.path.exists(self.currentInputDirectory):
			os.makedirs(self.currentInputDirectory)
		

	def open_lending_club(self,url):
		self.browser.get(url)

	def wait_for_some_time(self,time):
		self.browser.implicitly_wait(time)

	def login_into_account(self,username,password):
		singin_button = self.browser.find_element_by_id("master_sign-in-link")
		singin_button.click()
		self.wait_for_some_time(10)
		username_element = self.browser.find_element_by_id("email")
		username_element.click()
		username_element.clear()
		username_element.send_keys(username)
		password_element = self.browser.find_element_by_id("password")
		password_element.click()
		password_element.clear()
		password_element.send_keys(password)
		login_button = self.browser.find_element_by_id("master_accountSubmit")
		login_button.click()

	def browse_investment_notes(self):
		self.browser.implicitly_wait(180)
		self.browser.find_element_by_link_text("Browse Loans").click()
		self.browser.implicitly_wait(180)

	def open_loan_url(self,url):
		self.browser.get(url)

	def download_latest_note_info(self,inputdir,default_download_dir):
		self.browser.implicitly_wait(30)
		oldFile = inputdir+"primaryMarketNotes_browseNotes_1-RETAIL.csv"
		print oldFile
		if(os.path.isfile(oldFile)):
			print "deleting the old file before downloading latest note information"
			os.remove(oldFile)
		print "downloading new csv file"
	
		link = self.browser.find_element_by_id("browseDownloadAllLink")
		link.click()

		href = link.get_attribute('href')
		download = self.browser.get(href)
		self.browser.implicitly_wait(180)
		downloaded_file = default_download_dir+"primaryMarketNotes_browseNotes_1-RETAIL.csv"
		temp_file = downloaded_file+".part"
		while(os.path.isfile(temp_file)):
			self.browser.implicitly_wait(180)
			print "waiting for download to be completed.."
		shutil.move(downloaded_file,inputdir)

		
	def add_investment_to_order(self):
		browser.find_element_by_link_text("Add to Order").click

	def view_investment_order(self):
		browser.find_element_by_link_text("View order").click

	def complete_order(self):
		browser.find_element_by_link_text("Continue ").click 

	def close_browser(self):
		self.browser.close()
		








