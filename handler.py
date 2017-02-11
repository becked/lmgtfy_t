import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
site_pkgs = os.path.join(cwd, "venv", "lib", "python2.7", "site-packages")
sys.path.append(site_pkgs)

from lmgtfy_t import lmgtfy_t

def __main():
    reply = lmgtfy_t.main()

    response = {
        'statusCode': 200,
        'body': reply
    }
    return response;

def main(event, context):
    __main();

if __name__ == "__main__":
    print(__main())
