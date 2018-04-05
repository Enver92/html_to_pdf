from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseServerError
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

    if not answers:
        raise Http404("No answers.")

    p = PDFlib()

    try:
        # This means we must check return values of load_font() etc.
        p.set_option("errorpolicy=return")

        p.begin_document("", "")

        p.begin_page_ext(595, 842, "")

        font = p.load_font("Helvetica-Bold", "unicode", "")
        if font == -1:
            raise PDFlibException("Error: " + p.get_errmsg())

        p.setfont(font, 18)
        p.set_text_pos(90, 800)
        p.show(answers[0].question_name)
        p.continue_text("(says Python)")
        p.end_page_ext("")

        p.end_document("")

        pdf = p.get_buffer();
        response.write(pdf)

    except:
        return HttpResponseServerError()

    finally:
        p.delete()


    return response
