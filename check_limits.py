range_list=[[[0,2.251,42.749,45],['Temperature out of range','Temperature near minimum','','Temperature near maximum']],[[20,24.1,75.9,80],['Soc out of range','Approaching discharge','','Approaching charge-peak']],[[0,0.0039,0.08],['charge rate out of range','charge reat near minimum','','charge rate near maximum']]]
error_message="Out of range"
def battery_temp_is_ok(temperature):
  message=check_range(0,temperature)
    print_message(message)
    return False
  return True
def battery_soc_is_ok(soc):
  message=check_range(1,soc)
    print_message(message)
    return False
  return True
def battery__cr_is_ok(charge_rate):
  message=check_range(2,charge_rate)
    print_message(message)
    return False
  return True

def check_range(index_number,variable_value):
  for x in range_list[index_number][0]:
    if variable_value<x:
        return range_list[index_number][1][range_list[index_number][0].index(x)])
        break
    else:
        return error_message
        break
  
  
def print_message(message):
  print(message)
  
def battery_is_ok(temperature, soc, charge_rate):
  Battery_ok=battery_temp_is_ok(temperature)
  Soc_ok=battery_soc_is_ok(soc)
  Cr_ok=battery__cr_is_ok(charge_rate)
  return Battery_ok and Soc_ok and Cr_ok

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
