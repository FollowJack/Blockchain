import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        content_to_hash = (str(self.index) +
                           str(self.timestamp) +
                           str(self.data) +
                           str(self.previous_hash))
        return hasher.sha256(content_to_hash.encode("utf-16")).hexdigest()

    def __str__(self):
        return 'Block: ' + str(self.index) + ', data: ' + str(self.data) + ', hash: '+ str(self.hash) + ', prevHash: ' + str(self.previous_hash)

