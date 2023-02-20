# 代码自作参考不可抄袭
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import qrcode
import cv2
import os
"""
全局通用函数
"""


def made(string, filename, name, suffix):
    if not os.path.exists('images'):
        os.mkdir('images')
    os.chdir('images')
    img = qrcode.make(string)
    img.save(filename+name+suffix)
    img.show()
    messagebox.showinfo('提示', '%s保存成功' % filename)
    os.chdir('..')
# 自动隐藏滚动条


def scrollbar_autohide(bar, widget):
    def show():
        bar.lift(widget)

    def hide():
        bar.lower(widget)
    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_frame_Qr_code_generator_tag = Frame_Qr_code_generator_tag(
            self)

    def __win(self):
        self.title("二维码生成器")
        # 设置窗口大小、居中
        width = 640
        height = 439
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)


class Frame_Qr_code_generator_tag(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_frame_Qr_code_attribute_adjustment_label = Frame_Qr_code_attribute_adjustment_label(
            self)
        self.tk_tabs_set = Frame_set(self)
        self.tk_label_frame_copyright = Frame_copyright(self)
        self.tk_label_frame_options = Frame_options(self)

    def __frame(self):
        self.configure(text="二维码生成器")
        self.place(x=0, y=0, width=636, height=415)


class Frame_Qr_code_attribute_adjustment_label(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_link = self.__tk_label_link()
        self.tk_label_path = self.__tk_label_path()
        self.tk_input_link = self.__tk_input_link()
        self.tk_input_path = self.__tk_input_path()
        self.tk_label_suffix = self.__tk_label_suffix()
        self.tk_select_box_suffix = self.__tk_select_box_suffix()
        self.tk_label_name = self.__tk_label_name()
        self.tk_input_name = self.__tk_input_name()

    def __frame(self):
        self.configure(text="二维码属性调整")
        self.place(x=0, y=0, width=455, height=181)

    def __tk_label_link(self):
        label = Label(self, text="请输入链接：", anchor="center")
        label.place(x=10, y=0, width=81, height=24)
        return label

    def __tk_label_path(self):
        label = Label(self, text="请输入存储路径：", anchor="center")
        label.place(x=10, y=30, width=97, height=24)
        return label

    def __tk_input_link(self):
        ipt = Entry(self)
        ipt.place(x=100, y=0, width=348, height=24)
        return ipt

    def __tk_input_path(self):
        ipt = Entry(self)
        ipt.place(x=110, y=30, width=338, height=24)
        ipt.insert(0, "C:\\Users\\Administrator\\Desktop\\")
        return ipt

    def __tk_label_suffix(self):
        label = Label(self, text="二维码后缀名：", anchor="center")
        label.place(x=10, y=90, width=87, height=24)
        return label

    def __tk_select_box_suffix(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = (".png", ".jpg", ".bmp", ".jpeg", ".gif")
        cb.place(x=100, y=90, width=53, height=24)
        cb.current(0)
        return cb

    def __tk_label_name(self):
        label = Label(self, text="二维码名字：", anchor="center")
        label.place(x=10, y=60, width=95, height=24)
        return label

    def __tk_input_name(self):
        ipt = Entry(self)
        ipt.place(x=110, y=60, width=338, height=24)
        return ipt


class Frame_set(Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):

        self.tk_tabs_set_0 = Frame_set_0(self)
        self.add(self.tk_tabs_set_0, text="设置")

        self.tk_tabs_set_1 = Frame_set_1(self)
        self.add(self.tk_tabs_set_1, text="二维码解析")

        self.place(x=0, y=190, width=454, height=200)


class Frame_set_0(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_size = self.__tk_label_size()
        self.tk_input_size = self.__tk_input_size()
        self.tk_label_Accuracy_rate = self.__tk_label_Accuracy_rate()
        self.tk_select_box_Accuracy_rate = self.__tk_select_box_Accuracy_rate()

    def __frame(self):
        self.place(x=0, y=190, width=454, height=200)

    def __tk_label_size(self):
        label = Label(self, text="二维码大小：", anchor="center")
        label.place(x=0, y=0, width=76, height=24)
        return label

    def __tk_input_size(self):
        ipt = Entry(self)
        ipt.place(x=80, y=0, width=215, height=24)
        ipt.insert(0, "5")
        return ipt

    def __tk_label_Accuracy_rate(self):
        label = Label(self, text="二维码正确率：", anchor="center")
        label.place(x=0, y=30, width=85, height=24)
        return label

    def __tk_select_box_Accuracy_rate(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = (
            qrcode.ERROR_CORRECT_M,
            qrcode.ERROR_CORRECT_L,
            qrcode.ERROR_CORRECT_H,
            qrcode.ERROR_CORRECT_Q
        )
        cb.current(0)
        cb.place(x=0, y=60, width=296, height=24)
        return cb


class Frame_set_1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_text_link = self.__tk_text_link()
        self.tk_label_OR_path = self.__tk_label_OR_path()
        self.tk_input_OR_path = self.__tk_input_OR_path()
        self.tk_button_search = self.__tk_button_search()

    def __frame(self):
        self.place(x=0, y=190, width=454, height=200)

    def __tk_text_link(self):
        text = Text(self)
        text.place(x=10, y=70, width=435, height=100)
        text.config(state=DISABLED)
        return text

    def __tk_label_OR_path(self):
        label = Label(self, text="二维码路径：", anchor="center")
        label.place(x=0, y=10, width=91, height=24)
        return label

    def __tk_input_OR_path(self):
        ipt = Entry(self)
        ipt.place(x=100, y=10, width=341, height=24)
        ipt.config(state=DISABLED)
        return ipt

    def __tk_button_search(self):
        btn = Button(self, text="查找文件")
        btn.place(x=360, y=40, width=70, height=24)
        return btn


class Frame_copyright(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_zz = self.__tk_label_zz()

    def __frame(self):
        self.configure(text="版权：")
        self.place(x=460, y=10, width=164, height=170)

    def __tk_label_zz(self):
        label = Label(self, text="作者：朱智昇", anchor="center")
        label.place(x=0, y=0, width=94, height=24)
        return label


class Frame_options(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_button_start_OR = self.__tk_button_start_OR()
        self.tk_button_operation = self.__tk_button_operation()
        self.tk_button_start_OR_s = self.__tk_button_start_OR_s()

    def __frame(self):
        self.configure(text="选项")
        self.place(x=460, y=230, width=163, height=150)

    def __tk_button_start_OR(self):
        btn = Button(self, text="开始创建二维码")
        btn.place(x=30, y=20, width=112, height=24)
        return btn

    def __tk_button_operation(self):
        btn = Button(self, text="操作说明")
        btn.place(x=30, y=100, width=112, height=24)
        return btn

    def __tk_button_start_OR_s(self):
        btn = Button(self, text="开始解码")
        btn.place(x=30, y=60, width=112, height=24)
        return btn


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def generate(self, evt):
        string = self.tk_label_frame_Qr_code_generator_tag.tk_label_frame_Qr_code_attribute_adjustment_label.tk_input_link.get()
        file = self.tk_label_frame_Qr_code_generator_tag.tk_label_frame_Qr_code_attribute_adjustment_label.tk_input_path.get()
        name = self.tk_label_frame_Qr_code_generator_tag.tk_label_frame_Qr_code_attribute_adjustment_label.tk_input_name.get()
        suffixs = self.tk_label_frame_Qr_code_generator_tag.tk_label_frame_Qr_code_attribute_adjustment_label.tk_select_box_suffix.get()
        list = file.strip().split('.')
        if suffixs.strip() != '':
            try:
                # BMP、JPG、JPEG、PNG、GIF
                if string.strip() != '' and name.strip() != '':
                    made(string, file, name, suffixs)
                else:
                    messagebox.showerror(
                        '错误',
                        '输入错误'
                    )
            except FileNotFoundError:
                messagebox.showerror(
                    '错误',
                    '请自己检查有没有这个文件'
                )
            except IndexError:
                messagebox.showerror(
                    '错误',
                    '请输入正确的文件名'
                )
        elif suffixs.strip() == '':
            try:
                # BMP、JPG、JPEG、PNG、GIF
                if string.strip() != '' and (list[1] == 'jpg' or list[1] == 'jpeg' or list[1] == 'png' or list[1] == 'gif' or list[1] == 'bmp'):
                    made(string, file, suffixs)
                else:
                    messagebox.showerror(
                        '错误',
                        '输入错误'
                    )
            except FileNotFoundError:
                messagebox.showerror(
                    '错误',
                    '请自己检查有没有这个文件'
                )
            except IndexError:
                messagebox.showerror(
                    '错误',
                    '请输入正确'
                )

    def Operational_operation(self, evt):
        root = Tk()
        root.title("操作说明")
        root.geometry("500x300")
        root.resizable(False, False)
        Label(root, text="\
        1.二维码生成步骤：\n\
            1.首先输入二维码\n\
            2.输入存储地方\n\
            3.点击开始生成就完成了！！！\n\
        --------------------------------------------\n\
        2.二维码解码步骤：\n\
            1.输入你的二维码存放路径\n\
            2.点击解码就解码完成！！！\n\
        --------------------------------------------\n\
        3.图片类型可以有：BMP、JPG、JPEG、PNG、GIF"
              ).pack()
        root.mainloop()
    def selectPath(self):
        # path_ = askdirectory() #使用askdirectory()方法返回文件夹的路径
        # if path_ == "":
        #     self.tk_label_frame_Qr_code_generator_tag.tk_tabs_set.tk_tabs_set_1.tk_input_OR_path.get() #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        # else:
        #     path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
        #     self.tk_label_frame_Qr_code_generator_tag.tk_tabs_set.tk_tabs_set_1.tk_input_OR_path.set(path_)
    def __event_bind(self):
        self.tk_label_frame_Qr_code_generator_tag.tk_label_frame_options.tk_button_start_OR.bind(
            '<Button-1>', self.generate)
        self.tk_label_frame_Qr_code_generator_tag.tk_tabs_set.tk_tabs_set_1.tk_button_search.bind('<Button-1>',self.selectPath)


if __name__ == "__main__":
    win = Win()
    win.mainloop()
