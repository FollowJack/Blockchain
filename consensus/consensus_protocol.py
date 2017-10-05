
class ConsensusProtocol:

    def __init__(self):
        # TODO
        return

    # proposals
    # correct proposer at each round, and gossiped to the other validators.
    # If a proposal is not received in sufficient time, the proposer should be skipped.

    # votes
        # pre-vote
            # A set of pre-commits from more than two-thirds of the validators for the same block at the same round is a commit.
        # pre-commit

    # Locks
        # This is achieved using a locking mechanism which determines how a validator may pre-vote or pre-commit depending on previous pre-votes and pre-commits at the same height. Note that this locking mechanism must be carefully designed so as to not compromise liveness.

    # should be handled asynchronous
    # for simplicity reason: do it synchronous

    # should handle timeouts
    # manage transitions
    # two options against FLP:
            # 1 some leader-election mechanism
            # 2 include randomization
                # normally slower

    # synchronous behaviour could lead to forks