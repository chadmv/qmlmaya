"""qmlmaya contains a QMainWindow class that can be used to display QML-based UIs
inside Maya.
"""

import logging
import os
from six import string_types

from PySide2.QtQuick import QQuickView
from PySide2.QtCore import Qt, QUrl
from PySide2.QtWidgets import QWidget, QMainWindow

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin


class QuickWindow(MayaQWidgetBaseMixin, QMainWindow):
    """A window that can be used to display a QML UI in Maya."""

    def __init__(self, url=None, *args, **kwargs):
        super(QuickWindow, self).__init__(*args, **kwargs)
        self.view = QQuickView()
        self.view.statusChanged.connect(self.onStatusChanged)
        self.widget = None
        if url:
            self.setSource(url)
        self.setFocusPolicy(Qt.NoFocus)

    def setContextProperty(self, name, value):
        """Set a context property on the window.

        Context properties are used to handle the interop between QML and Python

        :param name: Name of the property
        :param value: Instance of the property object
        """
        self.view.engine().rootContext().setContextProperty(name, value)

    def addImportPath(self, path):
        """Add a new module import path to the window engine."""
        self.view.engine().addImportPath(path)

    def setSource(self, url):
        if isinstance(url, string_types):
            url = QUrl.fromLocalFile(os.path.abspath(url))
        self.view.setSource(url)
        size = self.view.size()
        self.widget = QWidget.createWindowContainer(self.view, self)
        self.setCentralWidget(self.widget)
        self.setFocusProxy(self.widget)
        self.resize(size)

    def onStatusChanged(self, status):
        if status == QQuickView.Error:
            errors = self.view.errors()
            for error in errors:
                logging.critical(error)

