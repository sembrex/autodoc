# AUTODOC v1.2 #

Autodoc is GUI application for making photos documentation folder by folder in .docx file automatically.

## Application Workflow ##

* User selects source directory
* Counting subdirectories and finding image files (jpg, jpeg, png)
* User selects target file to save result
* User starts the process
* Creating abstract .docx document
* Selecting root directory (#1)
* Finding image files
* #### If found,
* add heading to the document and use current directory name as its text
* then add table to the document with 1 row and 2 columns
* then start resizing every image and adding it to the cell
* adding new row after every 2 images and adding page break after every 6 images
* #### If not found,
* try finding subdirectories then process it like #1
* if no subdirectory found, end file process
* Trying to save document to the target file
* If the target file is not writeable, show error message
* Done !
* Logging every step above

## How to use ? ##

### Requirements ###

* Python 2.7
* PyQt4
* python-docx
* PIL
* PyInstaller (Only for making executable file. For windows users, use latest development version)

### Running ###

* Run this from terminal or cmd
```
cd path_to_autodoc

python dokumentasi.py
```

### Making Executable ###

* Run this from terminal or cmd
```
cd path_to_autodoc

pyinstaller -F -w -i folder.ico dokumentasi.py
```
* Executable created but there is an error
* Edit dokumentasi.spec
* (Linux\Mac) Change ``` datas=[] ``` to ``` datas=[('templates', 'docx/templates')] ```
* (Windows) Change ``` datas=[] ``` to ``` datas=[('templates', 'docx\\templates')] ```
* Run this
```
pyinstaller -F -w -i folder.ico dokumentasi.spec
```
* Executable created and ready to use

## References ##

* [Python 2.7](https://docs.python.org/2/)
* [PyQt4](http://pyqt.sourceforge.net/Docs/PyQt4/index.html)
* [python-docx](https://python-docx.readthedocs.io/en/latest/)
* [Pillow](https://python-pillow.org/)
* [PyInstaller](http://www.pyinstaller.org/)

## Contact ##

* [hanreev@gmail.com](mailto:hanreev@gmail.com)

## Changelog ##

#### v1.2 ###

* Add title prefix option
* Add margins option
* Add title to every page
* Changing cursor shape when processing

#### v1.1 ###

* SKIPPED
* Fix application icon
* Fix margins

#### v1.0 ###

* First release
* Create .docx document
* Find available pictures in source directory and its subdirectories
* Add heading to the document using directory name
* Optimalize pictures
* Add pictures to the document
* Save the document
* Logging all actions
