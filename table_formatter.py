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

		lengths = [[0, 0] for c in range(0, number_of_columns[0])]
		result = ''

		for row in data:
			for col, value in enumerate(row):
				length = len(value)
				int_value = self._cast(value, int)
				float_value = self._cast(value, float)

				if length > lengths[col][0]:
					lengths[col][0] = length

				if int_value == None and float_value != None:
					int_length = len(str(int(self._cast(value, float))))

					if int_length > lengths[col][1]:
						lengths[col][1] = int_length

		for row in data:
			for col, value in enumerate(row):
				value_length = len(value)
				max_length = lengths[col][0]
				column_length = max_length

				if align == 'auto':
					float_value = self._cast(value, float)

					if self._cast(value, int) != None:
						value_align = 'right'
					elif float_value != None:
						value_align = 'point'
						value_length = len(str(int(float_value)))
						max_length = lengths[col][1]
					else:
						value_align = 'left'
				else:
					value_align = align

				result += self._pad(value, value_length, max_length, column_length, col == len(lengths) - 1, value_align)

			result = result.rstrip(' ') + '\n'

		return result.rstrip('\n')

	def _pad(self, value, value_length, max_length, column_length, last=False, align='left'):
		if last and not value:
			return value

		padding_length = (max_length - value_length)

		if align == 'left' and not last:
			value = value + ' ' * padding_length
		elif align in 'right':
			value = ' ' * padding_length + value
		elif align == 'point':
			value = ' ' * padding_length + value
			value = value + ' ' * (column_length - len(value))

		if not last:
			value = value + ' ' * self.space

		return value


	def _cast(self, str, caster, default=None):
		str = str.rstrip('%').replace(',', '.').rstrip();

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