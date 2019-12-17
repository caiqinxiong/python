# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/17 10:09
from barcode.writer import ImageWriter
from barcode.ean import EuropeanArticleNumber13
import barcode

# python-barcode支持的条形码格式
print(barcode.PROVIDED_BARCODES)

EAN = barcode.get_barcode_class('ean13')  #创建ean13格式的条形码格式对象
print(EAN)

ean = EAN('5901234123457',writer=ImageWriter())  #创建条形码对象，内容为5901234123457
print(ean)
fullname = ean.save('ean13_barcode')  #保存条形码图片，并返回保存路径。图片格式为png

print(fullname)