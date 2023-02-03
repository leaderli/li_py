import logging
import subprocess
from subprocess import Popen, PIPE


def run(command: str) -> None:
    """
    :param command:  shell statement
    :return:
    """
    logging.debug(command)
    subprocess.run(command, shell=True, universal_newlines=True)


def call(command: str) -> str:
    logging.debug(command)
    with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True) as fd:
        out, err = fd.communicate()
        if fd.returncode:
            raise Exception(err.strip())
        logging.debug(out.strip())
        return out.strip()


def ssh_call(address, work_dir, command):
    return call(
        """
        ssh -q {address}  'cd {work_dir} && {command}'
        """.format(address=address, work_dir=work_dir, command=command)
    )
