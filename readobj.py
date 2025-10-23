def readobj(path):
    v, f = [], []
    with open(path, 'r') as file:
        data = file.readlines()
        for line in data:

            """
            if line.startswith('vn '):
                vn.append(line)
            elif line.startswith('vt '):
                vt.append(line)
            """

            if line.startswith('v '):
                v.append(line)
            elif line.startswith('f '):
                f.append(line)
    return v, f

monkey_v, monkey_f = readobj("monkey.obj")

def readfaces(faces):
    clean_faces = []
    for face in faces:
        face = face[1:-1] # remove f and \n
        clean_faces.append(face.split())
    
    finished_faces = []
    for face in clean_faces:
        usable_vertex = []
        for vertex in face:
            split_vertex = vertex.split("/")
            usable_vertex.append(int(split_vertex[0])) # must be int cuz we index list with this
        finished_faces.append(usable_vertex)
    return finished_faces

def readvertex(vertexes):
    clean_vertexes = []
    for vertex in vertexes:
        vertex = vertex[1:-1] # remove f and \n
        clean_vertexes.append(vertex.split())
    usable_vertexes = []
    for vertex in clean_vertexes:
        points = []
        for point in vertex:
            points.append(float(point))
        usable_vertexes.append(points)
    return usable_vertexes