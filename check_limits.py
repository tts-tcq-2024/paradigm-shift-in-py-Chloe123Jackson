def battery_temp_is_ok(temperature):
  if not 0<=temperature<=45:
    print('Temperature is out of range!')
    return False
  return True
def battery_soc_is_ok(soc):
  if not 20<=soc<=80:
    print('State of Charge is out of range!')
    return False
  return True
def battery__cr_is_ok(charge_rate):
  if charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False

  return True


if __name__ == '__main__':
  assert((battery_temp_is_ok(25) and battery_soc_is_ok(70) and battery__cr_is_ok(0.7)) is True)
  assert((battery_temp_is_ok(50) and battery_soc_is_ok(85) and battery__cr_is_ok(0)) is False)
