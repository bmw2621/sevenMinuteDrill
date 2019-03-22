from fpdf import FPDF

def gen_PDF(events, pdf):
    for event in events:
        pdf.add_page()
        pdf.set_draw_color(r=0, g=0, b=255)
        pdf.set_line_width(.05)
        pdf.rect(.15, .15, 10.7, 8.2)
        pdf.image('images/3IDcav3.png', x=.14, y=.22, h=1)
        pdf.image('images/3IDLogo.png', x=9.8, y=.22, h=1)
        pdf.set_draw_color(r=0, g=0, b=0)
        pdf.line(5.5, 1.5, 5.5, 8)
        pdf.line(.5, 4.25, 10.5, 4.25)

        pdf.set_font('Arial', 'B', 24)
        pdf.set_xy(0, .75)
        pdf.cell(w=0, txt=events[event].title, align='C')
        pdf.set_xy(1, 1.5)
        pdf.set_font('Arial', '', 14)
        pdf.multi_cell(4.5, .22, 'Purpose: {}\n\nFrequency: {}\n\nTime: {}\n\nLocation: {}'.format(
            events[event].purpose, events[event].frequency,
            events[event].time, events[event].location), 0, 'L')
        pdf.set_xy(1, 4.5)
        pdf.multi_cell(4.5, .22, 'Inputs: \n{}\nOutputs: \n{}'.format(
            '  -' + str(events[event].inputs)[1:-1].replace("'", "").replace(',', '\n  -'),
            '  -' + str(events[event].outputs)[1:-1].replace("'", "").replace(',', '\n  -'), 0, 'L'))
        pdf.set_xy(6.5, 1.5)
        pdf.multi_cell(4.5, .22, 'Chair: {}\n\nMembers: \n{}'.format(
            events[event].chair,
            '  -' + str(events[event].members)[1:-1].replace("'", "").replace(',', '\n  -'), 0, 'L'))
        pdf.set_xy(6.5, 4.5)
        pdf.multi_cell(4.5, .22, 'Agenda: \n{}'.format(
            '  -' + str(events[event].agenda)[1:-1].replace("'", "").replace(',', '\n  -'), 0, 'L'))

    pdf.output('test.pdf')