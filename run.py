from BRClasses import *
import PDF
from fpdf import FPDF

def exec():

    path = 'data/data.p'

    battle_rhythm = BREventList()
    battle_rhythm.load_data(path)

    pdf = FPDF('L', 'in', 'Letter')
    PDF.gen_PDF(battle_rhythm.events, pdf)


    #battle_rhythm.save_data(path)

if __name__ == "__main__":
    exec()