import bpy

def get_filename(path):
    if '/' in path:
        return(path.replace('\\', ' ').split[-1])
    else:
        return (path)


def validate_path(path):
    current_dir = str(bpy.data.filepath)
    blend_name = current_dir.replace('\\', ' ').split()[-1]
    current_dir = current_dir.replace(blend_name, '')
    if 'C:\\' not in path:
        path = current_dir + path
    return (path)


class ImageWrapper(object):
    """docstring for ImageWrapper"""
    def __init__(self, filename='', size=[1, 1]):
        '''
        If file name is empty/default create a new image.
        '''
        if filename == '':
            self.name = "NewImage"
            self.img_obj = bpy.data.images.new(self.name, size[0], size[1])
            self.pixels = self.img_obj.pixels[:]
        else:
            path = validate_path(filename)
            self.img_obj = bpy.data.images.load(path)
            self.name = get_filename(filename)
            self.pixels = self.img_obj.pixels[:]
            
        print (self.pixels)


img = ImageWrapper(filename='ground_truth\\0003.png')

