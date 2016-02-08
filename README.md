# LifeAutomation

LifeAutomation project started with good intention to help users in reducing time spent on non productive things or
things which they perfom regularly. Such as playing certain type of music, making financial investments based on custom 
defined risk, Running investment perform analytics ect, not limited to this in near future these features are going to
be enhanced to automate as much small task as possible evening using 3rd part hardware and software components. 


-----------------------------------------
FinancialAutomation: 
-----------------------------------------
Part of this automation, i would like to automate analytics for good investments, which can help users to perform 
analytics on different type investments.

****************************
Part1: LendingClubAnalytics:
**************************** 
Building personal customizable investments which can help people to get returns and define their own risk factor. 

Risk definations can be updated from confi file present in ./conf/Risk_Config.conf 
This file is available in JSON format, you can find sample below: 

{
	"RiskType":"Lowest",
	"RiskFactors": {
        "credit_score":800,
        "debt_to_income_ratio":10,
        "credit_utilization":10,
        "home_ownership":"",
        "loan_term":36,
        "open_credit_lines":10,
        "Delinquencies":0
	}
}

There are 4 risk types starting from Lowest to High, in these RiskTypes you have parameters credit score, credit utilization, debt to income ration ect. 
You can find different parameters which are very critical for making decission in peer to peer lending. 

For more details about LendingClubAnalytics Automation details are available in Readme.txt inside FinancialAutomation directory
