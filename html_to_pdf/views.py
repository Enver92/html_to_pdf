from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import settings

from sys import exc_info
from traceback import print_tb
from .PDFlib.PDFlib import *

from .models import Answer

# Create your views here.
def html_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'

    answers = Answer.objects.filter(user=request.user)


    p = PDFlib()

    try:
        # This means we must check return values of load_font() etc.
        p.set_option("errorpolicy=return")

        p.begin_document("", "")

        p.begin_page_ext(595, 842, "")

        font = p.load_font("Helvetica-Bold", "unicode", "")
        if font == -1:
            raise PDFlibException("Error: " + p.get_errmsg())

        p.setfont(font, 24)
        p.set_text_pos(50, 700)
        p.show("Hi")
        p.continue_text("(says Python)")
        p.end_page_ext("")

        p.end_document("")

        pdf = p.get_buffer();
        response.write(pdf)

    except PDFlibException:
        print("PDFlib exception occurred:\n[%d] %s: %s" %
    	((p.get_errnum()), p.get_apiname(),  p.get_errmsg()))
        print_tb(exc_info()[2])

    except Exception:
        print("Exception occurred: %s" % (exc_info()[0]))
        print_tb(exc_info()[2])

    finally:
        p.delete()


    return response
