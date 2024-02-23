import win32print
import win32ui
from PIL import Image, ImageWin
from imge_list import printer_list

# 列出所有打印机
printers = [printer[2] for printer in win32print.EnumPrinters(2)]
for i, printer in enumerate(printers):
    print(f"{i+1}: {printer}")


win32print.OpenPrinter()

# 选择打印机
choice = int(input("选择要使用的打印机 (输入对应的序号): ")) - 1
printer_name = printers[choice]

# 调用打印机打印图片
for i in printer_list():
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)

    # 打开图片
    bmp = Image.open(i)

    scale = 1
    w, h = bmp.size
    hDC.StartDoc("D:/temp/girl3.jpg")
    hDC.StartPage()

    dib = ImageWin.Dib(bmp)
    # (10,10,1024,768)前面的两个数字是坐标，后面两个数字是打印纸张的大小
    dib.draw(hDC.GetHandleOutput(), (10, 10, 1024, 768))

    hDC.EndPage()
    hDC.EndDoc()
hDC.DeleteDC()
