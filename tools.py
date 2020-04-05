from numpy import genfromtxt, array, linspace
from datetime import datetime
import time
from math import exp, sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TLegend, TMinuit
from ROOT import kBlue, kRed, gStyle, gROOT






############## common methods ################
def diferentiate(y):
	y_out = [0]
	for i in range(1, len(y)):
		y_out.append(y[i] - y[i-1])
	return y_out


def calc_doubling(slope):
	return 1./(slope * 24 * 3600) * TMath.Log(2.)

def date_to_ut(date):
	dt = datetime.strptime(date, "%m/%d/%y") - datetime.strptime("01/01/1970", "%m/%d/%Y")
	return dt.total_seconds()

def days_between(start, finish):
	return (datetime.strptime(finish, "%m/%d/%y") - datetime.strptime(start, "%m/%d/%y")).days

# def fit_hist(hist, date_0 = "03/15/20", date_1 = "03/31/20"):

# 	# func = TF1("exp", "[0]*pow(2., [1]*x)", x[0], x[-1])

# 	start =  date_to_ut(date_0)
# 	finish = date_to_ut(date_1)

# 	func = TF1("exp", "expo", start, finish)

# 	hist.Fit(func, "NI", "", start, finish)
# 	return func


def fit_hist(hist, date_0 = "03/15/20", date_1 = "03/31/20"):


	start =  date_to_ut(date_0)
	finish = date_to_ut(date_1)


	# sigmoid fit
	# func = TF1("exp", "[0] / (1. + exp([1]*(x - [3]) + [2]) )", start, finish)
	# func.SetParameter(0, 1.10332e+05)
	# func.SetParameter(1, -2.57546e-06)
	# func.SetParameter(2, -5.99971e+00)
	# func.SetParameter(3, start + 3600*24*50)

	# func = TF1("exp", "[0] / (1. + exp((x - [2]) / [1]) ) + [4] / (1. + exp((x - [2] - 604800*1.5) / [3]) )", start, finish)
	# func.SetParameter(0, 1.38585e+05)
	# func.SetParLimits(0, 1e2, 1e6)
	# func.SetParameter(1, -4.20453e+05)
	# # func.SetParameter(2, -5.99971e+00)
	# func.SetParameter(2, start + 3600*24*50)
	# func.SetParameter(3, -2.95643e+05)
	# func.SetParLimits(3, -1.64354e+010, -1.64354e+03)

	# func.SetParameter(4, 2.07433e+05)
	# func.SetParLimits(4, 0., 1e6)





	# func = TF1("exp", " exp()", start, finish)
	# func.SetParameter(0, 1.10332e+05)
	# func.SetParameter(1, -2.57546e-06)
	# func.SetParameter(2, -5.99971e+00)
	# func.SetParameter(3, start + 3600*24*50)



	
	func = TF1("exp", "expo", start, finish)

	hist.Fit(func, "N", "", start, finish)
	# hist.Fit(func, "N", "", start, finish)

	# par3 = func.GetParameter(3)
	# par2 = func.GetParameter(2)
	# par1 = func.GetParameter(1)
	# that_date =  datetime.fromtimestamp(par3 - par2 / par1 )
	# print that_date.strftime("%m/%d/%y")

	return func



def print_slope(func):
	slope = func.GetParameter(1)
	doubling = calc_doubling(slope)

	in_one_day = exp(slope * 24 * 3600)

	print "doubling: \t{} days".format(doubling)
	print "tomorrow will be {} times more".format(in_one_day)

	return doubling,  in_one_day


# TODO
def fit_hist_with_kinks():
	pass


###################################################

# def plotGraphs(plot1, plot2):
# 	c = TCanvas("name", "name", 1920, 1080)

# 	pad1 = TPad("pad1", "pad1", 0, 0, 0.5, 1.0)
# 	pad1.Draw()

# 	c.cd()  # returns to main canvas before defining pad2
# 	pad2 = TPad("pad2", "pad2", 0.5, 0, 1, 1)
# 	pad2.Draw()

# 	pad1.cd()
# 	plot1.Draw()
# 	try:
# 		for gr in plot1[1:]:
# 			gr.Draw("same")
# 	except:
# 		pass

# 	pad2.cd()
# 	plot2.Draw()
# 	try:
# 		for gr in plot2[1:]:
# 			gr.Draw("same")
# 	except:
# 		pass

