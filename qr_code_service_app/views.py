from django.http.response import HttpResponse, HttpResponseBadRequest
from qr_code_service_app.forms import QrGenerateForm
from qr_code_service_app.generator import create_qr_code


def index_view(request):
    form = QrGenerateForm(request.GET)
    if form.is_valid():
        qr = create_qr_code(form.cleaned_data['query'],
                            dark=form.cleaned_data['dark'],
                            light=form.cleaned_data['light'],
                            kind=form.cleaned_data['kind'],
                            scale=form.cleaned_data['scale'])
        return HttpResponse(qr, content_type=form.get_content_type())
    else:
        return HttpResponseBadRequest(form.errors.as_json())
