
from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
import string
import random
import base64
import qrcode
import time



print(Fore.GREEN + '-----------------------------------------' )
print(Fore.GREEN + '| |谢赵宇工具箱|                           |' )
print(Fore.GREEN + '| |qq:136805009@qq.com|                    |' )
print(Fore.GREEN + '| |开源免费的工具箱|                       |' )
print(Fore.GREEN + '-----------------------------------------' )
while True:
    raw_input = input(Fore.YELLOW + '请输入指令(不知道有哪些命令请输入5):')
    if raw_input == '5':
        # 使用 colorama 的 Fore.GREEN 来设置终端输出绿色
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
        print(Fore.GREEN + '| |版本:0.1.0|                           |' )
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
        print(Fore.GREEN + '| |1. 长度单位换算|                     |' ) #ok
        print(Fore.GREEN + '| |2. 重量单位换算|                     |' ) #ok
        print(Fore.GREEN + '| |3. 温度单位换算|                     |' ) #ok
        print(Fore.GREEN + '| |4. 时间单位换算|                     |' ) #ok
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
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
            if choice == '1':
                # 米转千米
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |米转千米|                             |' )
                print(Fore.GREEN + '-----------------------------------------' )
                meter = float(input(Fore.YELLOW + "请输入米数: "))
                kilometer = meter / 1000
                print(Fore.CYAN + "转换后的千米数: " + str(kilometer))
            elif choice == '2':
                # 千米转米
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |千米转米|                             |' )
                print(Fore.GREEN + '-----------------------------------------' )
                kilometer = float(input(Fore.YELLOW + "请输入千米数: "))
                meter = kilometer * 1000
                print(Fore.CYAN + "转换后的米数: " + str(meter))
        elif choice == '2':
                # 重量单位换算
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |重量单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 克-千克 (g)|                     |' )
                print(Fore.GREEN + '| |2. 千克-克 (kg)|                    |' )
                print(Fore.GREEN + '|                                      |' )
                print(Fore.GREEN + '|                                       |' )
                print(Fore.GREEN + '|                                       |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    # 克转千克
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |克转千克|                             |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    gram = float(input(Fore.YELLOW + "请输入克数: "))
                    kilogram = gram / 1000
                    print(Fore.CYAN + "转换后的千克数: " + str(kilogram))
                elif choice == '2':
                    # 千克转克
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |千克转克|                             |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    kilogram = float(input(Fore.YELLOW + "请输入千克数: "))
                    gram = kilogram * 1000
                    print(Fore.CYAN + "转换后的克数: " + str(gram))
        elif choice == '3':
            # 温度单位换算
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |温度单位换算|                        |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 摄氏度-华氏度 (°C)|              |' )
            print(Fore.GREEN + '| |2. 华氏度-摄氏度 (°F)|              |' )
            print(Fore.GREEN + '|                                      |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
            if choice == '1':
                # 摄氏度转华氏度
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |摄氏度转华氏度|                     |' )
                print(Fore.GREEN + '-----------------------------------------' )
                celsius = float(input(Fore.YELLOW + "请输入摄氏度: "))
                fahrenheit = (celsius * 9/5) + 32
                print(Fore.CYAN + "转换后的华氏度: " + str(fahrenheit))
            elif choice == '2':
                # 华氏度转摄氏度
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |华氏度转摄氏度|                     |' )
                print(Fore.GREEN + '-----------------------------------------' )
                fahrenheit = float(input(Fore.YELLOW + "请输入华氏度: "))
                celsius = (fahrenheit - 32) * 5/9
                print(Fore.CYAN + "转换后的摄氏度: " + str(celsius))
        elif choice == '6':
            # 面积单位换算
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |面积单位换算|                        |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 平方米-平方公里 (m²)|           |' )
            print(Fore.GREEN + '| |2. 平方公里-平方米 (km²)|          |' )
            print(Fore.GREEN + '|                                      |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
            if choice == '1':
                # 平方米转平方公里
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |平方米转平方公里|                 |' )
                print(Fore.GREEN + '-----------------------------------------' )
                square_meter = float(input(Fore.YELLOW + "请输入平方米数: "))
                square_kilometer = square_meter / 1000000
                print(Fore.CYAN + "转换后的平方公里数: " + str(square_kilometer))
            elif choice == '2':
                # 平方公里转平方米
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |平方公里转平方米|                 |' )
                print(Fore.GREEN + '-----------------------------------------' )
                square_kilometer = float(input(Fore.YELLOW + "请输入平方公里数: "))
                square_meter = square_kilometer * 1000000
                print(Fore.CYAN + "转换后的平方米数: " + str(square_meter))
            elif choice == '4':
                # 面积单位换算
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |时间单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 秒-分钟 (s)|                     |' )
                print(Fore.GREEN + '| |2. 分钟-秒 (min)|                   |' )
                print(Fore.GREEN + '|                                      |' )
                print(Fore.GREEN + '|                                       |' )
                print(Fore.GREEN + '|                                       |' )
                print(Fore.GREEN + '-----------------------------------------' )
                choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
                if choice == '1':
                    # 平方米转平方公里
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |秒转分钟|                         |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    second = float(input(Fore.YELLOW + "请输入秒数: "))
                    minute = second / 60
                    print(Fore.CYAN + "转换后的分钟数: " + str(minute))
                elif choice == '2':
                    # 分钟转秒
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |分钟转秒|                         |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    minute = float(input(Fore.YELLOW + "请输入分钟数: "))
                    second = minute * 60
                    print(Fore.CYAN + "转换后的秒数: " + str(second))
            elif choice == '5':
                # 面积单位换算
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |速度单位换算|                        |' )
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |1. 米/秒-千米/小时 (m/s)|           |' )
                print(Fore.GREEN + '| |2. 千米/小时-米/秒 (km/h)|          |' )
                print(Fore.GREEN + '|                                      |' )
                print(Fore.GREEN + '|                                       |' )
                print(Fore.GREEN + '|                                       |' )
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
                    # 千米/小时转米/秒
                    print(Fore.GREEN + '-----------------------------------------' )
                    print(Fore.GREEN + '| |千米/小时转米/秒|                 |' )
                    print(Fore.GREEN + '-----------------------------------------' )
                    kilometer_per_hour = float(input(Fore.YELLOW + "请输入千米/小时数: "))
                    meter_per_second = kilometer_per_hour / 3600
                    print(Fore.CYAN + "转换后的米/秒数: " + str(meter_per_second))
        elif choice == '7':
                # 面积单位换算
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |容量单位换算|                        |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. kb-MB (KB)|          |' )
            print(Fore.GREEN + '| |2. MB-kb (MB)|          |' )
            print(Fore.GREEN + '|                                      |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '-----------------------------------------' )
            choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
            if choice == '1':
                    # 平方米转平方公里
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |kb-MB|                         |' )
                print(Fore.GREEN + '-----------------------------------------' )
                kb = float(input(Fore.YELLOW + "请输入KB数: "))
                mb = kb / 1024
                print(Fore.CYAN + "转换后的MB数: " + str(mb))
            elif choice == '2':
                    # MB-kb
                print(Fore.GREEN + '-----------------------------------------' )
                print(Fore.GREEN + '| |MB-kb|                         |' )
                print(Fore.GREEN + '-----------------------------------------' )
                mb = float(input(Fore.YELLOW + "请输入MB数: "))
                kb = mb * 1024
                print(Fore.CYAN + "转换后的KB数: " + str(kb))
    if raw_input == '9':  
        #倒计时
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
        #密码字典生成器
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |密码字典生成器|                       |' )
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |1. 生成简单密码字典|                 |' )
        print(Fore.GREEN + '| |2. 生成复杂密码字典|                 |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '-----------------------------------------' )
        choice = input(Fore.YELLOW + "请选择操作 (1-2): ")
        if choice == '1':
            # 生成简单密码字典
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |生成简单密码字典|                   |' )
            print(Fore.GREEN + '-----------------------------------------' )
            password = input(Fore.YELLOW + "请输入密码长度: ")
            password_length = int(password)
            characters = "0123456789"
            #批量生成
            num_passwords = int(input(Fore.YELLOW + "请输入要生成的密码数量: "))
            random_passwords = [''.join(random.choice(characters) for i in range(password_length)) for _ in range(num_passwords)]
            open('simple_passwords.txt', 'w').write('\n'.join(random_passwords))
            print(Fore.CYAN + "简单密码字典已生成并保存到 simple_passwords.txt 文件中")
        elif choice == '2':
            # 生成复杂密码字典
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |生成复杂密码字典|                   |' )
            print(Fore.GREEN + '-----------------------------------------' )
            password = input(Fore.YELLOW + "请输入密码长度: ")
            password_length = int(password)
            characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
            #批量生成
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
        # 文本处理工具
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |文本处理工具|                         |' )
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |1. 文本大小写转换|                   |' )
        print(Fore.GREEN + '| |2. 文本字符统计|                     |' )
        print(Fore.GREEN + '| |3. 文本反转|                         |' )
        print(Fore.GREEN + '| |4. 文本去空格|                       |' )
        print(Fore.GREEN + '| |5. 文本替换|                         |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '-----------------------------------------' )
        choice = input(Fore.YELLOW + "请选择操作 (1-5): ")
        if choice == '1':
            # 文本大小写转换
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |文本大小写转换|                      |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 转为大写|                         |' )
            print(Fore.GREEN + '| |2. 转为小写|                         |' )
            print(Fore.GREEN + '| |3. 首字母大写|                       |' )
            print(Fore.GREEN + '|                                      |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
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
            # 文本字符统计
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
            # 文本反转
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |文本反转|                            |' )
            print(Fore.GREEN + '-----------------------------------------' )
            text = input(Fore.YELLOW + "请输入文本: ")
            result = text[::-1]
            print(Fore.CYAN + "反转后的文本: " + result)
        elif choice == '4':
            # 文本去空格
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |文本去空格|                          |' )
            print(Fore.GREEN + '-----------------------------------------' )
            text = input(Fore.YELLOW + "请输入文本: ")
            result = text.replace(" ", "")
            print(Fore.CYAN + "去空格后的文本: " + result)
        elif choice == '5':
            # 文本替换
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |文本替换|                            |' )
            print(Fore.GREEN + '-----------------------------------------' )
            text = input(Fore.YELLOW + "请输入文本: ")
            old_str = input(Fore.YELLOW + "请输入要替换的字符串: ")
            new_str = input(Fore.YELLOW + "请输入替换后的字符串: ")
            result = text.replace(old_str, new_str)
            print(Fore.CYAN + "替换后的文本: " + result)
    elif raw_input == '12':
        # 日期时间工具
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |日期时间工具|                         |' )
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |1. 获取当前时间|                     |' )
        print(Fore.GREEN + '| |2. 时间戳转换|                       |' )
        print(Fore.GREEN + '| |3. 日期计算|                         |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '-----------------------------------------' )
        choice = input(Fore.YELLOW + "请选择操作 (1-3): ")
        if choice == '1':
            # 获取当前时间
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |获取当前时间|                        |' )
            print(Fore.GREEN + '-----------------------------------------' )
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(Fore.CYAN + "当前时间: " + current_time)
        elif choice == '2':
            # 时间戳转换
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |时间戳转换|                          |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 时间戳转日期时间|                 |' )
            print(Fore.GREEN + '| |2. 日期时间转时间戳|                 |' )
            print(Fore.GREEN + '|                                      |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
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
            # 日期计算
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |日期计算|                            |' )
            print(Fore.GREEN + '-----------------------------------------' )
            days = int(input(Fore.YELLOW + "请输入天数: "))
            future_time = time.time() + (days * 24 * 3600)
            future_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(future_time))
            print(Fore.CYAN + str(days) + "天后的日期时间: " + future_date)
    elif raw_input == '13':
        # 数字处理工具
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |数字处理工具|                         |' )
        print(Fore.GREEN + '-----------------------------------------' )
        print(Fore.GREEN + '| |1. 数字格式化|                       |' )
        print(Fore.GREEN + '| |2. 数字转换|                         |' )
        print(Fore.GREEN + '| |3. 数字计算|                         |' )
        print(Fore.GREEN + '|                                      |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '|                                       |' )
        print(Fore.GREEN + '-----------------------------------------' )
        choice = input(Fore.YELLOW + "请选择操作 (1-3): ")
        if choice == '1':
            # 数字格式化
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |数字格式化|                          |' )
            print(Fore.GREEN + '-----------------------------------------' )
            number = float(input(Fore.YELLOW + "请输入数字: "))
            decimal_places = int(input(Fore.YELLOW + "请输入小数位数: "))
            formatted = round(number, decimal_places)
            print(Fore.CYAN + "格式化后的数字: " + str(formatted))
        elif choice == '2':
            # 数字转换
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |数字转换|                            |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 十进制转二进制|                   |' )
            print(Fore.GREEN + '| |2. 十进制转八进制|                   |' )
            print(Fore.GREEN + '| |3. 十进制转十六进制|                 |' )
            print(Fore.GREEN + '|                                      |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
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
            # 数字计算
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |数字计算|                            |' )
            print(Fore.GREEN + '-----------------------------------------' )
            print(Fore.GREEN + '| |1. 加法|                             |' )
            print(Fore.GREEN + '| |2. 减法|                             |' )
            print(Fore.GREEN + '| |3. 乘法|                             |' )
            print(Fore.GREEN + '| |4. 除法|                             |' )
            print(Fore.GREEN + '|                                       |' )
            print(Fore.GREEN + '|                                       |' )
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
        client = ZhipuAiClient(api_key="d286aa49ab044f3381955d95b8346502.6Qb2OTsWIoIaQbvH")  # 请填写您自己的 API Key

        response = client.chat.completions.create(
        model="glm-4.7",
        messages=[
            {"role": "user", "content": "帮助用户解决问题"},
            {"role": "assistant", "content": "帮助用户解决问题"},
            {"role": "user", "content": input(Fore.YELLOW + "请输入问题: ")}
            ],
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        stream=True,              # 启用流式输出
        max_tokens=65536,          # 最大输出tokens
        temperature=1.0           # 控制输出的随机性
        )
        for chunk in response:
            if chunk.choices[0].delta.reasoning_content:
                print(chunk.choices[0].delta.reasoning_content, end='', flush=True)

            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end='', flush=True)
   
            

           
            
           
            
            
        
    

