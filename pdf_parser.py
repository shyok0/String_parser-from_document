'''
Role  : parser for pdf
Author: Yokesh
Email : y.subrmanian@keele.ac.uk
Courtesy: tika Dev team
'''

from tika import parser

def pdf_parser(path):
    raw = parser.from_file(path)
    return raw['content']
