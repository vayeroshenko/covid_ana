from math import sqrt

from ROOT import TGraphErrors, TF1, TMath, TCanvas, TPad, TH1D, TAttFill
from ROOT import kBlue, kRed, gStyle, gROOT

from tools import *



country = "wo China"
# country = "China"
# country = "Ukraine"
# country = "Italy"
# country = "US"


# hist_conf, hist_dead, hist_rec, legend = make_SIR(country)
hist_conf, hist_dead, hist_rec, legend = make_def(country)


gStyle.SetOptStat(0)



gROOT.ForceStyle()


c = TCanvas("c", "c", 1920, 1080)

hist_conf.Draw("MIN0 HIST E1")
hist_rec.Draw("HIST E1 SAME")
hist_dead.Draw("HIST E1 SAME")

# func_conf = fit_hist(hist_dead, "03/05/20", "03/26/20")
# print_slope(func_conf)
# func_conf.Draw("same")

legend.Draw()


# func.Draw("SAME")


