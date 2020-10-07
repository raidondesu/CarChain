import csv




"""
could also use DictWriter - might be more straightforward

"""


class CSV:

    def __init__(self):

        pass


    def add_block(self, block):

        with open("storage/blockchain.csv", 'a+', newline='') as blockchain:
            fieldnames = ["_id","car_id","nonce","hash","details"]
            csv_writer = csv.DictWriter(blockchain, fieldnames=fieldnames)
            csv_writer.writerow(block)


    def add_adress(self, address):

        with open("storage/adresses.csv", "'a+', newline=''") as adresses:
            csv_writer = csv.writer(adresses)
            csv_writer.writerow("adress")


    def read_chain(self):

        """
        generator to go through blockchain and compare the hash of each row
        to the hash stored in the next row
        """

        with open("storage/blockchain.csv") as blockchain:

            csv_reader = csv.DictReader(blockchain)
            for row in csv_reader:
                yield row

    def get_last_block(self):


        with open("storage/blockchain.csv") as blockchain:

            return dict([row for row in csv.DictReader(blockchain)][-1])
        

    def read_adresses(self):

        """
        generator to yield adresses, row for row
        """

        with open("storage/adresses.csv") as addresses:

            csv_reader = csv.reader(addresses)
            for row in csv_reader:

                yield row


    def get_chain_length(self):

        with open("storage/blockchain.csv") as blockchain:

            csv_reader = csv.DictReader(blockchain)
            return sum(1 for row in csv_reader)



block = {"_id":0, 
        "car_id":"None",
        "nonce":0,
        "hash": {"block":"None","car":"None"}, 
        "details": {"Sale":"None"}}

test = CSV()
test.add_block(block)
print(test.get_last_block())
print(test.get_chain_length())






