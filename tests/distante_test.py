from mlproject.distance import haversine

def test_distante():
    assert int(haversine(48.865070, 2.380009, 48.235070, 2.393409)) == 70

