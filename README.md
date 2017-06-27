# skeleton
A python script to manage skeleton files.

Setup:  
 * After downloading the repository, populate the `./skeletons` directory with skeleton files.
 * Add the repository to the system path.
```
usage: skeleton.py [-h] [-n [NAME]] skeltype [skelname]

positional arguments:
  skeltype              The file type of the skeleton
  skelname              The name of the skeleton file

optional arguments:
  -h, --help            show this help message and exit
  -n [NAME], --name [NAME]
                        The file name of the destination file
```
 Example commands:
   * `skeleton html`
   * `skeleton json manifest`
   * `skeleton gitignore`
   * `skeleton html --name index`
