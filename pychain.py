# PyChain Ledger

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################
# Step 1:
# Create a Record Data Class that consists of the `sender`, `receiver`, and `amount` attributes
@dataclass
class Record:
    data: Any
    
    sender: str = "0"
    receiver: str = "0"
    amount: float = 0.00

################################################################################
# Step 2:
# Creates the Block and PyChain data classes

# Inside the provided `Block` class, add a function named `hash_block`. 
# This function should include an instance of the `sha256` hashing function, the processes to encode and hash the data, the creator ID, and the timestamp. 
# The function should return the resulting hashes in a `hexdigest` format.

@dataclass
class Block:
    record: Record

    creator_id: int
    prev_hash: str = "0"    
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    # Add a new function called `hash_block`
    def hash_block(self):
        # Add an instance of the `sha256` hashing function
        sha = hashlib.sha256()

        # Encode the Block's data attribute
        record = str(self.record).encode()
        # Update the encoded data using the hashing function
        sha.update(record)

        # Encode the Blocks's creator_id attribute
        creator_id = str(self.creator_id).encode()
        # Update the encoded creator_id using the hashing function
        sha.update(creator_id)

        # Encode the Block's timestamp attribute
        timestamp = str(self.timestamp).encode()
        # Update the encoded timestamp using the hashing function
        sha.update(timestamp)        

        # Encode the Block's previous hash
        prev_hash = str(self.prev_hash).encode()
        # Update the encoded previous hash using the hashing function
        sha.update(prev_hash)

        # Encode the Block's nonce counter number
        nonce = str(self.nonce).encode()
        # Update the encoded nonce using the hashing function
        sha.update(nonce)

        # Return the hashes of all the Block class attributes
        return sha.hexdigest()


# Inside the provided `Chain` class, add a function named `proof_of_work`.
# New blocks of user data are added to a Python blockchain.
# To build the chain of blocks 'proof_of_work' function defines the blocks by calculating the hash of the block per the 'difficulty' level and setting the nonce counter in a while loop.
# 'add_block' function adds the blocks to the chain
# 'is_valid' function validates the integrity of the PyChain by comparing the calculated hash code of each block to the `prev_hash` value contained in the following block.

@dataclass
class PyChain:
    chain: List[Block]

    # Add a `difficulty` data attribute with a data type of `int` and a default value of 4.
    difficulty: int = 4

    # Define the block
    def proof_of_work(self, block):

        calculated_hash = block.hash_block()
        
        # Add a `num_of_zeros` data attribute that multiplies the string value ("0") by the `difficulty` value.
        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    # Add the block to the chain
    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    # Check if the block is valid
    def is_valid(self):
        # Add the code to generate the hash of the first block in the chain.
        block_hash = self.chain[0].hash_block()

        # Create a for-loop to access the remainder of the blocks in the chain, starting at index position 1
        for block in self.chain[1:]:
            # If the two hashes are NOT equal, print a statement that says "Blockchain is invalid", and then return the value False
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False
            
            # Set the block_hash value equal to the hashed value of the current block
            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit
@st.cache_resource
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


# Create the application header using a markdown string
st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

# Initialize the blockchain in the Steamlit web interface
pychain = setup()

################################################################################
# Step 3:
# Add Relevant User Inputs to the Streamlit Interface

# Add an input area where you can get a value for `sender` from the user.
input_sender = st.text_input("Sender")

# Add an input area where you can get a value for `receiver` from the user.
input_receiver = st.text_input("Receiver")

# Add an input area where you can get a value for `amount` from the user.
input_amount = st.text_input("Amount")

# Concatenate the input data elements of 'sender', 'receiver' and 'amount' for the block
input_data = "Sender: " + input_sender + " , " + "Receiver: " + input_receiver + " , " + "Amount: $" + input_amount

# Streamlit “Add Block” button code so that when someone clicks the  button, the code adds a new block to the blockchain
if st.button("Add Block"):
    # Select the previous block in the chain
    prev_block = pychain.chain[-1]

    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()
    
    # Create a new block in the chain
    new_block = Block(
        record = input_data,
        creator_id=42,        
        prev_hash=prev_block_hash
    )
    
    # Add the new block to the chain
    pychain.add_block(new_block)

    # When a new user block of data is added successfully show balloons
    st.balloons() 

################################################################################
# Streamlit Code (continues)
# Display the the `PyChain` ledger data on the Streamlit webpage

st.markdown("## The PyChain Ledger")

# Create a Pandas DataFrame to display the `PyChain` ledger
pychain_df = pd.DataFrame(pychain.chain).astype(str)

# Use the Streamlit `write` function to display the `PyChain` DataFrame
st.write(pychain_df)

# Add a Streamlit component that can update the `difficulty` attribute of the `PyChain` class.
# Add a Streamlit slider named "Block Difficulty" that allows the user to update a difficulty value. Set this equal to the variable `difficulty`
difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)

# Update the `difficulty` data attribute of the `PyChain` data class (`pychain.difficulty`) with this new `difficulty` value
pychain.difficulty = difficulty

# Add a block inspector drop-down menu
st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

# Add a button with the text “Validate Blockchain” to your Streamlit interface.
if st.button("Validate Chain"):
    # Call the `is_valid` method of the `PyChain` data class and `write` the result to the Streamlit interface
    st.write(pychain.is_valid())

################################################################################
# Step 4:
# Test the PyChain Ledger by Storing Records