#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os.path

from PyQt6 import QtCore, QtGui
import sys
from PyQt6.QtCore import QEventLoop, QTimer, QSettings, QTranslator
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QFontDialog, QColorDialog

import backend
from backend import Ui_Form


class ControlBoard(QMainWindow, Ui_Form):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setupUi(self)
        # set General
        self.trans = QTranslator(self)
        self.comboBox_displayLanguage.currentIndexChanged.connect(self.index_changed)
        self.comboBox_displayLanguage.setCurrentIndex(settings.value('General/language', type=int))
        self.checkBox.stateChanged.connect(self.check_state_run_on_system_startup)
        self.checkBox.setChecked(settings.value('General/run_on_system_startup', type=bool))
        self.checkBox_2.stateChanged.connect(self.check_state_auto_backup)
        self.checkBox_2.setChecked(settings.value('General/auto_backup', type=bool))
        self.checkBox_3.stateChanged.connect(self.check_state_tray_menu)
        self.checkBox_3.setChecked(settings.value('General/tray_menu', type=bool))
        self.lineEdit_filePath.setText(settings.value('General/config', type=str))
        self.pushButton_openFolder.clicked.connect(self.open_ini_folder)
        self.pushButton_openFile.clicked.connect(self.open_ini_file)
        self.pushButton_alterFile.clicked.connect(self.alter_ini_file)
        self.pushButton_restoreDefault1.clicked.connect(self.general_restore_default)
        # set Form
        self.pushButton_interfaceFont.setText(QFont(settings.value('General/font')).family() + ', ' + str(QFont(settings.value('General/font')).pointSize()))
        self.pushButton_interfaceFont.setFont(settings.value('General/font'))
        self.pushButton_interfaceFont.clicked.connect(self.change_interface_font)
        self.pushButton_themeColor.setText('自定义')
        self.pushButton_themeColor.clicked.connect(self.change_theme_color)
        self.pushButton_restoreDefault2.clicked.connect(self.form_restore_default)
        # set Setup
        # set About

    def check_state_run_on_system_startup(self):
        if self.checkBox.checkState() == QtCore.Qt.CheckState.Unchecked:
            settings.setValue('General/run_on_system_startup', False)
        if self.checkBox.checkState() == QtCore.Qt.CheckState.Checked:
            settings.setValue('General/run_on_system_startup', True)

    def check_state_auto_backup(self):
        if self.checkBox_2.checkState() == QtCore.Qt.CheckState.Unchecked:
            settings.setValue('General/auto_backup', False)
        if self.checkBox_2.checkState() == QtCore.Qt.CheckState.Checked:
            settings.setValue('General/auto_backup', True)

    def check_state_tray_menu(self):
        if self.checkBox_3.checkState() == QtCore.Qt.CheckState.Unchecked:
            settings.setValue('General/tray_menu', False)
        if self.checkBox_3.checkState() == QtCore.Qt.CheckState.Checked:
            settings.setValue('General/tray_menu', True)

    def index_changed(self):
        if self.comboBox_displayLanguage.currentIndex() == 0:
            self.trans.load('en_US')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.retranslateUi(self)
            settings.setValue('General/language', self.comboBox_displayLanguage.currentIndex())
        elif self.comboBox_displayLanguage.currentIndex() == 1:
            self.trans.load('zh_CN')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.retranslateUi(self)
            settings.setValue('General/language', self.comboBox_displayLanguage.currentIndex())
        else:
            print(self.comboBox_displayLanguage.currentIndex())

    def open_ini_folder(self):
        file_path = self.lineEdit_filePath.text()
        file_realpath = os.path.realpath(file_path)
        os.system(f'explorer /select, {file_realpath}')
        print(file_realpath)

    def open_ini_file(self):
        print(self.lineEdit_filePath.text())
        os.system(f'notepad {self.lineEdit_filePath.text()}')
        print('open ini file')

    def alter_ini_file(self):
        result = QMessageBox.question(self, "是否更换配置文件", "确定更换配置文件",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
        print(result)
        if result == QMessageBox.StandardButton.Yes:
            new_ini_file_name, new_ini_file_type = QFileDialog.getOpenFileName(self, 'Open File', self.lineEdit_filePath.text(), '*.ini')
            print('alter ini file')
            print(new_ini_file_name)
            settings.setValue('General/config', new_ini_file_name.split('/')[-1])

    def general_restore_default(self):
        self.comboBox_displayLanguage.setCurrentIndex(0)
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.lineEdit_filePath.setText('backend_config.ini')
        print('default restore default')

    def form_restore_default(self):
        self.comboBox_displayLanguage.setCurrentIndex(0)
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.lineEdit_filePath.setText('backend_config.ini')
        print('form restore default')

    def change_interface_font(self):
        """font = QFont()
        font.setFamily(self.pushButton_interfaceFont.text())
        font.setPointSize(9)"""
        # font = self.pushButton_interfaceFont.font()
        form_font = QFontDialog(self.pushButton_interfaceFont.font(), self)

        # form_font.getFont()
        # print(form_font.selectedFont().family())
        if form_font.exec():
            self.pushButton_interfaceFont.setText(form_font.selectedFont().family() + ', ' + str(form_font.selectedFont().pointSize()))
            self.pushButton_interfaceFont.resize(50 + len(form_font.selectedFont().family())*5, 25)
            self.pushButton_interfaceFont.setFont(QFont(form_font.selectedFont()))
            settings.setValue('General/font', form_font.selectedFont())
            # settings.setValue('/General/ziti', form_font.selectedFont().toString())
            # print(form_font.selectedFont().toString())

    def change_theme_color(self):
        theme_color = QColorDialog(self)
        # font.getFont()
        if theme_color.exec():
            # self.pushButton_themeColor.setIcon(theme_color.selectedColor().name())
            print(theme_color.selectedColor().name())
            print(theme_color.currentColor().name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    settings = QSettings('backend_config.ini', QSettings.Format.IniFormat)
    win = ControlBoard()
    win.show()
    sys.exit(app.exec())
