# -*- mode: python -*-

block_cipher = None


a = Analysis(['DrawPython.py'],
             pathex=['E:\\02 大数据开发语言-Python\\01 课件\\大数据开发语言(Python语言程序设计)-课件\\Codes\\第02章 Python程序实例解析'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DrawPython',
          debug=False,
          strip=False,
          upx=True,
          console=True )
