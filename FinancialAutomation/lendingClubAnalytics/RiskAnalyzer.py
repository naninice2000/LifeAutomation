#! /usr/bin/python 

import csv

class RiskAnalyzer:
	
	LoanMap= {}

	def __init__(self):
		print "Analyzing risk.."

	def setDataSource(self,inputfile): 
		with open(inputfile, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				print ', '.join(row)

		


	def checkForCreditScore(self,lowerlimit):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			fico_range_lower = int(loanDetails[38].replace('"',''))
			if(fico_range_lower>lowerlimit):
				#print LoanID,fico_range_lower,lowerlimit
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap

	def checkForDebtToIncomeRatio(self,upperlimit):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			debt_to_income_ratio = float(loanDetails[34].replace('"',''))
			if(debt_to_income_ratio<=upperlimit):
				#print debt_to_income_ratio
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap

	def checkForCreditUtilization(self,upperlimit):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			revolving_credit_utilization = float(loanDetails[51].replace('"',''))
			if(revolving_credit_utilization<=upperlimit):
				#print LoanID,revolving_credit_utilization
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

	
	def checkIncomeLowerLimit(lowerLimit):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=loanMap[LoanID]
			income_amount = float(loanDetails[14].replace('"',''))
			if(income_amount<=lowerLimit):
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap
	
	def optimizeAvailableLoans(self,risk_factor):

		self.LoanMap=checkForCreditScore()
		self.LoanMap=checkForDebtToIncomeRatio()
		self.LoanMap=checkForCreditUtilization()
		self.LoanMap=checkForNoDelinquencyHistory()


