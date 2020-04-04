from datetime import date, timedelta
from plotter import Plotter


fit_start = (date.today() - timedelta(days = 5)).strftime("%m/%d/%y")
fit_finish = (date.today() - timedelta(days = 1)).strftime("%m/%d/%y")
month_ago = (date.today() - timedelta(days = 30)).strftime("%m/%d/%y")
two_month_ago = (date.today() - timedelta(days = 60)).strftime("%m/%d/%y")




# print "from {} to {}".format(fit_start, fit_finish)


date_for_filename = (date.today() - timedelta(days = 1)).strftime("%m-%d-%y")
filename = "stats_{}.pdf".format(date_for_filename)


###############################
plotter = Plotter("Ukraine",
	draw_seq = ("confirmed", "deaths", "recovered"),
	fit_start = fit_start,
	fit_end = fit_finish,
	draw_fit = True,
	derivative = 0
	)

plotter.zoom_axis(month_ago, fit_finish)
plotter.draw()

plotter.c.Print(filename+"(","pdf")

plotter.draw(log = True)
plotter.c.Print(filename,"pdf")


plotter.clear()
#################################


###############################
plotter = Plotter("Italy",
	draw_seq = ("confirmed", "recovered", "deaths"),
	fit_start = fit_start,
	fit_end = fit_finish,
	draw_fit = True,
	derivative = 0
	)

plotter.zoom_axis(month_ago, fit_finish)
plotter.draw()

plotter.c.Print(filename,"pdf")

plotter.draw(log = True)
plotter.c.Print(filename,"pdf")


plotter.clear()
#################################

###############################
plotter = Plotter("France",
	draw_seq = ("confirmed", "recovered", "deaths"),
	fit_start = fit_start,
	fit_end = fit_finish,
	draw_fit = True,
	derivative = 0
	)

plotter.zoom_axis(month_ago, fit_finish)
plotter.draw()

plotter.c.Print(filename,"pdf")


plotter.clear()
#################################

###############################
plotter = Plotter("US",
	draw_seq = ("confirmed", "recovered", "deaths"),
	fit_start = fit_start,
	fit_end = fit_finish,
	draw_fit = True,
	derivative = 0
	)

plotter.zoom_axis(month_ago, fit_finish)
plotter.draw()

plotter.c.Print(filename,"pdf")


plotter.clear()
#################################


###############################
plotter = Plotter("wo China",
	draw_seq = ("confirmed", "recovered", "deaths"),
	fit_start = fit_start,
	fit_end = fit_finish,
	draw_fit = True,
	derivative = 0
	)

plotter.zoom_axis(month_ago, fit_finish)
plotter.draw()

plotter.c.Print(filename,"pdf")

plotter.draw(log = True)
plotter.c.Print(filename+")","pdf")


plotter.clear()
#################################
