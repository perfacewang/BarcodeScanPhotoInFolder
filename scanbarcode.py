#-*- coding:utf-8 -*-
import cv2
import pyzbar.pyzbar as pyzbar
import os,shutil,sys
import xlsxwriter
import numpy as np
import win32com.client as win32

if getattr(sys,'frozen',False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(os.path.abspath(__file__))

def decode(img_path): 
    img_data= cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),cv2.IMREAD_GRAYSCALE)  

    img_binary = cv2.threshold(img_data,127, 255, cv2.THRESH_BINARY)[1]
    barcodes = pyzbar.decode(img_binary)

    bardict=[]
    if len(barcodes):
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # print barcode result and type
            #print("result==》 type： {0} content： {1}".format(barcodeType, barcodeData))
            b={}
            b["barcodeData"]=barcodeData
            b["barcodeType"]=barcodeType
            bardict.append(b)

        return bardict
    else:
        return False

#字符串相减  
def strsubtract(str1,str2):
    return str2[str2.find(str1)+len(str1)+1:]

def write_excel(rslt):
    startline = 1
    workbook = xlsxwriter.Workbook('barcodescanresult.xlsx') 
    worksheet = workbook.add_worksheet(u'sheet1')
    worksheet.set_column(0,3,20)
    worksheet.write('A1','Folder/name')
    worksheet.write('B1','PhotoName')
    worksheet.write('C1','BarcodeType')
    worksheet.write('D1','Barcode')
    for i in rslt:
        worksheet.write(startline,0,i[0])
        worksheet.write(startline,1,i[1])
        worksheet.write(startline,2,i[2])
        worksheet.write(startline,3,i[3])
        startline += 1
    workbook.close()

def open_excel():
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    excel.Workbooks.Open(path+'\\'+'barcodescanresult.xlsx')

def scan_barcode(path):
    scanrslt = []
    b=[]
    for root, dirs, files in os.walk(path):
        for jpgfile in files:
            if jpgfile[-3:].find("jpg")>-1 or jpgfile[-3:].find("JPG") >-1: 
                b = decode(root+ "\\"+ jpgfile)
                if b != False:
                    for i in b:
                        scanrslt.append([strsubtract(path,root),jpgfile,i["barcodeType"],i["barcodeData"]])          
    if len(scanrslt):
        write_excel(scanrslt)
    open_excel()

if __name__ == "__main__":
    #test 
    scan_barcode(r"C:\Users\perfa\Desktop\Python\barcdsc\1223")