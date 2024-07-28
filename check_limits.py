range_list=[[[0,2.251,42.749,45],[0,'Temperature near the minimum','','Temperature near the maximum'],[0,'Temperatur nahe dem Minimum','','Temperatur nahe dem Maximum']],[[20,24.1,75.9,80],[1,'Approaching discharge','','Approaching charge-peak'],[1,'Entladung nähert sich','','Annäherung an den Ladespitzenwert']],[[0,0.039,0.8],[2,'charge rate near minimum','','charge rate near maximum'],[2,'Laderate nahe Minimum','','Laderate nahe Maximum']]]
mapping=['Temperature','SOC','Charge rate']

def battery_temp_is_ok(temperature,language):
  message=deliver_range_message(0,temperature,language)
  print(message)
  print_message(message)
  return check_out_of_range(message)
  
def battery_soc_is_ok(soc,language):
  message=deliver_range_message(1,soc,language)
  print_message(message)
  return check_out_of_range(message)
  
def battery__cr_is_ok(charge_rate,language):
  message=deliver_range_message(2,charge_rate,language)
  print_message(message)
  return check_out_of_range(message)
  

def deliver_range_message(index_number,variable_value,language):
  for x in range_list[index_number][0]:
    if variable_value<x:
      y=range_list[index_number][language][range_list[index_number][0].index(x)]
      break
    else:
      y=index_number
  return y
      
def check_out_of_range(message):
  if message in range(0,3):
    return False
  else:
    return True
  
def print_message(message):
  if check_out_of_range(message)==False:
    print(mapping[message], "Out of range")
  else:
    print(message)
  
def battery_is_ok(temperature, soc, charge_rate,language):
  Battery_ok=battery_temp_is_ok(temperature,language)
  Soc_ok=battery_soc_is_ok(soc,language)
  Cr_ok=battery__cr_is_ok(charge_rate,language)
  return Battery_ok and Soc_ok and Cr_ok

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7,1) is True)
  assert(battery_is_ok(50, 85, 0,2) is False)
