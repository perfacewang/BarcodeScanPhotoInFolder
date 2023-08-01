# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['readphotobarcode.py'],
             pathex=[],
             binaries=[],
             datas=[(
            r'C:\Users\perfa\AppData\Local\Programs\Python\Python39\Lib\site-packages\pyzbar\libzbar-64.dll',
            r'.\pyzbar'
        ),
        (
            r'C:\Users\perfa\AppData\Local\Programs\Python\Python39\Lib\site-packages\pyzbar\libiconv.dll',
            r'.\pyzbar'
        )],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='readphotobarcode',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
