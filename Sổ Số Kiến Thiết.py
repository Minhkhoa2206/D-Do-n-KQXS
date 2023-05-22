from tkinter import simpledialog
from tkinter import messagebox
import tkinter as tk
import tkinter.messagebox
import random
import datetime
import os
from datetime import date
from datetime import timedelta





ACTIVE_FILE = "active.txt"

def check_install_date():
    if not os.path.exists(ACTIVE_FILE):
        with open(ACTIVE_FILE, "w") as f:
            fake_key = "Key Fake"
            install_date = str(date.today())
            user_id = "".join([str(random.randint(0, 9)) for _ in range(4)])
            f.write(f"{fake_key}\n{install_date}\n{user_id}")
        return True
    else:
        with open(ACTIVE_FILE, "r") as f:
            lines = f.read().splitlines()
            active_key = lines[0]
            active_date_str = lines[1]
            active_date = date.fromisoformat(active_date_str)
            if active_key == "Key Fake" and (date.today() - active_date).days > 3:
                return False
            else:
                 return True
                
def lottery_prediction(past_results, prize_numbers):
    # Sử dụng xác xuất để tính sổ số hôm nay
    today_result = []
    for i in range(8):
        today_prize = ""
        if i == 2:
            num_prizes = 2
        elif i == 3:
            num_prizes = 7
        elif i == 5:
            num_prizes = 3
        else:
            num_prizes = 1
        
        for _ in range(num_prizes):
            prize = ""
            for j in range(prize_numbers[i]):
                prize += random.choice(past_results[0][i][j] + past_results[1][i][j] + past_results[2][i][j])
            today_prize += prize + ","
        
        today_result.append(today_prize[:-1])
    
    special_prize = ""
    for j in range(prize_numbers[8]):
        special_prize += random.choice(past_results[0][8][j] + past_results[1][8][j] + past_results[2][8][j])
    today_result.append(special_prize)
    
    return today_result

def lottery_prediction(past_results, prize_numbers):
    # Sử dụng xác xuất để tính sổ số hôm nay
    today_result = []
    for i in range(8):
        today_prize = ""
        if i == 2:
            num_prizes = 2
        elif i == 3:
            num_prizes = 7
        elif i == 5:
            num_prizes = 3
        else:
            num_prizes = 1
        
        for _ in range(num_prizes):
            prize = ""
            for j in range(prize_numbers[i]):
                prize += random.choice(past_results[0][i][j] + past_results[1][i][j] + past_results[2][i][j])
            today_prize += prize + ","
        
        today_result.append(today_prize[:-1])
    
    special_prize = ""
    for j in range(prize_numbers[8]):
        special_prize += random.choice(past_results[0][8][j] + past_results[1][8][j] + past_results[2][8][j])
    today_result.append(special_prize)
    
    return today_result

def show_result():
    past_results = []
    for i in range(3):
        day_result = []
        for j in range(8):
            prize_frame_entries = entries[i][j]
            prize = ""
            
            # Tự động điền dữ liệu cho các ô nhập nếu chức năng "Không Cần Nhập liệu" được bật
            if auto_fill.get():
                for entry in prize_frame_entries:
                    entry.delete(0, tk.END)
                    entry.insert(0, "".join([str(random.randint(0, 9)) for _ in range(prize_numbers[j])]))
            
            for entry in prize_frame_entries:
                prize_value = entry.get()
                if len(prize_value) != prize_numbers[j]:
                    result_label.config(text=f"Lỗi: Giải {j+1} của ngày {i+1} phải có đúng {prize_numbers[j]} số")
                    entry.config(bg="red")
                    return
                else:
                    entry.config(bg="white")
                prize += prize_value + ","
            day_result.append(prize[:-1])
        
        special_prize_frame_entries = entries[i][8]
        special_prize = ""
        
        # Tự động điền dữ liệu cho các ô nhập nếu chức năng "Không Cần Nhập liệu" được bật
        if auto_fill.get():
            for entry in special_prize_frame_entries:
                entry.delete(0, tk.END)
                entry.insert(0, "".join([str(random.randint(0, 9)) for _ in range(prize_numbers[8])]))
        
        for entry in special_prize_frame_entries:
            special_prize_value = entry.get()
            if len(special_prize_value) != prize_numbers[8]:
                result_label.config(text=f"Lỗi: Giải đặc biệt của ngày {i+1} phải có đúng {prize_numbers[8]} số")
                entry.config(bg="red")
                return
            else:
                entry.config(bg="white")
            special_prize += special_prize_value + ","
        day_result.append(special_prize[:-1])
        
        past_results.append(day_result)
    
    result = lottery_prediction(past_results, prize_numbers)
    result_text = "Kết quả dự đoán sổ số hôm nay:\n"
    for i in range(8):
        
        result_text += f"Giải {i+1}: {result[i]}\n"
    result_text += f"Giải đặc biệt: {result[8]}"
    
    result_label.config(text=result_text)
    
def show_result_window():
    result_window = tk.Toplevel(root)
    result_window.title("Kết quả dự đoán")
    result_window.geometry("300x300")
    result_window.state('normal')
    
    result_text = tk.Text(result_window)
    result_text.pack(expand=True, fill='both')
    
    past_results = []
    for i in range(3):
        day_result = []
        for j in range(8):
            prize_frame_entries = entries[i][j]
            prize = ""
            
            # Tự động điền dữ liệu cho các ô nhập nếu chức năng "Không Cần Nhập liệu" được bật
            if auto_fill.get():
                for entry in prize_frame_entries:
                    entry.delete(0, tk.END)
                    entry.insert(0, "".join([str(random.randint(0, 9)) for _ in range(prize_numbers[j])]))
            
            for entry in prize_frame_entries:
                prize_value = entry.get()
                if len(prize_value) != prize_numbers[j]:
                    result_text.insert(tk.END, f"Lỗi: Giải {j+1} của ngày {i+1} phải có đúng {prize_numbers[j]} số\n")
                    entry.config(bg="red")
                    return
                else:
                    entry.config(bg="white")
                prize += prize_value + ","
            day_result.append(prize[:-1])
        
        special_prize_frame_entries = entries[i][8]
        special_prize = ""
        
        # Tự động điền dữ liệu cho các ô nhập nếu chức năng "Không Cần Nhập liệu" được bật
        if auto_fill.get():
            for entry in special_prize_frame_entries:
                entry.delete(0, tk.END)
                entry.insert(0, "".join([str(random.randint(0, 9)) for _ in range(prize_numbers[8])]))
        
        for entry in special_prize_frame_entries:
            special_prize_value = entry.get()
            if len(special_prize_value) != prize_numbers[8]:
                result_text.insert(tk.END, f"Lỗi: Giải đặc biệt của ngày {i+1} phải có đúng {prize_numbers[8]} số\n")
                entry.config(bg="red")
                return
            else:
                entry.config(bg="white")
            special_prize += special_prize_value + ","
        day_result.append(special_prize[:-1])
        
        past_results.append(day_result)
    
    result = lottery_prediction(past_results, prize_numbers)
    result_text.insert(tk.END, "Kết quả dự đoán sổ số hôm nay:\n")
    for i in range(8):
        result_text.insert(tk.END, f"Giải {i+1}: {result[i]}\n")
    result_text.insert(tk.END, f"Giải đặc biệt: {result[8]}")
root = tk.Tk()
root.title("Dự đoán sổ số")
copyright_label = tk.Label(root, text="Bản Quyền Thuộc Về ©KhoaWebs _Liên hệ: Hethongyoyn2@gmail.com", anchor="e")
copyright_label.pack(side=tk.TOP, fill=tk.X)

prize_numbers = [5, 5, 5, 5, 4, 4, 3, 2, 6]

entries = []
for i in range(3):
    day_entries = []
    day_frame = tk.Frame(root)
    day_frame.pack()
    tk.Label(day_frame, text=f"Ngày {i+1}").pack()
    for j in range(8):
        prize_frame = tk.Frame(day_frame)
        prize_frame.pack()
        tk.Label(prize_frame, text=f"Giải {j+1}").pack(side=tk.LEFT)
        
        # Thêm số lượng ô nhập cho giải 3, 4 và 6
        if j == 2:
            num_entries = 2
        elif j == 3:
            num_entries = 7
        elif j == 5:
            num_entries = 3
        else:
            num_entries = 1
        
        prize_frame_entries = []
        for _ in range(num_entries):
            entry = tk.Entry(prize_frame)
            entry.pack(side=tk.RIGHT)
            prize_frame_entries.append(entry)
        
        day_entries.append(prize_frame_entries)
    
    special_prize_frame = tk.Frame(day_frame)
    special_prize_frame.pack()
    tk.Label(special_prize_frame, text="Giải đặc biệt").pack(side=tk.LEFT)
    
    special_prize_frame_entries = []
    for _ in range(1):
        entry = tk.Entry(special_prize_frame)
        entry.pack(side=tk.RIGHT)
        special_prize_frame_entries.append(entry)
    
    day_entries.append(special_prize_frame_entries)
    
    entries.append(day_entries)

result_label = tk.Label(root, text="")
result_label.pack()

show_button = tk.Button(root, text="Hiển thị kết quả", command=show_result_window)
show_button.pack()


# Thêm biến toàn cục và hàm để quản lý trạng thái của chức năng "Không Cần Nhập liệu"
auto_fill = tk.BooleanVar(value=False)

def toggle_auto_fill():
    auto_fill.set(not auto_fill.get())

# Thêm nút vào thanh công cụ để bật/tắt chức năng "Không Cần Nhập liệu"
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Cài Đặt", menu=settings_menu)

settings_menu.add_checkbutton(label="Không Cần Nhập liệu", onvalue=True, offvalue=False,
                              variable=auto_fill,
                              command=toggle_auto_fill)

import random

def check_key():
    key = simpledialog.askstring("Kích hoạt bản quyền", "Nhập KEY:")
    with open("keybq.txt", "r") as f:
        valid_keys_3m = f.read().splitlines()
    if key in valid_keys_3m:
        duration = 90
    else:
        messagebox.showerror("Kích hoạt bản quyền", "Mã Kích Hoạt Sai - Vui Lòng Nhập Lại _ hoặc liên hệ: 0867544809")
        return
    
    if os.path.exists("active.txt"):
        with open("active.txt", "r") as f:
            lines = f.read().splitlines()
            active_key = lines[0]
            active_date_str = lines[1]
            active_date = datetime.date.fromisoformat(active_date_str)
            if key == active_key:
                days_left = (active_date + datetime.timedelta(days=duration) - datetime.date.today()).days
                if days_left > 0:
                    messagebox.showinfo("Kích hoạt bản quyền", f"Key này đã được kích hoạt. Còn lại {days_left} ngày sử dụng.")
                    return
    with open("active.txt", "w") as f:
        user_id = "".join([str(random.randint(0, 9)) for _ in range(4)])
        f.write(f"{key}\n{datetime.date.today()}\n{user_id}")
    messagebox.showinfo("Kích hoạt bản quyền", f"Đã Kích Hoạt Bản Quyền Thành Công. Hạn Sử Dụng Là {duration//30} Tháng")

if not check_install_date():
    root.withdraw()
    result = tk.messagebox.askokcancel("Error", "Bạn chỉ được sử dụng chương trình miễn phí trong 3 ngày. Vui lòng mua bản quyền để tiếp tục sử dụng. Nếu có Key Active vui lòng bấm OK để nhập mã Kích Hoạt. Bản Quyền Thuộc Về ©KhoaWebs _Liên hệ: Hethongyoyn2@gmail.com")
    if result:
        check_key()
    else:
        root.destroy()
        exit()
def display_user_info():
    with open(ACTIVE_FILE, "r") as f:
        lines = f.read().splitlines()
        key = lines[0]
        active_date_str = lines[1]
        active_date = date.fromisoformat(active_date_str)
        user_id = lines[2]
    
    if key == "Key Fake":
        days_left = 3 - (date.today() - active_date).days
        user_id = "Key Fake"
    else:
        days_left = (active_date + timedelta(days=90) - date.today()).days
    
    info_text = f"User: {user_id}\nNgày kích hoạt: {active_date_str}\nCòn lại: {days_left} ngày"
    info_label.config(text=info_text)

info_label = tk.Label(root, text="", anchor="w")
info_label.pack(side=tk.TOP, fill=tk.X)

display_user_info()

import webbrowser

def open_website():
    webbrowser.open("https://sites.google.com/view/khoawebs")

def show_info():
    with open(ACTIVE_FILE, "r") as f:
        lines = f.read().splitlines()
        key = lines[0]
        active_date_str = lines[1]
        active_date = date.fromisoformat(active_date_str)
        user_id = lines[2]
    
    if key == "Key Fake":
        days_left = 3 - (date.today() - active_date).days
        user_id = "Key Fake"
    else:
        days_left = (active_date + timedelta(days=90) - date.today()).days
    
    info_text = f"User: {user_id}\nNgày kích hoạt: {active_date_str}\nCòn lại: {days_left} ngày\n\nPHẦN MỀM DỰ ĐOÁN SỔ SỐ\nThiết Kế: Mr.Khoa\nEmail: Hethongyoyn2@gmail.com\nHotline: 0867544809 - 0825864379"
    messagebox.showinfo("Thông Tin", info_text)

menu = tk.Menu(root)
root.config(menu=menu)

menu.add_command(label="Trang Web", command=open_website)
menu.add_command(label="Thông Tin", command=show_info)
menu.add_command(label="Active", command=check_key)


def show_register_info():
    result = messagebox.askokcancel("Đăng Kí", "Liên Hệ Zalo: 0867544808 để mua bản quyền.")
    if result:
        webbrowser.open("https://zalo.me/0867544809")

menu.add_command(label="Đăng Kí", command=show_register_info)
def reset():
    for day_entries in entries:
        for entry in day_entries:
            entry.delete(0, tk.END)
    result_label.config(text="")

menu.add_command(label="Reset", command=reset)
def open_policy():
    os.startfile("banquyen.pdf")

menu.add_command(label="Chính sách & Quyền riêng tư", command=open_policy)

def open_xsmb():
    webbrowser.open("https://xoso.com.vn/xo-so-mien-bac/xsmb-p1.html")

def open_xsmt():
    webbrowser.open("https://xoso.com.vn/xo-so-mien-trung/xsmt-p1.html")

def open_xsmn():
    webbrowser.open("https://xoso.com.vn/xo-so-mien-nam/xsmn-p1.html")
def open_vietlott():
    webbrowser.open("https://xoso.com.vn/kqxs-vietlott-ket-qua-xo-so-vietlott.html")

submenu = tk.Menu(menu)
menu.add_cascade(label="Tra Cứu KQSS", menu=submenu)
submenu.add_command(label="XSMB", command=open_xsmb)
submenu.add_command(label="XSMT", command=open_xsmt)
submenu.add_command(label="XSMN", command=open_xsmn)
submenu.add_command(label="Vietlott", command=open_vietlott)

# Khởi tạo giá trị mặc định cho các tùy chọn
prediction_rate_value = "25%"
prediction_time_value = 10

def open_settings():
    def update_prediction_rate(*args):
        global prediction_rate_value
        prediction_rate_value = prediction_rate.get()
    
    def update_prediction_time(value):
        global prediction_time_value
        prediction_time_value = int(value)
    
    settings_window = tk.Toplevel(root)
    settings_window.title("Cài Đặt")
    
    tk.Label(settings_window, text="Tỉ Lệ Dự Đoán Kết Quả:").pack()
    prediction_rate = tk.StringVar(settings_window)
    prediction_rate.set(prediction_rate_value)
    prediction_rate.trace("w", update_prediction_rate)
    prediction_rate_options = ["25%", "50%", "75%", "90%"]
    prediction_rate_menu = tk.OptionMenu(settings_window, prediction_rate, *prediction_rate_options)
    prediction_rate_menu.pack()
    
    tk.Label(settings_window, text="Thời Gian Dự Đoán:").pack()
    prediction_time = tk.Scale(settings_window, from_=10, to=60, orient=tk.HORIZONTAL, command=update_prediction_time)
    prediction_time.set(prediction_time_value)
    prediction_time.pack()

    settings_menu.add_checkbutton(label="Không Cần Nhập liệu", onvalue=True, offvalue=False,
                              variable=auto_fill,
                              command=toggle_auto_fill)
menu.add_command(label="Cài Đặt", command=open_settings)

def create_password():
    def save_pin():
        pin = pin_entry.get()
        confirm_pin = confirm_pin_entry.get()
        backup_pin = backup_pin_entry.get()
        if pin == confirm_pin:
            with open("security.txt", "w") as f:
                f.write(f"{pin}\n{backup_pin}")
            create_password_window.destroy()
        else:
            messagebox.showerror("Tạo Mật Khẩu", "Mã Pin Không Trùng Khớp")
    
    create_password_window = tk.Toplevel(root)
    create_password_window.title("Tạo Mật Khẩu")
    
    tk.Label(create_password_window, text="Mã Pin:").pack()
    pin_entry = tk.Entry(create_password_window)
    pin_entry.pack()
    
    tk.Label(create_password_window, text="Nhập Lại Mã Pin:").pack()
    confirm_pin_entry = tk.Entry(create_password_window)
    confirm_pin_entry.pack()
    
    tk.Label(create_password_window, text="Mã Dự Phòng:").pack()
    backup_pin_entry = tk.Entry(create_password_window)
    backup_pin_entry.pack()
    
    tk.Button(create_password_window, text="OK", command=save_pin).pack()
if os.path.exists("security.txt"):
    with open("security.txt", "r") as f:
        lines = f.read().splitlines()
        pin = lines[0]
    
    entered_pin = simpledialog.askstring("Bảo Mật", "Nhập Mã Pin:")
    if entered_pin != pin:
        root.destroy()
def reset_password():
    def remove_pin():
        old_pin = old_pin_entry.get()
        with open("security.txt", "r") as f:
            lines = f.read().splitlines()
            current_pin = lines[0]
        if old_pin == current_pin:
            os.remove("security.txt")
            reset_password_window.destroy()
        else:
            messagebox.showerror("Reset Password", "Mã Pin Cũ Không Chính Xác")
    
    reset_password_window = tk.Toplevel(root)
    reset_password_window.title("Reset Password")
    
    tk.Label(reset_password_window, text="Mã Pin Cũ:").pack()
    old_pin_entry = tk.Entry(reset_password_window)
    old_pin_entry.pack()
    
    tk.Button(reset_password_window, text="OK", command=remove_pin).pack()

def open_security():
    security_window = tk.Toplevel(root)
    security_window.title("Bảo Mật")
    
    tk.Button(security_window, text="Tạo Mật Khẩu", command=create_password).pack()
    tk.Button(security_window, text="Reset Password", command=reset_password).pack()

menu.add_command(label="Bảo Mật", command=open_security)

root.mainloop()

