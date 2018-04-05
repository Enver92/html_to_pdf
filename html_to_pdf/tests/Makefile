# Sample Makefile for PDFlib's Python binding
# $Id$


RM	= rm -f
PYBIN = python

all: test

test::
	-$(PYBIN) hello.py
	-$(PYBIN) image.py
	-$(PYBIN) pdfclock.py
	-$(PYBIN) invoice.py
	-$(PYBIN) businesscard.py
	-$(PYBIN) starter_basic.py
	-$(PYBIN) starter_block.py
	-$(PYBIN) starter_color.py
	-$(PYBIN) starter_fallback.py
	-$(PYBIN) starter_graphics.py
	-$(PYBIN) starter_image.py
	-$(PYBIN) starter_layer.py
	-$(PYBIN) starter_opentype.py
	-$(PYBIN) starter_path.py
	-$(PYBIN) starter_pcos.py
	-$(PYBIN) starter_pdfa1b.py
	-$(PYBIN) starter_pdfa2b.py
	-$(PYBIN) starter_pdfmerge.py
	-$(PYBIN) starter_pdfua1.py
	-$(PYBIN) starter_pdfx3.py
	-$(PYBIN) starter_pdfx4.py
	-$(PYBIN) starter_portfolio.py
	-$(PYBIN) starter_pvf.py
	-$(PYBIN) starter_shaping.py
	-$(PYBIN) starter_svg.py
	-$(PYBIN) starter_table.py
	-$(PYBIN) starter_textflow.py
	-$(PYBIN) starter_textline.py
	-$(PYBIN) starter_webform.py

clean::
	$(RM) hello.pdf image.pdf pdfclock.pdf invoice.pdf
	$(RM) businesscard.pdf quickreference.pdf
	$(RM) starter*.pdf starter_pcos.txt
