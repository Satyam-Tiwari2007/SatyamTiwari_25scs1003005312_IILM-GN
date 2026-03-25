from shapely.geometry import LineString


def evaluate_corridor_risk(corridors, roads):
    evaluated = []
    conflict_points = []

    for corridor in corridors:
        line = LineString(corridor["coords"])
        risk = "Low"

        for road in roads:
            road_line = LineString(road["coords"])

            if line.intersects(road_line):
                risk = "High"
                intersection = line.intersection(road_line)

                # ✅ Case 1: Single point
                if intersection.geom_type == "Point":
                    conflict_points.append({
                        "coords": [intersection.y, intersection.x]
                    })

                # ✅ Case 2: Multiple points (FIXED HERE)
                elif intersection.geom_type == "MultiPoint":
                    for pt in intersection.geoms:   # 🔥 FIX
                        conflict_points.append({
                            "coords": [pt.y, pt.x]
                        })

        evaluated.append({**corridor, "risk": risk})

    return evaluated, conflict_points