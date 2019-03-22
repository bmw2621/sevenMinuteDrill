from BRClasses import BREventList
import PDF
from fpdf import FPDF
import json

def main():

    path = 'data/data.p'

    battle_rhythm = BREventList()
    battle_rhythm.load_data(path)

    battle_rhythm.add_event()

    PDF.gen_PDF(battle_rhythm.events)

    battle_rhythm.save_data(path)

if __name__ == "__main__":
    main()

