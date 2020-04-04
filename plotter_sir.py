from numpy import genfromtxt, array, linspace
from datetime import datetime
import time
from math import exp, sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TLegend, TMinuit

from tools import *

from plotter import Plotter



# __metaclass__ = type
class Plotter_SIR(Plotter):
	def __init__(   self, country,
					draw_seq = ("susceptible", "recovered", "infected"),
					derivative = 0,
					to_fit = True,
					fit_start = "03/22/20",
					fit_end = "03/28/20",
					fit_hist = "confirmed",
					draw_fit = True   ):
		super(Plotter_SIR, self).__init__(  country, 
											draw_seq,
											derivative,
											to_fit,
											fit_start,
											fit_end,
											fit_hist,
											draw_fit)
	self.make_SIR()


	def make_SIR(self):
		print(self)

		if self.country == "wo China":
			pop = self.populations["World"] - populations["China"]
		else:
			pop = self.populations[self.country]

		x, y_conf = self.data["confirmed"]
		x, y_dead = self.data[ "deaths"  ]
		x, y_rec  = self.data["recovered"]


		S = (- y_conf - y_dead - y_rec + pop) / pop 
		I = (y_conf - y_dead - y_rec) / pop 
		R = (y_dead + y_rec) / pop 

		# print S,I,R
		
		self.hists = {
			"susceptible" :  self.make_hist(x, S, "susceptible", self.fill_sandy),
			"infected"    :  self.make_hist(x, I, "infected", self.fill_redish),
			"recovered"   :  self.make_hist(x, R, "recovered", self.fill_greenish)
		}

		self.make_legend()







if __name__ == "__main__":
	# plotter = Plotter("wo China")
	plotter = Plotter_SIR("Ukraine",
		draw_seq = ("infected", "recovered"),
		to_fit = False
		)


	plotter.draw()
