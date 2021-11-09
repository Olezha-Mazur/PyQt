import matplotlib.pyplot as plt
# s = input()
# i = 1
# a = []
# while s != '':
#     s = input().rstrip('\t').rstrip('\n')
#     s1 = ''
#     for j in s:
#         if j == ',':
#             s1 += '.'
#         elif j != ' ':
#             s1 += j
#     i += 1
#     if i % 24 == 3:
#         a.append(round(eval(s1), 2))
# for i in range(len(a)):
#     print(a[i])
import datetime as dt
print((dt.date(2019, 12, 1) - dt.date(2019, 11, 2)).days)
print(dt.date.today())

# def update_history(self, summ, event):
    #     summ = summ
    #     hour = dt.datetime.now().time().hour
    #     minute = dt.datetime.now().time().minute
    #     second = dt.datetime.now().time().second
    #     time = f'{hour}-{minute}-{second}'
    #     data = dt.date.today()
    #     event = event
    #     con = sqlite3.connect('history1.db')
    #     cur = con.cursor()
    #     self.index += 1
    #     que = 'UPDATE history\n'
    #     que += f"SET Event = '{event}', summ = {summ}, " \
    #            f"time = '{time}', data = '{data}'\n"
    #     que += f'WHERE id = {self.index}'
    #     result = cur.execute(que).fetchall()
    #
    #     con.commit()
    #     con.close()


# def save(self):
    #     with open("Info.txt", mode='w', encoding='utf-8') as g:
    #         g.write(self.name)
    #         g.write('\n')
    #         g.write(str(self.score))
    #         g.write('\n')
    #         g.write(str(self.index))



# def create_pie(self, vals, labels):
    #     series = QPieSeries()
    #     vals = list(vals)
    #     labels = list(labels)
    #     for i in range(len(vals)):
    #         series.append(labels[i], int(vals[i]))
    #     slice = series.slices()[:]
    #     # slice.setExploded(True)
    #     # slice.setLabelVisible(True)
    #     for i in slice:
    #         i.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    #         # i.setPen(Qt.darkgreen)
    #
    #     chart = QChart()
    #     chart.legend().hide()
    #     chart.addSeries(series)
    #     chart.createDefaultAxes()
    #     chart.setAnimationOptions(QChart.SeriesAnimations)
    #     chart.setTitle("Pie Chart Example")
    #
    #     chart.legend().setVisible(True)
    #     chart.legend().setAlignment(Qt.AlignBottom)
    #
    #     self.chartview = QChartView(chart)
    #     self.chartview.setRenderHint(QPainter.Antialiasing)
    #     self.chartview.setGeometry(10, 100, 210, 210)

    # CentralWidgetLayout = QHBoxLayout()
    # # CentralWidgetLayout.setGeometry(10, 200, 210, 400)
    # CentralWidgetLayout.addWidget(chartview)