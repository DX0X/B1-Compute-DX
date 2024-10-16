# PD Controller logic
# Separate file to ensure modularity

class PDController:
    def __init__(self, KP=0.15, KD=0.6):
        self.KP = KP  # Proportional gain
        self.KD = KD  # Derivative gain
        self.prev_error = 0.0  # Initialize previous error

    def compute_control(self, error):
        derivative = error - self.prev_error
        control = self.KP * error + self.KD * derivative
        self.prev_error = error  # Update previous error
        return control