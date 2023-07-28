import wx
import scanbarcode as sb
#import os
 
###############################################################################
class DirDialog(wx.Frame):
    """"""
    path = ""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self,None,-1,u"图片条码扫描-Silence Wang")
        b = wx.Button(self,-1,u"请选择照片文件夹扫描")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        
    #----------------------------------------------------------------------
    def OnButton(self, event):
        dlg = wx.DirDialog(self,u"选择文件夹扫描",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            #print(dlg.GetPath()) #文件夹路径
            self.path = dlg.GetPath()
            #print(self.path)
        dlg.Destroy()
        #print(self.path)
        sb.scan_barcode(self.path)
        #os.system(sb.path +"\\"+'barcodescanresult.xlsx')
###############################################################################
if __name__ == '__main__':
    frame = wx.App()
    app = DirDialog()
    app.Show()
    app.OnButton(wx.EVT_BUTTON)
    #print(app.path)
    #sb.scan_barcode(app.path)
    frame.MainLoop()