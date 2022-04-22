import pause
import requests
import struct
import ctypes
import os
import ctypes
import win32con
import os


def SetWallpaper(path):
    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER,
                                               0, path, changed)
    os.system(f'"D:\Code\DailyBing\igcmdWin10.exe" setlockimage {path}')


WallpaperJson = requests.get(
    "https://bing.biturl.top/?mkt=zh-CN&resolution=3840")
WallpaperPhoto = requests.get(WallpaperJson.json()["url"])
with open("DailyWalp" + WallpaperJson.json()["start_date"] + ".jpg",
          "wb") as f:
    f.write(WallpaperPhoto.content)
while True:
    SetWallpaper(os.getcwd() + "\\DailyWalp" +
                 WallpaperJson.json()["start_date"] + ".jpg")
    pause.hours(1)