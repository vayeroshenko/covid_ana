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

def fit_hist(hist, date_0 = "03/15/20", date_1 = "03/31/20"):

	# func = TF1("exp", "[0]*pow(2., [1]*x)", x[0], x[-1])

	start =  date_to_ut(date_0)
	finish = date_to_ut(date_1)

	func = TF1("exp", "expo", start, finish)

	hist.Fit(func, "NI", "", start, finish)
	return func

def print_slope(func):
	slope = func.GetParameter(1)
	doubling = calc_doubling(slope)

	in_one_day = exp(slope * 24 * 3600)

	print "doubling: \t{} days".format(doubling)
	print "tomorrow will be {} times more".format(in_one_day)


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

