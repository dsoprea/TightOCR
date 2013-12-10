from tightocr.adapters.api_adapter import TessApi
from tightocr.adapters.lept_adapter import pix_read

def main():
    t = TessApi(None, 'eng');
    p = pix_read('receipt4.png')
    t.set_image_pix(p)
    t.recognize()
    print("Confidence: %d" % (t.mean_text_conf()))

    text = t.get_utf8_text()
    print(text)

if __name__ == '__main__':
    main()

