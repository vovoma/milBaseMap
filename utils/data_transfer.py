# coding=utf-8

from pprint import pprint
import requests

def request_api_methods():
	result = requests.get("")
	pprint(result.json())
	if __name__ = "__main__":
		request_api_methods() 

