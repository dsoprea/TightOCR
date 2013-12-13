from tightocr.adapters.api_adapter import TessApi
from tightocr.adapters.lept_adapter import pix_read
from tightocr.constants import RIL_PARA

def main():
    t = TessApi(None, 'eng');
    p = pix_read('receipt.png')
    t.set_image_pix(p)
    t.recognize()

    if t.mean_text_confidence() < 85:
        raise Exception("Too much error.")

    for block in t.iterate(RIL_PARA):
        print(block)

#    direction = t.get_text_direction()
#    print(t.get_hocr_text(1))
#    print(t.get_utf8_text())

if __name__ == '__main__':
    main()

