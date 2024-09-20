import os
from groq import Groq
from argparse import ArgumentParser
from dotenv import load_dotenv

# Tool Info
TOOL_NAME = "ReadMeMaker"
VERSION = "v0.1"

# Load environment variables from .env file
load_dotenv()

# Initializing Groq Client
def initialize_groq_client(api_key=None):
    # Uses default API key inside the .env file
    if api_key is None:
        api_key = os.getenv("GROQ_API_KEY")
    
    # Error handler if no api key is specified in the .env file or by the user
    if api_key is None:
        raise ValueError("API key must be provided either directly or through the environment variable.")

    return Groq(api_key=api_key)

# Function to generate README content using Groq
def generate_readme(input_content, client, user_model):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant to the user",
            },
            {
                "role": "user",
                "content": f"Generate a README.md file for the following input files:\n\n{input_content}",
            }
        ],
        model=user_model,
    )

    return chat_completion.choices[0].message.content

# CLI Setup
def main():
    # Set up argument parser
    parser = ArgumentParser(description="Generate a README.md file for the specified input files.")
    parser.add_argument("-i", "--input", nargs='+', required=True, help="The input files for which to generate a README.md.")
    parser.add_argument("-o", "--output", default=os.path.join(os.getcwd(), "README.md"), help="Specify the output file name and file path (default: Creates a README.md file in the same directory).")
    parser.add_argument("-v", "--version", action="version", version=f"{TOOL_NAME} {VERSION}", help="Show the version of the tool.")
    parser.add_argument("-m", "--model", default="llama3-8b-8192", help="Specify the model to use (default: llama3-8b-8192).")

    # Parse arguments
    args = parser.parse_args()

    # Read the contents of the input files using list comprehension
    input_contents = [open(input_file).read() for input_file in args.input]

    # Combine all input contents into a single string
    combined_input_content = "\n\n".join(input_contents)

    # Initialize Groq client
    client = initialize_groq_client()

    # Generate README content
    readme_content = generate_readme(combined_input_content, client, args.model)

    # Determine output file path
    output_file_path = args.output if args.output else "README.md"

    # Write the README content to the specified output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(readme_content)

    print(f"README.md has been created at: {os.path.abspath(output_file_path)}")

if __name__ == "__main__":
    main()
