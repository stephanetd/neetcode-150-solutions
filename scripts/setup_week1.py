"""
Setup script for Week 1: Arrays & Hashing
Creates all necessary files and structure
"""

import os
import sys

def create_directory_structure():
    """Create the directory structure for Week 1"""
    directories = [
        'python/arrays-hashing',
        'java/arrays-hashing',
        'notes',
        'progress',
        'scripts'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created: {directory}")
    
    # Create __init__.py for Python package
    with open('python/__init__.py', 'w') as f:
        f.write('')
    
    print("\n✅ Directory structure created!")

def create_problem_files():
    """Create empty solution files for all Week 1 problems"""
    problems = [
        ('217', 'Contains Duplicate', 'Easy'),
        ('242', 'Valid Anagram', 'Easy'),
        ('1', 'Two Sum', 'Easy'),
        ('49', 'Group Anagrams', 'Medium'),
        ('347', 'Top K Frequent Elements', 'Medium'),
        ('238', 'Product of Array Except Self', 'Medium'),
        ('36', 'Valid Sudoku', 'Medium'),
        ('128', 'Longest Consecutive Sequence', 'Medium'),
        ('271', 'Encode and Decode Strings', 'Medium')
    ]
    
    for num, name, difficulty in problems:
        # Python file
        py_file = f"python/arrays-hashing/{num}-{name.lower().replace(' ', '-')}.py"
        with open(py_file, 'w') as f:
            f.write(f'"""\n{num}. {name}\n\nDifficulty: {difficulty}\n"""\n\n')
        
        # Java file
        java_name = name.replace(' ', '')
        java_file = f"java/arrays-hashing/{java_name}.java"
        with open(java_file, 'w') as f:
            f.write(f'/**\n * {num}. {name}\n * Difficulty: {difficulty}\n */\n\n')
            f.write(f'public class {java_name} {{\n    // Implementation\n}}\n')
    
    print(f"✅ Created {len(problems) * 2} solution files")

if __name__ == "__main__":
    print("🚀 Setting up NeetCode 150 Week 1: Arrays & Hashing\n")
    #create_directory_structure()
    create_problem_files()
    print("\n🎉 Setup complete! Happy coding!")