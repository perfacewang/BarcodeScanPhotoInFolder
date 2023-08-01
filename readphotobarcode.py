import wx
import scanbarcode as sb
 
###############################################################################
class DirDialog(wx.Frame):

    path = ""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self,None,-1,u"ScanBarcodeFromPhotos")
        b = wx.Button(self,-1,u"Please select a photo folder to scan")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        
    #----------------------------------------------------------------------
    def OnButton(self, event):
        dlg = wx.DirDialog(self,u"Select folder scan",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
        dlg.Destroy()
        sb.scan_barcode(self.path)
###############################################################################
if __name__ == '__main__':
    frame = wx.App()
    app = DirDialog()
    app.Show()
    app.OnButton(wx.EVT_BUTTON)
    frame.MainLoop()