import pickle


class BREvent:

    title = ''
    time = ''
    frequency = ''
    chair = ''
    members = []
    location = ''
    purpose = ''
    inputs = []
    outputs = []
    agenda = []

    def __init__(self, **kwargs):
        self.title = kwargs["title"]
        self.time = kwargs["time"]
        self.frequency = kwargs["frequency"]
        self.chair = kwargs["chair"]
        self.members = kwargs["members"].split(', ')
        self.location = kwargs["location"]
        self.purpose = kwargs["purpose"]
        self.inputs = kwargs["inputs"].split(', ')
        self.outputs = kwargs["outputs"].split(', ')
        self.agenda = kwargs["agenda"].split(', ')

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

    def add(self):
        pass

    def add_event(self):
        new_event = {}
        for element in BREvent.__dict__.keys():
            if element[0] != '_':
                new_event[element] = input(element + ": ")
        self.events[new_event['title']] = BREvent(**new_event)


    def remove(self, del_event):
        del self.events[del_event]


