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

		self.data_sir = {
			"susceptible" : (x, S),
			"infected"    : (x, I),
			"recovered"   : (x, R)
		}

		self.hists = {
			"susceptible" :  self.make_hist(x, S, "susceptible", self.fill_sandy),
			"infected"    :  self.make_hist(x, I, "infected", self.fill_redish),
			"recovered"   :  self.make_hist(x, R, "recovered", self.fill_greenish)
		}

		self.make_legend()






	def solve_SIR(self, transition, recovery, time_range):
		from scipy.integrate import odeint 

		S_0 = 1.
		I_0 = 8. / (self.populations["World"] - self.populations["China"])
		# I_0 = 1. / populations["Italy"]
		R_0 = 0.

		# I_0 = 0.35e-6
		# R_0 = 31.3646819e-9
		# S_0 = 1. - I_0 - R_0

		def func(y, t, trans, reco):
			S, I, R = y
			dS = - trans * I * S 
			dI = trans * I * S - reco * I
			dR = reco * I

			return dS, dI, dR

		start = "01/22/20"
		# start = "01/29/20"
		# start = "03/03/20"
		finish = "4/03/20"

		# start, finish = time_range

		# n_bins = 1000
		n_bins = days_between(start, finish)

		t = linspace(date_to_ut(start), date_to_ut(finish), n_bins)

		y0 = [S_0, I_0, R_0]

		sol = odeint(func, y0, t, args=(transition, recovery))

		# print sol

		sol = zip(*sol)



		hist_s = self.make_hist(t, sol[0], "susceptible", 43)
		hist_i = self.make_hist(t, sol[1], "infected", 46)
		hist_r = self.make_hist(t, sol[2], "recovered", 30)


		return hist_s, hist_i, hist_r




	def fit_model(self, country, time_range):
		s_data = self.data_sir["susceptible"]
		i_data = self.data_sir["infected"]
		r_data = self.data_sir["recovered"]

		def fcn(nPar, gin, f, par, flag):
			tr = par[0]
			rec = par[1] 
			chi2 = 0.
			n_bins = s_data.GetNbinsX()
			s_model, i_model, r_model = solve_SIR(tr, rec, time_range)
			for i in range(1, n_bins+1):
				dif = (i_data.GetBinContent(i) - i_model.GetBinContent(i)) / i_data.GetBinError(i)
				chi2 += dif ** 2
				dif = (r_data.GetBinContent(i) - r_model.GetBinContent(i)) / r_data.GetBinError(i)
				chi2 += dif ** 2
			f[0] = chi2
			return

		minuit = TMinuit(3)
		minuit.SetFCN(fcn)

		vstep = [1e-10, 1e-10]
		vinit = [1e-10, 1e-10]
		# vinit = [1e-3, 1e-3]
		vmin = [1e-15, 1e-15]
		vmax = [1e0, 1e0]

		from ctypes import c_int, c_double
		import array as c_arr

		arglist = c_arr.array( 'd', 10*[0.] )
		ierflag = 0
		
		arglist[0] = 1
		minuit.mnexcm( "SET ERR", arglist, 1, c_int(ierflag) )

		minuit.mnparm(0, "transition rate", vinit[0], vstep[0], vmin[0], vmax[0], c_int(ierflag))
		minuit.mnparm(1, "recovery rate", vinit[1], vstep[1], vmin[1], vmax[1], c_int(ierflag))

		# minuit.SetErrorDef(1.)

		# minuit.SetMaxIteration(500)
		# minuit.Migrad()
		arglist[0] = 500
		arglist[1] = 1.
		# minuit.mnexcm( "MIGRAD", arglist, 2, c_int(ierflag) )


		res_trans = c_double(0.)
		res_rec = c_double(0.)
		err_trans = c_double(0.)
		err_rec = c_double(0.)
		
		minuit.GetParameter(0, res_trans, err_trans)
		minuit.GetParameter(1, res_rec, err_rec)

		# return res_trans.value, res_rec.value

		hists = self.solve_SIR(res_trans.value, res_rec.value, time_range)

		self.hists = {
			"susceptible" :  hists[0],
			"infected"    :  hists[1],
			"recovered"   :  hists[2]
		}

		self.draw()



if __name__ == "__main__":
	# plotter = Plotter("wo China")
	plotter = Plotter_SIR("Ukraine",
		draw_seq = ("infected", "recovered"),
		to_fit = False
		)

	# trans_rate, reco_rate = plotter.fit_model("wo China", ("02/29/20", "04/03/20"))

	plotter.draw()
