# PyChain Ledger

![alt=""](Images/application-image.png)

You’re a fintech engineer who’s working at one of the five largest banks in the world. You were recently promoted to act as the lead developer on their decentralized finance team. Your task is to build a blockchain-based ledger system, complete with a user-friendly web interface. This ledger should allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.

You’ll make the following updates to the provided Python file for this assignment, which already contains the basic `PyChain` ledger structure that you created throughout the module:

1. Create a new data class named `Record`. This class will serve as the blueprint for the financial transaction records that the blocks of the ledger will store.

2. Modify the existing `Block` data class to store `Record` data.

3. Add Relevant User Inputs to the Streamlit interface.

4. Test the PyChain Ledger by Storing Records.

---

---
## Streamlit PyChain Application Screenshot

![alt=""](Images/PyChain_Streamlit_Screenshot.png)

* This Streamlit Application emulates a ledger system based on blockchain, providing users with the ability to transfer funds (send and receive money) and validate the authenticity of the data recorded in the ledger.

  * To initiate the application, the user must input the Sender and Receiver addresses, as well as the amount of cryptocurrency to be transferred. The "PyChain Ledger" keeps track of and stores all transactions, and the user can inspect each block/transaction through the "Block Inspector" drop-down menu located on the left side of the application. Additionally, the user can assess the integrity of the Blockchain Ledger System by selecting the "Validate Chain" button, which checks the hash of the previous block against the previous hash of the current block.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
