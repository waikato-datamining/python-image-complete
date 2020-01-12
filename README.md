# python-image-complete
Python 3 library for checking whether an image is complete or not. 
It is either looking for EOF markers or checking the length of the file against one stored in file.

## Supported image formats

* BMP (extension: .bmp)
* GIF (extension: .gif)
* JPG (extension: .jpg, .jpeg)
* PNG (extension: .png)

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
  
  
## Examples

* auto detection

  ```python
  from image_complete.auto import is_image_complete

  print(is_image_complete("/some/where/hello_world.jpg"))
  print(is_image_complete("/some/where/image.png"))
  ```

* JPG specific

  ```python
  from image_complete.jpg import is_jpg_complete

  print(is_jpg_complete("/some/where/hello_world.jpg"))
  ```
