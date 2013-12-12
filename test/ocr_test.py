from tightocr.adapters.api_adapter import TessApi
from tightocr.adapters.lept_adapter import pix_read
from tightocr.constants import RIL_PARA

def main():
    t = TessApi(None, 'eng');
    p = pix_read('receipt4.png')
    t.set_image_pix(p)
    t.recognize()
    print("Confidence: %d" % (t.mean_text_conf()))

    for block in t.iterate(RIL_PARA):
        print block

#    text = t.get_utf8_text()
#    print(text)

if __name__ == '__main__':
    main()

