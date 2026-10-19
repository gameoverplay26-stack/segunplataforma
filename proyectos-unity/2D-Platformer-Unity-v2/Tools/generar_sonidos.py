# -*- coding: utf-8 -*-
"""
Genera los efectos de sonido del 2D Platformer v2 (estilo 8 bits, sintetizados).
Son propios: no dependen de bancos de sonido de terceros ni de licencias externas.

Uso (desde la carpeta del proyecto):  python Tools/generar_sonidos.py
Salida: Assets/Audio/sfx_moneda.wav, sfx_salto.wav, sfx_muerte.wav (44,1 kHz, 16 bits, mono).
Solo usa la biblioteca estándar de Python.
"""
import math
import os
import struct
import wave

RATE = 44100
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Assets", "Audio")


def square(phase, duty=0.5):
    return 1.0 if (phase % 1.0) < duty else -1.0


def envelope(i, n, attack=0.005, release=0.08):
    t, dur = i / RATE, n / RATE
    a = min(1.0, t / attack) if attack > 0 else 1.0
    r = min(1.0, (dur - t) / release) if release > 0 else 1.0
    return max(0.0, min(a, r))


def tone(freq_fn, dur, volume=0.35, duty=0.5, release=0.08):
    """freq_fn(t) devuelve la frecuencia en Hz en el instante t (s)."""
    n = int(RATE * dur)
    phase, out = 0.0, []
    for i in range(n):
        t = i / RATE
        phase += freq_fn(t) / RATE
        out.append(square(phase, duty) * envelope(i, n, release=release) * volume)
    return out


def write(name, samples):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, s)) * 32767)) for s in samples))
    print("OK ", path, "%.2f s" % (len(samples) / RATE))


# Moneda: dos notas agudas seguidas (Si5 -> Mi6), el "ding" clásico.
coin = tone(lambda t: 987.77, 0.07, release=0.01) + tone(lambda t: 1318.51, 0.22, release=0.18)

# Salto: barrido ascendente corto, onda con ciclo del 25 %.
jump = tone(lambda t: 280 + 2600 * t, 0.16, volume=0.3, duty=0.25, release=0.06)

# Muerte: barrido descendente con vibrato, más largo y grave.
death = tone(lambda t: max(80.0, 640 - 700 * t) * (1 + 0.06 * math.sin(2 * math.pi * 14 * t)), 0.75,
             volume=0.32, release=0.25)

write("sfx_moneda.wav", coin)
write("sfx_salto.wav", jump)
write("sfx_muerte.wav", death)
