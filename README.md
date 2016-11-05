# AUTODOC #

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

pyinstaller -F -w -i icon.app dokumentasi.py
```
* Executable created but there is an error
* Edit dokumentasi.spec
* (Linux\Mac) Change ``` datas=[] ``` to ``` datas=[('templates', 'docx/templates')] ```
* (Windows) Change ``` datas=[] ``` to ``` datas=[('templates', 'docx\\templates')] ```
* Run this
```
pyinstaller -F -w -i icon.app dokumentasi.spec
```
* Executable created and ready to use

### Contact ###

* [hanreev@gmail.com](mailto:hanreev@gmail.com)