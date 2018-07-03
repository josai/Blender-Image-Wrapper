import bpy

def get_filename(path):
    '''
    Gets filename from full path.
    '''
    if '/' in path:
        return(path.replace('\\', ' ').split[-1])
    else:
        return (path)


def validate_path(path):
    '''
    Uses location of blend file for parent directory
    unless otherwise stated.
    '''
    current_dir = str(bpy.data.filepath)
    blend_name = current_dir.replace('\\', ' ').split()[-1]
    current_dir = current_dir.replace(blend_name, '')
    if 'C:\\' not in path:
        path = current_dir + path
    return (path)


def remove_all_images():
    '''
    WARNING: Removes all images from blend file.
    '''
    for img in bpy.data.images: 
      img.user_clear() 
    for img in bpy.data.images: 
      if not img.users: 
        bpy.data.images.remove(img)


class Burrito(object):
    '''
    Wraps the greasy and meaty blender image api into
    something more light weight and easier to consume.
    '''
    def __init__(self, filename='', size=[1, 1], name="NewImage"):
        '''
        If file name is empty/default create a new image.
        '''
        if filename == '':
            self.name = name
            self.img_obj = bpy.data.images.new(self.name, size[0], size[1])
        else:
            path = validate_path(filename)
            self.img_obj = bpy.data.images.load(path)
            self.name = get_filename(filename)

        self.pixels = self.img_obj.pixels[:]
        self.file_type = 'PNG'
        print (self.pixels)

    def update_info(self):
        '''
        Updates relavant info in the blender image object.
        Only needed for saving.
        '''
        self.img_obj.name = self.name
        self.img_obj.pixels[:] = self.pixels
        self.img_obj.file_format = self.file_type

    def save(self, path='burritos\\'):
        self.update_info()
        file_type = '.' + self.file_type.lower()
        path = validate_path(path + self.img_obj.name)
        self.img_obj.filepath_raw = path + file_type
        self.img_obj.save()
