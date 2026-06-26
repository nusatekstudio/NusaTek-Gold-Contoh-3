# Dummy certificate PDF generator for Sofia Kirana's portfolio
import os
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

OUT_DIR = os.path.join(os.path.dirname(__file__), "certs")
os.makedirs(OUT_DIR, exist_ok=True)

RECIPIENT = "Sofia Kirana"

# (filename, course title, issuer, date, credential id)
CERTS = [
    ("adobe-visual-design.pdf",
     "Adobe Certified Professional — Visual Design",
     "Adobe", "May 2022", "ADB-VD-2022-08431"),
    ("google-ux-design.pdf",
     "Google UX Design Professional Certificate",
     "Google", "November 2021", "GOOG-UX-2021-55217"),
    ("rca-photography-masterclass.pdf",
     "Contemporary Photography Masterclass",
     "Royal College of Art, London", "March 2023", "RCA-PHM-2023-01194"),
    ("calarts-graphic-design.pdf",
     "Graphic Design Specialization",
     "California Institute of the Arts · Coursera", "July 2020", "CAL-GDS-2020-73620"),
    ("idf-mobile-ui-patterns.pdf",
     "Mobile UI Design Patterns",
     "Interaction Design Foundation", "September 2022", "IDF-MUI-2022-44980"),
    ("itb-web-development.pdf",
     "Web Development Fundamentals",
     "Institut Teknologi Bandung", "February 2019", "ITB-WDF-2019-30715"),
]

NAVY = HexColor("#1b2a4a")
BLUE = HexColor("#5cb3f5")
GOLD = HexColor("#c9a24b")
GREY = HexColor("#6c7585")
DARK = HexColor("#2b2b2b")


def draw_certificate(path, course, issuer, date, cred_id):
    W, H = landscape(A4)
    c = canvas.Canvas(path, pagesize=landscape(A4))

    # Outer border
    c.setStrokeColor(NAVY)
    c.setLineWidth(3)
    c.rect(12 * mm, 12 * mm, W - 24 * mm, H - 24 * mm)
    # Inner thin gold border
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.rect(16 * mm, 16 * mm, W - 32 * mm, H - 32 * mm)

    cx = W / 2

    # Header
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(cx, H - 35 * mm, issuer.upper())

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(cx, H - 52 * mm, "CERTIFICATE")
    c.setFillColor(GREY)
    c.setFont("Helvetica", 13)
    c.drawCentredString(cx, H - 60 * mm, "OF COMPLETION")

    # Divider
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(cx - 30 * mm, H - 66 * mm, cx + 30 * mm, H - 66 * mm)

    # Presented to
    c.setFillColor(GREY)
    c.setFont("Helvetica", 12)
    c.drawCentredString(cx, H - 80 * mm, "This is proudly presented to")

    # Recipient name
    c.setFillColor(DARK)
    c.setFont("Helvetica-BoldOblique", 34)
    c.drawCentredString(cx, H - 96 * mm, RECIPIENT)
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.8)
    c.line(cx - 70 * mm, H - 100 * mm, cx + 70 * mm, H - 100 * mm)

    # Course description
    c.setFillColor(GREY)
    c.setFont("Helvetica", 12)
    c.drawCentredString(cx, H - 112 * mm, "for successfully completing the program")
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(cx, H - 122 * mm, course)

    # Footer: date (left) and signature (right)
    base_y = 34 * mm
    left_x = 45 * mm
    right_x = W - 45 * mm

    c.setStrokeColor(DARK)
    c.setLineWidth(0.8)
    c.line(left_x - 22 * mm, base_y, left_x + 22 * mm, base_y)
    c.line(right_x - 22 * mm, base_y, right_x + 22 * mm, base_y)

    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(left_x, base_y - 6 * mm, date)
    c.setFont("Helvetica-Oblique", 14)
    c.drawCentredString(right_x, base_y + 2 * mm, issuer.split(" ")[0])
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(right_x, base_y - 6 * mm, "Authorized Signature")

    c.setFillColor(GREY)
    c.setFont("Helvetica", 9)
    c.drawCentredString(left_x, base_y - 11 * mm, "Date Issued")

    # Seal (center bottom)
    seal_y = base_y + 4 * mm
    c.setStrokeColor(GOLD)
    c.setFillColor(HexColor("#fbf6e9"))
    c.setLineWidth(2)
    c.circle(cx, seal_y + 4 * mm, 11 * mm, stroke=1, fill=1)
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cx, seal_y + 6 * mm, "VERIFIED")
    c.drawCentredString(cx, seal_y + 1 * mm, "CREDENTIAL")

    # Credential id
    c.setFillColor(GREY)
    c.setFont("Helvetica", 9)
    c.drawCentredString(cx, 20 * mm, "Credential ID: " + cred_id)

    c.showPage()
    c.save()


for fname, course, issuer, date, cred in CERTS:
    out = os.path.join(OUT_DIR, fname)
    draw_certificate(out, course, issuer, date, cred)
    print("created", out)

print("Done. %d certificates generated." % len(CERTS))
