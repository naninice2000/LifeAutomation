#! /usr/bin/python 

class DataInspection:
	debt_to_income_ratio=0
	credit_utilization=0
	credit_score=0
	LoanMap= {}

	def __init__(self):
		self.debt_to_income_ratio=10
		self.credit_utilization=10
		self.credit_score=740

	def setDataSource(self,inputfile): 
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
				self.LoanMap[data[0]]=datalist
		datafile.close()


	def checkForCreditScore(self,LoanMap):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			fico_range_lower = int(loanDetails[38].replace('"',''))
			if(fico_range_lower>lowerlimit):
				#print LoanID,fico_range_lower,lowerlimit
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap

	def checkForDebtToIncomeRatio(self,upperlimit,LoanMap):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			debt_to_income_ratio = float(loanDetails[34].replace('"',''))
			if(debt_to_income_ratio<=upperlimit):
				#print debt_to_income_ratio
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap

	def checkForCreditUtilization(self,upperlimit,LoanMap):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			revolving_credit_utilization = float(loanDetails[51].replace('"',''))
			if(revolving_credit_utilization<=upperlimit):
				#print LoanID,revolving_credit_utilization
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap

	def checkForNoDelinquencyHistory(self,LoanMap):
		updatedLoanMap={}
		for LoanID in LoanMap.keys():
			loanDetails=LoanMap[LoanID]
			delinquency_history = loanDetails[56].replace('"','')
			#print revolving_credit_utilization
			if(delinquency_history == " "):
				#print LoanID,delinquency_history
				updatedLoanMap[LoanID]=loanDetails
		return updatedLoanMap

	def checkForDelinquencyHistoryNumber(self,low_limit,high_limit):

	def checkForEmploymentLength(self,min_num_years):

	def checkForHomeType(self,home_owner_ship):

