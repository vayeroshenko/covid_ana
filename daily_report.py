from datetime import date, timedelta
from plotter import Plotter
from plotter_sir import Plotter_SIR




def make_daily_report(day):

	fit_start = (day - timedelta(days = 4)).strftime("%m/%d/%y")
	fit_finish = day.strftime("%m/%d/%y")
	month_ago = (day- timedelta(days = 30)).strftime("%m/%d/%y")
	two_month_ago = (day - timedelta(days = 61)).strftime("%m/%d/%y")
	three_month_ago = (day - timedelta(days = 91)).strftime("%m/%d/%y")
	four_month_ago = (day - timedelta(days = 122)).strftime("%m/%d/%y")




	# print "from {} to {}".format(fit_start, fit_finish)


	date_for_filename = day.strftime("%m-%d-%y")
	filename = "reports/stats_{}.pdf".format(date_for_filename)



	###############################
	plotter = Plotter("Ukraine",
		draw_seq = ("confirmed", "recovered", "deaths"),
		fit_start = fit_start,
		fit_end = fit_finish,
		draw_fit = True,
		derivative = 0
		)

	plotter.zoom_axis(two_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename+"(","pdf")

	plotter.draw(log = True)
	plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################

	###############################
	plotter = Plotter("Ukraine",
		draw_seq = ("confirmed", "recovered", "deaths"),
		to_fit = False,
		draw_fit = False,
		derivative = 1
		)

	plotter.zoom_axis(two_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################

	###############################
	plotter = Plotter_SIR("Ukraine",
		draw_seq = ("infected", "recovered"),
		to_fit = False
		)

	plotter.zoom_axis(two_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################

	###############################
	plotter = Plotter("Russia",
		draw_seq = ("confirmed", "recovered", "deaths"),
		fit_start = fit_start,
		fit_end = fit_finish,
		draw_fit = True,
		derivative = 0
		)

	plotter.zoom_axis(month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")

	# plotter.draw(log = True)
	# plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################


	###############################
	plotter = Plotter("Belarus",
		draw_seq = ("confirmed", "recovered", "deaths"),
		fit_start = fit_start,
		fit_end = fit_finish,
		draw_fit = True,
		derivative = 0
		)

	plotter.zoom_axis(month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")

	# plotter.draw(log = True)
	# plotter.c.Print(filename,"pdf")


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

	plotter.zoom_axis(three_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")

	# plotter.draw(log = True)
	# plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################

	###############################
	plotter = Plotter("Italy",
		draw_seq = ("confirmed", "recovered", "deaths"),
		to_fit = False,
		draw_fit = False,
		derivative = 1
		)

	plotter.zoom_axis(three_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")

	plotter.clear()
	#################################

	###############################
	plotter = Plotter_SIR("Italy",
		draw_seq = ("infected", "recovered"),
		to_fit = False
		)

	plotter.zoom_axis(three_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################

	###############################
	plotter = Plotter_SIR("China",
		draw_seq = ("recovered", "infected"),
		to_fit = False
		)

	plotter.zoom_axis(four_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################


	###############################
	plotter = Plotter("Spain",
		draw_seq = ("confirmed", "recovered", "deaths"),
		fit_start = fit_start,
		fit_end = fit_finish,
		draw_fit = True,
		derivative = 0
		)

	plotter.zoom_axis(two_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")

	# plotter.draw(log = True)
	# plotter.c.Print(filename,"pdf")

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

	plotter.zoom_axis(two_month_ago, fit_finish)
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

	plotter.zoom_axis(two_month_ago, fit_finish)
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

	plotter.zoom_axis(three_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename,"pdf")

	plotter.draw(log = True)
	plotter.c.Print(filename,"pdf")


	plotter.clear()
	#################################


	###############################
	plotter = Plotter_SIR("wo China",
		draw_seq = ("infected", "recovered"),
		to_fit = False
		)

	plotter.zoom_axis(three_month_ago, fit_finish)
	plotter.draw()

	plotter.c.Print(filename+")","pdf")


	plotter.clear()
	#################################




# for days in range(1, 15):
# 	today = (date.today() - timedelta(days = days))
# 	make_daily_report(today)

today = (date.today() - timedelta(days = 1))
make_daily_report(today)

