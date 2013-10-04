def move_rings(n, start, end, buff):
    if n == 1:
        end.append(start.pop())
        return

    move_rings(n-1, start, buff, end)
    end.append(start.pop())
    move_rings(n-1, buff, end, start)

def main():
    tower = [5,4,3,2,1]
    ending_tower = []
    b = []

    move_rings(len(tower), tower, ending_tower, b)

    print ending_tower

main()

