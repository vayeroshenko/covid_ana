from numpy import genfromtxt, array, linspace
from datetime import datetime
import time
from math import exp, sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TLegend, TMinuit
from ROOT import kBlue, kRed, gStyle, gROOT


# populations = { "World"   : 7.774797e9,
# 				"China"   : 1.439323776e9,
# 				"US"      : 331.002651e6,
# 				"Ukraine" : 43.733762e6,
# 				"Italy"	  : 60.461826e6,
# 				"France"  : 65.273511e6,
# 				"India"   : 1.380004385e9,	
# 				"Spain"   : 46.750411e6		
# }

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


# def calc_doubling(slope):
# 	return 1./(slope * 24 * 3600) * TMath.Log(2.)


# def get_data(country, data_type):
# 	path = "./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{}_global.csv".format(data_type)
# 	my_data = genfromtxt(path, delimiter=',', dtype=str)

# 	time_series_number = []

# 	for line in my_data:
# 		if line[1] == "Country/Region":
# 			time_series_date = line
# 		elif country == "wo China" and line[1] != "China":
# 			time_series_number.append(line)
		
# 		if line[1] == country:
# 			time_series_number.append(line)
# 		# if line[0] == "Hubei":
# 			# time_series_number = line


# 	cut = 4


# 	time_series_date = time_series_date[cut:]
# 	time_series_number = [time_series_number[i][cut:] for i in range(0, len(time_series_number))]
# 	time_series_number = zip(*time_series_number)

# 	y = array([list(map(float, i)) for i in time_series_number])

# 	y = array(list(map(sum, y)))

# 	x = array([date_to_ut(i) for i in time_series_date])
# 	# print x
# 	# x = x[(len(x) - len(y)):]

# 	return x, y

# def diferentiate(y):
# 	y_out = [0]
# 	for i in range(1, len(y)):
# 		y_out.append(y[i] - y[i-1])
# 	return y_out

# def fit_kink(ranges):
# 	pass

# def date_to_ut(date):
# 	dt = datetime.strptime(date, "%m/%d/%y") - datetime.strptime("01/01/1970", "%m/%d/%Y")
# 	return dt.total_seconds()

# def days_between(start, finish):
# 	return (datetime.strptime(finish, "%m/%d/%y") - datetime.strptime(start, "%m/%d/%y")).days
	
# def make_hist(x, y, name, color):
# 	gr = TH1D(name, name, len(x), x[0], x[-1]) 

# 	for x_i, y_i, i in zip(x, y, range(1, len(x)+1)):
# 		if y_i == 0.:
# 			gr.SetBinContent(i, 0. + 1e-20)
# 			# gr.SetBinError(i, 0.)
# 		else:
# 			gr.SetBinContent(i, y_i + 1e-20)
# 			# gr.SetBinError(i, y_i*0.05)
# 			gr.SetBinError(i, sqrt(y_i))



# 	# gr.Sumw2()
# 	gr.GetXaxis().SetTimeDisplay(1)
# 	gr.SetLineColor(color)
# 	gr.SetMarkerStyle(21)
# 	gr.SetMarkerSize(0.5)

# 	gr.SetFillStyle(3002)
# 	gr.SetFillColor(color)

# 	gr.GetXaxis().SetNdivisions(16)
# 	gr.GetXaxis().SetLabelSize(0.02)


# 	return gr

# def fit_hist(hist, date_0 = "03/15/20", date_1 = "03/31/20"):

# 	# func = TF1("exp", "[0]*pow(2., [1]*x)", x[0], x[-1])

# 	start =  date_to_ut(date_0)
# 	finish = date_to_ut(date_1)

# 	func = TF1("exp", "expo", start, finish)

# 	hist.Fit(func, "NI", "", start, finish)
# 	return func

# def print_slope(func):
# 	slope = func.GetParameter(1)
# 	doubling = calc_doubling(slope)

# 	in_one_day = exp(slope * 24 * 3600)

# 	print "doubling: \t{} days".format(doubling)
# 	print "tomorrow will be {} times more".format(in_one_day)


# def hist_from_data(country, data_type, color):
# 	x, y = get_data(country, data_type)
	
# 	# y = diferentiate(y)
# 	# y = diferentiate(y)
	
# 	return make_hist(x, y, data_type, color)



# def make_legend(hists, names):
# 	l = TLegend(0.15, 0.85, 0.4, 0.7)
# 	for hist, name in zip(hists, names):
# 		l.AddEntry(hist, name)

# 	return l

# def make_SIR(country):
# 	if country == "wo China":
# 		pop = populations["World"] - populations["China"]
# 	else:
# 		pop = populations[country]

# 	x, y_conf = get_data(country, "confirmed")
# 	x, y_dead = get_data(country, "deaths")
# 	x, y_rec = get_data(country, "recovered")


# 	S = (- y_conf - y_dead - y_rec + pop) / pop 
# 	I = (y_conf - y_dead - y_rec) / pop 
# 	R = (y_dead + y_rec) / pop 

# 	# print S,I,R
	

# 	hist_s = make_hist(x, S, "susceptible", 43)
# 	hist_i = make_hist(x, I, "infected", 46)
# 	hist_r = make_hist(x, R, "recovered", 30)

# 	legend = make_legend((hist_s, hist_i, hist_r), 
# 		("susceptible", "infected", "recovered"))


# 	return hist_s, hist_i, hist_r, legend

# def make_def(country):

# 	hist_conf = hist_from_data(country, "confirmed", 43)
# 	hist_dead = hist_from_data(country, "deaths", 46)
# 	hist_rec = hist_from_data(country, "recovered", 30)

# 	legend = make_legend((hist_conf, hist_rec, hist_dead), 
# 		("confirmed", "recovered", "deaths"))

# 	return hist_conf, hist_dead, hist_rec, legend

# from scipy.integrate import odeint 



# def draw_SIR(transition, recovery, time_range):
# 	# S_0 = 1.
# 	# I_0 = 8. / (populations["World"] - populations["China"])
# 	# I_0 = 1. / populations["Italy"]
# 	# R_0 = 0.

# 	I_0 = 0.35e-6
# 	R_0 = 31.3646819e-9
# 	S_0 = 1. - I_0 - R_0

# 	def func(y, t, trans, reco):
# 		S, I, R = y
# 		dS = - trans * I * S 
# 		dI = trans * I * S - reco * I
# 		dR = reco * I

# 		return dS, dI, dR

# 	start = "01/22/20"
# 	# start = "01/29/20"
# 	# start = "03/03/20"
# 	finish = "4/01/20"

# 	# start, finish = time_range

# 	# n_bins = 1000
# 	n_bins = days_between(start, finish)

# 	t = linspace(date_to_ut(start), date_to_ut(finish), n_bins)

# 	y0 = [S_0, I_0, R_0]

# 	sol = odeint(func, y0, t, args=(transition, recovery))

# 	# print sol

# 	sol = zip(*sol)



# 	hist_s = make_hist(t, sol[0], "susceptible", 43)
# 	hist_i = make_hist(t, sol[1], "infected", 46)
# 	hist_r = make_hist(t, sol[2], "recovered", 30)

# 	legend = make_legend((hist_s, hist_i, hist_r), 
# 		("susceptible", "infected", "recovered"))


# 	return hist_s, hist_i, hist_r, legend


# def fit_SIR(country, time_range):
# 	s_data, i_data, r_data, leg = make_SIR(country)

# 	def fcn(nPar, gin, f, par, flag):
# 		tr = par[0]
# 		rec = par[1] 
# 		chi2 = 0.
# 		n_bins = s_data.GetNbinsX()
# 		s_model, i_model, r_model, leg = draw_SIR(tr, rec, time_range)
# 		for i in range(1, n_bins+1):
# 			dif = (i_data.GetBinContent(i) - i_model.GetBinContent(i)) / i_data.GetBinError(i)
# 			chi2 += dif ** 2
# 			dif = (r_data.GetBinContent(i) - r_model.GetBinContent(i)) / r_data.GetBinError(i)
# 			chi2 += dif ** 2
# 		f[0] = chi2
# 		return

# 	minuit = TMinuit(3)
# 	minuit.SetFCN(fcn)

# 	vstep = [1e-10, 1e-10]
# 	# vinit = [1e-10, 1e-10]
# 	vinit = [1e-3, 1e-3]
# 	vmin = [1e-15, 1e-15]
# 	vmax = [1e0, 1e0]

# 	from ctypes import c_int, c_double
# 	import array as c_arr

# 	arglist = c_arr.array( 'd', 10*[0.] )
# 	ierflag = 0
	
# 	arglist[0] = 1
# 	minuit.mnexcm( "SET ERR", arglist, 1, c_int(ierflag) )

# 	minuit.mnparm(0, "transition rate", vinit[0], vstep[0], vmin[0], vmax[0], c_int(ierflag))
# 	minuit.mnparm(1, "recovery rate", vinit[1], vstep[1], vmin[1], vmax[1], c_int(ierflag))

# 	# minuit.SetErrorDef(1.)

# 	# minuit.SetMaxIteration(500)
# 	# minuit.Migrad()
# 	arglist[0] = 500
# 	arglist[1] = 1.
# 	minuit.mnexcm( "MIGRAD", arglist, 2, c_int(ierflag) )


# 	res_trans = c_double(0.)
# 	res_rec = c_double(0.)
# 	err_trans = c_double(0.)
# 	err_rec = c_double(0.)
	
# 	minuit.GetParameter(0, res_trans, err_trans)
# 	minuit.GetParameter(1, res_rec, err_rec)

# 	return res_trans.value, res_rec.value





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

