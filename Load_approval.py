import random

def simple_model(input_data):
    """Simulates a model that makes predictions with a confidence score."""
    labels = ["Approve", "Reject"]
    confidence = random.uniform(0, 1)  # Random confidence between 0 and 1
    prediction = random.choice(labels)
    return prediction, confidence

def human_review(input_data):
    """Requests human input for uncertain cases."""
    while True:
        human_decision = input(f"Model is uncertain. Please classify '{input_data}': (Approve/Reject) ")
        if human_decision in ["Approve", "Reject"]:
            return human_decision
        print("Invalid input. Please enter 'Approve' or 'Reject'.")

def hitl_agent(input_data, confidence_threshold=0.7):
    """Runs the Human-in-the-Loop agent on input data."""
    prediction, confidence = simple_model(input_data)
    print(f"Model Prediction: {prediction}, Confidence: {confidence:.2f}")
    
    if confidence < confidence_threshold:
        print("Confidence below threshold. Requesting human review...")
        return human_review(input_data)
    
    return prediction

if __name__ == "__main__":
    test_cases = ["Loan Application A", "Loan Application B", "Loan Application C", "Loan Application D"]
    
    for case in test_cases:
        final_decision = hitl_agent(case)
        print(f"Final Decision for '{case}': {final_decision}\n")
    
    print("All tests have been run. Program terminating.")
