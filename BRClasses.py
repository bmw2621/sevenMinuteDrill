import pickle
from fpdf import FPDF

class BREvent:
    def __init__(self, title, time='', frequency='', chair='', members=[],
                 location='', purpose='', inputs=[], outputs=[], agenda=[]):
        self.title = title
        self.time = time
        self.frequency = frequency
        self.chair = chair
        self.members = members
        self.location = location
        self.purpose = purpose
        self.inputs = inputs
        self.outputs = outputs
        self.agenda = agenda

    def __repr__(self):
        return '{} \n   Time: {} \n   Freq: {} \n   Chair: {} \n   Members: {} \n   ' \
               'Location: {} \n   Purpose: {} \n   Inputs: {} \n   Outputs: {} \n   ' \
               'Agenda: {}\n'.format(self.title, self.time, self.frequency, self.chair, self.members, self.location,
                                   self.purpose, self.inputs, self.outputs, self.agenda)



class BREventList:
    def __init__(self):
        self.events = {}

    def __repr__(self):
        return str([self.events[event].title for event in self.events])

    def load_data(self, path):
        data = pickle.load(open(path, 'rb'))
        self.events = data

    def save_data(self,path):
        pickle.dump(self.events, open(path, 'wb'))

    def add(self, new_event):
        if type(new_event) != type(BREvent('test')):
            raise Exception("New Event must be <class 'BRClasses.BREvent'>. Passed parameter is type: {}".format(type(new_event)))
        else:
            self.events[new_event.title] = new_event
    def add_event(self):
        title = input('Title: ')
        time = input('Time: ')
        frequency = input('Frequency: ')
        chair = input('Chair: ')
        members = input('Members (Comma delimited list): ').split(',')
        location = input('Location: ')
        purpose = input('Purpose: ')
        inputs = input('Inputs (Comma delimited list: ').split(',')
        outputs = input('Outputs (Comma delimited list: ').split(',')
        agenda = input('Agenda (Comma delimited list: ').split(',')
        self.events[title] = BREvent(title, time, frequency, chair, members, location, purpose, inputs, outputs, agenda)


    def remove(self, del_event):
        del self.events[del_event]


