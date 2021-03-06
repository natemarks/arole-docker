import pytest

""" use this exaple test later when we can actuslly run the service

"""


@pytest.mark.parametrize(
    "command,exit_code",
    [
        ("wget --version", 0),
        ("curl --version", 0),
        ("python3 --version", 0),
        ("ansible --version", 0),
        ("docker --version", 0),
        ("docker-compose --version", 0),
    ],
)
def test_run_binaries(host, command, exit_code):
    """Try to run  each of binaries we need in the image

    test the exit code for each
    """
    cmd = host.run(command)
    assert cmd.rc == exit_code


def test_docker(host):
    """Try to run  each of binaries we need in the image

    test the exit code for each
    """
    ubuntu_user = host.user("ubuntu")
    assert "docker" in ubuntu_user.groups
