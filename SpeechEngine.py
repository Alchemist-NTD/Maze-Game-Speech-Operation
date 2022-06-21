import librosa
import sounddevice as sd
import numpy as np
from dtw import dtw


def get_operation(train_set_x, train_set_y):
    arr_data = get_signal()
    if np.max(np.abs(librosa.amplitude_to_db(arr_data.reshape((-1))))) >= 100:
        return 'none'
    return predict(get_mfcc(librosa.effects.trim(arr_data.reshape((-1)),
                                                 top_db=26)[0], 22050), train_set_x, train_set_y)


def get_signal():
    samplerate = 22050  # Hertz
    duration = 1.5  # seconds
    print('Hearing...')
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
    print('Processing...')
    return mydata


def get_mfcc(signal, sr):
    mfccs = librosa.feature.mfcc(y=signal, n_mfcc=13, sr=sr)
    mfccs = mfccs - np.mean(mfccs, axis=1).reshape((-1, 1))
    delta_mfccs = librosa.feature.delta(mfccs, order=1, mode='nearest')
    delta2_mfccs = librosa.feature.delta(mfccs, order=2, mode='nearest')
    return np.concatenate((mfccs, delta_mfccs, delta2_mfccs)).T

def predict(samp, train_set_x, train_set_y):
    dist_min = np.inf
    res = 'none'
    min_idx = -1
    for j in range(len(train_set_y)):
        dist = dtw(samp, train_set_x[j],
                   dist=lambda test, train: np.linalg.norm(test - train, ord=1))[0]
        # if j in range(30, 45): dist -= 0
        if dist_min > dist:
            dist_min = dist
            min_idx = j
            res = train_set_y[j]
    print('distance min: ', dist_min, ' ', res, 'sample: ', min_idx)
    return res


def prepare_tools():
    train_x_best, train_y_best = [], []
    # load data train
    for i in range(15):
        train_x_best.append(np.loadtxt('./Audio Processing/align_sample/len/smp_' + str(i) + '.txt'))
    train_y_best.extend(['len' for i in range(15)])
    for i in range(15, 30):
        train_x_best.append(np.loadtxt('./Audio Processing/align_sample/xuong/smp_' + str(i) + '.txt'))
    train_y_best.extend(['xuong' for i in range(15)])
    for i in range(30, 45):
        train_x_best.append(np.loadtxt('./Audio Processing/align_sample/trai/smp_' + str(i) + '.txt'))
    train_y_best.extend(['trai' for i in range(15)])
    for i in range(45, 60):
        train_x_best.append(np.loadtxt('./Audio Processing/align_sample/phai/smp_' + str(i) + '.txt'))
    train_y_best.extend(['phai' for i in range(15)])
    return train_x_best, train_y_best