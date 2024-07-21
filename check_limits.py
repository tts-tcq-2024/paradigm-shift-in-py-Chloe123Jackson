def battery_temp_is_ok(temperature):
  if not 0<=temperature<=45:
    print_message()
    return False
  return True
def battery_soc_is_ok(soc):
  if not 20<=soc<=80:
    print_message()
    return False
  return True
def battery__cr_is_ok(charge_rate):
  if charge_rate > 0.8:
    print_message()
    return False

  return True
def print_message():
  print("Out of range")
  
def battery_is_ok(temperature, soc, charge_rate):
  Battery_ok=battery_temp_is_ok(temperature)
  Soc_ok=battery_soc_is_ok(soc)
  Cr_ok=battery__cr_is_ok(charge_rate)
  return Battery_ok and Soc_ok and Cr_ok

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
