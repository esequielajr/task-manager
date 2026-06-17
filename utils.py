def title(text='text', style='-', size=2):
	
	text = text.upper()
	
	print('\n', style * (len(text)*size), sep='')
	print(f'{text:^{len(text)*size}}')
	print(style * (len(text)*size), '\n', sep='')
