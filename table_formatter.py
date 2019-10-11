import sublime, sublime_plugin


class TableFormatter(object):
	def __init__(self, view):
		self.view = view
		self.space = 1

	def format(self, edit, align='left'):
		view = self.view

		for region in view.sel():
			if region.empty():
				region = sublime.Region(0, view.size())

			view.replace(edit, region, self._format(view.substr(region), align))

	def _format(self, data, align='left'):
		data = [row.split('\t') for row in data.split('\n')]
		number_of_columns = [0]

		for row in data:
			number_of_columns.append(len(row))
		number_of_columns.sort(reverse=True)

		lengths = [0 for c in range(0, number_of_columns[0])]
		result = ''

		for row in data:
			for col, value in enumerate(row):
				length = len(value)

				if length > lengths[col]:
					lengths[col] = length

		for row in data:
			for col, value in enumerate(row):
				result += self._pad(value, lengths[col] + self.space, col == 0, col == len(lengths) - 1, align)

			result += '\n'

		return result.rstrip('\n')

	def _pad(self, value, length, first=False, last=False, align='left'):
		pad = ' ' * (length - len(value))

		if align == 'left':
			if last:
				return value
			else:
				return value + pad
		else:
			if first:
				return value
			else:
				return pad + value


class FormatCommand(sublime_plugin.TextCommand):
	def __init__(self, *args):
		super(FormatCommand, self).__init__(*args)

		self.formatter = TableFormatter(self.view)


class FormatTableLeftCommand(FormatCommand):
	def run(self, edit):
		self.formatter.format(edit)


class FormatTableRightCommand(FormatCommand):
	def run(self, edit):
		self.formatter.format(edit, align='right')