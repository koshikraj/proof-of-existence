from multichain_driver import MultichainClient


class Document(object):

    def __init__(self):
        self.client = MultichainClient().connect()
        self.stream = 'poe'

    def verify(self, signature):
        """verifies the existence of a document in blockchain"""

        return self.fetch_by_key(signature)

    def publish(self, key, value):
        """publishes the existence of a document in blockchain"""

        return self.client.publish(self.stream, key, value)

    def fetch_latest(self, count):
        """fetches the last inserted docs from blockchain"""

        latest_docs = []
        for doc in self.client.liststreamitems(self.stream)[::-1][:count]:
            latest_docs.append({"signature": doc.get('key'),
             "blocktime": doc.get('blocktime'),
             "confirmations": doc.get('confirmations')})

        return latest_docs


    def fetch_by_key(self, key):
        """fetches the existence info of a document in blockchain"""

        return self.client.liststreamkeyitems(self.stream, key)

    def fetch_by_txid(self, tx_id):

        return self.client.getwallettransaction(tx_id)



