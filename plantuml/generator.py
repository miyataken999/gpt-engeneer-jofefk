import plantuml

def generate_sequence_diagram(knowledge):
    # Create a PlantUML sequence diagram from the knowledge data
    diagram = plantuml.PlantUML()
    diagram.skinparams("sequenceDiagram")
    for item in knowledge.data:
        diagram.add(item)
    return diagram.get_png()