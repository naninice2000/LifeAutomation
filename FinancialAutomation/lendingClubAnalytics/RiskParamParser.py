#! /usr/bin/python 

import json 

class RiskParamParser:
	debt_to_income_ratio=0
	credit_utilization=0
	credit_score=0
	LoanRiskConfigMap={}

	
	def __init__(self,risk_level):
		try:
			self.json_data=open("./conf/Risk_Config.conf").read()
		except: 
			print "not able to read confi file at location ./conf/Risk_Config.conf"
		else: 
			self.json_config_data = json.loads(self.json_data)
		
		if(risk_level=="Lowest"):
			self.risk_level_param = 0
		elif(risk_level=="Low"):
			self.risk_level_param=1
		elif(risk_level=="Medium"):
			self.risk_level_param=2
		elif(risk_level=="High"):
			self.risk_level_param=3
		else:
			self.risk_level_param=4

	def setRiskLevel(self):
		self.risk_level=risk_level
		
	def getCreditScore(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskType"]["credit_score"]
		
	def getDTIRatio(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskType"]["debt_to_income_ratio"]

	def getCreditUtilization(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskType"]["credit_utilization"]

	def getDelinquencyHistory(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskType"]["Delinquencies"]

	def getLoanTerm(self):
		return self.json_config_data["RiskDataSet"][self.risk_level_param]["RiskType"]["loan_term"]
