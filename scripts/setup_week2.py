import os

def create_directory():
    """Create the directory structure for Week 2"""
    directories = [
        'python/two-pointers-sliding-window',
        'java/two-pointers-sliding-window',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created: {directory}")
    
    print("\n✅ Directory structure created!")

def create_problem_files():
    """Create empty solution files for all Week 2 problems with enhanced templates"""
    problems = [
        ('125', 'Valid Palindrome', 'Easy'),
        ('121', 'Best Time to Buy and Sell Stock', 'Easy'),
        ('167', 'Two Sum II - Input Array Is Sorted', 'Medium'),
        ('15', '3Sum', 'Medium'),
        ('11', 'Container With Most Water', 'Medium'),
        ('42', 'Trapping Rain Water', 'Hard'),
        ('3', 'Longest Substring Without Repeating Characters', 'Medium'),
        ('424', 'Longest Repeating Character Replacement', 'Medium'),
        ('567', 'Permutation in String', 'Medium'),
        ('76', 'Minimum Window Substring', 'Hard'),
        ('239', 'Sliding Window Maximum', 'Hard')
    ]
    
    for num, name, difficulty in problems:
        # Format file names
        slug_name = name.lower().replace(' ', '-').replace('---', '-')
        
        # Python file
        py_file = f"python/two-pointers-sliding-window/{num}-{slug_name}.py"
        with open(py_file, 'w') as f:
            f.write(f'"""\n')
            f.write(f'{num}. {name}\n\n')
            f.write(f'Difficulty: {difficulty}\n')
            f.write(f'Topics: Two Pointers, Sliding Window\n\n')
            f.write(f'Problem:\n')
            f.write(f'[Brief description of the problem]\n\n')
            f.write(f'Approach:\n')
            f.write(f'[Brief explanation of approach]\n\n')
            f.write(f'Key Insights:\n')
            f.write(f'1. \n\n')
            f.write(f'Edge Cases:\n')
            f.write(f'1. \n\n')
            f.write(f'Complexity:\n')
            f.write(f'Time: O() - [Explanation]\n')
            f.write(f'Space: O() - [Explanation]\n')
            f.write(f'"""\n\n')
            f.write(f'def solution():\n')
            f.write(f'    pass\n\n')
            f.write(f'if __name__ == "__main__":\n')
            f.write(f'    # Test cases\n')
            f.write(f'    pass\n')
        
        # Java file
        java_name = ''.join(word.title() for word in name.split())
        java_file = f"java/two-pointers-sliding-window/{java_name}.java"
        with open(java_file, 'w') as f:
            f.write(f'/**\n')
            f.write(f' * {num}. {name}\n')
            f.write(f' * Difficulty: {difficulty}\n')
            f.write(f' * Topics: Two Pointers, Sliding Window\n')
            f.write(f' * \n')
            f.write(f' * Problem:\n')
            f.write(f' * [Brief description of the problem]\n')
            f.write(f' * \n')
            f.write(f' * Approach:\n')
            f.write(f' * [Brief explanation of approach]\n')
            f.write(f' * \n')
            f.write(f' * Key Insights:\n')
            f.write(f' * 1. \n\n')
            f.write(f' * Edge Cases:\n')
            f.write(f' * 1. \n\n')
            f.write(f' * Complexity:\n')
            f.write(f' * Time: O() - [Explanation]\n')
            f.write(f' * Space: O() - [Explanation]\n')
            f.write(f' */\n\n')
            f.write(f'public class {java_name} {{\n')
            f.write(f'    public static void main(String[] args) {{\n')
            f.write(f'        // Test cases\n')
            f.write(f'    }}\n\n')
            f.write(f'    public static Object solution() {{\n')
            f.write(f'        return null;\n')
            f.write(f'    }}\n')
            f.write(f'}}\n')
    
    print(f"✅ Created {len(problems) * 2} solution files with enhanced templates")
    print(f"📁 Python files: python/two-pointers-sliding-window/")
    print(f"📁 Java files: java/two-pointers-sliding-window/")

if __name__ == "__main__":
    print("🚀 Setting up NeetCode 150 Week 2: Two Pointers & Sliding Window\n")
    create_directory()
    create_problem_files()
    print("\n🎉 Setup complete! Happy coding!")