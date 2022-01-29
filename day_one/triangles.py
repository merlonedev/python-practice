def triangles(a, b, c):
    is_triangle = a + b > c and a + c > b and b + c > a
    if not is_triangle:
        print("não é triângulo")
    elif a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")


triangles(3, 4, 1)
