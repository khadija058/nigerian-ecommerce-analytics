#!/usr/bin/env python3
import os

def create_folders():
    print("Creating project folders...")
    
    folders = [
        'data/raw',
        'data/processed', 
        'src',
        'config',
        'notebooks',
        'reports',
        'sql',
        'logs'
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created: {folder}")
    
    # Create Python package file
    with open('src/__init__.py', 'w') as f:
        f.write('# Python package\n')
    
    print("Project structure created!")

def create_requirements():
    print("Creating requirements.txt...")
    
    requirements = """pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
plotly==5.15.0
kaggle==1.5.16
python-dotenv==1.0.0
jupyter==1.0.0"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    print("Requirements file created!")

def create_env_file():
    print("Creating .env.example...")
    
    env_content = """# Kaggle credentials
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_api_key

# Project settings
PROJECT_NAME=Nigerian E-Commerce Analytics"""
    
    with open('.env.example', 'w') as f:
        f.write(env_content)
    
    print("Environment file created!")

if __name__ == "__main__":
    print("Setting up Nigerian E-Commerce Analytics Project...")
    
    create_folders()
    create_requirements()
    create_env_file()
    
    print("\nSetup complete!")
    print("Next: Run 'pip3 install -r requirements.txt'")
