#! /usr/bin/python 

import sys
import os
from CalcualteIncome import *
from GenerateHTMLReport import *


input_dir = sys.argv[1]
input_dir=os.path.dirname(os.path.realpath(sys.argv[0]))+input_dir
list_file=os.listdir(input_dir)
total_interest=0
total_principle=0
total_fee=0
data_map = {}
date_range_map_interest={}
date_range_map_princi={}

for f in list_file: 
	filename=input_dir+f
	calcualtor = IncomeCalcualtor(filename)
	calcualtor.parse_30days_csv_file()
	total_interest=total_interest+calcualtor.get_monthly_interest_earned()
	total_fee=total_fee+calcualtor.get_monthly_fee_paid()
	total_principle=total_principle+calcualtor.get_monthly_principle_collected()
	date_range=str(calcualtor.get_statement_starting_date())+" to "+str(calcualtor.get_statement_ending_date())
	date_range_map_interest[date_range]=calcualtor.get_monthly_interest_earned()
	date_range_map_princi[date_range]=calcualtor.get_monthly_principle_collected()
	
data_map['Interest']=total_interest
data_map['Total Fee (-)']=(-1*total_fee)
data_map['Principle']=total_principle

gen_report = GenerateHTMLReport()
gen_report.createPieChart(data_map)
#gen_report.createInterestReceivedPatern(date_range_map_interest)
gen_report.createIncomePatternLineChart(date_range_map_interest,date_range_map_princi)

gen_report.generte_html_file()

