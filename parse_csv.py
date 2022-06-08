import csv


class Parser:
    def __init__(self, file='forward_bearings.csv'):
        self.file = file
        self.forward_bearings = []
        self.names = []
        self.back_bearings = []
        self._generate_data()

    def _generate_data(self):
        with open(self.file, newline='\n') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            for name, fb in list(content)[1:]:
                self.names.append(name)
                self.forward_bearings.append(fb)

    def generate_solution(self, data, file='solution.csv'):
        import os
        file_path = os.path.join(os.getcwd(), file)
        self.back_bearings = data
        with open(file_path, 'w', newline='\n') as f:
            fieldnames = ['Line', 'Forward_Bearing', 'Back_Bearing']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for line, fb, bb in zip(self.names, self.forward_bearings, self.back_bearings):
                row = {
                    fieldnames[0]: line,
                    fieldnames[1]: fb,
                    fieldnames[2]: bb
                }
                writer.writerow(row)
