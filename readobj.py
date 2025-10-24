import math

class point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

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
        point = point3d(float(vertex[0]), float(vertex[1]), float(vertex[2]))
        usable_vertexes.append(point)
    return usable_vertexes

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
    return readvertex(v), readfaces(f)