# download_images
  here is the Python code that you can use to download all the images on a specific website and rename them


This code will first download all the images from the specified website. Then, it will rename the downloaded images by checking if the name of the file starts with zero. If it does, the zero will be removed. Otherwise, the first 13 numbers of the file name will be kept, and everything else will be removed. If there are more than one image with the same number, the next images will be renamed with the number followed by a _1, _2, and so forth.

To run this code, you will need to install the requests and re modules. You can do this by running the following command in your terminal:

```
pip install requests re
```

Once you have installed the modules, you can run the code by saving it as a Python file and then running it from the command line.  you would run it by typing the following command into your terminal:

```
python download_images.py
```

This will download all the images from the specified website and rename them according to the specified criteria.
