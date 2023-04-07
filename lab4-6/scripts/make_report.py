#!/usr/bin/env python3

from fpdf import FPDF

m = 10 
pw = 210 - 2*m
ch = 50
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=5, txt="Roksana Malinowska. Solutions for labs 4-6.")
pdf.ln(10)
pdf.multi_cell(w=0, h=5, txt="Task2")
pdf.image('../plots/task2a.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task2b.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task2c.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task2d.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.ln(10)
pdf.multi_cell(w=0, h=5, txt="Task3")
pdf.image('../plots/task3a.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task3b.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task3c.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.ln(10)
pdf.multi_cell(w=0, h=5, txt="Task4")
pdf.image('../plots/task4a.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task4b.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task4c.png', x = 10, y = None, w = 170, h = 0, type = 'PNG')
pdf.ln(10)
pdf.multi_cell(w=0, h=5, txt="Task5")
pdf.image('../plots/task5a.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.ln(5)
pdf.image('../plots/task5b.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task5c.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.ln(5)
pdf.image('../plots/task5d.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.image('../plots/task5e.png', x = 10, y = None, w = 150, h = 0, type = 'PNG')
pdf.output(f'../report.pdf', 'F')