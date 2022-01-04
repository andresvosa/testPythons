"""[summary]
"""
import dearpygui.dearpygui as dpg

def save_callback():
    """[summary]
    """
    print("Save Clicked: " + dpg.get_value(sis_tekst))

with dpg.window(label="Example Window", height=300, width=300):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    sis_tekst = dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")


dpg.setup_viewport()
dpg.set_viewport_height(300)
dpg.set_viewport_width(300)
dpg.start_dearpygui()
