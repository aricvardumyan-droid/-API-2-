def to_spn(toponym):
    bounds = tuple(map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split())), tuple(
        map(float, toponym['boundedBy']['Envelope']['upperCorner'].split())
    )
    return (abs(bounds[0][0] - bounds[1][0]), abs(bounds[0][1] - bounds[1][1]))
