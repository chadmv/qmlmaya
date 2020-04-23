# qmlmaya
qmlmaya contains a QMainWindow class that can be used to display QML-based UIs inside Maya.

QML examples are also included.

Maya does not ship with the QML modules found in default Qt installations. This repo contains the
modules and the Maya module makes it easy to use them.

# Requirements
Currently only Maya 2020 on Windows is supported.

# Installation Instructions
qmlmaya is Maya module that can be installed like all other Maya modules.  You can do one of the following:

* Add the qmlmaya root directory to the MAYA_MODULE_PATH environment variable.
* Add the qmlmaya root directory to the MAYA_MODULE_PATH in your Maya.env.  e.g.  MAYA_MODULE_PATH += /path/to/qmlmaya
* Edit the qmlmaya.mod file, and replace the ./ with the full path to the qmlmaya root directory, then copy the qmlmaya.mod file to where your modules are loaded from.

# Running the Examples
If you don't need the examples, you can delete the scripts/qmlmaya_examples directory

```
import qmlmaya_examples.quickcontrols2.flatstyle as flatstyle
flatstyle.show()

import qmlmaya_examples.quickcontrols2.gallery as gallery
gallery.show()
```
