import unittest
import socket
import time


#TESTING for ACTIVE Server
class TestServer (unittest.TestCase):

    host = '127.0.0.1'
    port = 42069

    def test_server1(self): #Fake client testing Server
        """
        Testar servern
        """
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.host, self.port))
        msg = "Username"
        conn.send(msg.encode("ascii"))
        time.sleep(1)
        msg2 = "Message"
        conn.send(msg2.encode("ascii"))
        time.sleep(1)
        rec = conn.recv(1024).decode("ascii")
        conn.close()
        self.assertEqual("Username > Message", rec)


if __name__ == '__main__':
    unittest.main()
