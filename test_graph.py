from graph import geolocate
from graph import location_sequence
from graph import green_between    
    
    def test_geolocate(self)
        s=graph.geolocate()
        self.assertTrue(insistance,(s,str))
    
    def test_location_sequence(self)
        array=np.vstack([lats,longs]).transpose
        if array.dtype.kind != 'r' and len(array) > 0:
            raise TypeError("array should be an array of *reals*.")
    
    def test_green(self)
        i=graph.green_between()
        self.assertTrue(insistance,(i,int))
Writing test_graph