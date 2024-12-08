from helpers import read_file, execute


def part_one(file_name="02/data/2.in"):
    reports = read_file(file_name)
    total = 0
    for report in reports:
        readings = report.split(" ")
        sign = "P" if int(readings[0]) - int(readings[1]) > 0 else "N"
        safe = True
        for i in range(len(readings) - 1):
            difference = int(readings[i]) - int(readings[i + 1])
            if difference > 3 or difference < -3:
                safe = False
                break
            elif difference < 0 and sign == "P":
                safe = False
                break
            elif difference > 0 and sign == "N":
                safe = False
                break
            elif difference == 0:
                safe = False
                break
        if safe == True:
            total += 1
        safe = True

    print(f"Part One: {total}")
    return total


def part_two(file_name="02/data/2.in"):
    def check_readings(readings):
        sign = "P" if int(readings[0]) - int(readings[1]) > 0 else "N"
        for i in range(len(readings) - 1):
            difference = int(readings[i]) - int(readings[i + 1])
            if difference > 3 or difference < -3:
                return False
            elif difference < 0 and sign == "P":
                return False
            elif difference > 0 and sign == "N":
                return False
            elif difference == 0:
                return False
        return True

    reports = read_file(file_name)
    total = 0
    for report in reports:
        readings = report.split(" ")
        for i in range(len(readings)):
            safe = check_readings(readings[:i] + readings[i + 1 :])
            if safe:
                total += 1
                break
        sign = "P" if int(readings[0]) - int(readings[1]) > 0 else "N"

    print(f"Part Two: {total}")
    return total


if __name__ == "__main__":
    execute(part_one, part_two)
