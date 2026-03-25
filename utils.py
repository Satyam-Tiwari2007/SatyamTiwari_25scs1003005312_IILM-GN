def load_sample_data():

    habitats = [
        {"name": "Kanha", "coords": [22.33, 80.61]},
        {"name": "Pench", "coords": [22.0, 79.5]},
        {"name": "Corbett", "coords": [29.6, 78.8]},
        {"name": "Rajaji", "coords": [30.0, 78.3]},
        {"name": "Kaziranga", "coords": [26.6, 92.9]},
        {"name": "Manas", "coords": [26.9, 92.3]},
        {"name": "Bandipur", "coords": [11.7, 76.6]},
        {"name": "Nagarhole", "coords": [12.0, 76.2]},
        {"name": "Periyar", "coords": [9.5, 77.2]},
        {"name": "Gir", "coords": [21.1, 70.8]},
    ]

    # 18 REALISTIC CURVED CORRIDORS
    corridors = [
        {"name": "Kanha → Pench", "coords": [[22.33,80.61],[22.30,80.4],[22.25,80.2],[22.2,80.0],[22.1,79.8],[22.05,79.65],[22.0,79.5]]},
        {"name": "Pench → Kanha Alt", "coords": [[22.0,79.5],[22.1,79.7],[22.2,79.9],[22.3,80.1],[22.32,80.3],[22.33,80.61]]},
        {"name": "Corbett → Rajaji", "coords": [[29.6,78.8],[29.65,78.7],[29.7,78.6],[29.75,78.5],[29.8,78.45],[29.9,78.4],[30.0,78.3]]},
        {"name": "Kaziranga → Manas", "coords": [[26.6,92.9],[26.65,92.8],[26.7,92.7],[26.75,92.6],[26.8,92.5],[26.85,92.4],[26.9,92.3]]},
        {"name": "Bandipur → Nagarhole", "coords": [[11.7,76.6],[11.75,76.5],[11.8,76.45],[11.85,76.4],[11.9,76.3],[12.0,76.2]]},
        {"name": "Periyar → Meghamalai", "coords": [[9.5,77.2],[9.55,77.25],[9.6,77.3],[9.7,77.35],[9.8,77.4],[9.9,77.45],[10.0,77.5]]},
        {"name": "Gir → Girnar", "coords": [[21.1,70.8],[21.15,70.85],[21.2,70.9],[21.25,70.95],[21.3,71.0]]},

        # EXTRA 11 CORRIDORS
        {"name": "Kanha → Bandhavgarh", "coords": [[22.33,80.61],[22.4,80.8],[22.5,81.0],[22.6,81.2],[22.7,81.4]]},
        {"name": "Bandhavgarh → Achanakmar", "coords": [[22.7,81.4],[22.6,81.6],[22.5,81.8],[22.4,82.0],[22.3,82.2]]},
        {"name": "Achanakmar → Udanti", "coords": [[22.3,82.2],[22.2,82.4],[22.1,82.6],[22.0,82.8]]},
        {"name": "Udanti → Indravati", "coords": [[22.0,82.8],[21.9,83.0],[21.8,83.2],[21.7,83.4]]},
        {"name": "Indravati → Kanger", "coords": [[21.7,83.4],[21.6,83.6],[21.5,83.8],[21.4,84.0]]},
        {"name": "Kanger → Simlipal", "coords": [[21.4,84.0],[21.5,84.5],[21.6,85.0],[21.7,85.5]]},
        {"name": "Simlipal → Sundarbans", "coords": [[21.7,85.5],[21.8,86.0],[21.85,87.0],[21.9,88.4]]},
        {"name": "Kaziranga → Namdapha", "coords": [[26.6,92.9],[26.7,93.2],[26.8,93.6],[26.9,94.0]]},
        {"name": "Manas → Dibru", "coords": [[26.9,92.3],[27.0,92.7],[27.1,93.2],[27.2,93.8]]},
        {"name": "Gir → Velavadar", "coords": [[21.1,70.8],[21.2,71.2],[21.3,71.6],[21.4,72.0]]},
        {"name": "Periyar → Silent Valley", "coords": [[9.5,77.2],[9.8,76.9],[10.2,76.6],[10.5,76.3]]},
    ]

    # ROADS aligned with intersections
    roads = [
        {"coords": [[22.2,80.4],[22.1,79.6]]},
        {"coords": [[29.7,78.6],[29.9,78.3]]},
        {"coords": [[26.7,92.7],[26.85,92.4]]},
        {"coords": [[11.8,76.5],[11.9,76.3]]},
        {"coords": [[21.5,83.8],[21.6,84.2]]},
        {"coords": [[21.8,86.5],[21.9,88.4]]},
    ]

    return habitats, corridors, roads


def get_risk_color(risk):
    return "#d73027" if risk == "High" else "#1a9850"