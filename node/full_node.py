class FullNode:

    # provide an API
    # talk with consensus protocol
        # have an broadcast mechanism
    # maintain a transaction log (memPool)
    # (set new states)
    # asymmetric cryptographic key-pair for producing digital signatures.
    # maintains a whitelist of nodes

    def __init__(self):
        # TODO
        return

    # vote
        # sign with private key
        #

    # proposal
        # sign with private key

    # commit
        # 2/3 reached

    # new round
        # no 2/3 reached --> propose new validator and next round
        # The proposer for the given round takes a batch of recently received transactions from its local cache (the Mempool
        # composes a block, and broadcasts a signed ProposalMsg con- taining the block.

    # validate block
        # If a validator does not receive a correct proposal within ProposalTimeout, it pre-votes for nil instead.