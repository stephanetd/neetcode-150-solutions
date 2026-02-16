import os

def create_directory():
    """Create the directory structure for Week 2"""
    directories = [
        'python/stack_linked_list',
        'java/stack_linked_list',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created: {directory}")
    
    print("\n✅ Directory structure created!")

def create_problem_files():
    """Create empty solution files for all Week 2 problems with enhanced templates"""
    problems = [
        ('20', 'Valid Parentheses', 'Easy'),
        ('394', 'Decode String', 'Medium'),
        ('155', 'Min Stack', 'Medium'),
        ('150', 'Evaluate Polish Reverse Notation', 'Medium'),
        ('739', 'Daily Temperatures', 'Medium'),
        ('853', 'Car Fleet', 'Medium'),
        ('84', 'Largest Rectangle in Histogram', 'Hard'),
        ('206', 'Reverse Linked List', 'Easy'),
        ('21', 'Merge Two Sorted Lists', 'Easy'),
        ('141', 'Linked List Cycle', 'Easy'),
        ('143', 'Reorder List', 'Medium'),
        ('19', 'Remove Nth Node From End of List', 'Medium'),
        ('138', 'Copy List From Random Pointer', 'Medium'),
        ('2', 'Add Two Numbers', 'Medium'),
        ('146', 'LRU Cache', 'Medium'),
        ('23', 'Merge k Sorted Lists', 'Hard'),
        ('25', 'Reverse Nodes in k-Group', 'Hard')
    ]
    
    for num, name, difficulty in problems:
        # Format file names
        slug_name = name.lower().replace(' ', '-').replace('---', '-')
        
        # Python file
        py_file = f"python/stack_linked_list/{num}-{slug_name}.py"
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
        java_file = f"java/stack_linked_list/{java_name}.java"
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
    print(f"📁 Python files: python/stack_linked_list/")
    print(f"📁 Java files: java/stack_linked_list/")

if __name__ == "__main__":
    print("🚀 Setting up NeetCode 150 Week 3: Stack & Linked List\n")
    create_directory()
    create_problem_files()
    print("\n🎉 Setup complete! Happy coding!")