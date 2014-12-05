import clipboard

class ClipBoardTest():
	def paste_clipboard(self):
		text = clipboard.paste()
		return text
