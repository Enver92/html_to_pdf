from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseServerError
# from django.conf import settings

from .PDFlib.PDFlib import *

from sys import exc_info
from traceback import print_tb
from .models import Answer

# Create your views here.
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'

    answers = Answer.objects.filter(user=request.user)

    if not answers:
        raise Http404("No answers.")

    x = 55
    xt = 280
    center = xt/2
    y = 60
    yoff = 20
    baseopt = "fontname={Helvetica} embedding encoding=unicode "
            # "tabalignment {right left right right right} " +\
            # "hortabmethod ruler fontsize 12 "
    # user_name =

    p = PDFlib()

    try:
        # This means we must check return values of load_font() etc.
        p.set_option("errorpolicy=return")
        p.begin_document("", "")
        p.begin_page_ext(0, 0, "width=a4.width height=a4.height topdown")

        # Setting font properties
        boldfont = p.load_font("Helvetica-Bold", "unicode", "")
        if boldfont == -1:
            raise PDFlibException("Error: " + p.get_errmsg())
        regularfont = p.load_font("Helvetica", "unicode", "")
        if regularfont == -1:
            raise PDFlibException("Error: " + p.get_errmsg())


        # optlist = baseopt +"font " + repr(regularfont)

        p.fit_textline("NOTICE: THIS DOCUMENT CONTAINS SENSITIVE DATA", x, y, "fontname={Helvetica} embedding fontsize=12 encoding=unicode")

            # p.fit_textline("{}: <underline=true>{}<underline=false>".format(answer.question_name, answer.value),
            #                 x,
            #                 y,
            #                 "fontname={Helvetica} embedding fontsize=16 encoding=unicode")



        y += yoff
        p.fit_textline("CASE NUMBER: {}".format(answers[1].value), center, y, "fontname={Helvetica} embedding fontsize=16 encoding=unicode")
        y += yoff
        p.fit_textline("IN THE MATTER OF THE MARRIAGE OF", center, y+yoff, "fontname={Helvetica} embedding fontsize=16 encoding=unicode")
    
        for answer in answers:
            y += yoff
            text = "{}: <underline=true>{}<underline=false>".format(answer.question_name, answer.value)
            tflow = p.create_textflow(text, "fontname={Helvetica} embedding fontsize=16 encoding=unicode")
            p.fit_textflow(tflow, x, y, 500, 300, "fitmethod=auto")


        # p.show("{}\t\t{}".format(answers[0].question_name, answer.value))
        # for answer in answers[1:]:
        #     p.continue_text("{}\t\t{}".format(answer.question_name, answer.value))
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
