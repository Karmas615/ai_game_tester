import easyocr as ocr

reader = ocr.Reader(['en'])

def read_text(path, min_conf=0.49):
    result = reader.readtext(path)
    output = []

    for (bbox, text, prob) in result:
        if prob >= min_conf:
            output.append((bbox, text, prob))
            print(text, prob)

    return output



