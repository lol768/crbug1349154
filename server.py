#!/usr/bin/env python3

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.pkpasses': 'application/vnd.apple.pkpasses',
})

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print("serving at port", PORT)
    httpd.serve_forever()
