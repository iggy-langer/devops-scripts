#!/bin/bash

# Set title and version information
TITLE="devops-scripts"
VERSION="1.0"

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run unit tests
echo "Running unit tests..."
python -m unittest discover -s tests

# Run integration tests
echo "Running integration tests..."
python -m unittest discover -s tests/integration

# Build documentation
echo "Building documentation..."
sphinx-build -b html docs docs/build

# Create release
echo "Creating release..."
git add .
git commit -m "Release $VERSION"
git tag -a "$VERSION" -m "Release $VERSION"