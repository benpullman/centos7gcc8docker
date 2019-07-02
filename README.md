# Dockerized SPS

### Getting Started

0. Make sure you have both Python and Docker installed on your computer.

1. Clone the repository and run *generate_container.py* with two arguments, the first (-s) is the absolute path to the sps codebase, and the second (-w) is the absolute path to your working directory.

2. Once this file is run, a directory called "generated" will be created and inside there will be 3 files in the directory.

3. Run *build.sh* in the "generated" directory.  This will create a docker image from the created Dockerfile.

### Running Docker

1. Run *start_container.sh* in the "generated" directory.  This will create a new docker contained from the newly created docker image.

### Using the Docker image to build and run SPS

1. Add the "bin" directory to your path.

2. You should now be able to run "dockermake" anywhere in your sps path to build the codebase or "convert" or "main_execmodule" anywhere in your working directory.
