#!/usr/bin/env python3
"""
Japanese Flashcards Web Server
A simple HTTP server to serve the Japanese Flashcards application
"""

import http.server
import socketserver
import os
import sys
import json
from urllib.parse import unquote
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class FlashcardHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for the flashcard app"""

    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        self.directory = os.getcwd()
        super().__init__(*args, **kwargs)

    def log_message(self, format, *args):
        """Override logging to use our custom logger"""
        logging.info("%s - %s" % (self.address_string(), format % args))

    def do_GET(self):
        """Handle GET requests"""
        try:
            # Log the request
            logging.info(f"Request: {self.path} from {self.client_address[0]}")

            # Handle root path
            if self.path == '/' or self.path == '':
                self.path = '/index.html'

            # Handle favicon requests
            if self.path == '/favicon.ico':
                self.send_error(404, "Favicon not found")
                return

            # Serve the file
            return super().do_GET()

        except Exception as e:
            logging.error(f"Error handling request {self.path}: {str(e)}")
            self.send_error(500, f"Internal server error: {str(e)}")

    def end_headers(self):
        """Add custom headers"""
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def create_server(port=6000, host='127.0.0.1'):
    """Create and start the HTTP server"""
    try:
        with socketserver.TCPServer((host, port), FlashcardHTTPRequestHandler) as httpd:
            print(f"""
╔══════════════════════════════════════════════════════════════╗
║                 🎌 JAPANESE FLASHCARDS 🎌                      ║
║                 ✨ SUPER COOL EDITION ✨                       ║
║                                                                      ║
║  📚 180 + N5 Level Kanji Characters                                 ║
║  🎨 Beautiful Glassmorphism Design                               ║
║  ✨ Animated Particles & Effects                                 ║
║  💾 Auto-Save Progress                                           ║
║                                                                      ║
║  🌐 Access your app at: http://{host}:{port}                       ║
║  📁 Serving files from: {os.getcwd()}                              ║
║                                                                      ║
║  Press Ctrl+C to stop the server                                    ║
╚══════════════════════════════════════════════════════════════╝
            """)

            logging.info(f"Server started on http://{host}:{port}")
            logging.info(f"Serving directory: {os.getcwd()}")

            # Start serving
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        logging.info("Server stopped by user")

    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python server.py --port 6001")
        else:
            print(f"❌ Error starting server: {e}")
        logging.error(f"Server error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description='Japanese Flashcards Web Server')
    parser.add_argument('--port', type=int, default=6000,
                       help='Port to run the server on (default: 6000)')
    parser.add_argument('--host', type=str, default='127.0.0.1',
                       help='Host to bind to (default: 127.0.0.1)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Check if required files exist
    required_files = ['index.html', 'style.css', 'app.js']
    missing_files = [f for f in required_files if not os.path.exists(f)]

    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Please make sure all flashcard files are in the current directory.")
        sys.exit(1)

    # Print server info
    print(f"🚀 Starting Japanese Flashcards Server...")
    print(f"📂 Directory: {os.getcwd()}")
    print(f"🌐 Host: {args.host}")
    print(f"🔌 Port: {args.port}")

    # Start the server
    create_server(port=args.port, host=args.host)

if __name__ == '__main__':
    main()
