from PIL import Image
import pytesseract
# import cv2
from pdf2image import convert_from_path
from spellchecker import SpellChecker

spell = SpellChecker()
# images = convert_from_path('chapter_8_-_chemistry_-_classifying_compounds.pdf')
text = open('text.txt', 'r+')
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# for i in range(len(images)):
#     text.writelines(pytesseract.image_to_string(Image.open(f"page{i}.jpg")))
mispelled = list()
for line in text:
    mispelled += line.split(" ")
mispell = spell.unknown(mispelled)
print(mispelled)
for word in mispell:
    try:
        text.write(spell.correction(word))
    except TypeError:
        text.write("")

text.close()
