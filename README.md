# img_to_ASCII

Python function that turns any image to ASCII-art.

## Function defenition

img_to_ASCII(PATH:str, chars = [' ', '.','+','=', '#'], spacing = 10, scale = 0.1,background = (255,255,255),textcolor = (0,0,0), verbose = True, original_resolution = False, flip = True, sys_font_size = (6,6))

### Inputs

+ PATH (Str)- path to image that you want to convert
+ chars (list of Char) - ASCII characters that will represent colors
+ spacing (Int) - spasing berween chars in the final image, when in 'grayscale mode'
+ scale (Float) - final image scale (original_img_scale/final_img_scale) for HD images it's best to use 0.1 - 0.2
+ background (RGB triplet) - color of the final image's background 
+ textcolor (RGB triplet/ 'original') - color of the final image's text. If provided with RGB triplet, works in grayscale mode,  
+ if provided with keyword 'original' works in full color mode, preserving original image colors
+ verbose (True/False) - if True shows final image on screen
+ original_resolution (True/False)- if True final img will be in the same resolution as input image
+ flip (True/False)- if True flips the chars array
+ sys_font_size (touple of 2 Floats) - needed because in different systems default system font size differs (in windows (6,6), in ubuntu (13,6))i
 
### Outputs

+ PIL Image - containing final image
+ np.array of str32 - containing characters of final image

## Gallery

### Original colors 0.1 scale

'''
ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ','.','+','#','@'], spacing = 8, scale = 0.1,background = (255,255,255),textcolor = 'original', verbose = False, original_resolution = False, flip = True,sys_font_size = (13,6))
ascii_img.save("Results/original_colors_scale_0_1.jpg")
'''

![Original colors 0.1 scale]<Results/original_colors_scale_0_1.jpg>

_________

### Grayscale 0.1 scale

'''
ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ', '.', '-','+','#', '@'], spacing = 9, scale = 0.1,background = (255,255,255),textcolor = (0,0,0), verbose = True, original_resolution = False, flip = True, sys_font_size = (13,6))
ascii_img.save("Results/grayscale_scale_0_1.jpg")
'''

![Grayscale 0.1 scale]<Results/grayscale_scale_0_1.jpg>

_________

### Original colors 0.2 scale

'''
ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ','.','+','#','@'], spacing = 8, scale = 0.2,background = (255,255,255),textcolor = 'original', verbose = False, original_resolution = False, flip = True,sys_font_size = (13,6))
ascii_img.save("Results/original_colors_scale_0_2.jpg")
'''

![Original colors 0.2 scale]<Results/original_colors_scale_0_2.jpg>

_________

### Grayscale 0.2 scale

'''
ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ', '.', '-','+','#', '@'], spacing = 9, scale = 0.2,background = (255,255,255),textcolor = (0,0,0), verbose = True, original_resolution = False, flip = True, sys_font_size = (13,6))
ascii_img.save("Results/grayscale_scale_0_2.jpg")
'''

![Grayscale 0.1 scale]<Results/grayscale_scale_0_2.jpg>

_________

### Original colors 0.2 scale, black background

'''
ascii_img, chars = img_to_ASCII('Data/Penguins.jpg', chars = [' ','.','+','#','@'], spacing = 8, scale = 0.2,background = (0,0,0),textcolor = 'original', verbose = False, original_resolution = False, flip = True,sys_font_size = (13,6))
ascii_img.save("Results/original_colors_scale_0_2_blackBG.jpg")
'''

![Original colors 0.2 scale black BG]<Results/original_colors_scale_0_2_blackBG.jpg>

_________
