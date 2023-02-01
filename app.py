import io
from PIL import Image
from flask import Flask, render_template, request, Response

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jpgtowebp")
def jpgtowebp():
    return render_template("jpgtowebp.html")

@app.route("/pngtowebp")
def pngtowebp():
    return render_template("pngtowebp.html")

@app.route("/bmptowebp")
def bmptowebp():
    return render_template("bmptowebp.html")

@app.route("/jpgtopdf")
def jpgtopdf():
    return render_template("jpgtopdf.html")

@app.route("/pngtopdf")
def pngtopdf():
    return render_template("pngtopdf.html")

@app.route("/bmptopdf")
def bmptopdf():
    return render_template("bmptopdf.html")

@app.route("/api/jpgtowebp", methods=["POST"])
def jpg_to_webp():
    output_filename = "converted.webp"
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'WEBP')
    byte_io.seek(0)
    return Response(byte_io, content_type='image/webp', headers={
        "Content-Disposition": "attachment; filename="+output_filename
    })

@app.route("/api/pngtowebp", methods=["POST"])
def png_to_webp():
    output_filename = "converted.webp"
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'WEBP')
    byte_io.seek(0)
    return Response(byte_io, content_type='image/webp', headers={
        "Content-Disposition": "attachment; filename="+output_filename
    })

@app.route("/api/bmptowebp", methods=["POST"])
def bmp_to_webp():
    output_filename = "converted.webp"
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'WEBP')
    byte_io.seek(0)
    return Response(byte_io, content_type='image/webp', headers={
        "Content-Disposition": "attachment; filename="+output_filename
    })

@app.route("/api/jpgtopdf", methods=["POST"])
def jpg_to_pdf():
    output_filename = "converted.pdf"
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'PDF')
    byte_io.seek(0)
    return Response(byte_io, content_type='application/pdf', headers={
        "Content-Disposition": "attachment; filename="+output_filename
    })

@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    output_filename = "converted.pdf"
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'PDF')
    byte_io.seek(0)
    return Response(byte_io, content_type='application/pdf', headers={
        "Content-Disposition": "attachment; filename="+output_filename
    })

@app.route("/api/bmptopdf", methods=["POST"])
def bmp_to_pdf():
    output_filename = "converted.pdf"
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'PDF')
    byte_io.seek(0)
    return Response(byte_io, content_type='application/pdf', headers={
        "Content-Disposition": "attachment; filename="+output_filename
    })

if __name__ == "__main__":
    app.run(debug=True)
