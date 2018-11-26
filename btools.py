from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from calculators import BrewingCalculators

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.createWeightedWort()
        self.brew_calc = BrewingCalculators()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.weighted_wort, 1, 0)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)



    def createWeightedWort(self):
        self.weighted_wort = QGroupBox("Weighted Wort")
        value_width = 75

        wort1_label = QLabel("Wort 1:")
        wort1_volume_label = QLabel("Volume")
        wort1_gravity_label = QLabel("Gravity")
        wort1_volume_value = QDoubleSpinBox(self.weighted_wort)
        wort1_volume_value.valueChanged.connect(lambda: update_weighted_wort())
        wort1_volume_value.setDecimals(2)
        wort1_volume_value.setFixedWidth(value_width)

        wort1_gravity_value = QDoubleSpinBox(self.weighted_wort)
        wort1_gravity_value.setDecimals(3)
        wort1_gravity_value.setFixedWidth(value_width)
        wort1_gravity_value.valueChanged.connect(lambda: update_weighted_wort())

        wort2_label = QLabel("Wort 2:")
        wort2_volume_label = QLabel("Volume")
        wort2_gravity_label = QLabel("Gravity")
        wort2_volume_value = QDoubleSpinBox(self.weighted_wort)
        wort2_volume_value.setDecimals(2)
        wort2_volume_value.setFixedWidth(value_width)
        wort2_volume_value.valueChanged.connect(lambda: update_weighted_wort())
        wort2_gravity_value = QDoubleSpinBox(self.weighted_wort)
        wort2_gravity_value.setDecimals(3)
        wort2_gravity_value.setFixedWidth(value_width)
        wort2_gravity_value.valueChanged.connect(lambda: update_weighted_wort())

        result_label = QLabel("Overall Wort Gravity: 1.000")

        # Create layout
        wort1_volume_box = QHBoxLayout()
        wort1_volume_box.addWidget(wort1_volume_label)
        wort1_volume_box.addWidget(wort1_volume_value)

        wort1_gravity_box = QHBoxLayout()
        wort1_gravity_box.addWidget(wort1_gravity_label)
        wort1_gravity_box.addWidget(wort1_gravity_value)

        wort1_box = QVBoxLayout()
        wort1_box.addWidget(wort1_label)
        wort1_box.addLayout(wort1_volume_box)
        wort1_box.addLayout(wort1_gravity_box)

        wort2_volume_box = QHBoxLayout()
        wort2_volume_box.addWidget(wort2_volume_label)
        wort2_volume_box.addWidget(wort2_volume_value)

        wort2_gravity_box = QHBoxLayout()
        wort2_gravity_box.addWidget(wort2_gravity_label)
        wort2_gravity_box.addWidget(wort2_gravity_value)

        wort2_box = QVBoxLayout()
        wort2_box.addWidget(wort2_label)
        wort2_box.addLayout(wort2_volume_box)
        wort2_box.addLayout(wort2_gravity_box)

        wort_box = QHBoxLayout()
        wort_box.addLayout(wort1_box)
        wort_box.addSpacing(42)
        wort_box.addLayout(wort2_box)

        layout_main = QVBoxLayout()
        layout_main.addLayout(wort_box)
        layout_main.addSpacing(20)
        layout_main.addWidget(result_label)

        self.weighted_wort.setLayout(layout_main)

        def update_weighted_wort():
            ww = self.brew_calc.weightedWort(
                [wort1_volume_value.value(), wort2_volume_value.value()]
                , [wort1_gravity_value.value(), wort2_gravity_value.value()]
            )

            result_label.setText("Overall Wort Gravity: " + ww)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Windows'))
    app.setPalette(app.style().standardPalette())

    gallery = WidgetGallery()
    gallery.setWindowTitle('Brewing Tools')
    gallery.show()
    sys.exit(app.exec_()) 
