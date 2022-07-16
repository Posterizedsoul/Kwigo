import dearpygui.dearpygui as dpg
import os
import ctypes
import webbrowser
import random

os.chdir(os.getcwd())

dpg.create_context()
WIDTH, HEIGHT = 1920, 1080
cur_dir = os.getcwd()

os.chdir('D:/All the coding stuff/Mangadex')

width, height, channels, data = dpg.load_image('images/manga_neko.png')

with dpg.texture_registry():
    dpg.add_static_texture(width, height, data, tag="image_id")


'''
About Page
'''
with dpg.window(label="About", width=300, height=120,pos=[WIDTH // 2 -300//2, HEIGHT // 2- 250//2],modal=True, show=False, id="about_id", no_title_bar=True):
    dpg.add_text("Past Paper Viewer",pos=[70,0],color=(200, 142, 255))
    dpg.add_spacer(height=8)
    dpg.add_text("Made with love by Beebek", pos=[35,20])
    dpg.add_spacer(height=20)
    dpg.add_text('Version: 0.0.1') 
    dpg.add_spacer(height = 10)
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("about_id", show=False))
        dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("about_id", show=False))

'''
Main Window
'''
with dpg.window(tag='main window',no_resize=True,no_move=True,no_background=True):
  '''
  Menu Bar
  '''
  with dpg.menu_bar():
    with dpg.menu(label="File"):
      dpg.add_menu_item(label="Change default download location")
    
    with dpg.menu(label='Tools'):
      dpg.add_menu_item(label='Settings')
      dpg.add_menu_item(label='Help')
      dpg.add_menu_item(label='About', callback=lambda: dpg.configure_item("about_id", show=True))
      dpg.add_menu_item(label='Logger', callback=lambda: dpg.show_metrics())
      dpg.add_menu_item(label='Exit')
      dpg.add_menu_item(label='Style Editor', callback=lambda: dpg.show_style_editor())
      dpg.add_menu_item(label='Save Init file', callback=lambda: dpg.save_init_file('dpg.ini'))
  
  '''
  Search Box
  '''
  with dpg.group(label='Search_Box',horizontal=True):
    with dpg.child_window(tag='main_child_window',autosize_x=False,autosize_y=True,border=False):
      # with dpg.add_child_window(tag='search_box',autosize_x=False,autosize_y=True,border=False):
      #   dpg.add_text('Search',pos=[0,0])
      with dpg.child_window(autosize_x=False,autosize_y=True,delay_search=True):
        # dpg.add_input_text(hint="Search for a Paper", width = -1,on_enter=True)
        dpg.add_combo(['Subjects'])
        dpg.add_combo(['Year'])
        dpg.add_combo(['PaperVariant'])
        dpg.add_combo(['s','w','m'])
        dpg.add_combo(['sp','ms','qp','er','ir','gt'])



dpg.create_viewport(title='Custom Title', width=800, height=600)  
with dpg.font_registry():
  mono_lisa =dpg.add_font('fonts\MonoLisa\MonoLisa-Bold.ttf', 20)

dpg.bind_font(mono_lisa)

while dpg.is_dearpygui_running():
    jobs = dpg.get_callback_queue() # retrieves and clears queue
    dpg.run_callbacks(jobs)
    dpg.render_dearpygui_frame()

dpg.create_viewport(title='PyMangaDex', width=WIDTH, height=HEIGHT)
dpg.setup_dearpygui()
dpg.maximize_viewport()
dpg.set_primary_window('main window', True)
ctypes.windll.shcore.SetProcessDpiAwareness(2)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()