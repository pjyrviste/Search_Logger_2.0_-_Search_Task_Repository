#!/usr/bin/python

import SocketServer, SimpleHTTPServer, SimpleHTTPServer
import re, time, os, cStringIO

PORT = 3128
PAGE_LOAD = "pageload"
PAGE_UNLOAD = "pageunload"

# information must be given in a list like:
# [time, client ip, action, url, referrer]
def write_human(filehandler, information):
    # report page loaded event
    if information[2] == PAGE_LOAD:
        print >>filehandler, "At %s a user opened %s. The user IP was %s." \
        % (information[0], information[3], information[1])
        # referrer is set
        if information[4]:
            print >>filehandler, "The user came from %s." % (information[4])
    # report page unload event
    if information[2] == PAGE_UNLOAD:
        print >>filehandler, "It was %s when the user from %s moved away from %s." \
        % (information[0], information[1], information[3])

# information must be given in a list like:
# [time, client ip, action, url, referrer]
def write_geek(filehandler, information):
    filehandler.write(str(information) + "\n")

def log(info):
    # create directory if needed
    if not os.path.exists("logs"):
        os.makedirs("logs")
    # turn input into a list, order unchanged
    fields = info.split("|+0+|")
    # write technical log
    f = open("logs/for_geeks.txt", "a")
    write_geek(f, fields)
    f.close()
    # write human-readable log
    g = open("logs/for_humans.txt", "a")
    write_human(g, fields)
    g.close()

def main():
    try:
        class Logger(SimpleHTTPServer.SimpleHTTPRequestHandler):
            def do_GET(self):
                # if request to dummy url, just log
                # information is formatted like shown below, field separator is |+0+|
                # time |+0+| client ip |+0+| action |+0+| url |+0+| referrer
                if '?data=' in self.path:
                    client_data = re.sub(r'.*/\?data=', '', self.path)
                    log(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())) + \
                    "|+0+|" + str(self.client_address[0]) + "|+0+|" + client_data)
                # wrong request
                else:
                    print 'We should not be getting this:', self.path           
        httpd = SocketServer.ForkingTCPServer(('', PORT), Logger)
        print "Logger serving at port", PORT
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '\n^C received, shutting down logging server'
        httpd.socket.close()
        print 'Bye!'

if __name__ == '__main__':
    main()
