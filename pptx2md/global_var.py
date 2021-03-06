class global_var(object):
    def __init__(self):
        pass
    # utilities
    def path_name_ext(self, path, name, ext):
        return path + '/' + name + '.' + ext


g = global_var()

# configs
# image output dir
g.img_path = 'img'
# maximum image width
g.max_img_width = 500
# weather use predefined TOC in titles.txt
g.use_custom_title = False
# output path & filename
g.out_path = 'out.md'
# text frame thar contain more characters than this will be transferred 
g.text_block_threshold = 15
# disable image extraction
g.disable_image = False


# global variables
g.titles = {}
g.file_prefix = '1'

g.last_title = {}
g.max_custom_title = 1

