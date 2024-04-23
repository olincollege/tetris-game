def fall(self):
    for square in self.coordinates:
        square[0] -= 1


def move_left(self):
    for sqaure in self.coordinates:
        square[1] -= 1


def move_right(self):
    for square in self.coordinates:
        square[1] += 1


# I rotation
def rotate_cw(self, orientation):
    if orientation % 2 == 1:
        for i in range(4):
            self.coordinates[i][0] += i
            self.coordinates[i][1] += i

    if orientation % 2 == 0:
        for i in range(4):
            self.coordinates[i][0] -= i
            self.coordinates[i][1] -= i


# J rotation
def rotate_cw(self, orientation):
    if orientation == 1:
        self.coordinates[0][0] += 1

        self.coordinates[1][1] -= 1

        self.coordinates[2][0] -= 1

        self.coordinates[3][0] -= 2
        self.coordinates[3][1] += 1

    elif orientation == 2:
        self.coordinates[0][0] += 1
        self.coordinates[0][1] += 1

        self.coordinates[1][0] += 2

        self.coordinates[2][0] += 1
        self.coordinates[2][1] -= 1

        self.coordinates[3][1] -= 2

    elif orientation == 3:
        self.coordinates[0][0] -= 1
        self.coordinates[0][1] += 1

        self.coordinates[1][1] += 2

        self.coordinates[2][0] += 1
        self.coordinates[2][1] += 1

        self.coordinates[3][0] += 2

    elif orientation == 0:
        self.coordinates[0][0] -= 1
        self.coordinates[0][1] -= 2

        self.coordinates[1][0] -= 2
        self.coordinates[1][1] -= 1

        self.coordinates[2][0] -= 1

        self.coordinates[3][1] += 1


def rotate_ccw(self, orientation):
    if orientation == 3:
        self.coordinates[0][0] += 1
        self.coordinates[0][1] += 2

        self.coordinates[1][0] += 2
        self.coordinates[1][1] += 1

        self.coordinates[2][0] += 1

        self.coordinates[3][1] -= 1

    elif orientation == 2:
        self.coordinates[0][0] += 1
        self.coordinates[0][1] -= 1

        self.coordinates[1][1] -= 2

        self.coordinates[2][0] -= 1
        self.coordinates[2][1] -= 1

        self.coordinates[3][0] -= 2

    elif orientation == 1:
        self.coordinates[0][0] -= 1
        self.coordinates[0][1] -= 1

        self.coordinates[1][0] -= 2

        self.coordinates[2][0] -= 1
        self.coordinates[2][1] += 1

        self.coordinates[3][1] += 2

    elif orientation == 0:
        self.coordinates[0][0] -= 1

        self.coordinates[1][1] += 1

        self.coordinates[2][0] += 1

        self.coordinates[3][0] += 2
        self.coordinates[3][1] -= 1


# L rotation
def rotate_cw(self, orientation):
    if orientation == 1:
        self.coordinates[0][0] += 1
        self.coordinates[0][1] += 1

        self.coordinates[2][0] -= 1
        self.coordinates[2][1] -= 1

        self.coordinates[3][1] -= 2

    elif orientation == 2:
        self.coordinates[0][0] += 1

        self.coordinates[1][1] += 1

        self.coordinates[2][0] -= 1
        self.coordinates[2][1] += 2

        self.coordinates[3][0] -= 2
        self.coordinates[3][1] += 1

    elif orientation == 3:
        self.coordinates[0][1] -= 2

        self.coordinates[1][0] += 1
        self.coordinates[1][1] -= 1

        self.coordinates[2][0] += 2

        self.coordinates[3][0] += 1
        self.coordinates[3][1] += 1

    elif orientation == 0:
        self.coordinates[0][0] -= 2
        self.coordinates[0][1] += 1

        self.coordinates[1][0] -= 1

        self.coordinates[2][1] -= 1

        self.coordinates[3][0] += 1


def rotate_ccw(self, orientation):
    if orientation == 3:
        self.coordinates[0][0] += 2
        self.coordinates[0][1] -= 1

        self.coordinates[1][0] += 1

        self.coordinates[2][1] += 1

        self.coordinates[3][0] -= 1

    if orientation == 2:
        self.coordinates[0][1] += 2

        self.coordinates[1][0] -= 1
        self.coordinates[1][1] += 1

        self.coordinates[2][0] -= 2

        self.coordinates[3][0] -= 1
        self.coordinates[3][1] -= 1

    if orientation == 1:
        self.coordinates[0][0] -= 1

        self.coordinates[1][1] -= 1

        self.coordinates[2][0] += 1
        self.coordinates[2][1] -= 2

        self.coordinates[3][0] += 2
        self.coordinates[3][1] -= 1

    if orientation == 0:
        self.coordinates[0][0] -= 1
        self.coordinates[0][1] -= 1

        self.coordinates[2][0] += 1
        self.coordinates[2][1] += 1

        self.coordinates[3][1] += 2


# S rotation
def rotate_cw(self, orientation):
    if orientation == 1:
        self.coordinates[0][0] += 2

        self.coordinates[1][0] += 1
        self.coordinates[1][1] += 1

        self.coordinates[3][0] -= 1
        self.coordinates[3][1] += 1

    if orientation == 0:
        self.coordinates[0][0] -= 2

        self.coordinates[1][0] -= 1
        self.coordinates[1][1] -= 1

        self.coordinates[3][0] += 1
        self.coordinates[3][1] -= 1


# Z rotation
def rotate_cw(self, orientation):
    if orientation == 1:
        self.coordinates[0][1] += 2

        self.coordinates[1][0] += 1

        self.coordinates[2][1] += 1

        self.coordinates[3][0] += 1
        self.coordinates[3][1] -= 1

    if orientation == 0:
        self.coordinates[0][1] -= 2

        self.coordinates[1][0] -= 1

        self.coordinates[2][1] -= 1

        self.coordinates[3][0] -= 1
        self.coordinates[3][1] += 1


# T rotation
def rotate_cw(self, orientation):
    if orientation == 1:
        self.coordinates[0][1] += 2

        self.coordinates[1][0] += 1
        self.coordinates[1][1] += 1

        self.coordinates[2][0] += 2

    if orientation == 2:
        self.coordinates[0][0] += 2

        self.coordinates[1][0] += 1
        self.coordinates[1][1] -= 1

        self.coordinates[2][1] -= 2

    if orientation == 3:
        self.coordinates[0][1] -= 2

        self.coordinates[1][0] -= 1
        self.coordinates[1][1] -= 1

        self.coordinates[2][0] -= 2

    if orientation == 0:
        self.coordinates[0][0] -= 2

        self.coordinates[1][0] -= 1
        self.coordinates[1][1] += 1

        self.coordinates[2][1] += 2


def rotate_ccw(self, orientation):
    if orientation == 3:
        self.coordinates[0][0] += 2

        self.coordinates[1][0] += 1
        self.coordinates[1][1] -= 1

        self.coordinates[2][1] -= 2

    if orientation == 2:
        self.coordinates[0][1] += 2

        self.coordinates[1][0] += 1
        self.coordinates[1][1] += 1

        self.coordinates[2][0] += 2

    if orientation == 1:
        self.coordinates[0][0] -= 2

        self.coordinates[1][0] -= 1
        self.coordinates[1][1] += 1

        self.coordinates[2][1] += 2

    if orientation == 0:
        self.coordinates[0][1] -= 2

        self.coordinates[1][0] -= 1
        self.coordinates[1][1] -= 1

        self.coordinates[2][0] -= 2
