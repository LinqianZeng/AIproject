import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# 游戏数据（图片文件名 : 正确单词）
game_data = {
    "apple.png": "Apple",
    "banana.png": "Banana"
}

# 初始化主窗口
root = tk.Tk()
root.title("识图识字小游戏")
root.geometry("400x400")
root.config(bg="#f0f8ff")

score = 0
current_question = 0
image_label = None
answer_buttons = []
image_list = list(game_data.keys())

def load_question():
    global image_label
    global current_image
    if current_question >= len(image_list):
        messagebox.showinfo("游戏结束", f"你得了 {score} 分！")
        root.quit()
        return

    # 清除旧按钮
    for btn in answer_buttons:
        btn.destroy()
    answer_buttons.clear()

    img_path = f"./assets/{image_list[current_question]}"
    correct_word = game_data[image_list[current_question]]

    # 加载图片
    img = Image.open(img_path).resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    current_image = photo

    if image_label:
        image_label.config(image=current_image)
    else:
        image_label = tk.Label(root, image=current_image, bg="#f0f8ff")
        image_label.pack(pady=10)

    # 随机生成按钮（包含正确和错误选项）
    import random
    options = [correct_word, "Orange", "Car", "Pencil"]
    random.shuffle(options)

    for word in options:
        btn = tk.Button(root, text=word, width=20, height=2,
                        command=lambda w=word: check_answer(w))
        btn.pack(pady=2)
        answer_buttons.append(btn)

def check_answer(selected):
    global score, current_question
    correct = game_data[image_list[current_question]]
    if selected == correct:
        score += 10
        messagebox.showinfo("正确！", "答对啦！+10分")
    else:
        messagebox.showerror("错误！", f"正确答案是：{correct}")
    current_question += 1
    load_question()

# 开始游戏
load_question()
root.mainloop()
