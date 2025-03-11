import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def generate_wave(frequency, amplitude, duration, wave_type='P'):
    """Genera una señal sísmica basada en una función sinusoidal."""
    t = np.linspace(0, duration, int(1000 * duration))
    if wave_type == 'P':
        signal = amplitude * np.sin(2 * np.pi * frequency * t)
    elif wave_type == 'S':
        signal = amplitude * np.sin(2 * np.pi * frequency * t + np.pi/2)
    elif wave_type == 'R':
        signal = amplitude * chirp(t, f0=frequency, f1=frequency*2, t1=duration, method='linear')
    return t, signal

def simulate_propagation(signal, soil_properties):
    """Simula la propagación de la onda a través del suelo."""
    density = soil_properties['density']
    elasticity = soil_properties['elasticity']
    velocity = np.sqrt(elasticity / density)

    # Distorsión simulada
    distorted_signal = signal * np.exp(-0.02 * np.arange(len(signal)))

    return distorted_signal
