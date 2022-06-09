import dearpygui.dearpygui as dpg

WIDTH = 600
HEIGHT = 500

dpg.create_context()


def print_me(sender, app_data, user_data):
    print(user_data)


with dpg.window(tag='main', label='Hello'):
    with dpg.viewport_menu_bar(tag='menu') as viewport_menu:
        with dpg.menu(label='File') as file_tab:
            dpg.add_menu_item(label='Open', callback=lambda: dpg.show_item('open_file'))
            dpg.add_menu_item(label='Save', callback=print_me, user_data='Save')
            dpg.add_menu_item(label='Save As', callback=print_me, user_data='Save As')
            with dpg.menu(label='Settings') as settings_tab:
                dpg.add_menu_item(label='Settings 1', callback=print_me, user_data='Settings 1')
                dpg.add_menu_item(label='Settings 2', callback=print_me, user_data='Settings 2')
        dpg.add_menu_item(label='Help', callback=print_me, user_data='Help')
        with dpg.menu(label='Edit'):
            dpg.add_checkbox(label='Copy', callback=print_me, user_data='Copy')
            dpg.add_button(label='Cut', callback=print_me, user_data='Cut')
            dpg.add_checkbox(label='Paste', callback=print_me, user_data='Paste')
    with dpg.child_window():
        dpg.add_text('Hello World')
        dpg.add_text(tag='file_content', show=True, label='Content')


dpg.create_viewport(title='Notepad', width=WIDTH, height=HEIGHT)
dpg.set_primary_window('main', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()