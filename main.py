from pikepdf import Pdf, Page, Rectangle, Encryption
import json


def pdfMerge(pdf_1_location, pdf_2_location):
    pdf_1 = Pdf.open(pdf_1_location)
    pdf_2 = Pdf.open(pdf_2_location)

    pdf_1.pages.extend(pdf_2.pages)
    pdf_1.save("out-pdf-files/out-pdfMerge.pdf")


def pdfReturn(pdf_location, page_numbers):
    pdf = Pdf.open(pdf_location)
    nd_page_numbers = [*set(page_numbers)]
    
    pdf.save("out-pdf-files/out-pdfReturn.pdf")


def pdfDelete(pdf_location, page_numbers):
    pdf = Pdf.open(pdf_location)
    nd_page_numbers = [*set(page_numbers)]
    for i in range(len(nd_page_numbers)):
        pdf.pages.remove(p = page_numbers[i])
    pdf.save("out-pdf-files/out-pdfDelete.pdf")


def pdfMetadata(pdf_location):
    pdf = Pdf.open(pdf_location)
    meta = pdf.open_metadata()
    data = {"title":meta['dc:title'], 
            "pdf version":meta['pdf:Producer'], 
            "creation date":meta['xmp:CreateDate'], 
            "description":meta['dc:description']}
    file = open("json/pdf-info.json", "w")
    file.write(json.dumps(data, indent=4))
    file.close()


def pdfWatermark(pdf_location, watermark_location):
    pdf = Pdf.open(pdf_location)
    watermark_pdf = Pdf.open(watermark_location)
    watermark = Page(watermark_pdf.pages[0])
    for page in range(len(pdf.pages)):
        Page(pdf.pages[page]).add_overlay(watermark, Rectangle(50, 50, 150, 150))
    pdf.save("out-pdf-files/out-pdfWatermark.pdf")


def pdfEncrypt(pdf_location, password, owner_password):
    pdf = Pdf.open(pdf_location)
    pdf.save("out-pdf-files/out-pdfEncrypt.pdf", encryption=Encryption(user=password, owner=owner_password))

#pdfMerge('pdf-files/rtx-2070-manual.pdf', 'pdf-files/rx-5700xt-manual.pdf')
pdfReturn('pdf-files/rtx-2070-manual.pdf', [1,25])
#pdfDelete('pdf-files/rtx-2070-manual.pdf', [1,25])
#pdfMetadata('pdf-files/rtx-2070-manual.pdf')
#pdfWatermark('pdf-files/rtx-2070-manual.pdf', "watermark/triangle_watermark.pdf")
#pdfEncrypt('pdf-files/rtx-2070-manual.pdf', "user", "owner")

