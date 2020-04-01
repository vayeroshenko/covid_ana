from math import sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TAttFill
from ROOT import kBlue, kRed, gStyle, gROOT

from tools import *



country = "wo China"
# country = "China"
# country = "Ukraine"
# country = "Italy"

# x, y = get_data(country, "confirmed")
# x, y = get_data(country, "deaths")
# x, y = get_data(country, "recovered")
# y = diferentiate(y)
# y = diferentiate(y)

hist_conf = hist_from_data(country, "confirmed", 43)
hist_dead = hist_from_data(country, "deaths", 46)
hist_rec = hist_from_data(country, "recovered", 30)


gStyle.SetOptStat(0)



gROOT.ForceStyle()


c = TCanvas("c", "c", 1920, 1080)

hist_conf.Draw("MIN0 HIST E1")
hist_rec.Draw("HIST E1 SAME")
hist_dead.Draw("HIST E1 SAME")

legend = make_legend((hist_conf, hist_rec, hist_dead), 
	("confirmed", "recovered", "deaths"))

legend.Draw()


# func.Draw("SAME")


