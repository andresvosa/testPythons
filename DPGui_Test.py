import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

with dpg.window(label="Example Window", height=300, width=300):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.setup_viewport()
dpg.start_dearpygui()