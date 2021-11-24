import os
import re
import sys
import traceback
import collections
import shutil

pagedir = r"C:\Users\froze\OneDrive\Documents\Python\Websites\KGA\output\pages"
basedir = r"C:\Users\froze\OneDrive\Documents\Python\Websites\KGA"
outputdir = r"C:\Users\froze\OneDrive\Documents\Python\Websites\KGA\output"

for root, dirs, files in os.walk(pagedir):
    for filename in dirs:
        if filename == 'index.html':
            old_name = os.path.join( os.path.abspath(root), filename )
            base, extension = os.path.splitext(filename)
            new_name = os.path.join(basedir, base, dirs)

            shutil.copy(old_name, new_name)

homepage = outputdir + '\index.html'
githubhomepage = basedir + '\index.html'
shutil.copy(homepage, githubhomepage)