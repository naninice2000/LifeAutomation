#! /usr/bin/python 

import json 

class RiskParamParser:
	debt_to_income_ratio=0
	credit_utilization=0
	credit_score=0
	LoanRiskConfigMap={}
	risk_level_param=0
	
	def __init__(self,risk_level):
		risk_level=risk_level.upper()
		try:
			self.json_data=open("./conf/Risk_Config.conf").read()
		except: 
			print "not able to read confi file at location ./conf/Risk_Config.conf"
		else: 
			self.json_config_data = json.loads(self.json_data)
		
		if(risk_level=="LOWEST"):
			self.risk_level_param=0
		elif(risk_level=="LOW"):
			print "Risk level is set as Low"
			self.risk_level_param=1
		elif(risk_level=="MEDIUM"):
			self.risk_level_param=2
		elif(risk_level=="HIGH"):
			self.risk_level_param=3
		else:
			self.risk_level_param=4

	def setRiskLevel(self):
		self.risk_level=risk_level
		
	def getCreditScore(self):
		score = int(self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskFactors"]["credit_score"])
		return score
		
	def getDTIRatio(self):
		DTI = int(self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskFactors"]["debt_to_income_ratio"])
		return DTI 
		
	def getCreditUtilization(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskFactors"]["credit_utilization"]

	def getDelinquencyHistory(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskFactors"]["Delinquencies"]

	def getLoanTerm(self):
		return int(self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskFactors"]["loan_term"])
