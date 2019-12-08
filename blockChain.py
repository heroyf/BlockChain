import hashlib

def sha256(dataNeedSha):
    sha256 = hashlib.sha256()
    sha256.update(dataNeedSha.encode('utf-8'))
    return sha256.hexdigest()

# 区块
class Block:
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.hash = self.ComputeHash

    @property
    def ComputeHash(self):
        return str(sha256(self.data))

    def showBlock(self):
        print ({'data':self.data, 'previousHash': self.previousHash, 'hash': self.hash})


# 链
class Chain:
    def __init__(self):
        self.chain = [self.ancestorBlock]

    @property
    def ancestorBlock(self):
        ancestor_block = Block('祖先区块', '')
        return ancestor_block

    @property
    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlockToChain(self, newBlock):
        newBlock.previousHash = self.getLatestBlock.hash
        newBlock.hash = newBlock.ComputeHash
        self.chain.append(newBlock)

    def showChain(self):
        for i in self.chain:
            i.showBlock()

    def validateChain(self):
        if len(self.chain) == 1:
            if self.chain[0].hash != self.chain[0].ComputeHash:
                return False
            return True

        for i in range(1,len(self.chain)):
            blockToValidate = self.chain[i]
            if (blockToValidate.hash) != blockToValidate.ComputeHash:
                print('数据被篡改')
                return False
            previousBlock = self.chain[i-1]
            if blockToValidate.previousHash != previousBlock.hash:
                print('前后区块链接断裂')
                return False
        return True

block1 = Block('转账10', '')
block2 = Block('转账20', '')
bitChain = Chain()
bitChain.addBlockToChain(block1)
bitChain.addBlockToChain(block2)


# 尝试篡改区块
bitChain.chain[1].data = '转账500'
# 尝试修正hash
bitChain.chain[1].hash = bitChain.chain[1].ComputeHash
bitChain.showChain()
print(bitChain.validateChain())



    