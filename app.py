import json
import sys


def convert_notebook_to_script(notebook_path, script_path):
    # Read the notebook file
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = json.load(notebook_file)

    # Open the output script file
    with open(script_path, 'w', encoding='utf-8') as script_file:
        # Write a header comment
        script_file.write(f"# Converted from {notebook_path}\n\n")

        # Iterate through the notebook cells
        for cell in notebook_content['cells']:
            if cell['cell_type'] == 'code':
                # Write code cells
                script_file.write('# In[]\n')
                script_file.write(''.join(cell['source']))
                script_file.write('\n\n')
            elif cell['cell_type'] == 'markdown':
                # Convert markdown cells to comments
                script_file.write('# ' + '# '.join(cell['source']))
                script_file.write('\n\n')

    print(f"Conversion complete. Python script saved to {script_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_notebook.ipynb> <output_script.py>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    script_path = sys.argv[2]

    convert_notebook_to_script(notebook_path, script_path)
