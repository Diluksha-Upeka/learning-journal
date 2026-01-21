# Traditional coding vs Machine Learning

# Traditional: Input + Rule = Output
# Machine Learning: Input + Output = Rule

# TRADITIONAL CODING EXAMPLE
def traditional_converter(km):
    return km * 0.621371 # Convert kilometers to miles

# MACHINE LEARNING EXAMPLE
def simple_ml_training(inputs, outputs):
    print(f" Training on data...")
    weight = 0.5 # Dummy weight for illustration
    step_size = 0.000001 # Dummy step size for illustration

    max_km = max(inputs)
    max_miles = max(outputs)
    inputs = [x / max_km for x in inputs]  # Normalize inputs
    outputs = [y / (max_km * 0.621371) for y in outputs]  # Normalize outputs

    # Run 1000 iterations of training
    for i in range(1000):
        if i % 100 == 0:
            print(f"  Iteration {i}, Current weight: {weight}")
        total_error = 0
        for idx, val_in in enumerate(inputs):
            target = outputs[idx]   # Get the corresponding target output

            prediction = val_in * weight # Make a prediction

            error = prediction - target # Calculate the error
            total_error += val_in * error # Calculate gradient

            weight += step_size * total_error # Adjust the weight based on error

    print(f" Training complete. Learned weight: {weight}")
    return weight

# What happens above
# 1. We start with some initial weight (0.5 here).
# 2. For each input, we make a prediction using the current weight.
# 3. We calculate the error (difference between prediction and actual output).
# 4. We adjust the weight slightly based on the error.
# 5. We repeat this process for a few iterations (1000 here).
# 6. After training, we return the final weight.

# DATA (Supervised Learning)

# X: Input data (kilometers)
km_data = [10, 20, 30, 40, 50, 100]
# Y: Output data (miles)
miles_data = [6.21371, 12.4274, 18.6411, 24.8548, 31.0685, 62.1371]


# TEST
learned_weight = simple_ml_training(km_data, miles_data)

# Using the learned weight to make predictions
new_input = 100 
predicted_miles = new_input * learned_weight
print(f"Predicted miles for {new_input} km: {predicted_miles}")