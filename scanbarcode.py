#-*- coding:utf-8 -*-
import cv2
import pyzbar.pyzbar as pyzbar
import os,shutil,sys
import xlsxwriter
import numpy as np
import win32com.client as win32
#from PIL import Image
#import winreg

#def GetDesktopPath():
#    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
#    return winreg.QueryValueEx(key, "Desktop")[0]
if getattr(sys,'frozen',False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(os.path.abspath(__file__))

def decode(img_path): 
    img_data= cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),cv2.IMREAD_GRAYSCALE)  
    # 转为黑白图像  
    img_binary = cv2.threshold(img_data,127, 255, cv2.THRESH_BINARY)[1]
    barcodes = pyzbar.decode(img_binary)
    #img = Image.open(img_path)
    #barcodes = pyzbar.decode(img)
    #test=pyzbar.decode(frame,ymbols=[64])
    #print(barcodes)
    bardict=[]
    #print(barcodes)
    if len(barcodes):
        for barcode in barcodes:
            # 条形码数据为字节对象，所以如果我们想在输出图像上
            # 画出来，就需要先将它转换成字符串
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # 向终端打印条形码数据和条形码类型
            #print("扫描结果==》 类别： {0} 内容： {1}".format(barcodeType, barcodeData))
            b={}
            b["barcodeData"]=barcodeData
            b["barcodeType"]=barcodeType
            bardict.append(b)
            #bardict.append(barcodeType)
            #return barcodeType,barcodeData
            #print(b)
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
    worksheet.write('A1','文件夹/款号')
    worksheet.write('B1','照片名')
    worksheet.write('C1','条码类型')
    worksheet.write('D1','条码')
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
    '''
    if getattr(sys,'frozen',False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(os.path.abspath(__file__))
    '''
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
    #decode(r"C:\Users\perfa\Desktop\Python\barcdsc\1223\IMG_6895.JPG")
    scan_barcode(r"C:\Users\perfa\Desktop\Python\barcdsc\1223")