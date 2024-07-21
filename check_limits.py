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

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_colour_code_table():
    table=[['Pair number','Major colour','Minor colour']]
    pair_number=1
    row=[]
    for major_colour in MAJOR_COLORS:
        for minor_colour in MINOR_COLORS:
            row.append(pair_number)
            row.append(major_colour)
            row.append(minor_colour)
            table.append(row)
            pair_number+=1
            row=[]
            print(table)
    for row in table:
        print('--------------------------------------------')
        print('| {:^11} | {:^12} | {:^12} |'.format(*row))


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
