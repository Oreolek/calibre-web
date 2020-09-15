# -*- coding: utf-8 -*-

import sys
import os
sys.path.append("..")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendor'))
from modules import epub
use_epub_meta = True

meta = epub.get_epub_info('./input.epub', 'imported.epub', 'epub')
print(meta)
