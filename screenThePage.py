import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QUrl, QTimer, QCoreApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class Screenshot(QWebEngineView):

    def capture(self, url, output_file):
        self.output_file = output_file
        self.load(QUrl(url))
        self.loadFinished.connect(self.on_loaded)
        # Create hidden view without scrollbars
        self.setAttribute(Qt.WA_DontShowOnScreen)
        self.page().settings().setAttribute(
            QWebEngineSettings.ShowScrollBars, False)
        self.show()

    def on_loaded(self):
        size = self.page().contentsSize().toSize()
        self.resize(size)
        # Wait for resize
        QTimer.singleShot(1000, self.take_screenshot)

    def take_screenshot(self):
        self.grab().save(self.output_file, b'PNG')
        self.app.quit()


# s.capture('https://pypi.org/project/PyQt5/', 'webpage.png')
# 'https://pypi.org/project/PyQt5/'
# 'webpage.png'
def screenThePage(pageUrl, savePath):
    app = QApplication()
    s = Screenshot()
    s.app = app
    s.capture(pageUrl, savePath)
    sys.exit(app.exec_())


if __name__ == '__main__':
    pageUrl = "https://www.avito.ru/saratov/kvartiry/1-k_kvartira_34_m_89_et._1989595079"
    savePath = 'imgs/webpage'
    ext = '.png'

    screenThePage(pageUrl, savePath + ext)
