import requests

    def map_at(self, lat, long, satellite=True,
            zoom=10, size=(400,400), sensor=False):
        base="http://maps.googleapis.com/maps/api/staticmap?"

        params=dict(
        sensor= str(sensor).lower(),
        zoom= zoom,
        size= "x".join(map(str, size)),
        center= ",".join(map(str, (lat, long) )),
        style="feature:all|element:labels|visibility:off"
)

        if satellite:
            params["maptype"]="satellite"
        return requests.get(base,params=params)
    
    from mock import patch
    with patch.object(requests,'get') as mock_get:
        london_map=map_at(51.5073509, -0.1277583)
        print mock_get.mock_calls
        
        
    def test_build_default_params():
        with patch.object(requests,'get') as mock_get:
        default_map=map_at(51.0, 0.0)
        mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            'sensor':'false',
            'zoom':12,
            'size':'400x400',
            'center':'51.0,0.0',
            'style':'feature:all|element:labels|visibility:off'
            }
        )
    test_build_default_params()
    
    Writing mocking.py