from logger import log
import easyocr as ocr

reader = ocr.Reader(['en'])

def read_text(path, min_conf=0.49):
    log(f"Reading text from {path}")

    result = reader.readtext(path)
    output = []

    for (bbox, text, prob) in result:
        if prob >= min_conf:

            # Convert bbox → Python floats
            bbox_py = []
            for point in bbox:
                bbox_py.append([float(x) for x in point])

            # Convert prob → Python float
            prob_py = float(prob)

            output.append({
                "bbox": bbox_py,
                "text": text,
                "confidence": prob_py
            })

    log(f"OCR found {len(output)} items")
    return output
