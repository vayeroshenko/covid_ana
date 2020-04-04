from numpy import genfromtxt, array, linspace
from datetime import datetime
import time
from math import exp, sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TLegend, TMinuit

from tools import *


class Plotter():
	populations = { "World"   : 7.774797e9,
					"China"   : 1.439323776e9,
					"US"      : 331.002651e6,
					"Ukraine" : 43.733762e6,
					"Italy"	  : 60.461826e6,
					"France"  : 65.273511e6,
					"India"   : 1.380004385e9,	
					"Spain"   : 46.750411e6	}

	day = 3600. * 24.
	s = 1.

	fill_redish = 46
	fill_sandy = 43
	fill_greenish = 30



	def __init__(   self, country,
					draw_seq = ("confirmed", "recovered", "deaths"),
					derivative = 0,
					
					to_fit = True,
					fit_start = "03/22/20",
					fit_end = "03/28/20",
					fit_hist = "confirmed",
					draw_fit = True   ):
		
		self.country = country

		self.data = {
			"confirmed" : self.get_data("confirmed"),
			"deaths"    : self.get_data("deaths"),
			"recovered" : self.get_data("recovered") 
		}

		self.sequence = draw_seq
		self.derivative = derivative

		self.to_fit = to_fit
		self.fit_start = fit_start
		self.fit_end = fit_end
		self.fit_hist = fit_hist
		self.draw_fit = draw_fit

		self.has_fit = False

		self.make_def()

		if to_fit:
			self.fit()



	def fit(self):
		self.func = fit_hist(self.hists[self.fit_hist],
			self.fit_start,
			self.fit_end)

		self.has_fit = True

		print_slope(self.func)




	def make_hist(self, x, y, name, color):
		gr = TH1D(name, name, len(x), x[0], x[-1]) 

		for x_i, y_i, i in zip(x, y, range(1, len(x)+1)):
			if y_i == 0.:
				gr.SetBinContent(i, 0. + 1e-20)
				# gr.SetBinError(i, 0.)
			else:
				gr.SetBinContent(i, y_i + 1e-20)
				# gr.SetBinError(i, y_i*0.05)
				gr.SetBinError(i, sqrt(y_i))



		# gr.Sumw2()
		gr.GetXaxis().SetTimeDisplay(1)
		gr.SetLineColor(color)
		gr.SetMarkerStyle(21)
		gr.SetMarkerSize(0.5)

		gr.SetFillStyle(3002)
		gr.SetFillColor(color)

		gr.GetXaxis().SetNdivisions(16)
		gr.GetXaxis().SetLabelSize(0.02)


		return gr


	def hist_from_data(self, data_type, color):
		x, y = self.data[data_type]

		for i in range(self.derivative):
			y = diferentiate(y)

		return self.make_hist(x, y, data_type, color)



	def draw_cases(self):
		self.setup_graphics()

		self.hists[self.sequence[0]].Draw("MIN0 HIST E1")
		for i in range(1, len(self.sequence)):
			self.hists[self.sequence[i]].Draw("HIST E1 SAME")
		
		if self.has_fit and self.draw_fit:
			self.func.Draw("same")

		self.legend.Draw()
		input()

	def setup_graphics(self):
		gStyle.SetOptStat(0)
		gROOT.ForceStyle()

		self.c = TCanvas("c", "c", 1920, 1080)

	def make_hist(self, x, y, name, color):
		gr = TH1D(name, name, len(x), x[0], x[-1]) 

		for x_i, y_i, i in zip(x, y, range(1, len(x)+1)):
			if y_i == 0.:
				gr.SetBinContent(i, 0.)
			else:
				gr.SetBinContent(i, y_i + 1e-30)
				gr.SetBinError(i, 0.05 * y_i)



		# gr.Sumw2()
		gr.GetXaxis().SetTimeDisplay(1)
		gr.SetLineColor(color)
		gr.SetMarkerStyle(21)
		gr.SetMarkerSize(0.5)

		gr.SetFillStyle(3002)
		gr.SetFillColor(color)

		gr.GetXaxis().SetNdivisions(16)
		gr.GetXaxis().SetLabelSize(0.02)


		return gr


	def make_def(self):

		self.hists = {
			"confirmed" :  self.hist_from_data("confirmed", self.fill_sandy),
			"deaths"    :  self.hist_from_data("deaths", self.fill_redish),
			"recovered" :  self.hist_from_data("recovered", self.fill_greenish)
		}

		self.make_legend()


	def make_legend(self):
		l = TLegend(0.15, 0.85, 0.4, 0.7)
		names = ("confirmed", "deaths", "recovered")

		if self.country != "wo China":
			l.SetHeader(self.country, "c")
		else:
			l.SetHeader("World (without mainland China)", "c")

		for name in self.hists:
			l.AddEntry(self.hists[name], name)

		self.legend = l


	def get_data(self, data_type):
		path = "./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{}_global.csv".format(data_type)
		my_data = genfromtxt(path, delimiter=',', dtype=str)

		time_series_number = []

		for line in my_data:
			if line[1] == "Country/Region":
				time_series_date = line
			elif self.country == "wo China" and line[1] != "China":
				time_series_number.append(line)
			
			if line[1] == self.country:
				time_series_number.append(line)
			# if line[0] == "Hubei":
				# time_series_number = line

		cut = 4
		
		time_series_date = time_series_date[cut:]
		time_series_number = [time_series_number[i][cut:] for i in range(0, len(time_series_number))]
		time_series_number = zip(*time_series_number)

		y = array([list(map(float, i)) for i in time_series_number])

		y = array(list(map(sum, y)))

		x = array([date_to_ut(i) for i in time_series_date])
		# print x
		# x = x[(len(x) - len(y)):]

		return x, y






if __name__ == "__main__":
	# plotter = Plotter("wo China")
	plotter = Plotter("Ukraine",
		draw_seq = ("confirmed", "deaths", "recovered"),
		fit_start = "03/30/20",
		fit_end = "04/03/20",
		draw_fit = False,
		derivative = 0
		)


	plotter.draw_cases()
