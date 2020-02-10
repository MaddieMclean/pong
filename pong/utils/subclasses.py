from __future__ import annotations

from kivy import vector


class Vector(vector.Vector):
    # noinspection PyBroadException
    def __mul__(self, val) -> Vector:
        try:
            return Vector(list(map(lambda x, y: x * y, self, val)))
        except Exception:
            return Vector([x * val for x in self])
