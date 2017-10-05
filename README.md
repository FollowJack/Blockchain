Goal:
1. Get a feel for every component in the blockchain ecosystem
2. Deeper understanding in consensus algorithms and underlying mechanisms
3. Get a sense for possible attack vectors based on the implementation of the blockchain
4. Share your understanding in order to push the progess of future development 

Result:
0.2 Structure of underlying Blockchain components 
0.1 Structure of Blockchain project

Blockchain <3
A blockchain is, at heart, an integrity-focused approach to Byzantine Fault
Tolerant Atomic Broadcast.
The blockchain gets its name from the two key optimizations it employs
in solving ABC. The first is that it groups transactions in blocks in order to amortize the high commit latency (on the order of ten minutes) over many transactions. The second is to link blocks via cryptographic hashes into an immutable chain, such that is easy to verify the historical record. Both optimizations are natural improvements to a naive BFT-ABC. 

On the one hand are the public blockchains, known affectionately as the Big Bad Public Blockchains or BBPBs, whose protocols are dominated by in-built economic incentives bootstrapped by a native currency. On the other are so called private blockchains, which might more accurately be called “consortia blockchains”, and which are effectively improvements on traditional consen- sus and BFT algorithms through the use of hash trees, digital signatures, peer-to-peer peer-to-peer networking, and enhanced accountability.