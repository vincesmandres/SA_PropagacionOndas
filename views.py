from django.shortcuts import render
from .models import Soil, SeismicSignal
from .utils.wave_simulation import generate_wave, simulate_propagation

def home(request):
    soils = Soil.objects.all()
    return render(request, 'home.html', {'soils': soils})

def simulate_wave(request):
    soil_id = request.GET.get('soil_id')
    signal_id = request.GET.get('signal_id')

    soil = Soil.objects.get(id=soil_id)
    signal = SeismicSignal.objects.get(id=signal_id)

    t, wave = generate_wave(signal.frequency, signal.amplitude, signal.duration, signal.wave_type)
    distorted_wave = simulate_propagation(wave, {
        'density': soil.density,
        'elasticity': soil.elasticity
    })

    context = {
        'time': t.tolist(),
        'original_wave': wave.tolist(),
        'distorted_wave': distorted_wave.tolist()
    }
    return render(request, 'results.html', context)
