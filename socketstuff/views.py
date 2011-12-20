import gevent
from pyramid.response import Response
from pyramid_socketio.io import SocketIOContext, socketio_manage
from pyramid.view import view_config
import redis

class ConnectIOContext(SocketIOContext):
    # self.io is the Socket.IO socket
    # self.request is the request

    def msg_connect(self, msg):
        print "Connect message received", msg
        self.msg("connected", hello="world")

        server = redis.Redis(host='localhost', port=6379, db=0)
        client = server.pubsub()
        client.subscribe('points')
        client.subscribe('jaberwocky')
        messages = client.listen()

        def sendcpu():
            """Calculate CPU utilization"""
            prev = None
            while self.io.connected():
                try:
                    msg = messages.next()
                    if msg['channel'] == 'points':
                        data = msg['data']
                        np = [int(l.strip()) for l in data.split(',')]
                        for val in np:
                            self.msg("showdata", point=val)
                    if msg['channel'] == 'jaberwocky':
                        self.msg("jaberwocky", word=msg['data'])
                except:
                    print "Parse error, bad data?\ndata:  %s"
        self.spawn(sendcpu)

# Socket.IO implementation
@view_config(route_name="socketio")
def socketio_service(request):
    print "Socket.IO request running"
    retval = socketio_manage(ConnectIOContext(request))
    return Response(retval)
