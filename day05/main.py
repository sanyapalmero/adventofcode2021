from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


@dataclass
class Point:
    x: int
    y: int


@dataclass
class LineSegment:
    start: Point
    end: Point

    def get_cover_points(self) -> list[Point]:
        cover_points = []
        if self.start.x == self.end.x:
            start = min([self.start.y, self.end.y])
            end = max([self.start.y, self.end.y]) + 1
            for i in range(start, end):
                cover_points.append(Point(x=self.start.x, y=i))
        elif self.start.y == self.end.y:
            start = min([self.start.x, self.end.x])
            end = max([self.start.x, self.end.x]) + 1
            for i in range(start, end):
                cover_points.append(Point(x=i, y=self.start.y))
        else:
            points_count = abs(self.start.x - self.end.x) + 1
            if self.start.x > self.end.x and self.start.y > self.end.y:
                for i in range(points_count):
                    cover_points.append(Point(x=self.start.x - i, y=self.start.y - i))
            elif self.start.x < self.end.x and self.start.y < self.end.y:
                for i in range(points_count):
                    cover_points.append(Point(x=self.start.x + i, y=self.start.y + i))
            elif self.start.x > self.end.x and self.start.y < self.end.y:
                for i in range(points_count):
                    cover_points.append(Point(x=self.start.x - i, y=self.start.y + i))
            elif self.start.x < self.end.x and self.start.y > self.end.y:
                for i in range(points_count):
                    cover_points.append(Point(x=self.start.x + i, y=self.start.y - i))

        return cover_points


@dataclass
class SegmentsList:
    segments: list[LineSegment]

    def get_horizontal_and_vertical_lines(self) -> "SegmentsList":
        lines = []
        for line in self.segments:
            if line.start.x == line.end.x or line.start.y == line.end.y:
                lines.append(line)
        return SegmentsList(lines)

    def get_max_x_and_y(self):
        max_x = 0
        max_y = 0

        for line in self.segments:
            current_max_x = line.start.x if line.start.x > line.end.x else line.end.x
            if current_max_x > max_x:
                max_x = current_max_x

            current_max_y = line.start.y if line.start.y > line.end.y else line.end.y
            if current_max_y > max_y:
                max_y = current_max_y

        return max_x, max_y


def parse_input(input_txt) -> SegmentsList:
    data = []

    input_txt = input_txt.splitlines()
    for line in input_txt:
        start, end = line.split("->")
        x1, y1 = start.rstrip().split(",")
        x2, y2 = end.lstrip().split(",")
        segment = LineSegment(
            start=Point(x=int(x1), y=int(y1)),
            end=Point(x=int(x2), y=int(y2)),
        )
        data.append(segment)

    return SegmentsList(data)


def create_empty_diagram(size_x, size_y):
    diagram = []
    for _ in range(size_x + 1):
        row = []
        for _ in range(size_y + 1):
            row.append(0)
        diagram.append(row)
    return diagram


def fill_diagram(diagram, data: SegmentsList):
    segments = data.segments
    for point in segments:
        cover_points = point.get_cover_points()
        for cover_point in cover_points:
            diagram[cover_point.y][cover_point.x] += 1
    return diagram


def count_overlaps(diagram):
    overlaps = 0
    for row in diagram:
        for elem in row:
            if elem > 1:
                overlaps += 1
    return overlaps


def part_1(input_txt):
    segments_list = parse_input(input_txt)
    straight_lines = segments_list.get_horizontal_and_vertical_lines()
    max_x, max_y = straight_lines.get_max_x_and_y()
    diagram = create_empty_diagram(max_x, max_y)
    diagram = fill_diagram(diagram, straight_lines)
    overlaps = count_overlaps(diagram)
    return overlaps


def part_2(input_txt):
    segments_list = parse_input(input_txt)
    max_x, max_y = segments_list.get_max_x_and_y()
    diagram = create_empty_diagram(max_x, max_y)
    diagram = fill_diagram(diagram, segments_list)
    overlaps = count_overlaps(diagram)
    return overlaps


def main():
    input_txt = (BASE_DIR / "input.txt").read_text()

    res_1 = part_1(input_txt)
    print(res_1)

    res_2 = part_2(input_txt)
    print(res_2)


if __name__ == "__main__":
    main()
