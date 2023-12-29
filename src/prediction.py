# Import necessary libraries
# from sklearn.cross_decomposition import PLSRegression
# import joblib


# Load the PLS model from the file
# loaded_pls_model = joblib.load(
#     'C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\model\\saved_model\\silt_model.joblib')

# # Assuming you have new data for prediction, replace X_new with your actual data
# X_new = [0.2935, 0.2932, 0.2934, 0.295, 0.3022, 0.3175, 0.3376, 0.347, 0.3487, 0.3458, 0.3402, 0.3319, 0.323, 0.3133, 0.3043, 0.2958, 0.2869, 0.2787, 0.2712, 0.2655, 0.2611, 0.2596, 0.2602, 0.2636, 0.2692, 0.2764, 0.2896, 0.3188, 0.3712, 0.4314, 0.4769, 0.5013, 0.5138, 0.5244, 0.5346, 0.5408, 0.5445, 0.5439, 0.5334, 0.5173, 0.5028, 0.4922, 0.4849, 0.4824, 0.4833, 0.488, 0.4971, 0.5102, 0.5293, 0.5557, 0.589, 0.6272, 0.6674, 0.7066, 0.742, 0.7759, 0.8157, 0.8733, 0.9577, 1.052, 1.1269, 1.1743, 1.2015,
#          1.215, 1.2237, 1.2291, 1.2292, 1.2318, 1.2262, 1.2156, 1.209, 1.1964, 7, 1.2291, 1.2292, 1.2318, 1.2262, 1.2156, 1.209, 1.1964, 1.1816, 1.1676, 1.1521, 1.1318, 1.114, 1.0959, 1.0758, 1.0585, 1.0417, 1.0248, 1.0078, 0.9919, 0.9781, 0.9621, 0.9479, 0.9354, 0.9254, 0.914, 0.9044, 0.8945, 0.8855, 0.8784, 0.8696, 0.8435, 0.7917, 0.7278, 0.6684, 0.6261, 0.5947, 0.5666, 0.5378, 0.5187, 0.5019, 0.4891, 0.4777, 0.4676, 0.4609, 0.4548, 0.4508, 0.4443, 0.4426, 0.438, 0.4322, 0.4231]  # Your new data for prediction

# # Make predictions using the loaded model
# predictions = loaded_pls_model.predict(X_new)

# # Print or use the predictions as needed
# print(predictions)


import subprocess
import sys
import os


def activate_virtual_environment(env_path):
    """
    Activate a virtual environment.

    Parameters:
    - env_path (str): Path to the virtual environment.

    Returns:
    - None
    """
    if sys.platform.startswith('win'):  # Check if running on Windows
        activate_script = os.path.join(env_path, 'Scripts', 'activate')
        activate_cmd = f'call "{activate_script}"'
    else:
        activate_script = os.path.join(env_path, 'bin', 'activate')
        activate_cmd = f'source "{activate_script}"'

    # Activate the virtual environment using subprocess
    subprocess.run(activate_cmd, shell=True)


# Example usage:
env32_path = './env32'
env64_path = './env64'

# Activate 32-bit environment
# activate_virtual_environment(env32_path)

# Your code that requires 32-bit Python
# ...

# Manually reset environment variables (for both Windows and Unix-like systems)
for var in ('VIRTUAL_ENV', 'PATH'):
    os.environ.pop(var, None)

# Activate 64-bit environment
activate_virtual_environment(env64_path)

print(sys.version)
# Your code that requires 64-bit Python
# ...

# Manually reset environment variables (for both Windows and Unix-like systems)
for var in ('VIRTUAL_ENV', 'PATH'):
    os.environ.pop(var, None)
