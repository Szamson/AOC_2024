from math import gcd

class PairOfAntennas:
  max_m = -1
  max_n = -1

  def __init__(self, p1, p2, signal):
    self.p1 = p1
    self.p2 = p2
    self.signal = signal
    self.slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    self.dif = ()
    self.potential_anti_antennas = []
    self.calculate_dif()
  
  def calculate_dif(self):
    print((self.p2[0] - self.p1[0], self.p2[1] - self.p1[1]))
    self.dif = simplify_fraction(self.p2[0] - self.p1[0], self.p2[1] - self.p1[1])
    print(self.dif)
    self.generate_potential_anti_antennas_multiple() #generate_potential_anti_antennas for puzzle1 generate_potential_anti_antennas_multiple for puzzle_2

  def generate_potential_anti_antennas(self):
    c_1 = (self.p1[0] - self.dif[0], self.p1[1] - self.dif[1])
    if 0 <= c_1[0] < PairOfAntennas.max_m and 0 <= c_1[1] < PairOfAntennas.max_n:
      self.potential_anti_antennas.append(c_1)

    c_2 = (self.p2[0] + self.dif[0], self.p2[1] + self.dif[1])
    if 0 <= c_2[0] < PairOfAntennas.max_m and 0 <= c_2[1] < PairOfAntennas.max_n:
      self.potential_anti_antennas.append(c_2)

  def generate_potential_anti_antennas_multiple(self):

    c_1 = (self.p1[0] - self.dif[0], self.p1[1] - self.dif[1])
    while 0 <= c_1[0] < PairOfAntennas.max_m and 0 <= c_1[1] < PairOfAntennas.max_n:
        self.potential_anti_antennas.append(c_1)
        c_1 = (c_1[0] - self.dif[0], c_1[1] - self.dif[1])

    c_2 = (self.p2[0] + self.dif[0], self.p2[1] + self.dif[1])
    while 0 <= c_2[0] < PairOfAntennas.max_m and 0 <= c_2[1] < PairOfAntennas.max_n:
        self.potential_anti_antennas.append(c_2)
        c_2 = (c_2[0] + self.dif[0], c_2[1] + self.dif[1])



def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return simplified_numerator, simplified_denominator