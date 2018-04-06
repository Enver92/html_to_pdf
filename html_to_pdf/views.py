from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseServerError
# from django.conf import settings

from .PDFlib.PDFlib import *

from .models import Answer

# Create your views here.
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'

    answers = Answer.objects.filter(user=request.user)
    for answer in answers:
        print(answer.value)
    if not answers:
        raise Http404("No answers.")

    left = 55
    right = 530
    fontsize = 12
    pagewidth = 595
    pageheight = 842
    baseopt = \
            "ruler        {   30 45     275   375   475} " +\
            "tabalignment {right left right right right} " +\
            "hortabmethod ruler fontsize 12 "
    # user_name =

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
        
        p.show("{}\t\t{}".format(answers[0].question_name, answer.value))
        for answer in answers[1:]:
            p.continue_text("{}\t\t{}".format(answer.question_name, answer.value))
        p.end_page_ext("")

        p.end_document("")

        pdf = p.get_buffer();
        response.write(pdf)

    except:
        return HttpResponseServerError()

    finally:
        p.delete()


    return response
