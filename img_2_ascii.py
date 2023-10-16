
from PIL import Image, ImageDraw
import numpy as np
import re

def img_to_ASCII(PATH = '', chars = [' ', '.','+','=', '#'], spacing = 10, scale = 0.1,background = (255,255,255),textcolor = (0,0,0), verbose = True, original_resolution = False, flip = True, sys_font_size = (6,6),IMAGE = None): 
    # converts image to provided chars and outputs them as PIL image
    
    # flip char array if needed
    if flip:
        chars = np.flip(chars)
    
    chars = np.array(chars)

    if IMAGE is None:
        img = Image.open(PATH)
    else:
        img = IMAGE

    h,l = img.size
    img = img.resize((np.array((h,l))*scale).astype(np.uint64))
    img = np.array(img) 
    
    # convert colors to 0 to 1 grayscale
    # img_g = np.mean(img, axis=2)
    img_g = np.mean(img, axis=2)/255
    
    # convert colors to indexes in chars array
    # coords = (img_g//(255/len(chars))).astype(np.uint64)
    coords = (img_g * (len(chars) - 1) + 0.5).astype(np.uint64)
    
    #convert index array to str array made from chars
    coords = chars[coords]
    

    
    
    # needed bc. ImageDraw.text doesn't work with np.array(str)
    if textcolor == 'original':    
        L,H = spacing*np.array((coords.shape))
        n_img = Image.new('RGB', (H,L),background)
        d = ImageDraw.Draw(n_img)
        
        # for every pixel
        for row in range(coords.shape[0]):    
            for column in range(coords.shape[1]):
                # draw text
                d.text((column*spacing, row*spacing),str(coords[row,column]),fill = tuple(img[row,column,:]))
    else:
        # doublle each column to match char width
        new_coords = np.empty((coords.shape[0],2*coords.shape[1])).astype(str)
        new_coords[:,0::2] = coords
        new_coords[:,1::2] = coords
        coords = new_coords
        
        H,L = np.array((coords.shape))*sys_font_size
        n_img = Image.new('RGB', (L,H),background)
        d = ImageDraw.Draw(n_img)
        
        # conversion from array of str to big str
        N=coords.astype('|S1').tobytes().decode('UTF8)')
        # insert newline chars every image width pixels
        N= re.sub("(.{"+f"{coords.shape[1]}"+"})", "\\1\n", N, 0, re.DOTALL)
        
        # draw text
        d.text((0,0),N,fill = (0,0,0), spacing = 2.5)
        # for row in range(coords.shape[0]):    
        #     for column in range(coords.shape[1]):
        #         d.text((column*spacing, row*spacing),str(coords[row,column]),fill = textcolor)

    
    
    # resize image to original resolution if needed
    if original_resolution:    
        n_img = n_img.resize((h,l))

    # show on screen if needed
    if verbose:    
        n_img.show()

    return n_img, coords

# ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ','.','+','#','@'], spacing = 8, scale = 0.1,background = (255,255,255),textcolor = 'original', verbose = False, original_resolution = False, flip = True,sys_font_size = (13,6))
# ascii_img.save("Results/original_colors_scale_0_1.jpg")
# 
# ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ', '.', '-','+','#', '@'], spacing = 9, scale = 0.1,background = (255,255,255),textcolor = (0,0,0), verbose = True, original_resolution = False, flip = True, sys_font_size = (13,6))
# ascii_img.save("Results/grayscale_scale_0_1.jpg")
# 
# ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ','.','+','#','@'], spacing = 8, scale = 0.2,background = (255,255,255),textcolor = 'original', verbose = False, original_resolution = False, flip = True,sys_font_size = (13,6))
# ascii_img.save("Results/original_colors_scale_0_2.jpg")
# 
# ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ', '.', '-','+','#', '@'], spacing = 9, scale = 0.2,background = (255,255,255),textcolor = (0,0,0), verbose = True, original_resolution = False, flip = True, sys_font_size = (13,6))
# ascii_img.save("Results/grayscale_scale_0_2.jpg")
# 
# ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ','.','+','#','@'], spacing = 8, scale = 0.2,background = (0,0,0),textcolor = 'original', verbose = False, original_resolution = False, flip = True,sys_font_size = (13,6))
# ascii_img.save("Results/original_colors_scale_0_2_blackBG.jpg")


