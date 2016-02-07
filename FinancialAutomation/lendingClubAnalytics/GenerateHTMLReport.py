#! /usr/bin/python 

import sys
import os

class GenerateHTMLReport:
	html_tmp_header="<html><head><script type=\"text/javascript\" src=\"https://www.google.com/jsapi\"></script>"
	html_tmp_footer="</head><body>"
	tmp_chart_data=""
	div_count=1
	report_file_name = "./report/report.html"
	def __init__(self):
		self.tmp_chart_data=""
	def createPieChart(self,data_map):
		div_id="chart_"+str(self.div_count)
		section_header="<script type=\"text/javascript\">google.load(\"visualization\", \"1\", {packages:[\"corechart\"]});google.setOnLoadCallback(drawChart);function drawChart() {var data = google.visualization.arrayToDataTable([['Task', 'Hours per Day'],"
		section_footer=" ]); var options = {title: 'Spending per location chart',is3D: true,};var chart = new google.visualization.PieChart(document.getElementById('"+div_id+"'));chart.draw(data, options);}</script>"
		chart_data = ""
		for i in data_map:
			chart_data=chart_data+"['"+i+"',"+str(data_map[i])+"],"
		self.div_count=self.div_count+1
		self.tmp_chart_data=self.tmp_chart_data+section_header+chart_data.rstrip()+section_footer
	
	def createIncomePatternLineChart(self,interest_map,princi_map):
		div_id="chart_"+str(self.div_count)
		section_header=" <script type=\"text/javascript\">google.load('visualization', '1.1', {packages: ['line']});google.setOnLoadCallback(draw_monthly_interest_chart);function draw_monthly_interest_chart() {var data = new google.visualization.DataTable();data.addColumn('string', 'Duration');data.addColumn('number', 'Interest earned','Principle Collected');data.addRows(["
		section_footer="]);var options = {chart: {title: 'Interest earned during statement period',subtitle: 'in USD'},axes: {x: {0: {side: 'top'}}}};var chart = new google.charts.Line(document.getElementById('"+div_id+"'));chart.draw(data, options);} </script>"
		section_map_data=""
		for i in sorted(interest_map.keys()):
			section_map_data=section_map_data+"['"+i+"',"+str(interest_map[i])+","+str(princi_map[i])+"],"
		section_map_data=section_map_data.rstrip()
		self.div_count=self.div_count+1
		self.tmp_chart_data=self.tmp_chart_data+section_header+section_map_data+section_footer
			
	def generte_html_file(self):
		count = 1
		chart_div_info=""
		while(count<=self.div_count):
			div_id="chart_"+str(count)
			chart_div_info=chart_div_info+"<div id=\""+div_id+"\" style=\"width: 600px; height: 300px;\"></div>"
			count=count+1
	
		file_data=self.html_tmp_header+self.tmp_chart_data+self.html_tmp_footer+chart_div_info+"</body></html>"
		try:
			fh=open("report.html","w")
		except:
			print "not able to write into a file"
		else:
			fh.write(file_data)
			fh.close()
	
		