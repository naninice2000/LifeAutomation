#######################################################################################################
# Description: This script will help you to filter the peer to peer lending options based on 		  #
#			   No Delinquency, Revolving Line Utilization < 15%, Debt-to-Income ratio less than 10%  #
#			   Credit Scrore > 720  #
######################################################################################################
#! /usr/bin/python 

import sys
from LendingClubUIIntractions import * 
import platform
import glob,os
import os.path 


inputfile=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
expected_min_interest_rate=float(sys.argv[4])
default_download_dir = sys.argv[5]


LowestRisk={"Credit_Score":760,"DTI":10,"MaxCreditUtilization":10,"RequestedLoanToIncomeFactor":0.10}
LowRisk={"Credit_Score":720,"DTI":20,"MaxCreditUtilization":25,"RequestedLoanToIncomeFactor":0.25}
MediumRisk={"Credit_Score":680,"DTI":20,"MaxCreditUtilization":50,"RequestedLoanToIncomeFactor":0.50}
HighRisk={"Credit_Score":600,"DTI":20,"MaxCreditUtilization":65,"RequestedLoanToIncomeFactor":0.65}
HighestRisk={"Credit_Score":500,"DTI":20,"MaxCreditUtilization":80,"RequestedLoanToIncomeFactor":1}

LoanMap={}
#expected_min_interest_rate=raw_input("Please enter minimun expected rate of interest looking to earn:")


currentDirectory=os.getcwd()
currentInputDirectory=""
if(platform.system() == "Windows"):
	currentInputDirectory = currentDirectory+"/inputdir/"
else:
	currentInputDirectory = currentDirectory+"/inputdir/"

if not os.path.exists(currentInputDirectory):
	os.makedirs(currentInputDirectory)

	
def read_note_data_file():
	try: 
		datafile=open(inputfile,"r")
	except: 
		print "not able to open input data file which is provided from command line as input please check the file locaiton and path",inputfile
	else: 
		for line in datafile.readlines()[1:]: 
			line=line.rstrip()
			data=line.split(",")
			datalist=[]
			for i in data:
				datalist.append(i)
			LoanMap[data[0]]=datalist
		datafile.close()


########################################################################################################
# Description: This function will return the list of loans which are going to be with mini fico score  #
# what ever we pass to lowerlimit
########################################################################################################

def checkForCreditScore(lowerlimit):
	updatedLoanMap={}
	for LoanID in LoanMap.keys():
		loanDetails=LoanMap[LoanID]
		fico_range_lower = int(loanDetails[38].replace('"',''))
		if(fico_range_lower>lowerlimit):
			#print LoanID,fico_range_lower,lowerlimit
			updatedLoanMap[LoanID]=loanDetails
	return updatedLoanMap

def checkForDebtToIncomeRatio(upperlimit):
	updatedLoanMap={}
	for LoanID in LoanMap.keys():
		loanDetails=LoanMap[LoanID]
		debt_to_income_ratio = float(loanDetails[34].replace('"',''))
		if(debt_to_income_ratio<=upperlimit):
			#print debt_to_income_ratio
			updatedLoanMap[LoanID]=loanDetails
	return updatedLoanMap

def checkForCreditUtilization(upperlimit):
	updatedLoanMap={}
	for LoanID in LoanMap.keys():
		loanDetails=LoanMap[LoanID]
		revolving_credit_utilization = float(loanDetails[51].replace('"',''))
		if(revolving_credit_utilization<=upperlimit):
			#print LoanID,revolving_credit_utilization
			updatedLoanMap[LoanID]=loanDetails
	return updatedLoanMap

def checkIncomeLowerLimit(lowerLimit):
	updatedLoanMap={}
	for LoanID in LoanMap.keys():
		loanDetails=loanMap[LoanID]
		income_amount = float(loanDetails[14].replace('"',''))
		if(income_amount<=lowerLimit):
			updatedLoanMap[LoanID]=loanDetails
	return updatedLoanMap
	
def getRequestedDebitToIncomeFactor(income_amount,debit):
	requestedDebitToIncomeFactor = 0
	requestedDebitToIncomeFactor = debit/income_amount
	return requestedDebitToIncomeFactor


def checkForRiskFactor(request_factor):
	updatedLoanMap={}
	for LoanID in LoanMap.keys():
		loanDetails=LoanMap[LoanID]
		AnnualGrossIncome = loanDetails[14].replace('"','')
		RequestedLoanAmount = loanDetails[2].replace('"','')
		# print revolving_credit_utilization
		if(request_factor <= getRequestedDebitToIncomeFactor(float(AnnualGrossIncome),float(RequestedLoanAmount))):
			print LoanID,request_factor,getRequestedDebitToIncomeFactor(float(AnnualGrossIncome),float(RequestedLoanAmount))
			updatedLoanMap[LoanID]=loanDetails
	return updatedLoanMap
	
def checkForNoDelinquencyHistory():
	updatedLoanMap={}
	for LoanID in LoanMap.keys():
		loanDetails=LoanMap[LoanID]
		delinquency_history = loanDetails[56].replace('"','')
		#print revolving_credit_utilization
		if(delinquency_history == " "):
			#print LoanID,delinquency_history
			updatedLoanMap[LoanID]=loanDetails
	return updatedLoanMap

	
	
print "*************************************************************************"
print "                     Peer to Peer Lending Optimizer                      "
print "Algoritham Author: Venkata "
print "Build: 0.1 "
print "*************************************************************************"

lending_club_ui = LendingClub(username,password)
lending_club_ui.open_lending_club("https://www.lendingclub.com/")
#lending_club_ui.wait_for_some_time(10)
lending_club_ui.login_into_account(username,password)
lending_club_ui.wait_for_some_time(10)
lending_club_ui.browse_investment_notes()
lending_club_ui.wait_for_some_time(10)
lending_club_ui.download_latest_note_info(currentInputDirectory,default_download_dir)
lending_club_ui.wait_for_some_time(10)
print "Downloading latest note information completed"
		
read_note_data_file()
LoanMap=checkForCreditScore(720)
LoanMap=checkForDebtToIncomeRatio(20)
LoanMap=checkForCreditUtilization(20)
LoanMap=checkForNoDelinquencyHistory()
LoanMap=checkForRiskFactor(0.25)
for loanid in LoanMap.keys():
	loan_details=LoanMap[loanid]
	interest_rate = loan_details[5].replace('"','')
	if(expected_min_interest_rate<=float(interest_rate)):
		interest_rate=interest_rate+"%"
		loan_url = loan_details[22].replace('"','')
		print "Loan id with possible reduced risk",loanid
		print "Interest Rate:",interest_rate
		print "URL:",loan_url
		lending_club_ui.open_loan_url(loan_url)
		print "*************************************************************************"

lending_club_ui.close_browser()

