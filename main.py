from scipy.stats import beta
from scipy.stats import binom
import numpy as np

bsize = 10000   # количество эксперементов, сравнивающие 2 модели

real_prob1 = 0.01 # вероятность конверсии для первого баннера. Этот показатель скрыт для эксперементатора
real_prob2 = 0.02 # вероятность конверсии для второго баннера. Этот показатель скрыт для эксперементатора

impr1, impr2 = 100, 1500 # количество показов для обоих моделей

clicks1 = binom.rvs(impr1, real_prob1)  # количество кликов для первого баннера. Известный показатель
clciks2 = binom.rvs(impr2, real_prob2) # количество кликов для второго баннера. Известный показатель

model1 = beta(clicks1, impr1) # модель для первого баннера
model2 = beta(clciks2, impr2) # модель для втого баннера

randmodel1 = model1.rvs(bsize) # генерим новые данные для модели 1
randmodel2 = model2.rvs(bsize) # генерим новые данные для модели 2

model_1_is_better = np.sum(randmodel1 > randmodel2) / bsize  # сравниваем результаты рандомно сгенерированных обоими моделями случайных цифр.
# По сути мы на собраннных данных генерируем переменные real_prob1 и real_prob2 и смотрим в скольки случаях одна из моделей будет генерить более высокие вероятности

print('Model_1 is better then Model_2 in {rate} over 100% cases'.format(rate= model_1_is_better))


