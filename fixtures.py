import yaml
import os
import greengraph

def test_fix():
    with open(os.path.join(os.path.dirname(greengraph),
        'fixtures','samples.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
Writing fixtures.py