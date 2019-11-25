import sublime, sublime_plugin


class TableFormatter(object):
	def __init__(self, view):
		self.view = view
		self.space = 1

	def format(self, edit, align='auto'):
		view = self.view

		for region in view.sel():
			if region.empty():
				region = sublime.Region(0, view.size())

			view.replace(edit, region, self._format(view.substr(region), align))

	def _format(self, data, align):
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
				if align == 'auto':
					if (self._cast(value, int) or self._cast(value, float)) != None:
						value_align = 'right'
					else:
						value_align = 'left'
				else:
					value_align = align

				result += self._pad(value, lengths[col], col == len(lengths) - 1, value_align)

			result += '\n'

		return result.rstrip('\n')

	def _pad(self, value, column_width, last=False, align='left'):
		pad = ' ' * (column_width - len(value))

		if align == 'left' and not last:
			value = value + pad
		elif align == 'right':
			value = pad + value

		if not last:
			value = value + ' ' * self.space

		return value


	def _cast(self, str, caster, default=None):
		try:
			return caster(str)
		except (ValueError, TypeError):
			return default


class FormatCommand(sublime_plugin.TextCommand):
	def __init__(self, *args):
		super(FormatCommand, self).__init__(*args)

		self.formatter = TableFormatter(self.view)


class FormatTableCommand(FormatCommand):
	def run(self, edit):
		self.formatter.format(edit)


class FormatTableLeftCommand(FormatCommand):
	def run(self, edit):
		self.formatter.format(edit, align='left')


class FormatTableRightCommand(FormatCommand):
	def run(self, edit):
		self.formatter.format(edit, align='right')