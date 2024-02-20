def primary_stress_position(phoneme_list):
    for i in range(len(phoneme_list)):
        if '1' in phoneme_list[i]:
            return i
        