from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class TradingApp(EWrapper, EClient):
    """automated trading bot"""

    def __init__(self):
        """Init trading bot"""
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        """
        This event is called when there is an error with the
        communication or when TWS wants to send a message to the client.

        :param
        reqId: the request identifier which generated the error. Note: -1 will
        indicate a notification and not true error condition.
        errorCode: the code identifying the error.
        errorString:error's description.

        :return: None
        """
        print(f"Error {reqId} {errorCode} {errorString}")

    def contractDetails(self, reqId, contractDetails):
        print(f"reqID: {reqId}, contract: {contractDetails}")


app = TradingApp()

app.connect("127.0.0.1", 7497, clientId=1)
app.run()
