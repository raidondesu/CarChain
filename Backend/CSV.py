import csv




"""
could also use DictWriter - might be more straightforward

"""


class CSV:

    def __init__(self):

        pass


    def add_block(self, block):

        with open("storage/blockchain.csv", 'a+', newline='') as blockchain:
            fieldnames = ["_id","car_id","nonce","car_hash","block_hash","details"]
            csv_writer = csv.DictWriter(blockchain, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerow(block)


    def add_adress(self, address):

        with open("storage/adresses.csv", "'a+', newline=''") as adresses:
            csv_writer = csv.writer(adresses)
            csv_writer.writerow("adress")


    def read_chain(self):

        """
        generator to go through blockchain and return consecutive blocks
        """

        with open("storage/blockchain.csv") as blockchain1:

            with open("storage/blockchain.csv") as blockchain2:

                previous_blocks = csv.DictReader(blockchain1)
                current_blocks = csv.DictReader(blockchain2)
                next(current_blocks)

                for previous_block, current_block in zip(previous_blocks, current_blocks):
        	        yield dict(previous_block), dict(current_block)

    def get_last_block(self):

        """
        this should be done in a more efficent way
        """

        with open("storage/blockchain.csv") as blockchain:

            csv_reader = csv.DictReader(blockchain)
        
            for _ in range(1,self.get_chain_length()):

                next(csv_reader)

            return dict([row for row in csv_reader][0])
        

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
        "car_hash":"None",
        "block_hash":"None",
        "details": "Sale "}  

test = CSV()
test.add_block(block)





