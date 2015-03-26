#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides an implementation of the Stochastic Oscillator

Requirements:
	- numpy
	- technical indicators library (http://sourceforge.net/projects/py-tech-ind)

Author:
Stefan Andersen

"""

import numpy as np
import technical_indicators as ti

def stoch(prices, kperiod=14, dperiod=5):
	"""
	Theory:	

	%K = (Current Close - Lowest Low in %K-period)/(Highest High in %K-period - Lowest Low in %K-period) * 100
	%D = %D-day SMA of %K

	Lowest Low = lowest low for the look-back period
	Highest High = highest high for the look-back period
	%K is multiplied by 100 to move the decimal point two places

	Takes =>
	
	prices: A multidimensional array which contains [close_price, high, low] for each given day
	k-period: Integer of k-period  
	d-period: Integer of d-period

	Returns =>

	{k:k_value, d:d_value}
	"""

	assert(kperiod > 0), "/-/ kperiod must be > zero"
	assert(dperiod > 0), "/-/ dperiod must by > zero"
	assert(len(prices) >= kperiod + dperiod), "/-/ set of prices too small for given periods"
	
	return {"k":k(prices, kperiod),
			"d":d(prices, kperiod, dperiod)}

def k(prices, period):
	"""
	Implementation of k-value-formula for %K-period
	"""
	return (current_close(prices) - lowest_low(lows(prices)[:period]))/(highest_high(highs(prices)[:period]) - lowest_low(lows(prices)[:period])) * 100

def d(prices, kperiod, dperiod):
	"""
	Implementation of d-value-formula for %K-period and %D-period
	"""
	return ti.sma(np.array(k_list(prices, dperiod)), dperiod)[0]

def highest_high(highs):
	return max(highs)

def lowest_low(lows):
	return min(lows)

def current_close(prices):
	try:
		return close_prices(prices)[0]	
	except IndexError:
		raise SystemExit("/-/ Current close price unavailable")	

def lows(prices):
	try:
		return [row[2] for row in prices]
	except IndexError:
		raise SystemExit("/-/ Prices format does not contain LOWS")

def highs(prices):
	try:
		return [row[1] for row in prices]
	except IndexError:
		raise SystemExit("/-/ Prices format does not contain HIGHS")

def close_prices(prices):
	try:
		return [row[0] for row in prices]	
	except IndexError:
		raise SystemExit("/-/ Prices format does not contain CLOSINGS")

def k_list(prices, length, L=[]):
	"""
	Recursive creation of k-value list with given length
	Length will normally be equal to the %D-period
	"""
	if(len(L) is length):
		return L		
	L.append(k(prices[len(L)+1:], length))
	return k_list(prices, length, L) 

def is_bullish(prices, kperiod=14, dperiod=5):
	"""
	Convenience method to provide a meaningful result
	"""
	if(stoch(prices, kperiod, dperiod)["k"] > stoch(prices, kperiod, dperiod)["d"]):
		return True
	return False	

