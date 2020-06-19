"""FolderMaker Project Templating App"""
import sys
from PySide2.QtWidgets import \
    QFileSystemModel, QLabel,\
    QTreeView, QLineEdit,\
    QVBoxLayout, QGridLayout,\
    QPushButton, QWidget,\
    QApplication, QMessageBox
from lib.lib import conf_to_starr, split_types, create_dirs

ROOT_PATH = r'/home/kozova1/FolderMaker/test'
CONF_FILE = r'lib/conf.cf'
CONF = split_types(conf_to_starr(CONF_FILE))

class App(QWidget):
    '''The FolderMaker base class'''
    def __init__(self):
        super().__init__()
        self.title = 'FolderMaker'
        self.init_ui()

    def on_btn(self):
        '''Creates buttons on click'''
        basedir = ROOT_PATH
        try:
            create_dirs(CONF, basedir, range(int(self.start_box.text()), int(self.stop_box.text())))
        except ValueError:
            msg = QMessageBox()
            msg.setText('Error! Invalid numbers in text boxes!')
            msg.exec()
        except FileExistsError as file_ex:
            msg = QMessageBox()
            msg.setText(f'Error! Directory already exists! Exception: {str(file_ex)}')
            msg.exec()

    def init_ui(self):
        '''Initializes the UI'''
        self.setWindowTitle(self.title)
        self.model = QFileSystemModel()
        self.model.setRootPath(ROOT_PATH)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(ROOT_PATH))
        self.start_box = QLineEdit()
        self.stop_box = QLineEdit()
        self.make_btn = QPushButton("Create Project Folders")
        self.make_btn.clicked.connect(self.on_btn)
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        subgrid = QGridLayout()
        subgrid.addWidget(self.start_box, 0, 1)
        subgrid.addWidget(self.stop_box, 1, 1)
        subgrid.addWidget(QLabel('From (inc.): '), 0, 0)
        subgrid.addWidget(QLabel('To (not inc.): '), 1, 0)
        layout.addLayout(subgrid)
        layout.addWidget(self.make_btn)
        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
