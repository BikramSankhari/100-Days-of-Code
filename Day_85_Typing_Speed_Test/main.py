from tkinter import *
from tkinter import ttk, font
from threading import Thread

all_words = "Lately, I have been noticing how my sentences have a tendency to keep going when I write them onscreen. " \
            "This goes for concentrated writing as well as correspondence. (Twain probably believed that " \
            "correspondence, in an ideal world, also demands concentration. But he never used email.) Last week " \
            "I caught myself packing four conjunctions into a three-line sentence in an email. That’s inexcusable. " \
            "Since then, I have tried to eschew conjunctions whenever possible. Gone are the commas, the and’s, " \
            "but’s, and so’s; in are staccato declarative. Better to read like bad Hemingway than bad Faulkner.Try " \
            "putting some prose onscreen, though, and they mix themselves up pretty quickly. This has much to do " \
            "with the time constraints we claim to feel in the digital age. We don’t have time to compose letters " \
            "and post them anymore–much less pay postage, what with all the banks kinda-sorta losing our money these " \
            "days–so we blast a few emails. We don’t have time to talk, so we text. We don’t have time to text to " \
            "specific people, so we update our Facebook status. We don’t have time to write essays, so we blog."

selected_words_list = list(all_words.split(" "))
words = ''


def get_words():
    global words
    for word in selected_words_list:
        words += word + ' '


word_selecting_thread = Thread(target=get_words)
word_selecting_thread.start()

root = Tk()
root.title("Typing Speed Test")
starting_location = "700x600+" + str((root.winfo_screenwidth() // 2) - 350) + "+" + str(
    (root.winfo_screenheight() // 2) - 300)
root.geometry(starting_location)
style = ttk.Style()

main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)


def start_test():
    result.grid_remove()
    start_button.configure(state='disabled')
    word_index = 0
    word_count = 0

    def something_written(event):
        nonlocal word_index, word_count
        if event.keysym == 'space':
            current_word = user_input.get()

            if current_word[0] == ' ':
                current_word = current_word[1:]

            if current_word == selected_words_list[word_index]:
                word_count += 1
            word_index += 1
            user_input.set('')

    user_input_box.bind('<Key>', something_written)
    user_input.set('')
    user_input_box.state(['!disabled'])
    user_input_box.focus()
    time.set("01:00")
    root.after(1000, lambda: time.set("00:59"))
    seconds_left = 59

    def countdown():
        nonlocal seconds_left, word_count
        seconds_left -= 1
        if seconds_left < 10:
            time.set(f"00:0{seconds_left}")
        else:
            time.set(f"00:{seconds_left}")

        if seconds_left == 0:
            user_input_box.state(['disabled'])
            start_button.configure(state='!disabled', text="Start Again")
            result.configure(text=f"Your Score is: {word_count} wpm")
            result.grid()
        else:
            root.after(1000, countdown)

    root.after(2000, countdown)


clock_font = font.Font(size=40, weight='bold')
time = StringVar(value="00:00")
style.configure('clock.TLabel', font=clock_font, foreground='red')
clock = ttk.Label(main_frame, textvariable=time, style='clock.TLabel')
clock.grid(row=0, column=0, pady=20)

start_button_font = font.Font(size=20, weight='bold')
style.configure('start.TButton', height=20, font=start_button_font, foreground='green')
start_button = ttk.Button(main_frame, text="Start", style='start.TButton', command=start_test)
start_button.grid(row=0, column=1)

words_font = font.Font(size=20)
word_box = Text(main_frame, height=10, width=40, font=words_font, wrap='word')
word_box.insert(1.0, words)
word_box.configure(state='disabled')
word_box.grid(row=1, column=0, padx=50, columnspan=2)

user_input_font = font.Font(size=18)
user_input = StringVar(value="Click Start")
user_input_box = ttk.Entry(main_frame, width=10, font=user_input_font, justify='center',
                           textvariable=user_input, state='disabled')
user_input_box.grid(row=2, column=0, pady=15, columnspan=2)

result_font = font.Font(name='MV Boli', size=20)
style.configure('result.TLabel', font=result_font, foreground='red')
result = ttk.Label(main_frame, style='result.TLabel')
result.grid(row=3, columnspan=2, column=0, pady=40)
result.grid_remove()

root.mainloop()
