# String_parser-from_document
Strip pdf/text into strings


	args in: {file_name, type = 'file_type', delete = [], start = [], end = [], both = [], lower_case = Bool}

	file_name: Name of the file with extension as string
	path   : only specify if the file is in a different directory, input as string
	type   : 'txt' or 'pdf'
	delete : Removes the char everywhere in the string_list
	start  : Removes the char at the start of string_list but not everywhere
	end    : Removes the char at the end of string_list but not everywhere
	both   : Removes the char at either ends. If both is defined, start and end lists are redundant
	lower_case: Boolean input for forcing all chars to lower case; True by default

No packages required unless you wish to parse strings from pdf, then the only requirement is the package 'tika'

Note: tika requires java 7+ to run pdf_parser file courtesy: tika Dev team.

Errors while running tika: Make sure that Java version 7+ is installed, added to path variable and PC restarted once Java is installed.
