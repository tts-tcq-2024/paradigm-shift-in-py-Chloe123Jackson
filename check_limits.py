range_list=[[[0,2.251,42.749,45],[0,'Temperature near minimum','','Temperature near maximum']],[[20,24.1,75.9,80],[1,'Approaching discharge','','Approaching charge-peak']],[[0,0.0039,0.08],[2,'charge reat near minimum','','charge rate near maximum']]]
mapping=['Temperature','SOC','Charge rate']
def battery_temp_is_ok(temperature):
  message=check_range(0,temperature)
  return print_message(message)
  
def battery_soc_is_ok(soc):
  message=check_range(1,soc)
  return print_message(message)
  
def battery__cr_is_ok(charge_rate):
  message=check_range(2,charge_rate)
  return print_message(message)
  
def check_out_of_range(message):
  if message in range(0,3):
    return False
  return True

def check_range(index_number,variable_value):
  for x in range_list[index_number][0]:
    if variable_value<x:
        return range_list[index_number][1][range_list[index_number][0].index(x)]
        break
    else:
        return variable_value
        break
  
  
def print_message(message):
  if message in range(0,3):
    print(mapping[message], "Out of range")
    return False
  else:
    print(message)
    return True
  
def battery_is_ok(temperature, soc, charge_rate):
  Battery_ok=battery_temp_is_ok(temperature)
  Soc_ok=battery_soc_is_ok(soc)
  Cr_ok=battery__cr_is_ok(charge_rate)
  return Battery_ok and Soc_ok and Cr_ok

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
