<h1>.fastaq.gz to .fasta file converter</h1>

This is a project developed in Python with the sys, gzip and biopython libraries. The script is capable of converting .fastaq.gz files to .fasta.

<h3>Requirements</h3>

Before using this script, you must have installed `Python 3.x` and the `sys`, `gzip` and `biopython` libraries. If not, you can install them using pip:

```
pip install sys gzip biopython
```

<h3>How to use</h3>

To use the script, open the terminal in the folder where the `converter.py` file is located and execute the following command:

```
python converter.py 'file1.fastaq.gz' 'file2.fastaq.gz' 'file3.fastaq.gz'
```

Replace `file1.fastaq.gz`, `file2.fastaq.gz` and `file3.fastaq.gz` with the names of the files you want to convert. You can convert as many files as you like, just add them as arguments to the command.

The script output will be saved in the same folder where the `fastaq.gz` file was obtained.

<h3>Example</h3>

Suppose you want to convert `example1.fastaq.gz` and `example2.fastaq.gz` files. To do so, open a terminal in the folder where the `converter.py` file is located and run the following command:

```
python converter.py 'exemplo1.fastaq.gz' 'exemplo2.fastaq.gz'
```

After executing the script, `example1.fasta` and `example2.fasta` files will be created in the same folder where `example1.fastaq.gz` and `example2.fastaq.gz` files were obtained.

<h3>Contributions</h3>

Contributions are always welcome! Feel free to fork this repository and submit pull requests with improvements and bug fixes.
