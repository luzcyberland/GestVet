from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += '<li> {} </li>'.format(event.get_html_url)

		if day != 0:
			return "<td>{}<ul> {} </ul></td>".format(day,d)
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return '<tr> {} </tr>'.format(week)

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = '<table border="0" cellpadding="0" cellspacing="0" class="table table-bordered">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += '{}\n'.format(self.formatweekheader())
		for week in self.monthdays2calendar(self.year, self.month):
			cal += '{}\n'.format(self.formatweek(week, events))
		return cal
