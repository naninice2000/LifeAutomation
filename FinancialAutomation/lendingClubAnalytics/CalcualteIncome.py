#! /usr/bin/python

import glob
import os
from datetime import datetime, date, time


class IncomeCalcualtor:
	total_interest=0
	total_fee=0
	total_amount_reiceved=0
	directory_path=""
	file_list=[]
	statement_starting_date = date(1999,01,01)
	statement_ending_date = date(1999,01,01)
	def __init__(self,directory_path):
		print "calcualting income recived for specific duration"
		self.directory_path=directory_path
	def get_list_of_files(self):
		return os.listdir(os.path.dirname(os.path.realpath(sys.argv[0])))
	def parse_30days_csv_file(self):
		try: 
			fh=open(self.directory_path,"r")
		except: 
			print "not able to read the file"
		else:
			for line in fh:
				line=line.rstrip()
				datalist=line.split(",")
				if(datalist[1] != "Date"):
					date_info=datalist[1].split("/")
					if(self.statement_starting_date == date(1999,01,01)):
						self.statement_starting_date = date(int(date_info[2]),int(date_info[0]),int(date_info[1]))
					elif(self.statement_starting_date > date(int(date_info[2]),int(date_info[0]),int(date_info[1]))):
						self.statement_starting_date = date(int(date_info[2]),int(date_info[0]),int(date_info[1]))
					if(self.statement_ending_date == date(1999,01,01)):
						self.statement_ending_date = date(int(date_info[2]),int(date_info[0]),int(date_info[1]))
					elif(self.statement_ending_date < date(int(date_info[2]),int(date_info[0]),int(date_info[1]))):
						self.statement_ending_date = date(int(date_info[2]),int(date_info[0]),int(date_info[1]))
				
				if(datalist[2] == "T11_BORROWER_MTL_PYMT_TO_LENDER"):
					self.total_interest=self.total_interest+float(datalist[7])
					self.total_amount_reiceved=self.total_amount_reiceved+float(datalist[4])
				elif(datalist[2] == "T8_LENDER_PAYS_SERVICE_FEE"):
					self.total_fee=self.total_fee+float(datalist[4])
			fh.close()

	def get_monthly_total_recived(self):
		return self.total_amount_reiceved
	def get_monthly_interest_earned(self):
		return self.total_interest
	def get_monthly_fee_paid(self):
		return self.total_fee
	def get_monthly_principle_collected(self):
		return (self.total_amount_reiceved-self.total_interest)
	def write_data_to_db(self):
		print "TBD"

	def get_statement_starting_date(self):
		return self.statement_starting_date
	def get_statement_ending_date(self):
		return self.statement_ending_date

