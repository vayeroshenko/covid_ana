from math import sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TAttFill
from ROOT import kBlue, kRed, gStyle, gROOT

from tools import *



# country = "wo China"
# country = "China"
# country = "Spain"
country = "Ukraine"
# country = "Belarus"
# country = "Italy"
# country = "France"
# country = "US"
# country = "India"

# hist_conf, hist_dead, hist_rec, legend = make_SIR(country)
hist_conf, hist_dead, hist_rec, legend = make_def(country)


gStyle.SetOptStat(0)
gROOT.ForceStyle()


# trans_rate = 0.01132018 
# reco_rate = 0.0053761 


# trans_rate, reco_rate = fit_SIR("China", ("02/22/20", "03/31/20"))
# trans_rate, reco_rate = fit_SIR("Italy", ("02/29/20", "04/01/20"))
# hist_conf, hist_dead, hist_rec, legend = draw_SIR(trans_rate, reco_rate, ("02/22/20", "03/31/20"))

# print trans_rate / reco_rate

c = TCanvas("c", "c", 1920, 1080)

hist_conf.Draw("MIN0 HIST E1")
hist_rec.Draw("HIST E1 SAME")
hist_dead.Draw("HIST E1 SAME")


# hist_dead.Draw("MIN0 HIST E1")
# hist_rec.Draw("HIST E1 SAME")
# hist_rec.Draw("MIN0 HIST E1")
# hist_dead.Draw("HIST E1 SAME")


func_conf = fit_hist(hist_conf, "03/30/20", "04/03/20")
print_slope(func_conf)
func_conf.Draw("same")

legend.Draw()

# func_conf.Draw("SAME")


