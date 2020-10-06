import socket
import csv
from Blockchain import Blockchain



"""
Class Architecture:

1. Top Level: The network. The blockchain class is instantiated inside of the network class. 

2. The blockchain class, contains code to mine new blocks and validate the chain and the car history

3. DBConnect, is instantiated inside the blockchain class


Information flow: The interaction between the website and the P2P network

1. The website is the place to download the client for the P2P network

2. The website allows to create an account, download the client and query the car history

3. But since querying the car history requires code from the blockchain class it would make sense
to have the website be a node aswell - at least on the server side. 

4. This way the new nodes could query the website node for the adresses of the other nodes. 

5. Also the query for the car history could be validated by the website node.

--> This is just a current state, I have not quite understodd if this is a possible and viable setup. 


"""


class P2P:

    def __init__(self):


        self.blockchain = Blockchain()

        """
        when initialized the server has to be instantiated,
        the valid version of the blockchain has to be queried and if necessary 
        replaced. 
        the adresses have to be kept up to date.


        """

        pass

    def register_node(self):


        """"
        send ip address to central sql data base(why sql? no reason except for practice - I guess
        MongoDB would work just as well?)
        """

        pass

    def client(self):

        """
    	queries length of other blockchains
        returns longest valid chain, this will be 
        used by the blockchain class to replace the current chain
        """

        pass


    def server(self):


        """
        has to be online 24/7
        returns
        1. adresses
        2. blockchain


        Does the blockchain live on the server? Yes the blockchain has to be instantiated here.
        


        """

        pass

    def load_adresses(self):

        """
        load adresses from hard drive 
        adresses are saved in csv format

        should be implemented with a yield statement
        to save on memory == generator
        """

        pass

    def get_adresses(self):

        """
        1. query central website with an sql data base
        2. query other nodes in the network that are online
        """

        pass

    def load_blockchain(self):

        """
        load blockchain from memory when executable is being executed
        """

        pass

    def save_blockchain(self):

        """
        save blockchain to memory
        """

        pass

    def add_block(self):

        """"
        add block to blockchain, other nodes will only accept the change if the new blockchain is valid.

        It would make sense if only the website node actually adds new entries to the data base. 

        so the flow would be:

        1. Node adds block.

        2. Website node discovers the change, validates it and updates the chain 

        3. then adds the entries to the data base
        """

        pass







