import win32gui
import win32ui
import win32con
import tkinter

def capture_with_area(path: str):
    start_pos, size = select_area()
    capture_screen(*start_pos, *size, path)

def capture_screen(x, y, width, height, path):
    # grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()

    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc,
                    (x, y), win32con.SRCCOPY)

    # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, path)

    # free our objects
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
    
def select_area():
    root = tkinter.Tk()
    # root.wm_attributes("-disabled", True)
    root.wm_attributes("-topmost", True)
    root.attributes('-alpha', 0.3)
    root.state('zoomed')
    root.overrideredirect(True)
    root.resizable(False, False)
    root.configure(bg='black')
    
    start_pos = ()
    end_pos = ()

    root.update_idletasks() 
    canvas = tkinter.Canvas(root, bg='black', width=root.winfo_width(), height=root.winfo_height())
    canvas.pack()

    def mouse_down_callback(event):
        start_pos = (event.x, event.y)

    def mouse_up_callback(event):
        end_pos = (event.x, event.y)
        root.destroy()
        
    def mouse_move_callback(event): 
        cur_pos = (event.x, event.y)
        canvas.delete('all')
        canvas.create_rectangle(start_pos[0], start_pos[1], cur_pos[0], cur_pos[1], fill='white')

    root.bind('<Button-1>', mouse_down_callback)
    root.bind('<ButtonRelease-1>', mouse_up_callback)
    root.bind('<B1-Motion>', mouse_move_callback)
    root.mainloop()

    # TODO: resolve `IndexError: tuple index out of range` error
    return (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])), (abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
