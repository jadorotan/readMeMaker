**ReadMeMaker**
================

**Version:** v0.1

**Tool Description:**
ReadMeMaker is a tool that generates a README.md file for the specified input files using Groq's Chat Completion API. It uses a provided model to complete the README content based on the input files.

**Prerequisite Dependencies:**
------------
In order you use this tool, you must install the required dependencies by running the command
```
pip install -r requirements.txt
```
**Usage:**
------------

To use ReadMeMaker, simply run the command and specify the input files and model you want to use.

**Example usage:**
```
python read_memaker.py -i input1.txt input2.py -o output.md -m llama3-8b-8192
```
This command will generate a README.md file using the input files `input1.txt` and `input2.py`, and write the output to the file `output.md`. The `llama3-8b-8192` will be the default model to be used to generate the README content.

**Options:**
------------

* `-i, --input`: Specify the input file(s) for which to generate a README.md.
* `-o, --output`: Specify the output file name and file path. Default is `README.md` file located in the same directory.
* `-m, --model`: Specify the model to use. Default is `llama3-8b-8192`.
* `-v, --version`: Show the version of the tool.

**Demo:**
------------
![YouTube Video](https://www.youtube.com/embed/5jO_uVnIooE)

**Troubleshooting:**
-------------------

If you encounter any issues while using ReadMeMaker, you can try the following:

* Check that the input files are valid and readable.
* Verify that the output file path is correct.
* Make sure the Groq client is properly initialized and the model is correctly specified.
* Make sure to specify the API key in a .env file or define it inside the Python program.

**Acknowledgments:**
-----------------

ReadMeMaker uses the Groq client and is powered by a Chat Completion AI model. Any wrong/inaccurate information will likely occur and user review is most likely necessary.

**License:**
---------

ReadMeMaker is released under the [MIT License](https://opensource.org/licenses/MIT).

**Contact:**
----------

If you have any questions, suggestions, or feedback about ReadMeMaker, please feel free to reach out and contact me at [jadorotan@myseneca.ca].