from django.http.response import HttpResponse
import qrcode
import qrcode.image.svg
import io


# Create your views here.
# ERROR_CORRECT_L = 1
# ERROR_CORRECT_M = 0
# ERROR_CORRECT_Q = 3
# ERROR_CORRECT_H = 2


def index_view(request):
    data = request.GET.get('query', '')
    version = int(request.GET.get('version', 1))
    error_correction = int(request.GET.get('error_correction', 0))
    box_size = int(request.GET.get('box_size', 10))
    border = int(request.GET.get('border', 4))

    res = get_qr_svg_string(data, version=version, error_correction=error_correction, box_size=box_size, border=border)

    return HttpResponse(res, content_type="image/svg+xml")


def get_qr_svg_string(data, version=1, error_correction=qrcode.ERROR_CORRECT_M, box_size=10, border=4):
    factory = qrcode.image.svg.SvgPathFillImage
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
        image_factory=factory
    )
    qr.add_data(str(data))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    stream = io.BytesIO()
    img.save(stream)

    svg_string = str(stream.getvalue().decode("utf-8"))

    return svg_string
