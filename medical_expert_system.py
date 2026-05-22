# ============================================
# Medical Expert System for Tropical Diseases
# SEN312 - AI and Expert Systems Lab 2
# Forward Chaining Expert System
# ============================================

# Knowledge Base
diseases = {
    "Malaria": {
        "symptoms": {
            "fever": 0.9,
            "headache": 0.7,
            "chills": 0.8,
            "sweating": 0.6,
            "body_pain": 0.5
        },
        "threshold": 2.5
    },

    "Typhoid": {
        "symptoms": {
            "fever": 0.8,
            "abdominal_pain": 0.9,
            "weakness": 0.7,
            "loss_of_appetite": 0.6,
            "diarrhea": 0.5
        },
        "threshold": 2.3
    },

    "COVID-19": {
        "symptoms": {
            "fever": 0.8,
            "cough": 0.9,
            "shortness_of_breath": 1.0,
            "loss_of_taste": 0.9,
            "fatigue": 0.6
        },
        "threshold": 2.5
    },

    "Dengue Fever": {
        "symptoms": {
            "fever": 0.9,
            "rash": 0.8,
            "joint_pain": 0.9,
            "headache": 0.7,
            "nausea": 0.5
        },
        "threshold": 2.5
    },

    "Pneumonia": {
        "symptoms": {
            "cough": 0.9,
            "fever": 0.8,
            "chest_pain": 0.9,
            "shortness_of_breath": 1.0,
            "fatigue": 0.6
        },
        "threshold": 2.6
    }
}

# List of all possible symptoms
all_symptoms = set()

for disease in diseases.values():
    all_symptoms.update(disease["symptoms"].keys())

# Convert to sorted list
all_symptoms = sorted(list(all_symptoms))


def get_user_symptoms():
    """
    Ask user about symptoms
    """
    print("\n=== Medical Expert System ===")
    print("Answer with yes or no.\n")

    user_symptoms = []

    for symptom in all_symptoms:
        answer = input(f"Do you have {symptom.replace('_', ' ')}? ").lower()

        if answer == "yes":
            user_symptoms.append(symptom)

    return user_symptoms


def diagnose(user_symptoms):
    """
    Forward chaining inference engine
    """
    results = {}

    for disease_name, disease_data in diseases.items():

        score = 0

        for symptom, weight in disease_data["symptoms"].items():

            if symptom in user_symptoms:
                score += weight

        results[disease_name] = score

    return results


def display_results(results):
    """
    Display diagnosis results
    """
    print("\n=== Diagnosis Results ===\n")

    found = False

    for disease_name, score in results.items():

        threshold = diseases[disease_name]["threshold"]

        if score >= threshold:
            confidence = min((score / 5) * 100, 100)

            print(f"{disease_name} detected")
            print(f"Score: {score:.2f}")
            print(f"Confidence Level: {confidence:.1f}%")
            print("-" * 30)

            found = True

    if not found:
        print("No disease matched the threshold.")
        print("Please consult a medical professional.")


# Main Program
if __name__ == "__main__":

    symptoms = get_user_symptoms()

    diagnosis_results = diagnose(symptoms)

    display_results(diagnosis_results)