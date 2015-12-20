class HtmlOutputer():
    def __init__(self):
        self.dataSet = []

    def collect_data(self, data):
        if data is None:
            return
        self.dataSet.append(data)

    def output_html(self):

        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.dataSet:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
