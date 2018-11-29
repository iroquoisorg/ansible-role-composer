import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_composer_exists(host):
    f = host.file('/usr/local/bin/composer')

    assert f.exists
    assert f.is_file
    assert f.mode == 0o755
