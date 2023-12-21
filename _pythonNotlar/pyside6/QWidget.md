

### Composite Widgets

Birleşik widget olarak bilinir . Eğer bir widget bir dizi alt widget gruplandırmak için kapsayıcı olarak kullanılmışsa ***compoesite widget*** olarak adlandırılır


ÖR:

```python
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout  , QLabel

class MyCompositeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.button = QPushButton('Click me!')
        self.label = QLabel('Hello, World!')

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText('Button clicked!')

# Kullanım
if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    widget = MyCompositeWidget()
    widget.show()
    app.exec()

```



QWidget, QPaintDevice sınıfının bir alt sınıfı olduğundan, alt sınıflar, QPainter sınıfının bir örneğiyle bir dizi boyama işlemi kullanılarak oluşturulan özel içeriği görüntülemek için kullanılabilir



fonksiyonu, bir widget'ın boyut politikasını belirlemek için kullanılır. Boyut politikası, bir widget'ın bir düzen içinde nasıl genişleyeceği veya daralacağına dair kuralları belirtir. Bu, bir widget'ın bir konteyner içinde nasıl yerleştirileceğini ve boyutlandırılacağını kontrol etmenize olanak tanır. fonksiyonu genellikle iki argüman alır: yatay (horizontal) ve dikey (vertical) boyut politikaları

```python
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout , QSizePolicy

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        button = QPushButton('Click me!')
        layout = QVBoxLayout(self)
        layout.addWidget(button)

        # Yatayda genişlemeyi ve dikeyde sabit boyutu ayarla
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()

```


detaylar için kaynak kod dan ``PySide6.QtWidgets.QSizePolicy`` ye git **Policy** sınıfını kullanabilirsin




### [EVENT SİSTEMİ](https://doc.qt.io/qtforpython-6/overviews/eventsandfilters.html#sending-events)



## Font Değiştirmek

`` PySide6.QtWidgets.QWidget.font`` 

özel bir yazı tipini ve bir widget'in adını setFont() fonksiyonu ile  widget'lar için varsayılan yazı tiplerini kendiniz de tanımlayabilirsiniz.

[KALDIM](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.focus)



