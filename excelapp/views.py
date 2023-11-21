from django.shortcuts import render
import os
import openpyxl

import pprint
from django.http import HttpResponse
from openpyxl import Workbook
from django.conf import settings
from . models import Product

def index(request):
    
    a='XXXXX'
    b='YYYYY'
    
    return returnExcel(a,b)

def returnExcel(a,b):
    """
      Excel output from template
    """
    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook(os.path.join(settings.BASE_DIR, 'media/exceltemplate/sample.xlsx'))

    sheet = wb['Sheet1']
    sheet['C2'] = a
    sheet['E2'] = b
# Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'report.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response

# https://studygyaan.com/django/how-to-export-excel-file-with-django
def export_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="products.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    # Add headers
    headers = ["Name", "Price", "Quantity"]
    ws.append(headers)

    # Add data from the model
    products = Product.objects.all()
    for product in products:
        ws.append([product.name, product.price, product.quantity])

    # Save the workbook to the HttpResponse
    wb.save(response)
    return response