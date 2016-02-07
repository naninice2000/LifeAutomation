#! /usr/bin/python 

import json 

class RiskParamParser:
	debt_to_income_ratio=0
	credit_utilization=0
	credit_score=0
	LoanRiskConfigMap={}
	json_config_data=json.loads({})
	risk_level=""
	LowestRiskDataMap={}
	owRiskDataMap={}
	MediumRiskDataMap={}
	HighRiskDataMap={}
	HighestRiskDataMap={}

	def __init__(self):
		try:
			json_data=open("./conf/Risk_Config.conf").read()
		except: 
			print "not able to read confi file at location ./conf/Risk_Config.conf"
		else: 
			json_config_data = json.loads(json_data)
			LowestRiskDataMap["credit_score"]=data["RiskDataSet"][0]["RiskFactors"]["credit_score"]
			LowestRiskDataMap["credit_utilization"]=data["RiskDataSet"][0]["RiskFactors"]["credit_utilization"]
			LowestRiskDataMap["debt_to_income_ratio"]=data["RiskDataSet"][0]["RiskFactors"]["debt_to_income_ratio"]
			LowRiskDataMap["credit_score"]=data["RiskDataSet"][1]["RiskFactors"]["credit_score"]
			LowRiskDataMap["credit_utilization"]=data["RiskDataSet"][1]["RiskFactors"]["credit_utilization"]
			LowRiskDataMap["debt_to_income_ratio"]=data["RiskDataSet"][1]["RiskFactors"]["debt_to_income_ratio"]
			MediumRiskDataMap["credit_score"]=data["RiskDataSet"][2]["RiskFactors"]["credit_score"]
			MediumRiskDataMap["credit_utilization"]=data["RiskDataSet"][2]["RiskFactors"]["credit_utilization"]
			MediumRiskDataMap["debt_to_income_ratio"]=data["RiskDataSet"][2]["RiskFactors"]["debt_to_income_ratio"]
			HighRiskDataMap["credit_score"]=data["RiskDataSet"][3]["RiskFactors"]["credit_score"]
			HighRiskDataMap["credit_utilization"]=data["RiskDataSet"][3]["RiskFactors"]["credit_utilization"]
			HighRiskDataMap["debt_to_income_ratio"]=data["RiskDataSet"][3]["RiskFactors"]["debt_to_income_ratio"]
			HighestRiskDataMap["credit_score"]=data["RiskDataSet"][4]["RiskFactors"]["credit_score"]
			HighestRiskDataMap["credit_utilization"]=data["RiskDataSet"][4]["RiskFactors"]["credit_utilization"]
			HighestRiskDataMap["debt_to_income_ratio"]=data["RiskDataSet"][4]["RiskFactors"]["debt_to_income_ratio"]


	def setRiskLevel(self,risk_level):
		self.risk_level=risk_level
		
	def getCreditScore(self):
		
	def getDTIRatio(self):

	def getCreditUtilization(self):
 