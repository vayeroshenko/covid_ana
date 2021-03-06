from numpy import genfromtxt, array, linspace
from datetime import datetime
import time
from math import exp, sqrt

from ROOT import 	TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, \
					TPaveLabel, TLegend, TMinuit, TPaveText

from tools import *


class Plotter(object):
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


	# names = ("confirmed", "deaths", "recovered")


	def __init__(   self, country,
					draw_seq     		= ("confirmed", "recovered", "deaths"),
					derivative   		= 0,
					
					to_fit       		= True,
					fit_start    		= "03/22/20",
					fit_end      		= "03/28/20",
					fit_hist     		= "confirmed",
					draw_fit     		= True,
					floating_average 	= -1   ):
		super(Plotter, self).__init__()
		

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

		if floating_average != -1:
			self.do_floating_average(floating_average)



	def fit(self):
		self.func = fit_hist(self.hists[self.fit_hist],
			self.fit_start,
			self.fit_end)

		self.has_fit = True


	def make_hist(self, x, y, name, color):
		gr = TH1D(name, name, len(x), x[0], x[-1]) 

		for x_i, y_i, i in zip(x, y, range(1, len(x)+1)):
			if y_i == 0.:
				gr.SetBinContent(i, 0. + 1e-20)
				# gr.SetBinError(i, 0.)
			else:
				gr.SetBinContent(i, y_i + 1e-20)
				gr.SetBinError(i, y_i*0.05)
				# gr.SetBinError(i, sqrt(y_i))



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


	def zoom_axis(self, begin, end):
		begin = date_to_ut(begin)
		end = date_to_ut(end)

		for key in self.hists:
			self.hists[key].GetXaxis().SetRangeUser(begin, end)

		# self.draw()


	def draw(self, log = False):
		self.setup_graphics()
		if log:
			self.c.SetLogy()

		for i in range(0, len(self.sequence)):
			if i == 0:
				self.hists[self.sequence[0]].Draw("MIN0 HIST E1")
			else:
				self.hists[self.sequence[i]].Draw("HIST E1 SAME")
		
		self.legend.Draw()
			
		if self.has_fit and self.draw_fit:
			self.func.Draw("same")
			
			doubling, oneday = print_slope(self.func)
			newpad = TPad("newpad","a transparent pad",0.15, 0.65, 0.4, 0.55);
			self.text = TPaveText(0.1, 0.1, 0.9, 0.9)
			self.text.AddText("Doubles every {} days".format(doubling))
			self.text.AddText("Multiplies by {} every day".format(oneday))
			newpad.SetFillStyle(4000);
			newpad.Draw()
			newpad.cd()
			self.text.Draw()

		# input()

	def setup_graphics(self):
		gStyle.SetOptStat(0)
		gStyle.SetOptTitle(0)

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

		if self.country != "wo China":
			l.SetHeader(self.country, "c")
		else:
			l.SetHeader("World (without Mainland China)", "c")

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


	def clear(self):
		for key in self.hists:
			self.hists[key].Delete()
		try:
			self.func.Delete()
		except:
			pass
		self.c.Delete()

	def do_floating_average(self, length):
		for key in self.hists:
			nBins = self.hists[key].GetNbinsX()
			temp_length = length
			for bin_i in range(1, nBins + 1):
				if bin_i  < length:
					temp_length = bin_i
				average_value = 0
				total_error = 0
				for float_i in range(bin_i - temp_length + 1, bin_i + 1):
					average_value += self.hists[key].GetBinContent(float_i)
					total_error += self.hists[key].GetBinError(float_i)**2
				average_value /= temp_length
				total_error = sqrt(total_error) / temp_length

				self.hists[key].SetBinContent(bin_i, average_value)
				self.hists[key].SetBinError(bin_i, total_error)

				temp_length = length
		return



if __name__ == "__main__":
	# plotter = Plotter("wo China")
	plotter = Plotter("Ukraine",
		# draw_seq = ("confirmed", "deaths", "recovered"),
		fit_start = "04/04/20",
		fit_end = "04/06/20",
		draw_fit = False,
		derivative = 1,
		floating_average = 7
		)
	
	# plotter = Plotter("Italy",
	# 	# draw_seq = ("confirmed", "deaths", "recovered"),
	# 	to_fit = False,
	# 	# fit_start = "04/04/20",
	# 	# fit_end = "04/06/20",
	# 	# draw_fit = False,
	# 	derivative = 1
	# 	)

	# plotter = Plotter("France",
	# 	draw_seq = ("confirmed", "recovered", "deaths"),
	# 	fit_start = "04/01/20",
	# 	fit_end = "04/06/20",
	# 	draw_fit = True,
	# 	derivative = 0
	# 	)

	# plotter = Plotter("China",
	# 	draw_seq    = ("confirmed", "recovered", "deaths"),
	# 	fit_hist    = "confirmed",
	# 	fit_start   = "01/22/20",
	# 	fit_end     = "04/03/20",
	# 	draw_fit    = True,
	# 	derivative  = 0
	# 	)



	# plotter.zoom_axis("02/19/20","04/03/20")

	plotter.draw(log = False)
