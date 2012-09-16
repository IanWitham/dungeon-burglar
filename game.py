import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)

libtcod.sys_set_fps(LIMIT_FPS)

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_background(0, libtcod.white)
    libtcod.console_print(0, 1, 1, '@')
    libtcod.console_flush()

