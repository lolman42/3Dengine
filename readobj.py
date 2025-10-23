def readobj(path):
    v, f = [], []
    with open(path, 'r') as file:

            """
            if line.startswith('vn '):
                vn.append(line)
            elif line.startswith('vt '):
                vt.append(line)
            """

            if line.startswith('v '):
                v.append(data)
            elif line.startswith('f '):
                f.append(data)
    return v, f

def readfaces(faces):

def readvertex(vertexes):

