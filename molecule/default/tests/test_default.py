import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_composer_exists(host):
    composer_executable = host.file('/usr/local/bin/composer')

    assert composer_executable.exists
    assert composer_executable.is_file
    assert composer_executable.mode == 0o755
