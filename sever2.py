from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
import string
import random
import base64
import qrcode
import time
import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from PIL import Image, ImageTk
import threading


def run_cli():
    print(Fore.GREEN + '-----------------------------------------' )
    print(Fore.GREEN + '| |谢赵宇工具箱|                           |' )
    print(Fore.GREEN + '| |qq:136805009@qq.com|                    |' )
    print(Fore.GREEN + '| |开源免费的工具箱|                       |' )
    print(Fore.GREEN + '-----------------------------------------' )
    while True:
        raw_input = input(Fore.YELLOW + '请输入指令(不知道有哪些命令请输入5):')
        if raw_input == '5':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 密码生成器|                      *|' )
            print(Fore.GREEN + '| |2. 密码强度检查器|                   |' )
            print(Fore.GREEN + '| |3.关于|                              |' )
            print(Fore.GREEN + '| |4. 随机数生成器|                     |' )
            print(Fore.GREEN + '| |6. Base64 编码/解码|                 |' )
            print(Fore.GREEN + '| |7. 二维码生成器|                     |' )
            print(Fore.GREEN + '| |8. 单位换算器|                       |' )
            print(Fore.GREEN + '| |9. 倒计时器|                         |' )
            print(Fore.GREEN + '| |10. 密码字典生成器|                 *|' )
            print(Fore.GREEN + '| |11. 文本处理工具|                    |' )
            print(Fore.GREEN + '| |12. 日期时间工具|                    |' )
            print(Fore.GREEN + '| |13. 数字处理工具|                    |' )
            print(Fore.GREEN + '| |14. 简单的AI|                        |' )
            print(Fore.GREEN + '-----------------------------------------' )
        if raw_input == '1':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |密码生成器|                           |' )
            print(Fore.GREEN + '-----------------------------------------' )
            length = int(input(Fore.YELLOW + "请输入密码长度: "))
            charset = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(charset) for _ in range(length))
            print(Fore.CYAN + "生成的密码: " + password)
        if raw_input == '2':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |密码强度检查器|                       |' )
            print(Fore.GREEN + '-----------------------------------------' )
            password = input(Fore.YELLOW + "请输入密码: ")
            strength = 0
            if any(char.islower() for char in password):
                strength += 1
            if any(char.isupper() for char in password):
                strength += 1
            if any(char.isdigit() for char in password):
                strength += 1
            if any(char in string.punctuation for char in password):
                strength += 1
            if len(password) >= 8:
                strength += 1
            if strength == 6:
                print(Fore.GREEN + "密码强度: 强")
            elif strength >= 4:
                print(Fore.YELLOW + "密码强度: 中")
            else:
                print(Fore.RED + "密码强度: 菜鸡")
        if raw_input == '3':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |关于|                                 |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |谢赵宇工具箱|                         |' )
            print(Fore.GREEN + '| |版本:0.2.0|                           |' )
            print(Fore.GREEN + '| |开源免费的工具箱|                     |' )
            print(Fore.GREEN + '-----------------------------------------' )
        if raw_input == '4':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |随机数生成器|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            min_val = int(input(Fore.YELLOW + "请输入最小值: "))
            max_val = int(input(Fore.YELLOW + "请输入最大值: "))
            random_num = random.randint(min_val, max_val)
            print(Fore.CYAN + "生成的随机数: " + str(random_num))
        if raw_input == '6':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |Base64 编码/解码|                     |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1. 编码 2. 解码): ")
            if choice == '1':
                text = input(Fore.YELLOW + "请输入要编码的文本: ")
                encoded = base64.b64encode(text.encode()).decode()
                print(Fore.CYAN + "编码后的文本: " + encoded)
            elif choice == '2':
                encoded = input(Fore.YELLOW + "请输入要解码的文本: ")
                decoded = base64.b64decode(encoded.encode()).decode()
                print(Fore.CYAN + "解码后的文本: " + decoded)
            else:
                print(Fore.RED + "无效选择")
        if raw_input == '7':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |二维码生成器|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            text = input(Fore.YELLOW + "请输入要生成二维码的文本: ")
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")
            print(Fore.CYAN + "二维码已保存为 qrcode.png")
        if raw_input == '8':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |单位换算器|                           |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 长度单位换算|                     |' )
            print(Fore.GREEN + '| |2. 重量单位换算|                     |' )
            print(Fore.GREEN + '| |3. 温度单位换算|                     |' )
            print(Fore.GREEN + '| |4. 时间单位换算|                     |' )
            print(Fore.GREEN + '| |5. 速度单位换算|                     |' )
            print(Fore.GREEN + '| |6. 面积单位换算|                     |' )
            print(Fore.GREEN + '| |7. 容量单位换算|                     |' )
            print(Fore.GREEN + '| |8. 敬请期待|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-8): ")
            if choice == '1':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |长度单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 米-千米 (m)|                      |' )
                print(Fore.GREEN + '| |2. 千米-米 (km)|                     |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |米转千米|                             |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    meter = float(input(Fore.YELLOW + "请输入米数: "))
                    kilometer = meter / 1000
                    print(Fore.CYAN + "转换后的千米数: " + str(kilometer))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |千米转米|                             |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    kilometer = float(input(Fore.YELLOW + "请输入千米数: "))
                    meter = kilometer * 1000
                    print(Fore.CYAN + "转换后的米数: " + str(meter))
            elif choice == '2':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |重量单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 克-千克 (g)|                     |' )
                print(Fore.GREEN + '| |2. 千克-克 (kg)|                    |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |克转千克|                             |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    gram = float(input(Fore.YELLOW + "请输入克数: "))
                    kilogram = gram / 1000
                    print(Fore.CYAN + "转换后的千克数: " + str(kilogram))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |千克转克|                             |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    kilogram = float(input(Fore.YELLOW + "请输入千克数: "))
                    gram = kilogram * 1000
                    print(Fore.CYAN + "转换后的克数: " + str(gram))
            elif choice == '3':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |温度单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 摄氏度-华氏度 (°C)|              |' )
                print(Fore.GREEN + '| |2. 华氏度-摄氏度 (°F)|              |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |摄氏度转华氏度|                     |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    celsius = float(input(Fore.YELLOW + "请输入摄氏度: "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(Fore.CYAN + "转换后的华氏度: " + str(fahrenheit))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |华氏度转摄氏度|                     |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    fahrenheit = float(input(Fore.YELLOW + "请输入华氏度: "))
                    celsius = (fahrenheit - 32) * 5/9
                    print(Fore.CYAN + "转换后的摄氏度: " + str(celsius))
            elif choice == '6':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |面积单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 平方米-平方公里 (m²)|           |' )
                print(Fore.GREEN + '| |2. 平方公里-平方米 (km²)|          |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |平方米转平方公里|                 |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    square_meter = float(input(Fore.YELLOW + "请输入平方米数: "))
                    square_kilometer = square_meter / 1000000
                    print(Fore.CYAN + "转换后的平方公里数: " + str(square_kilometer))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |平方公里转平方米|                 |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    square_kilometer = float(input(Fore.YELLOW + "请输入平方公里数: "))
                    square_meter = square_kilometer * 1000000
                    print(Fore.CYAN + "转换后的平方米数: " + str(square_meter))
            elif choice == '4':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |时间单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 秒-分钟 (s)|                     |' )
                print(Fore.GREEN + '| |2. 分钟-秒 (min)|                   |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |秒转分钟|                         |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    second = float(input(Fore.YELLOW + "请输入秒数: "))
                    minute = second / 60
                    print(Fore.CYAN + "转换后的分钟数: " + str(minute))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |分钟转秒|                         |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    minute = float(input(Fore.YELLOW + "请输入分钟数: "))
                    second = minute * 60
                    print(Fore.CYAN + "转换后的秒数: " + str(second))
            elif choice == '5':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |速度单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 米/秒-千米/小时 (m/s)|           |' )
                print(Fore.GREEN + '| |2. 千米/小时-米/秒 (km/h)|          |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |米/秒转千米/小时|                 |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    meter_per_second = float(input(Fore.YELLOW + "请输入米/秒数: "))
                    kilometer_per_hour = meter_per_second * 3600
                    print(Fore.CYAN + "转换后的千米/小时数: " + str(kilometer_per_hour))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |千米/小时转米/秒|                 |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    kilometer_per_hour = float(input(Fore.YELLOW + "请输入千米/小时数: "))
                    meter_per_second = kilometer_per_hour / 3600
                    print(Fore.CYAN + "转换后的米/秒数: " + str(meter_per_second))
            elif choice == '7':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |容量单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. kb-MB (KB)|          |' )
                print(Fore.GREEN + '| |2. MB-kb (MB)|          |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |kb-MB|                         |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    kb = float(input(Fore.YELLOW + "请输入KB数: "))
                    mb = kb / 1024
                    print(Fore.CYAN + "转换后的MB数: " + str(mb))
                elif choice == '2':
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |MB-kb|                         |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    mb = float(input(Fore.YELLOW + "请输入MB数: "))
                    kb = mb * 1024
                    print(Fore.CYAN + "转换后的KB数: " + str(kb))
        if raw_input == '9':  
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |倒计时|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            second = int(input(Fore.YELLOW + "请输入倒计时秒数: "))
            while second > 0:
                print(Fore.CYAN + "倒计时: " + str(second))
                second -= 1
                time.sleep(1)
            print(Fore.CYAN + "倒计时结束!")
        elif raw_input == '10':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |密码字典生成器|                       |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 生成简单密码字典|                 |' )
            print(Fore.GREEN + '| |2. 生成复杂密码字典|                 |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
            if choice == '1':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |生成简单密码字典|                   |' )
                print(Fore.GREEN + '-----------------------------------------' )
                password = input(Fore.YELLOW + "请输入密码长度: ")
                password_length = int(password)
                characters = "0123456789"
                num_passwords = int(input(Fore.YELLOW + "请输入要生成的密码数量: "))
                random_passwords = [''.join(random.choice(characters) for i in range(password_length)) for _ in range(num_passwords)]
                open('simple_passwords.txt', 'w').write('\n'.join(random_passwords))
                print(Fore.CYAN + "简单密码字典已生成并保存到 simple_passwords.txt 文件中")
            elif choice == '2':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |生成复杂密码字典|                   |' )
                print(Fore.GREEN + '-----------------------------------------' )
                password = input(Fore.YELLOW + "请输入密码长度: ")
                password_length = int(password)
                characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
                num_passwords = int(input(Fore.YELLOW + "请输入要生成的密码数量: "))
                random_passwords = [''.join(random.choice(characters) for i in range(password_length)) for _ in range(num_passwords)]
                open('simple_passwords.txt', 'w').write('\n'.join(random_passwords))
                print(Fore.CYAN + "复杂密码字典已生成并保存到 complex_passwords.txt 文件中")
        elif raw_input == 'xzyyyds':
            print(Fore.CYAN + '-----------------------------------------' )
            print(Fore.CYAN + '|        感谢大家下载并使用我这款脚本   |' )
            print(Fore.CYAN + '|        我也会一直更新,一直免费        |' )
            print(Fore.CYAN + '-----------------------------------------' )
        elif raw_input == '11':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |文本处理工具|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 文本大小写转换|                   |' )
            print(Fore.GREEN + '| |2. 文本字符统计|                     |' )
            print(Fore.GREEN + '| |3. 文本反转|                         |' )
            print(Fore.GREEN + '| |4. 文本去空格|                       |' )
            print(Fore.GREEN + '| |5. 文本替换|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-5): ")
            if choice == '1':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |文本大小写转换|                      |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 转为大写|                         |' )
                print(Fore.GREEN + '| |2. 转为小写|                         |' )
                print(Fore.GREEN + '| |3. 首字母大写|                       |' )
                print(Fore.GREEN + '-----------------------------------------' )
                sub_choice = input(Fore.YELLOW + "请选择操作 (1-3): ")
                text = input(Fore.YELLOW + "请输入文本: ")
                if sub_choice == '1':
                    result = text.upper()
                    print(Fore.CYAN + "转换后的文本: " + result)
                elif sub_choice == '2':
                    result = text.lower()
                    print(Fore.CYAN + "转换后的文本: " + result)
                elif sub_choice == '3':
                    result = text.title()
                    print(Fore.CYAN + "转换后的文本: " + result)
            elif choice == '2':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |文本字符统计|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                text = input(Fore.YELLOW + "请输入文本: ")
                total_chars = len(text)
                alpha_chars = sum(c.isalpha() for c in text)
                digit_chars = sum(c.isdigit() for c in text)
                space_chars = sum(c.isspace() for c in text)
                print(Fore.CYAN + "总字符数: " + str(total_chars))
                print(Fore.CYAN + "字母数: " + str(alpha_chars))
                print(Fore.CYAN + "数字数: " + str(digit_chars))
                print(Fore.CYAN + "空格数: " + str(space_chars))
            elif choice == '3':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |文本反转|                            |' )
                print(Fore.GREEN + '-----------------------------------------' )
                text = input(Fore.YELLOW + "请输入文本: ")
                result = text[::-1]
                print(Fore.CYAN + "反转后的文本: " + result)
            elif choice == '4':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |文本去空格|                          |' )
                print(Fore.GREEN + '-----------------------------------------' )
                text = input(Fore.YELLOW + "请输入文本: ")
                result = text.replace(" ", "")
                print(Fore.CYAN + "去空格后的文本: " + result)
            elif choice == '5':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |文本替换|                            |' )
                print(Fore.GREEN + '-----------------------------------------' )
                text = input(Fore.YELLOW + "请输入文本: ")
                old_str = input(Fore.YELLOW + "请输入要替换的字符串: ")
                new_str = input(Fore.YELLOW + "请输入替换后的字符串: ")
                result = text.replace(old_str, new_str)
                print(Fore.CYAN + "替换后的文本: " + result)
        elif raw_input == '12':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |日期时间工具|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 获取当前时间|                     |' )
            print(Fore.GREEN + '| |2. 时间戳转换|                       |' )
            print(Fore.GREEN + '| |3. 日期计算|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-3): ")
            if choice == '1':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |获取当前时间|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(Fore.CYAN + "当前时间: " + current_time)
            elif choice == '2':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |时间戳转换|                          |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 时间戳转日期时间|                 |' )
                print(Fore.GREEN + '| |2. 日期时间转时间戳|                 |' )
                print(Fore.GREEN + '-----------------------------------------' )
                sub_choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if sub_choice == '1':
                    timestamp = float(input(Fore.YELLOW + "请输入时间戳: "))
                    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                    print(Fore.CYAN + "转换后的日期时间: " + date_time)
                elif sub_choice == '2':
                    date_str = input(Fore.YELLOW + "请输入日期时间 (格式: YYYY-MM-DD HH:MM:SS): ")
                    try:
                        timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))
                        print(Fore.CYAN + "转换后的时间戳: " + str(timestamp))
                    except ValueError:
                        print(Fore.RED + "日期时间格式错误，请按照 YYYY-MM-DD HH:MM:SS 格式输入")
            elif choice == '3':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |日期计算|                            |' )
                print(Fore.GREEN + '-----------------------------------------' )
                days = int(input(Fore.YELLOW + "请输入天数: "))
                future_time = time.time() + (days * 24 * 3600)
                future_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(future_time))
                print(Fore.CYAN + str(days) + "天后的日期时间: " + future_date)
        elif raw_input == '13':
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |数字处理工具|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 数字格式化|                       |' )
            print(Fore.GREEN + '| |2. 数字转换|                         |' )
            print(Fore.GREEN + '| |3. 数字计算|                         |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-3): ")
            if choice == '1':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |数字格式化|                          |' )
                print(Fore.GREEN + '-----------------------------------------' )
                number = float(input(Fore.YELLOW + "请输入数字: "))
                decimal_places = int(input(Fore.YELLOW + "请输入小数位数: "))
                formatted = round(number, decimal_places)
                print(Fore.CYAN + "格式化后的数字: " + str(formatted))
            elif choice == '2':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |数字转换|                            |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 十进制转二进制|                   |' )
                print(Fore.GREEN + '| |2. 十进制转八进制|                   |' )
                print(Fore.GREEN + '| |3. 十进制转十六进制|                 |' )
                print(Fore.GREEN + '-----------------------------------------' )
                sub_choice = input(Fore.YELLOW + "请选择操作 (1-3): ")
                number = int(input(Fore.YELLOW + "请输入十进制数字: "))
                if sub_choice == '1':
                    result = bin(number)
                    print(Fore.CYAN + "二进制: " + result)
                elif sub_choice == '2':
                    result = oct(number)
                    print(Fore.CYAN + "八进制: " + result)
                elif sub_choice == '3':
                    result = hex(number)
                    print(Fore.CYAN + "十六进制: " + result)
            elif choice == '3':
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |数字计算|                            |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 加法|                             |' )
                print(Fore.GREEN + '| |2. 减法|                             |' )
                print(Fore.GREEN + '| |3. 乘法|                             |' )
                print(Fore.GREEN + '| |4. 除法|                             |' )
                print(Fore.GREEN + '-----------------------------------------' )
                sub_choice = input(Fore.YELLOW + "请选择操作 (1-4): ")
                num1 = float(input(Fore.YELLOW + "请输入第一个数字: "))
                num2 = float(input(Fore.YELLOW + "请输入第二个数字: "))
                if sub_choice == '1':
                    result = num1 + num2
                    print(Fore.CYAN + "结果: " + str(result))
                elif sub_choice == '2':
                    result = num1 - num2
                    print(Fore.CYAN + "结果: " + str(result))
                elif sub_choice == '3':
                    result = num1 * num2
                    print(Fore.CYAN + "结果: " + str(result))
                elif sub_choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(Fore.CYAN + "结果: " + str(result))
                    else:
                        print(Fore.RED + "错误: 除数不能为0")
        elif raw_input == "caidan" :
            name = 'xzy'
            print(Figlet().renderText(name))
        elif raw_input =="14" :
            input(Fore.RED + "警告:此功能不适用于手机命令行请勿在手机端使用,如要继续请回车")
            from zai import ZhipuAiClient
            client = ZhipuAiClient(api_key="d286aa49ab044f3381955d95b8346502.6Qb2OTsWIoIaQbvH")
            response = client.chat.completions.create(
            model="glm-4.7",
            messages=[
                {"role": "user", "content": "帮助用户解决问题"},
                {"role": "assistant", "content": "帮助用户解决问题"},
                {"role": "user", "content": input(Fore.YELLOW + "请输入问题: ")}
                ],
            thinking={
                "type": "enabled",
            },
            stream=True,
            max_tokens=65536,
            temperature=1.0
            )
            for chunk in response:
                if chunk.choices[0].delta.reasoning_content:
                    print(chunk.choices[0].delta.reasoning_content, end='', flush=True)
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end='', flush=True)


class ToolBoxGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("谢赵宇工具箱")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.create_about_tab()
        self.create_password_generator_tab()
        self.create_password_checker_tab()
        self.create_random_number_tab()
        self.create_base64_tab()
        self.create_qrcode_tab()
        self.create_unit_converter_tab()
        self.create_countdown_tab()
        self.create_password_dict_tab()
        self.create_text_tools_tab()
        self.create_datetime_tab()
        self.create_number_tools_tab()
        self.create_ai_tab()
    
    def create_about_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='关于')
        
        ttk.Label(frame, text='谢赵宇工具箱', font=('Arial', 24, 'bold')).pack(pady=20)
        ttk.Label(frame, text='版本: 0.2.0', font=('Arial', 14)).pack(pady=10)
        ttk.Label(frame, text='开源免费的工具箱', font=('Arial', 14)).pack(pady=10)
        ttk.Label(frame, text='qq: 736805009@qq.com', font=('Arial', 14)).pack(pady=10)
    
    def create_password_generator_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='密码生成器')
        
        ttk.Label(frame, text='密码生成器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text='密码长度:').grid(row=0, column=0, padx=5, pady=5)
        self.password_length = ttk.Entry(input_frame, width=20)
        self.password_length.grid(row=0, column=1, padx=5, pady=5)
        self.password_length.insert(0, '12')
        
        ttk.Button(input_frame, text='生成密码', command=self.generate_password).grid(row=1, column=0, columnspan=2, pady=10)
        
        ttk.Label(frame, text='生成的密码:', font=('Arial', 12)).pack(pady=10)
        self.generated_password = ttk.Entry(frame, width=50, font=('Arial', 14))
        self.generated_password.pack(pady=5)
    
    def generate_password(self):
        try:
            length = int(self.password_length.get())
            if length <= 0:
                messagebox.showerror('错误', '密码长度必须大于0')
                return
            charset = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(charset) for _ in range(length))
            self.generated_password.delete(0, tk.END)
            self.generated_password.insert(0, password)
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
    
    def create_password_checker_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='密码强度检查')
        
        ttk.Label(frame, text='密码强度检查器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        ttk.Label(frame, text='请输入密码:').pack(pady=10)
        self.password_input = ttk.Entry(frame, width=40, show='*', font=('Arial', 14))
        self.password_input.pack(pady=5)
        
        ttk.Button(frame, text='检查强度', command=self.check_password_strength).pack(pady=10)
        
        self.strength_result = ttk.Label(frame, text='', font=('Arial', 16, 'bold'))
        self.strength_result.pack(pady=20)
        
        self.strength_details = ttk.Label(frame, text='', font=('Arial', 10))
        self.strength_details.pack(pady=10)
    
    def check_password_strength(self):
        password = self.password_input.get()
        strength = 0
        details = []
        
        if any(char.islower() for char in password):
            strength += 1
            details.append('✓ 包含小写字母')
        else:
            details.append('✗ 缺少小写字母')
        
        if any(char.isupper() for char in password):
            strength += 1
            details.append('✓ 包含大写字母')
        else:
            details.append('✗ 缺少大写字母')
        
        if any(char.isdigit() for char in password):
            strength += 1
            details.append('✓ 包含数字')
        else:
            details.append('✗ 缺少数字')
        
        if any(char in string.punctuation for char in password):
            strength += 1
            details.append('✓ 包含特殊字符')
        else:
            details.append('✗ 缺少特殊字符')
        
        if len(password) >= 8:
            strength += 1
            details.append('✓ 长度>=8')
        else:
            details.append('✗ 长度<8')
        
        if strength == 5:
            self.strength_result.config(text='密码强度: 强', foreground='green')
        elif strength >= 3:
            self.strength_result.config(text='密码强度: 中', foreground='orange')
        else:
            self.strength_result.config(text='密码强度: 弱', foreground='red')
        
        self.strength_details.config(text='\n'.join(details))
    
    def create_random_number_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='随机数生成')
        
        ttk.Label(frame, text='随机数生成器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text='最小值:').grid(row=0, column=0, padx=5, pady=5)
        self.min_val = ttk.Entry(input_frame, width=15)
        self.min_val.grid(row=0, column=1, padx=5, pady=5)
        self.min_val.insert(0, '1')
        
        ttk.Label(input_frame, text='最大值:').grid(row=1, column=0, padx=5, pady=5)
        self.max_val = ttk.Entry(input_frame, width=15)
        self.max_val.grid(row=1, column=1, padx=5, pady=5)
        self.max_val.insert(0, '100')
        
        ttk.Button(input_frame, text='生成随机数', command=self.generate_random_number).grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Label(frame, text='生成的随机数:', font=('Arial', 12)).pack(pady=10)
        self.random_result = ttk.Label(frame, text='', font=('Arial', 20, 'bold'))
        self.random_result.pack(pady=5)
    
    def generate_random_number(self):
        try:
            min_v = int(self.min_val.get())
            max_v = int(self.max_val.get())
            if min_v >= max_v:
                messagebox.showerror('错误', '最小值必须小于最大值')
                return
            random_num = random.randint(min_v, max_v)
            self.random_result.config(text=str(random_num))
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
    
    def create_base64_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Base64')
        
        ttk.Label(frame, text='Base64 编码/解码', font=('Arial', 18, 'bold')).pack(pady=20)
        
        ttk.Label(frame, text='输入文本:').pack(pady=5)
        self.base64_input = scrolledtext.ScrolledText(frame, width=60, height=8)
        self.base64_input.pack(pady=5)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text='编码', command=self.base64_encode).pack(side='left', padx=5)
        ttk.Button(button_frame, text='解码', command=self.base64_decode).pack(side='left', padx=5)
        
        ttk.Label(frame, text='输出结果:', font=('Arial', 12)).pack(pady=10)
        self.base64_output = scrolledtext.ScrolledText(frame, width=60, height=8)
        self.base64_output.pack(pady=5)
    
    def base64_encode(self):
        text = self.base64_input.get('1.0', tk.END).strip()
        try:
            encoded = base64.b64encode(text.encode()).decode()
            self.base64_output.delete('1.0', tk.END)
            self.base64_output.insert('1.0', encoded)
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def base64_decode(self):
        text = self.base64_input.get('1.0', tk.END).strip()
        try:
            decoded = base64.b64decode(text.encode()).decode()
            self.base64_output.delete('1.0', tk.END)
            self.base64_output.insert('1.0', decoded)
        except Exception as e:
            messagebox.showerror('错误', '解码失败，请检查输入格式')
    
    def create_qrcode_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='二维码')
        
        ttk.Label(frame, text='二维码生成器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        ttk.Label(frame, text='输入文本或URL:').pack(pady=5)
        self.qrcode_input = ttk.Entry(frame, width=50)
        self.qrcode_input.pack(pady=5)
        
        ttk.Button(frame, text='生成二维码', command=self.generate_qrcode).pack(pady=10)
        
        self.qrcode_label = ttk.Label(frame)
        self.qrcode_label.pack(pady=10)
        
        ttk.Button(frame, text='保存二维码', command=self.save_qrcode).pack(pady=5)
    
    def generate_qrcode(self):
        text = self.qrcode_input.get()
        if not text:
            messagebox.showerror('错误', '请输入文本')
            return
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            img.save("temp_qrcode.png")
            
            photo = ImageTk.PhotoImage(Image.open("temp_qrcode.png"))
            self.qrcode_label.config(image=photo)
            self.qrcode_label.image = photo
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def save_qrcode(self):
        text = self.qrcode_input.get()
        if not text:
            messagebox.showerror('错误', '请先生成二维码')
            return
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            if filename:
                img.save(filename)
                messagebox.showinfo('成功', f'二维码已保存为 {filename}')
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def create_unit_converter_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='单位换算')
        
        ttk.Label(frame, text='单位换算器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        type_frame = ttk.Frame(frame)
        type_frame.pack(pady=10)
        
        ttk.Label(type_frame, text='选择单位类型:').grid(row=0, column=0, padx=5, pady=5)
        self.unit_type = ttk.Combobox(type_frame, values=['长度', '重量', '温度', '时间', '速度', '面积', '容量'], state='readonly', width=15)
        self.unit_type.grid(row=0, column=1, padx=5, pady=5)
        self.unit_type.bind('<<ComboboxSelected>>', self.on_unit_type_change)
        self.unit_type.current(0)
        
        ttk.Label(type_frame, text='转换方向:').grid(row=1, column=0, padx=5, pady=5)
        self.convert_direction = ttk.Combobox(type_frame, state='readonly', width=15)
        self.convert_direction.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(type_frame, text='输入值:').grid(row=2, column=0, padx=5, pady=5)
        self.unit_input = ttk.Entry(type_frame, width=15)
        self.unit_input.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(type_frame, text='转换', command=self.convert_unit).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.unit_result = ttk.Label(frame, text='', font=('Arial', 16, 'bold'))
        self.unit_result.pack(pady=20)
        
        self.on_unit_type_change(None)
    
    def on_unit_type_change(self, event):
        unit_type = self.unit_type.get()
        directions = {
            '长度': ['米→千米', '千米→米'],
            '重量': ['克→千克', '千克→克'],
            '温度': ['摄氏度→华氏度', '华氏度→摄氏度'],
            '时间': ['秒→分钟', '分钟→秒'],
            '速度': ['米/秒→千米/小时', '千米/小时→米/秒'],
            '面积': ['平方米→平方公里', '平方公里→平方米'],
            '容量': ['KB→MB', 'MB→KB']
        }
        self.convert_direction['values'] = directions.get(unit_type, [])
        if self.convert_direction['values']:
            self.convert_direction.current(0)
    
    def convert_unit(self):
        try:
            value = float(self.unit_input.get())
            unit_type = self.unit_type.get()
            direction = self.convert_direction.get()
            
            if unit_type == '长度':
                if direction == '米→千米':
                    result = value / 1000
                    self.unit_result.config(text=f'{value} 米 = {result} 千米')
                else:
                    result = value * 1000
                    self.unit_result.config(text=f'{value} 千米 = {result} 米')
            elif unit_type == '重量':
                if direction == '克→千克':
                    result = value / 1000
                    self.unit_result.config(text=f'{value} 克 = {result} 千克')
                else:
                    result = value * 1000
                    self.unit_result.config(text=f'{value} 千克 = {result} 克')
            elif unit_type == '温度':
                if direction == '摄氏度→华氏度':
                    result = (value * 9/5) + 32
                    self.unit_result.config(text=f'{value}°C = {result}°F')
                else:
                    result = (value - 32) * 5/9
                    self.unit_result.config(text=f'{value}°F = {result}°C')
            elif unit_type == '时间':
                if direction == '秒→分钟':
                    result = value / 60
                    self.unit_result.config(text=f'{value} 秒 = {result} 分钟')
                else:
                    result = value * 60
                    self.unit_result.config(text=f'{value} 分钟 = {result} 秒')
            elif unit_type == '速度':
                if direction == '米/秒→千米/小时':
                    result = value * 3.6
                    self.unit_result.config(text=f'{value} 米/秒 = {result} 千米/小时')
                else:
                    result = value / 3.6
                    self.unit_result.config(text=f'{value} 千米/小时 = {result} 米/秒')
            elif unit_type == '面积':
                if direction == '平方米→平方公里':
                    result = value / 1000000
                    self.unit_result.config(text=f'{value} 平方米 = {result} 平方公里')
                else:
                    result = value * 1000000
                    self.unit_result.config(text=f'{value} 平方公里 = {result} 平方米')
            elif unit_type == '容量':
                if direction == 'KB→MB':
                    result = value / 1024
                    self.unit_result.config(text=f'{value} KB = {result} MB')
                else:
                    result = value * 1024
                    self.unit_result.config(text=f'{value} MB = {result} KB')
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
    
    def create_countdown_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='倒计时')
        
        ttk.Label(frame, text='倒计时器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text='秒数:').grid(row=0, column=0, padx=5, pady=5)
        self.countdown_input = ttk.Entry(input_frame, width=15)
        self.countdown_input.grid(row=0, column=1, padx=5, pady=5)
        self.countdown_input.insert(0, '60')
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text='开始', command=self.start_countdown).pack(side='left', padx=5)
        ttk.Button(button_frame, text='停止', command=self.stop_countdown).pack(side='left', padx=5)
        
        self.countdown_display = ttk.Label(frame, text='00:00:00', font=('Arial', 36, 'bold'))
        self.countdown_display.pack(pady=20)
        
        self.countdown_running = False
        self.countdown_thread = None
    
    def start_countdown(self):
        if self.countdown_running:
            return
        
        try:
            seconds = int(self.countdown_input.get())
            if seconds <= 0:
                messagebox.showerror('错误', '请输入大于0的秒数')
                return
            
            self.countdown_running = True
            self.countdown_thread = threading.Thread(target=self._countdown_worker, args=(seconds,))
            self.countdown_thread.daemon = True
            self.countdown_thread.start()
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
    
    def stop_countdown(self):
        self.countdown_running = False
        self.countdown_display.config(text='00:00:00')
    
    def _countdown_worker(self, total_seconds):
        remaining = total_seconds
        while remaining > 0 and self.countdown_running:
            hours = remaining // 3600
            minutes = (remaining % 3600) // 60
            seconds = remaining % 60
            time_str = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
            self.root.after(0, lambda: self.countdown_display.config(text=time_str))
            time.sleep(1)
            remaining -= 1
        
        if remaining == 0:
            self.root.after(0, lambda: self.countdown_display.config(text='倒计时结束!'))
            self.countdown_running = False
    
    def create_password_dict_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='密码字典')
        
        ttk.Label(frame, text='密码字典生成器', font=('Arial', 18, 'bold')).pack(pady=20)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text='密码长度:').grid(row=0, column=0, padx=5, pady=5)
        self.dict_length = ttk.Entry(input_frame, width=15)
        self.dict_length.grid(row=0, column=1, padx=5, pady=5)
        self.dict_length.insert(0, '8')
        
        ttk.Label(input_frame, text='密码数量:').grid(row=1, column=0, padx=5, pady=5)
        self.dict_count = ttk.Entry(input_frame, width=15)
        self.dict_count.grid(row=1, column=1, padx=5, pady=5)
        self.dict_count.insert(0, '100')
        
        ttk.Label(input_frame, text='类型:').grid(row=2, column=0, padx=5, pady=5)
        self.dict_type = ttk.Combobox(input_frame, values=['简单(仅数字)', '复杂(字母数字符号)'], state='readonly', width=15)
        self.dict_type.grid(row=2, column=1, padx=5, pady=5)
        self.dict_type.current(0)
        
        ttk.Button(input_frame, text='生成字典', command=self.generate_password_dict).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.dict_result = ttk.Label(frame, text='', font=('Arial', 12))
        self.dict_result.pack(pady=10)
    
    def generate_password_dict(self):
        try:
            length = int(self.dict_length.get())
            count = int(self.dict_count.get())
            dict_type = self.dict_type.get()
            
            if length <= 0 or count <= 0:
                messagebox.showerror('错误', '长度和数量必须大于0')
                return
            
            if dict_type == '简单(仅数字)':
                characters = "0123456789"
                filename = 'simple_passwords.txt'
            else:
                characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
                filename = 'complex_passwords.txt'
            
            random_passwords = [''.join(random.choice(characters) for i in range(length)) for _ in range(count)]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(random_passwords))
            
            self.dict_result.config(text=f'已生成 {count} 个密码，保存到 {filename}')
            messagebox.showinfo('成功', f'密码字典已生成并保存到 {filename}')
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def create_text_tools_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='文本工具')
        
        ttk.Label(frame, text='文本处理工具', font=('Arial', 18, 'bold')).pack(pady=20)
        
        type_frame = ttk.Frame(frame)
        type_frame.pack(pady=10)
        
        ttk.Label(type_frame, text='选择功能:').grid(row=0, column=0, padx=5, pady=5)
        self.text_tool_type = ttk.Combobox(type_frame, values=['大小写转换', '字符统计', '文本反转', '去空格', '文本替换'], state='readonly', width=15)
        self.text_tool_type.grid(row=0, column=1, padx=5, pady=5)
        self.text_tool_type.bind('<<ComboboxSelected>>', self.on_text_tool_change)
        self.text_tool_type.current(0)
        
        ttk.Label(frame, text='输入文本:').pack(pady=5)
        self.text_input = scrolledtext.ScrolledText(frame, width=60, height=8)
        self.text_input.pack(pady=5)
        
        self.text_options_frame = ttk.Frame(frame)
        self.text_options_frame.pack(pady=5)
        
        ttk.Button(frame, text='执行', command=self.execute_text_tool).pack(pady=10)
        
        ttk.Label(frame, text='输出结果:', font=('Arial', 12)).pack(pady=10)
        self.text_output = scrolledtext.ScrolledText(frame, width=60, height=8)
        self.text_output.pack(pady=5)
        
        self.on_text_tool_change(None)
    
    def on_text_tool_change(self, event):
        tool_type = self.text_tool_type.get()
        
        for widget in self.text_options_frame.winfo_children():
            widget.destroy()
        
        if tool_type == '大小写转换':
            ttk.Label(self.text_options_frame, text='转换方式:').grid(row=0, column=0, padx=5, pady=5)
            self.case_convert_type = ttk.Combobox(self.text_options_frame, values=['转为大写', '转为小写', '首字母大写'], state='readonly', width=15)
            self.case_convert_type.grid(row=0, column=1, padx=5, pady=5)
            self.case_convert_type.current(0)
        elif tool_type == '文本替换':
            ttk.Label(self.text_options_frame, text='查找:').grid(row=0, column=0, padx=5, pady=5)
            self.replace_old = ttk.Entry(self.text_options_frame, width=15)
            self.replace_old.grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(self.text_options_frame, text='替换为:').grid(row=1, column=0, padx=5, pady=5)
            self.replace_new = ttk.Entry(self.text_options_frame, width=15)
            self.replace_new.grid(row=1, column=1, padx=5, pady=5)
    
    def execute_text_tool(self):
        tool_type = self.text_tool_type.get()
        text = self.text_input.get('1.0', tk.END).strip()
        
        try:
            if tool_type == '大小写转换':
                convert_type = self.case_convert_type.get()
                if convert_type == '转为大写':
                    result = text.upper()
                elif convert_type == '转为小写':
                    result = text.lower()
                else:
                    result = text.title()
            elif tool_type == '字符统计':
                total_chars = len(text)
                alpha_chars = sum(c.isalpha() for c in text)
                digit_chars = sum(c.isdigit() for c in text)
                space_chars = sum(c.isspace() for c in text)
                result = f'总字符数: {total_chars}\n字母数: {alpha_chars}\n数字数: {digit_chars}\n空格数: {space_chars}'
            elif tool_type == '文本反转':
                result = text[::-1]
            elif tool_type == '去空格':
                result = text.replace(' ', '')
            elif tool_type == '文本替换':
                old_str = self.replace_old.get()
                new_str = self.replace_new.get()
                result = text.replace(old_str, new_str)
            
            self.text_output.delete('1.0', tk.END)
            self.text_output.insert('1.0', result)
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def create_datetime_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='日期时间')
        
        ttk.Label(frame, text='日期时间工具', font=('Arial', 18, 'bold')).pack(pady=20)
        
        type_frame = ttk.Frame(frame)
        type_frame.pack(pady=10)
        
        ttk.Label(type_frame, text='选择功能:').grid(row=0, column=0, padx=5, pady=5)
        self.datetime_tool_type = ttk.Combobox(type_frame, values=['获取当前时间', '时间戳转换', '日期计算'], state='readonly', width=15)
        self.datetime_tool_type.grid(row=0, column=1, padx=5, pady=5)
        self.datetime_tool_type.bind('<<ComboboxSelected>>', self.on_datetime_tool_change)
        self.datetime_tool_type.current(0)
        
        self.datetime_options_frame = ttk.Frame(frame)
        self.datetime_options_frame.pack(pady=5)
        
        ttk.Button(frame, text='执行', command=self.execute_datetime_tool).pack(pady=10)
        
        self.datetime_result = ttk.Label(frame, text='', font=('Arial', 12))
        self.datetime_result.pack(pady=10)
        
        self.on_datetime_tool_change(None)
    
    def on_datetime_tool_change(self, event):
        tool_type = self.datetime_tool_type.get()
        
        for widget in self.datetime_options_frame.winfo_children():
            widget.destroy()
        
        if tool_type == '时间戳转换':
            ttk.Label(self.datetime_options_frame, text='转换方向:').grid(row=0, column=0, padx=5, pady=5)
            self.timestamp_convert_type = ttk.Combobox(self.datetime_options_frame, values=['时间戳→日期时间', '日期时间→时间戳'], state='readonly', width=15)
            self.timestamp_convert_type.grid(row=0, column=1, padx=5, pady=5)
            self.timestamp_convert_type.current(0)
            
            ttk.Label(self.datetime_options_frame, text='输入:').grid(row=1, column=0, padx=5, pady=5)
            self.timestamp_input = ttk.Entry(self.datetime_options_frame, width=20)
            self.timestamp_input.grid(row=1, column=1, padx=5, pady=5)
        elif tool_type == '日期计算':
            ttk.Label(self.datetime_options_frame, text='天数:').grid(row=0, column=0, padx=5, pady=5)
            self.date_calc_days = ttk.Entry(self.datetime_options_frame, width=15)
            self.date_calc_days.grid(row=0, column=1, padx=5, pady=5)
            self.date_calc_days.insert(0, '7')
    
    def execute_datetime_tool(self):
        tool_type = self.datetime_tool_type.get()
        
        try:
            if tool_type == '获取当前时间':
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.datetime_result.config(text=f'当前时间: {current_time}')
            elif tool_type == '时间戳转换':
                convert_type = self.timestamp_convert_type.get()
                input_val = self.timestamp_input.get()
                
                if convert_type == '时间戳→日期时间':
                    timestamp = float(input_val)
                    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                    self.datetime_result.config(text=f'转换结果: {date_time}')
                else:
                    date_str = input_val
                    try:
                        timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))
                        self.datetime_result.config(text=f'时间戳: {timestamp}')
                    except ValueError:
                        messagebox.showerror('错误', '日期时间格式错误，请按照 YYYY-MM-DD HH:MM:SS 格式输入')
            elif tool_type == '日期计算':
                days = int(self.date_calc_days.get())
                future_time = time.time() + (days * 24 * 3600)
                future_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(future_time))
                self.datetime_result.config(text=f'{days}天后的日期时间: {future_date}')
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def create_number_tools_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='数字工具')
        
        ttk.Label(frame, text='数字处理工具', font=('Arial', 18, 'bold')).pack(pady=20)
        
        type_frame = ttk.Frame(frame)
        type_frame.pack(pady=10)
        
        ttk.Label(type_frame, text='选择功能:').grid(row=0, column=0, padx=5, pady=5)
        self.number_tool_type = ttk.Combobox(type_frame, values=['数字格式化', '数字转换', '数字计算'], state='readonly', width=15)
        self.number_tool_type.grid(row=0, column=1, padx=5, pady=5)
        self.number_tool_type.bind('<<ComboboxSelected>>', self.on_number_tool_change)
        self.number_tool_type.current(0)
        
        self.number_options_frame = ttk.Frame(frame)
        self.number_options_frame.pack(pady=5)
        
        ttk.Button(frame, text='执行', command=self.execute_number_tool).pack(pady=10)
        
        self.number_result = ttk.Label(frame, text='', font=('Arial', 14))
        self.number_result.pack(pady=10)
        
        self.on_number_tool_change(None)
    
    def on_number_tool_change(self, event):
        tool_type = self.number_tool_type.get()
        
        for widget in self.number_options_frame.winfo_children():
            widget.destroy()
        
        if tool_type == '数字格式化':
            ttk.Label(self.number_options_frame, text='数字:').grid(row=0, column=0, padx=5, pady=5)
            self.format_number = ttk.Entry(self.number_options_frame, width=15)
            self.format_number.grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(self.number_options_frame, text='小数位数:').grid(row=1, column=0, padx=5, pady=5)
            self.format_decimals = ttk.Entry(self.number_options_frame, width=15)
            self.format_decimals.grid(row=1, column=1, padx=5, pady=5)
            self.format_decimals.insert(0, '2')
        elif tool_type == '数字转换':
            ttk.Label(self.number_options_frame, text='十进制数字:').grid(row=0, column=0, padx=5, pady=5)
            self.convert_number = ttk.Entry(self.number_options_frame, width=15)
            self.convert_number.grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(self.number_options_frame, text='转换类型:').grid(row=1, column=0, padx=5, pady=5)
            self.convert_type = ttk.Combobox(self.number_options_frame, values=['二进制', '八进制', '十六进制'], state='readonly', width=15)
            self.convert_type.grid(row=1, column=1, padx=5, pady=5)
            self.convert_type.current(0)
        elif tool_type == '数字计算':
            ttk.Label(self.number_options_frame, text='第一个数字:').grid(row=0, column=0, padx=5, pady=5)
            self.calc_num1 = ttk.Entry(self.number_options_frame, width=15)
            self.calc_num1.grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(self.number_options_frame, text='第二个数字:').grid(row=1, column=0, padx=5, pady=5)
            self.calc_num2 = ttk.Entry(self.number_options_frame, width=15)
            self.calc_num2.grid(row=1, column=1, padx=5, pady=5)
            
            ttk.Label(self.number_options_frame, text='运算:').grid(row=2, column=0, padx=5, pady=5)
            self.calc_operation = ttk.Combobox(self.number_options_frame, values=['加法', '减法', '乘法', '除法'], state='readonly', width=15)
            self.calc_operation.grid(row=2, column=1, padx=5, pady=5)
            self.calc_operation.current(0)
    
    def execute_number_tool(self):
        tool_type = self.number_tool_type.get()
        
        try:
            if tool_type == '数字格式化':
                number = float(self.format_number.get())
                decimals = int(self.format_decimals.get())
                formatted = round(number, decimals)
                self.number_result.config(text=f'格式化结果: {formatted}')
            elif tool_type == '数字转换':
                number = int(self.convert_number.get())
                convert_type = self.convert_type.get()
                
                if convert_type == '二进制':
                    result = bin(number)
                elif convert_type == '八进制':
                    result = oct(number)
                else:
                    result = hex(number)
                
                self.number_result.config(text=f'{convert_type}: {result}')
            elif tool_type == '数字计算':
                num1 = float(self.calc_num1.get())
                num2 = float(self.calc_num2.get())
                operation = self.calc_operation.get()
                
                if operation == '加法':
                    result = num1 + num2
                elif operation == '减法':
                    result = num1 - num2
                elif operation == '乘法':
                    result = num1 * num2
                else:
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        messagebox.showerror('错误', '除数不能为0')
                        return
                
                self.number_result.config(text=f'结果: {result}')
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数字')
        except Exception as e:
            messagebox.showerror('错误', str(e))
    
    def create_ai_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='AI助手')
        
        ttk.Label(frame, text='简单的AI助手', font=('Arial', 18, 'bold')).pack(pady=20)
        
        ttk.Label(frame, text='请输入问题:').pack(pady=5)
        self.ai_input = scrolledtext.ScrolledText(frame, width=60, height=8)
        self.ai_input.pack(pady=5)
        
        ttk.Button(frame, text='发送', command=self.send_ai_question).pack(pady=10)
        
        ttk.Label(frame, text='AI回答:', font=('Arial', 12)).pack(pady=10)
        self.ai_output = scrolledtext.ScrolledText(frame, width=60, height=12)
        self.ai_output.pack(pady=5)
        
        self.ai_running = False
    
    def send_ai_question(self):
        if self.ai_running:
            messagebox.showwarning('提示', '正在处理中，请稍候...')
            return
        
        question = self.ai_input.get('1.0', tk.END).strip()
        if not question:
            messagebox.showerror('错误', '请输入问题')
            return
        
        self.ai_running = True
        self.ai_output.delete('1.0', tk.END)
        self.ai_output.insert('1.0', '正在思考中...\n')
        
        thread = threading.Thread(target=self._ai_worker, args=(question,))
        thread.daemon = True
        thread.start()
    
    def _ai_worker(self, question):
        try:
            from zai import ZhipuAiClient
            client = ZhipuAiClient(api_key="d286aa49ab044f3381955d95b8346502.6Qb2OTsWIoIaQbvH")
            
            response = client.chat.completions.create(
                model="glm-4.7",
                messages=[
                    {"role": "user", "content": "帮助用户解决问题"},
                    {"role": "assistant", "content": "帮助用户解决问题"},
                    {"role": "user", "content": question}
                ],
                thinking={
                    "type": "enabled",
                },
                stream=True,
                max_tokens=65536,
                temperature=1.0
            )
            
            self.root.after(0, lambda: self.ai_output.delete('1.0', tk.END))
            
            for chunk in response:
                if chunk.choices[0].delta.reasoning_content:
                    content = chunk.choices[0].delta.reasoning_content
                    self.root.after(0, lambda c=content: self.ai_output.insert(tk.END, c))
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    self.root.after(0, lambda c=content: self.ai_output.insert(tk.END, c))
            
            self.root.after(0, lambda: self.ai_output.insert(tk.END, '\n\n回答完成'))
        except Exception as e:
            self.root.after(0, lambda: self.ai_output.delete('1.0', tk.END))
            self.root.after(0, lambda: self.ai_output.insert('1.0', f'错误: {str(e)}'))
        finally:
            self.ai_running = False


def run_gui():
    root = tk.Tk()
    app = ToolBoxGUI(root)
    root.mainloop()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        run_gui()
    else:
        run_cli()
