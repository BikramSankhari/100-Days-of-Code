from tkinter import *
from tkinter import ttk, filedialog, font
from PIL import ImageTk, Image


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(('JPG', '*.jpg'),
                                                     ('JPEG', '*.jpeg'),
                                                     ('PNG', '*.png')))

    global canvas_image
    try:
        new_image = Image.open(filename)
    except AttributeError:
        pass
    else:
        canvas_image = ImageTk.PhotoImage(new_image)
        canvas.itemconfig(canvas_image_container, image=canvas_image)
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Width e Boro
        if new_image.size[0] > 1200:
            horizontal_scrollbar.grid(sticky="ew", row=1, column=0)
        else:
            canvas.coords(canvas_image_container,
                          [(1100 - new_image.size[0]) / 2, canvas.coords(canvas_image_container)[1]])
            horizontal_scrollbar.grid_remove()

        # Height e Boro
        if new_image.size[1] > 500:
            vertical_scrollbar.grid(row=0, column=1, sticky="ns")
        else:
            canvas.coords(canvas_image_container,
                          [canvas.coords(canvas_image_container)[0], (500 - new_image.size[1]) / 2])
            vertical_scrollbar.grid_remove()

        watermark.state(['!disabled'])
        watermark_text.set('')
        watermark_scale.state(['!disabled'])
        left_button.state(['!disabled'])
        right_button.state(['!disabled'])
        up_button.state(['!disabled'])
        down_button.state(['!disabled'])


root = Tk()
root.title("Image WaterMarker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry('1230x670+15+30')

style = ttk.Style(root)
style.configure('new.TFrame')
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

canvas_frame = ttk.Frame(main_frame)
canvas_frame.grid(row=0, column=0, padx=40)
canvas = Canvas(canvas_frame, width=1100, height=500)
canvas.grid(row=0, column=0)

button_font = font.Font(family='Times New Roman', name='Times New Roman', size=20)
style.configure('new.TButton', font=button_font)
button = ttk.Button(main_frame, text='Browse', padding=10, command=browse_files, style='new.TButton')
button.grid(row=1, column=0)

sub_frame = ttk.Frame(main_frame)
sub_frame.grid(row=3, column=0, pady=10)
label_font = font.Font(size=12)
style.configure('new.TLabel', font=label_font)
entry_label = ttk.Label(sub_frame, text="Enter Your Watermark Here:", style='new.TLabel')
entry_label.grid(row=0, column=0, sticky=W)


def something_written(var, index, mode):
    canvas.itemconfig(canvas_watermark, text=watermark_text.get())


watermark_text = StringVar(value="Select an Image File First!")
watermark = ttk.Entry(sub_frame, width=60, state='disabled', textvariable=watermark_text)
watermark.grid(row=0, column=1, padx=20)

watermark_text.trace_add('write', something_written)

size_label = ttk.Label(sub_frame, text='Adjust Size Here:', style='new.TLabel')
size_label.grid(row=0, column=2, sticky=W)


def size_change(val):
    new_size = font.Font(size=int(float(val)))
    canvas.itemconfig(canvas_watermark, font=new_size)


watermark_scale = ttk.Scale(sub_frame, orient=HORIZONTAL, length=200, from_=20.0, to=200.0, command=size_change,
                            state='disabled')
watermark_scale.grid(row=0, column=3, padx=20)

frame_two = ttk.Frame(main_frame)
frame_two.grid(row=4, column=0, sticky=W, padx=85)
position_label = ttk.Label(frame_two, text='Set Position from Here:', style='new.TLabel')
position_label.grid(row=0, column=0, padx=20, sticky=W)


def move_left():
    canvas.coords(canvas_watermark, [canvas.coords(canvas_watermark)[0] - 10, canvas.coords(canvas_watermark)[1]])


def move_right():
    canvas.coords(canvas_watermark, [canvas.coords(canvas_watermark)[0] + 10, canvas.coords(canvas_watermark)[1]])


def move_up():
    canvas.coords(canvas_watermark, [canvas.coords(canvas_watermark)[0], canvas.coords(canvas_watermark)[1] - 10])


def move_down():
    canvas.coords(canvas_watermark, [canvas.coords(canvas_watermark)[0], canvas.coords(canvas_watermark)[1] + 10])


left_button = ttk.Button(frame_two, text='← LEFT', command=move_left, state='disabled')
right_button = ttk.Button(frame_two, text='RIGHT →', command=move_right, state='disabled')
up_button = ttk.Button(frame_two, text='UP ↑', command=move_up, state='disabled')
down_button = ttk.Button(frame_two, text='DOWN ↓', command=move_down, state='disabled')

left_button.grid(row=0, column=1)
right_button.grid(row=0, column=2)
up_button.grid(row=0, column=3)
down_button.grid(row=0, column=4)

canvas_image = ImageTk.PhotoImage(Image.open('gray_box.png').resize((1100, 500)))
canvas_image_container = canvas.create_image(0, 0, image=canvas_image, anchor="nw")
watermark_font = font.Font(size=60)

# noinspection PyArgumentList
canvas_watermark = canvas.create_text(570, 250, text='Your Text Here!', fill='white', font=watermark_font,
                                      angle='25')

vertical_scrollbar = ttk.Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview)
horizontal_scrollbar = ttk.Scrollbar(canvas_frame, orient=HORIZONTAL, command=canvas.xview)

canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set,
                 scrollregion=canvas.bbox("all"))

canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

horizontal_scrollbar.grid(sticky="ew", row=1, column=0)
vertical_scrollbar.grid(row=0, column=1, sticky="ns")
horizontal_scrollbar.grid_remove()
vertical_scrollbar.grid_remove()

root.mainloop()
