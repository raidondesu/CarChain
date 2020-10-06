from csv import writer 


class CSV:

    def __init__(self):

        pass


    def add_block(self, block_type, block_data):

        with open("storage/blockchain.csv", 'a+', newline='') as f:
            csv_writer = writer(f)
            csv_writer.writerow(["third row?"])


    def add_adress(self, address):

        with open("storage/adresses.csv", 'a+', newline='') as f:
            csv_writer = writer(f)
            csv_writer.writerow(["third row?"])


    def read_chain(self):

        """
        generator to go thorough blockchain and compare the hash of each row
        to the hash stored in the next row
        """


        pass


    def read_adresses(self):

        """
        generator to yield adresses, row for row
        """

        pass



