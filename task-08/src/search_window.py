from PySide6 import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PySide6.QtGui import QPixmap
import requests
import json
import shutil

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        self.w = None        
        self.setFixedSize(850, 500)

        self.setStyleSheet("""
            QPushButton , QLineEdit{
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QLabel {
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)
        self.poke_list = []
        self.label = QLabel(self)
        self.pixmap = QPixmap("../assets/landing.jpg")
        self.label.setPixmap(self.pixmap)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)
        label1.setStyleSheet("color : white ; font-size: 18px ; font-weight : bold")

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search)
        self.description_label  = QLabel(self)
        
        
        self.label3 = QLabel(self)
        self.label3.setGeometry(500, 20, 200, 200)

        self.label4 = QLabel(self)
        self.label4.setGeometry(500, 250, 400, 400)
        
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.downlaod_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_downloaded)

    def display_downloaded(self):
        self.k = ShowDownloads(self.poke_list)
        self.k.setup_window()
        self.k.show()

    def downlaod_pokemon(self):
        url = self.data['sprites']['other']['official-artwork']['front_default']
        pic_response = requests.get(url, stream=True)
        with open(f"../Downloads/{self.name}.png", 'wb') as out_file:
            shutil.copyfileobj(pic_response.raw, out_file)
        self.poke_list.append(self.name)
        self.n = CustomDialog()
        self.n.set_var(self.name)
        self.n.exec_()

    def display_pokemon(self):
        self.label3.clear()
        pix  = QPixmap()
        #pix = pix.scaled(200,200)
        self.pixmap = QPixmap("../assets/grey.jpg")
        self.label.setPixmap(self.pixmap)
        pix.loadFromData(self.Load_image.content)
        self.label3.setPixmap(pix)
        self.label3.setScaledContents(True)
        self.label3.show()
    
    def display_description(self):
        self.description_label.clear()
        self.description_label.setText(self.desc)
        self.description_label.setGeometry(500, 150 ,300, 400)
        self.description_label.setStyleSheet("color : white")
        self.description_label.show()
        

    def search(self):
        pokemon = self.textbox.text()
        self.response =  requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
        self.data = json.loads(self.response.text)
        self.Load_image = requests.get(self.data['sprites']['other']['official-artwork']['front_default'])
        self.name = self.data['name']
        self.abilities = [self.data['abilities'][0]['ability']['name'], self.data['abilities'][1]['ability']['name']]
        self.Types = self.data['types'][0]['type']['name']
        self.stats = {'hp':self.data['stats'][0]['base_stat'], 'attack':self.data['stats'][1]['base_stat'], 'defence':self.data['stats'][2]['base_stat'],
                 'special-attack':self.data['stats'][3]['base_stat'], 'special-defence':self.data['stats'][4]['base_stat'], 'speed':self.data['stats'][5]['base_stat']}
        self.desc = f"Name : {self.name} \nAbilities : {self.abilities[0]}, {self.abilities[1]} \nTypes : {self.Types} \nStats :\nHp : {self.stats['hp']} \nAttack : {self.stats['attack']} \nDefence : {self.stats['defence']} \nSpecial-Attack : {self.stats['special-attack']} \nSpecial-Defence : {self.stats['special-defence']} \nSpeed : {self.stats['speed']} "
        self.display_pokemon()
        self.display_description()
    
    
        
    

class CustomDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
    def set_var(self, name):
        self.name = name
        self.setWindowTitle("captured !!")

        QBtn = QDialogButtonBox.Ok 
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        

        self.layout = QVBoxLayout()
        message = QLabel(f"{self.name} was captured successfully !")
        message.setStyleSheet("background-color : grey; color : white ; font-size: 18px ; font-weight : bold")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class ShowDownloads(QWidget):

    def __init__(self, download_list):
        super().__init__()
        self.counter =  0 
        self.download_list = download_list
        self.setFixedSize(450, 475)

        self.setStyleSheet("""
            QWidget{
                background-color: dark-grey
            }               
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QLabel {
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """) 
        
        self.pokemon = QLabel(self)
        self.poke_pix = QPixmap(f"../Downloads/{self.download_list[self.counter]}.png")
        self.pokemon_name = QLabel(self)
        self.pokemon.setGeometry(0,0,450,400)
        self.pokemon_name.setGeometry(10, 415 ,300, 25)
        self.pokemon.setPixmap(self.poke_pix)
        self.prev_button = QPushButton("Previous", self)
        self.prev_button.setGeometry(10, 440, 200, 20)
        self.prev_button.clicked.connect(self.decrement)
        self.next_button = QPushButton("Next", self) 
        self.next_button.setGeometry(230, 440, 200, 20) 
        self.next_button.clicked.connect(self.increment)
        
        

    def increment(self):
        self.counter +=1
        if(self.counter > len(self.download_list)-1):
            self.counter = 0    
        self.setup_window()

    
    def decrement(self):
        self.counter -= 1
        if(self.counter < 0):
            self.counter = len(self.download_list)-1
        self.setup_window()
   
    
    def setup_window(self):
        self.pokemon.clear()
        self.pokemon_name.clear()
        
        self.poke_pix = QPixmap(f"../Downloads/{self.download_list[self.counter]}.png")
        self.pokemon.setPixmap(self.poke_pix)
        self.pokemon.setScaledContents(True)
        self.pokemon_name.setText(f"{self.download_list[self.counter]}")
        self.pokemon_name.setStyleSheet("color : white")
        self.pokemon_name.show()




            
            


   

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
