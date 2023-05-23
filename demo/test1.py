from cnocr import CnOcr

img_fp = r'E:\dataset\PNGImages_OCR\ADSP-2189M_3.png'

# ocr = CnOcr(rec_model_name='en_number_mobile_v2.0')
cr = CnOcr(rec_model_name='ch_PP-OCRv3', det_model_name='en_PP-OCRv3_det', cand_alphabet='()±+-.0123456789')
out = cr.ocr(img_fp)

print(out)
