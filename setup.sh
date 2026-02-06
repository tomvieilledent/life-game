#!/bin/bash
# Setup script for Game of Life

echo "🎮 Game of Life - Installation"
echo "================================"
echo ""

# Check Python version
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✓ Python detected: $PYTHON_VERSION"
else
    echo "✗ Python 3 not found. Please install Python 3.7+"
    exit 1
fi

# Check if running on Ubuntu/Debian
if command -v apt &> /dev/null; then
    echo ""
    echo "Option 1: Install pygame via apt (recommended on Ubuntu/Debian)"
    echo "   sudo apt update && sudo apt install python3-pygame"
    echo ""
fi

echo "Option 2: Install pygame in virtual environment"
echo "   python3 -m venv venv"
echo "   source venv/bin/activate"
echo "   pip install -r requirements.txt"
echo ""
echo "After installation, run the game with:"
echo "   python3 game_of_life.py"
echo ""
