"""
4-Bit Arithmetic Circuit Simulator - Web Server & Project Runner
Serves the modern interactive dashboard and integrates with the Python circuit engine.
"""

import sys
import os
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
import test_circuit
import main as cli_main

DEFAULT_PORT = 8000

class CircuitHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable caching-free development headers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server(port=DEFAULT_PORT, open_browser=True):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ('', port)
    
    print("=" * 60)
    print("      4-BIT ARITHMETIC CIRCUIT SIMULATOR - WEB SERVER")
    print("=" * 60)
    print(f"[*] Serving web dashboard at: http://localhost:{port}/")
    print("[*] Press Ctrl+C in terminal to stop server.")
    print("=" * 60)
    
    if open_browser:
        webbrowser.open(f"http://localhost:{port}/index.html")
        
    try:
        httpd = HTTPServer(server_address, CircuitHTTPRequestHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")

if __name__ == '__main__':
    args = sys.argv[1:]
    if "--test" in args:
        test_circuit.test_circuit()
    elif "--cli" in args:
        cli_main.main()
    else:
        port = DEFAULT_PORT
        for arg in args:
            if arg.isdigit():
                port = int(arg)
        run_server(port=port, open_browser=False)
