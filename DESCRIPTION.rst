The **python-image-complete** package allows you to check for various
image types to check whether the image is complete or not. For doing
this, it looks for EOF (end of file) markers in the files or compares
the stored file length against the actual file length.

Can also operate on bytes or BytesIO objects.

By default, the library operates in **strict** mode, i.e., no trailing junk data
is tolerated. However, by supplying the parameters `strict` and `check_size` this
can turned into **lenient** mode. The parameter `check_size` (i.e., the number of
bytes to read from the end of the file) is only used for formats gif, jpg, png.

Supported file formats:

* BMP (extension: .bmp)
* GIF (extension: .gif)
* JPG (extension: .jpg, .jpeg)
* PNG (extension: .png)
* WebP (extension: .webp)

