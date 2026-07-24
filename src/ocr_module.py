from logger import log
import easyocr as ocr

reader = ocr.Reader(['en'])

def read_text(path, min_conf=0.49):
    log(f"Reading text from {path}")

    result = reader.readtext(path)
    output = []

    for (bbox, text, prob) in result:
        if prob >= min_conf:
            output.append((bbox, text, prob))

    log(f"OCR found {len(output)} items")
    return output
