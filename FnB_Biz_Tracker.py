''' 
This code helps to keep track of F&B businesses, corresponding franchises as well as the relevant food menus.
'''

from datetime import datetime

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

#string representation
  def __repr__(self):
      return ("The menu, {menu} is availale from {start_time} to {end_time}.".format(menu = self.name,start_time = self.start_time, end_time = self.end_time))
  
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for purchased_item in purchased_items:
      try:
        purchased_item_price = self.items.get(purchased_item)
        total_bill += purchased_item_price
      except:
        pass
    return total_bill

brunch = Menu('brunch',{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},'11am','4pm')

early_bird = Menu('early_bird',{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},'3pm','6pm')

dinner = Menu('dinner',{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},'5pm','11pm')

kids= Menu('kids',{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},'11am','9pm')

#test test
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

class Franchise():
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address

  def available_menus(self,time):
    list_menus = []
    tme = datetime.strptime(time, "%I%p")
    for meal in flagship_store.menus:
      if tme >= datetime.strptime(meal.start_time, "%I%p") and tme <= datetime.strptime(meal.end_time, "%I%p"):
        list_menus.append(meal.name)
    return list_menus

flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

#Testing testing
#print(flagship_store.available_menus('12pm'))
#print(flagship_store.available_menus('5pm'))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

first_biz = Business("Basta Fazoolin\' with my Heart",[flagship_store, new_installment])

arepas_menu = Menu('arepas_menu',{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},'10am','8pm')

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

new_biz = Business("Take a\' Arepa",[arepas_place])