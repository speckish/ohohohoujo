define cgs = [{'name': "School is now in session",
               'image': "cg_1"},
              {'name': "A rivalry begins!",
               'image': "cg_2"},
              {'name': "I-it's not like I like her...",
               'image': "cg_3"},
              {'name': "A prayer to St. Sapphica",
               'image': "cg_4"},
              {'name': "The price comes riding in?!",
               'image': "cg_6"},
              {'name': "An answer to my prayers!",
               'image': "cg_6"},
              {'name': "That's not how you play basketball!",
               'image': "cg_7"},
              {'name': "Vaping in the Greenhouse",
               'image': "cg_8"}]

define tracks = [{'name': 'The Superiority',
                  'track': "audio/The Superiority_looped.mp3"},
                 {'name': 'Unbreakable',
                  'track': "audio/1. Unbreakable.mp3"},
                 {'name': 'Abstract Vision',
                  'track': "audio/Abstract Vision #3 (Looped).mp3"},
                 {'name': 'Hidden Threat',
                  'track': "audio/Hidden Threat_looped.mp3"},
                 {'name': 'Lift Me Up',
                  'track': "audio/Lift Me Up.mp3"},
                 {'name': 'Magic Within',
                  'track': "audio/Magic Within.mp3"},
                 {'name': 'Mystical Loop',
                  'track': "audio/Mystical  Loop #1.mp3"},
                 {'name': 'Soft Relaxation',
                  'track': "audio/Soft Relaxing Track (looped).mp3 "}]

init -10 python:
    import math
    class Paginator(object):
        def __init__(self, items, page_size=6, page=0):
            self.items = items
            self.page_size = page_size
            self.page = page
            self.last = math.ceil(len(items)/page_size)
            if len(items) % page_size == 0:
                self.last -= 1
        def get_items(self):
            i = self.page*self.page_size
            return self.items[i:i+self.page_size]
        def get_by_item(self, item):
            i = self.items.index(item)
            p = i//self.page_size
            return Paginator(self.items, self.page_size, p)
        def has_prev(self):
            if self.page > 0:
                return True
            else:
                return False
        def prev(self):
            if self.page > 0:
                return Paginator(self.items, self.page_size, self.page-1)
            else:
                return self
        def has_next(self):
            if self.page < self.last:
                return True
            else:
                return False
        def next(self):
            if self.page < self.last:
                return Paginator(self.items, self.page_size, self.page+1)
            else:
                return self

screen gallery():
    tag menu
    default paginator = Paginator(cgs)
    use game_menu(_("gallery")):
        frame:
            xysize (1.0, 1.0)
            background None
            vbox:
                align (0.5, 0.5)
                grid 3 2 spacing 20:
                    style_prefix "gallery_button"
                    for i in range(6):
                        if i < len(paginator.get_items()):
                            $ cg = paginator.get_items()[i]
                            button ysize 200:
                                if renpy.seen_image(cg['image']):
                                    action Show("cg_large", cg=cg['image'])
                                vbox spacing 5:
                                    if renpy.seen_image(cg['image']):
                                        add cg['image'] at gallery_thumbnail
                                        text cg['name']
                                    else:
                                        add "cg_locked" at gallery_thumbnail
                                        text "Locked"
                        else:
                            null width 128*2 height 72*2
    if paginator.has_prev():
        textbutton "Prev":
            action SetScreenVariable('paginator', paginator.prev()) align (0.10, 0.5)
    if paginator.has_next():
        textbutton "Next":
            action SetScreenVariable('paginator', paginator.next()) align (0.90, 0.5)


transform gallery_thumbnail:
    size (128*2, 72*2)

transform cg_fade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        linear 0.5 alpha 0.0

screen cg_large(cg):
    modal True
    imagebutton idle cg at cg_fade:
        action Hide("cg_large")

screen music_box():
    tag menu
    default paginator = Paginator(tracks)
    use game_menu(_("music box")):
        frame:
            xysize (1.0, 1.0)
            background None
            vbox:
                align (0.5, 0.5)
                grid 2 3:
                    spacing 50
                    for i in range(6):
                        if i < len(paginator.get_items()):
                            $ track = paginator.get_items()[i]
                            if renpy.seen_audio(track['track']):
                                textbutton track['name']:
                                    action Play('music', track['track'], selected=True)
                            else:
                                textbutton "Locked"
                        else:
                            null

    if paginator.has_prev():
        textbutton "Prev":
            action SetScreenVariable('paginator', paginator.prev()) align (0.10, 0.5)
    if paginator.has_next():
        textbutton "Next":
            action SetScreenVariable('paginator', paginator.next()) align (0.90, 0.5)
