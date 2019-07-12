import argparse
import sys

def recover(data: str, file: str) -> str:
    file.write(bytearray(data[0:1024]))
    for chunk in range(1024, len(data) - 3072, 3072):
        print(chunk)
        file.seek(chunk)
        file.write(bytearray(data[chunk:chunk+2048]))
        file.write(bytearray(data[chunk+2048:chunk+3072][::-1]))
        file.seek(0)
    file.close()
    return "Recovery completed in same file"

def recover_as(data: str, file: str) -> str:
    with open(file, "wb+") as f:
        f.write(bytearray(data[0:1024]))
        for chunk in range(1024, len(data) - 3072, 3072):
            f.write(bytearray(data[chunk:chunk+2048]))
            f.write(bytearray(data[chunk+2048:chunk+3072][::-1]))

    return "Recovery completed in givven output file"


def parsing():
    parser = argparse.ArgumentParser(description="This program is designed to \
    recover damaged jpg file")
    parser.add_argument("file", metavar="", help="input jpg file")
    parser.add_argument("-o", "--output", metavar="", help="recovered file")
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    f = open(args.file, "rb+")
    data = f.read().strip()

    if args.output:
        return recover_as(data, args.output)
        f.close()
    else:
        return recover(data, f)

print(parsing())
