# Calculate storage sizes for two audio files.

audio_files = [
    (11000, "stereo", 8, 1.75, 2),
    (44100, "mono", 8, 1.75, 1)
]

print("Sample Rate | Audio Type | Bits/Sample | Length (min) | KB | MB")
print("-" * 68)

for sample_rate, audio_type, bits_per_sample, length_minutes, channels in audio_files:
    length_seconds = length_minutes * 60

    total_bits = sample_rate * bits_per_sample * length_seconds * channels
    total_bytes = total_bits / 8

    kilobytes = total_bytes / 10**3
    megabytes = total_bytes / 10**6

    print(
        f"{sample_rate:11} | {audio_type:10} | {bits_per_sample:11} | "
        f"{length_minutes:12.2f} | {kilobytes:.4f} | {megabytes:.4f}"
    )
