#!/usr/bin/env python3
"""
Demo script for Japanese Flashcards App
This script provides a quick way to start the development server
and open the app in the default browser.
"""

import sys
import webbrowser
import time
import subprocess
from pathlib import Path

def main():
    """Main function to run the demo"""
    print("🎌 Japanese Flashcards App - Demo")
    print("=" * 40)

    # Get the current directory
    current_dir = Path(__file__).parent.absolute()

    # Check if required files exist
    required_files = ['index.html', 'style.css', 'app.js', 'kanji.json']
    missing_files: list[str] = []

    for file in required_files:
        if not (current_dir / file).exists():
            missing_files.append(file)

    if missing_files:
        print(f"❌ Error: Missing required files: {', '.join(missing_files)}")
        sys.exit(1)

    print("✅ All required files found")

    # Start the server
    print("🚀 Starting development server...")
    try:
        # Start server in background
        server_process = subprocess.Popen(
            [sys.executable, 'server.py'],
            cwd=current_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait a moment for server to start
        time.sleep(2)

        # Check if server is running
        if server_process.poll() is None:
            print("✅ Server started successfully")
            print("🌐 Opening browser...")

            # Open browser
            webbrowser.open('http://localhost:6000')

            print("\n📋 Instructions:")
            print("- Use Previous/Next buttons to browse kanji")
            print("- Click 'Show Answer' to reveal meanings and readings")
            print("- Your progress is automatically saved")
            print("\n🔄 Press Ctrl+C to stop the server")

            # Keep server running
            try:
                server_process.wait()
            except KeyboardInterrupt:
                print("\n🛑 Stopping server...")
                server_process.terminate()
                server_process.wait()
                print("✅ Server stopped")

        else:
            print("❌ Failed to start server")
            _, stderr = server_process.communicate()
            if stderr:
                print(f"Error: {stderr.decode()}")

    except FileNotFoundError:
        print("❌ Error: Python not found in PATH")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
