import io
import segno


def create_qr_code(query, dark="#000000", light="#FFFFFF", scale="10", kind="svg"):
    out = io.BytesIO()
    qr = segno.make(query, micro=False)
    qr.save(out, dark=dark, light=light, scale=scale, kind=kind)
    return out.getvalue()
