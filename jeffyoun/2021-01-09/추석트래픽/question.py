from operator import itemgetter
import re


def solution(lines):
    logs = []

    p = re.compile("[0-9,-]* (\\d{2}):(\\d{2}):(\\d{2}).(\\d{3}) (\\d)[.]?(\\d{1,3})?s")

    for log in lines:
        timeNumber = 0
        m = p.search(log)

        parsedList = list(map(int, [m.group(i + 1) for i in range(4)]))
        timeNumber += ((parsedList[0] * 60 + parsedList[1]) * 60 + parsedList[2]) * 1000 + parsedList[3]

        processTime = int(m.group(5)) * 1000 + (m.group(6) and int(m.group(6)) or 0)

        logs.append(("0start", timeNumber - processTime + 1))
        logs.append(("1end", timeNumber + 999))

    logs = sorted(logs, key=itemgetter(1, 0))

    [maxCount, count] = [0, 0]

    for [typeName, _] in logs:
        if typeName == "0start":
            count += 1
        else:
            maxCount = max(maxCount, count)
            count -= 1

    return maxCount


test = ["2016-09-15 20:59:57.421 0.001s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"]
print(solution(test))
