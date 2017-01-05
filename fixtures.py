from nose.tools import assert_almost_equal,assert_equal
import yaml
import os
from .map import Map
from .graph import Greengraph

def test_fix():
    with open(os.path.join(os.path.dirname(greengraph),
        'fixtures','samples.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        g=Greengraph('','')
        lat_long=g.geocoder.geocode(t_info['Name'],exactly_one=False)[0][1]
        assert_almost_equal(t_info['Lat'],lat_long[0],places=2)
        assert_almost_equal(t_info['Long'],lat_long[1],places=2)
Writing fixtures.py