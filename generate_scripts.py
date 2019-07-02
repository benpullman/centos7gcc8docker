import argparse
import sys
import os

def arguments():
    parser = argparse.ArgumentParser(description='Create a docker image for CCMS SPS codebase')
    parser.add_argument('-s','--sps_path', type = str, help='Path to SPS codebase')
    parser.add_argument('-w','--working_path', type = str, help='Working path for using codebase')
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()

def generate_startup(sps_path,data_path):
    startup_script = """#!/bin/bash

docker run -i -t -v {}:/_sps -v {}:{} --rm --name cluster proteosafe""".format(sps_path,data_path,data_path)

    if not os.path.exists("generated"):
        os.makedirs("generated")

    with open("generated/startdocker.sh","w") as w:
        w.write(startup_script)

def generate_build():

    build_script ="""#!/bin/bash

docker build -t proteosafe ."""

    with open("generated/build.sh","w") as w:
        w.write(build_script)

def main():
    args = arguments()
    generate_startup(args.sps_path,args.working_path)
    generate_build()

if __name__ == '__main__':
    main()
