# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['gui_sensorlyze.py'],
             pathex=['C:/Users/admin/Desktop/Sensorlyzev2'],
             binaries=[],
             datas =[('C:/Users/admin/Desktop/Sensorlyzev2/icon.jpg','.'),('C:/Users/admin/Desktop/Sensorlyzev2/background.jpg','.')],
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
          name='Sensorlyze',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='C:/Users/admin/Desktop/Sensorlyzev2/icon_gui.ico')
