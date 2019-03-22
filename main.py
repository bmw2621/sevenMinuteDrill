from BRClasses import BREventList
import PDF
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/pdfGen')
def pdf_gen():
    return render_template('pdfGenForm.html')

if __name__ == "__main__":

    app.run()







#def main():
    # path = 'data/data.p'
    #
    # battle_rhythm = BREventList()
    # battle_rhythm.load_data(path)
    #
    #
    #
    # PDF.gen_PDF(battle_rhythm.events)




