class PointC0llision:

    def lenght_line(self, start: list, end: list) -> float:

        return pow((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2 + (start[2] - end[2]) ** 2, 0.5)

    def point_perestenie(self, otr_1: ((), (),), otr_2: ((), (),)) -> list:

        lm = self.lenght_line(otr_1[0], otr_2[0])
        sum_radius = otr_1[2] + otr_2[2]
        step = 0.01 * self.lenght_line(otr_1[0], otr_1[1])
        two_plus = 0
        lenght_start = self.lenght_line(otr_1[0], otr_2[0]) # растояние между начальными точками
        lenght_point_1 = self.lenght_line(otr_1[0], otr_1[1]) # велечена перемещения точки 1
        lenght_point_2 = self.lenght_line(otr_2[0], otr_2[1]) # # велечена перемещения точки 2

        sin_a = (otr_1[1][0] - otr_1[0][0]) / lenght_point_1  # изменение х при перемещению точки по lb
        cos_a = (otr_1[1][1] - otr_1[0][1]) / lenght_point_1  # изменение y при перемещению точки по lb
        z_l_a = (otr_1[1][2] - otr_1[0][2]) / lenght_point_1  # изменение z при перемещению точки по lb
        sin_b = (otr_2[1][2] - otr_2[0][2]) / lenght_point_2  # изменение х при перемещению точки по la
        cos_b = (otr_2[1][2] - otr_2[0][2]) / lenght_point_2  # изменение y при перемещению точки по la
        z_l_b = (otr_2[1][2] - otr_2[0][2]) / lenght_point_2  # изменение z при перемещению точки по la

        def find_point(lbd: float):

            res = lenght_start - sum_radius
            lbd = lbd
            lac = lbd * (lenght_point_2 / lenght_point_1)

            x_c = otr_1[0][0] + lbd * sin_a
            y_c = otr_1[0][1] + lbd * cos_a
            z_l_c = otr_1[0][2] + lbd * z_l_a
            x_d = otr_2[0][0] + lac * sin_b
            y_d = otr_2[0][1] + lac * cos_b
            z_l_d = otr_2[0][2] + lac * z_l_b
            l1 = self.lenght_line([x_c, y_c, z_l_c], [x_d, y_d, z_l_d])
            ####################################################
            #if lb + 0.05 < lbd <= lac:  # огранечение если точки не должны выдти за рамки отрезка
            #    return False,
            #if la + 0.05 < lac <= lbd:
            #    return False,  # огранечение если точки не должны выдти за рамки отрезка
            ########################################################
            if 0.05 > sum_radius - l1 > 0:  # 0.05 погрешность поиска
                return True, x_c, y_c, z_l_c, x_d, y_d, z_l_d
            if l1 >= lenght_start and i == 0:
                return False,
            nonlocal lm
            b = lm - sum_radius
            lm = l1
            nonlocal two_plus
            b1 = lm - sum_radius
            two_plus = "++" if b1 > b else "--"
            f = (lenght_start - l1)
            df = (res / f)
            k = df * lbd
            return k, x_c, y_c, z_l_c, x_d, y_d, z_l_d

        i = 0
        while True:
            c = (find_point(step))
            if c[0]:
                c1 = c[0]
                if c1 == True:
                    return find_point(step)[1::]
                if c1 == False:
                    return False
                step = (find_point(c1)[0])
                if step == False:
                    return False
                if step == True:
                    return find_point(c1)[1::]
            else:
                return False
            if two_plus == "++":  # bb  нужно

                return False
            if i > 10:
                return False
            i += 1

    def result_coord(self, coords, radius_1, radius_2):
        x = (coords[3] - coords[0]) / (radius_1 + radius_2) * radius_1
        y = (coords[4] - coords[1]) / (radius_1 + radius_2) * radius_1
        z = (coords[5] - coords[2]) / (radius_1 + radius_2) * radius_1
        return coords, coords[0] + x, coords[1] + y, coords[2] + z

    def work(self, start_coord_1, end_coord_1, radius_1, start_coord_2, end_coord_2, radius_2):
        res = self.point_perestenie((start_coord_1, end_coord_1, radius_1), (start_coord_2, end_coord_2, radius_2))

        return self.result_coord(res, radius_1, radius_2) if res != False else False


if __name__ == "__main__":
    p = PointC0llision()
    v = p.work((0, 0, 0), (400, 400, 400), 10, (2000, 2000, 2000), (1600, 1600, 1600,), 4)
    print(v)
