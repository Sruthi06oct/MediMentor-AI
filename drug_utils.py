def check_interaction(drug1: str, drug2: str) -> str:
    interactions = {
        ("ibuprofen", "aspirin"): "May cause increased bleeding risk.",
        ("paracetamol", "alcohol"): "May cause liver damage.",
    }
    pair = (drug1.lower(), drug2.lower())
    return interactions.get(pair, "No significant interaction found.")

def get_drug_info(drug: str) -> str:
    info = {
        "paracetamol": "Used to treat fever and mild pain.",
        "ibuprofen": "NSAID for pain and inflammation.",
        "aspirin": "Used for pain relief and blood thinning.",
    }
    return info.get(drug.lower(), "No information available.")

def recommend_alternatives(drug: str) -> list:
    alt = {
        "paracetamol": ["Ibuprofen", "Naproxen"],
        "aspirin": ["Clopidogrel", "Acetaminophen"],
    }
    return alt.get(drug.lower(), ["Consult doctor for alternatives."])
