'''
Copyright (c) <2015> <William Ebertz>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import requests
import json


URL = "https://api.bitlendingclub.com"

#paste token here
token = ""

def list_loans(limit = 10, offset = 0, country = None, loanType = None, term = None, frequency = None, status = None, trusted = None, social = None, amountFrom = None, amountTo = None, reputationFrom = None, reputationTo = None, timeLeftFrom = None, timeLeftTo = None, denomination = None, paymentStatus = None, fundedFrom = None, fundedTo = None, ratioFrom = None, ratioTo = None, listingDateFrom = None, listingDateTo = None, expirationDateFrom = None, expirationDateTo = None, repaidDateFrom = None, repaidDateTo = None, dueDateFrom = None, dueDateTo = None, votesFrom = None, votesTo = None, salary = None):
	
	func_params = locals()
	params = {}
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	
	r = requests.get(URL + '/api/loans', headers = header, params = func_params)
	resp = r.json()
	
	return resp
	
def loan_details(loan_id):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	
	r = requests.get(URL + '/api/loan/' + loan_id, headers = header, params = 			func_params)
	resp = r.json()
	
	return resp

def repay_loan(loan_id):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	header['Authorization'] = 'Bearer ' + token
	header['Content-Type'] = 'application/x-www-form-urlenclosed'
	
	r = requests.post(URL + '/api/loan/' + loan_id + '/repay', headers = header, 			params = func_params)
	resp = r.json()
	
	return resp
	
def amortization_schedule(loan_id):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	header['Authorization'] = 'Bearer ' + token
	header['Content-Type'] = 'application/x-www-form-urlenclosed'
	
	r = requests.get(URL + '/api/loan/' + loan_id + '/schedule', headers = header, 			params = func_params)
	resp = r.json()
	
	return resp
	
def list_investments(loan_id):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	header['Content-Type'] = 'application/x-www-form-urlenclosed'
	
	r = requests.get(URL + '/api/investments/' + loan_id, headers = header,
	params = func_params)
	resp = r.json()
	
	return resp
	
def investment_details(investment_id):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	
	r = requests.get(URL + '/api/investment/' + investment_id, headers = header, 			params = func_params)
	resp = r.json()
	
	return resp
	
def create_investment(loan_id, amount, rate):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	header['Authorization'] = 'Bearer ' + token
	header['Content-Type'] = 'application/x-www-form-urlenclosed'
	
	r = requests.post(URL + '/api/investment/', headers = header, 
		params = func_params)
	resp = r.json()
	
	return resp
	
def modify_investment(investment_id, amount, rate, loan_id = None):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	header['Authorization'] = 'Bearer ' + token
	header['Content-Type'] = 'application/x-www-form-urlenclosed'
	
	r = requests.put(URL + '/api/investment/' + investment_id, headers = header,
		params = func_params)
	resp = r.json()
	
	return resp
	
def delete_investment(investment_id, loan_id = None):
	func_params = locals()
	header = {}
	header['Accept'] = 'application/vnd.blc.v1+json'
	header['Cache-Control'] = 'no-cache'
	header['Authorization'] = 'Bearer ' + token
	header['Content-Type'] = 'application/x-www-form-urlenclosed'
	
	r = requests.delete(URL + '/api/investment/' + investment_id, headers = header,
		params = func_params)
	resp = r.json()
	
	return resp
