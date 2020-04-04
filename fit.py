from plotter import Plotter
from plotter_sir import Plotter_SIR



############### To draw number of cases #################

plotter = Plotter("France",
		draw_seq = ("confirmed", "deaths", "recovered"),
		fit_start = "03/30/20",
		fit_end = "04/03/20",
		draw_fit = True,
		derivative = 0
		)

# plotter = Plotter("wo China",
# 		draw_seq = ("confirmed", "recovered", "deaths"),
# 		fit_start = "03/30/20",
# 		fit_end = "04/03/20",
# 		draw_fit = True,
# 		derivative = 0
# 		)


plotter.draw()

###########################################################


####################### To draw SIR #######################

# plotter = Plotter_SIR("Ukraine",
# 		draw_seq = ("infected", "recovered"),
# 		to_fit = False
# 		)

# plotter.draw()

###########################################################
