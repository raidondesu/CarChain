import csv




"""
could also use DictWriter - might be more straightforward

"""


class CSV:

    def __init__(self):

        pass


    def add_block(self, block_type, block_data):

        with open("storage/blockchain.csv", 'a+', newline='') as blockchain:
            csv_writer = csv.writer(blockchain)
            csv_writer.writerow(["third row?"])


    def add_adress(self, address):

        with open("storage/adresses.csv", "'a+', newline=''") as adresses:
            csv_writer = csv.writer(adresses)
            csv_writer.writerow(["third row?"])


    def read_chain(self):

        """
        generator to go through blockchain and compare the hash of each row
        to the hash stored in the next row
        """

        with open("storage/blockchain.csv") as blockchain:

            csv_reader = csv.reader(blockchain)
            for row in csv_reader:
                yield row

    def read_adresses(self):

        """
        generator to yield adresses, row for row
        """

        with open("storage/adresses.csv") as adresses:

            csv_reader = csv.reader(adresses)
            for row in csv_reader:
                yield row

test = CSV()

for row in test.read_chain():

    print(row)


