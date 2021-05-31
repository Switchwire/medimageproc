from io import BytesIO
from IPython.display import Image
import matplotlib as mpl


def numpy_array_2_image(arr):
    if arr.ndim == 2:
        img_format, cmap = 'png', mpl.cm.gray
    elif arr.ndim == 3:
        img_format, cmap = 'jpg', None
    else:
        raise ValueError("Only 2- or 3-d arrays can be displayed as images.")
    with BytesIO() as buffer:
        mpl.image.imsave(buffer, arr, format=img_format, cmap=cmap, vmin=0, vmax=255)
        out = buffer.getvalue()
    return Image(out)
