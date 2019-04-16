# python-image-complete
Python 3 library for checking whether an image is complete or not (looking for EOF markers).

## Supported image formats

* GIF (extension: .gif)
* JPG (extension: .jpg, .jpeg)
* PNG (extension: .png)

## EOF marker specifications

* GIF

  * https://en.wikipedia.org/wiki/GIF#File_format

* JPG

  * http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

* PNG

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
