# python-image-complete

Python 3 library for checking whether an image is complete or not. 
It is either looking for EOF markers or checking the length of the file against one stored in the file.

Can also operate on bytes or BytesIO objects. 

By default, the library operates in **strict** mode, i.e., no trailing junk data 
is tolerated. However, by supplying the parameters `strict` and `check_size` this
can turned into **lenient** mode. `check_size` is only used for formats gif, jpg, png.


## Supported image formats

* BMP (extension: .bmp)
* GIF (extension: .gif)
* JPG (extension: .jpg, .jpeg)
* PNG (extension: .png)
* WebP (extension: .webp)


## File structures

* BMP (checks file length)

  * https://en.wikipedia.org/wiki/BMP_file_format#File_structure

* GIF (checks EOF marker)

  * https://en.wikipedia.org/wiki/GIF#File_format

* JPG (checks EOF marker)

  * http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

* PNG (checks EOF marker)

  * https://en.wikipedia.org/wiki/Portable_Network_Graphics#Critical_chunks
  * http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html#Chunk-layout
  * http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html#C.IEND

* WebP (compares data length after RIFF header with file length)

  * https://developers.google.com/speed/webp/docs/riff_container

  
## Examples

### Auto detection

```python
from image_complete.auto import is_image_complete

# using file names
print(is_image_complete("/some/where/hello_world.jpg"))
print(is_image_complete("/some/where/image.png"))

# using bytes or BytesIO
with open("/some/where/image.bmp", "rb") as fp:
    b = fp.read()
print(is_image_complete(b))
```


### JPG specific

```python
from image_complete.jpg import is_jpg_complete, is_jpg

f = "/some/where/hello_world.jpg"
if is_jpg(f):
    print(is_jpg_complete(f))
else:
    print("Not a JPG!")
```


### Lenient mode (i.e., tolerating trailing junk data)

```python
from image_complete.auto import is_image_complete

# using file names
print(is_image_complete("/some/where/hello_world.jpg", strict=False, check_size=100))
print(is_image_complete("/some/where/image.png", strict=False, check_size=100))

# using bytes or BytesIO
with open("/some/where/image.bmp", "rb") as fp:
    b = fp.read()
print(is_image_complete(b, strict=False))
```
