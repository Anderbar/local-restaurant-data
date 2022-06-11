import restaurantmanager_util
import webbrowser

restaurants = restaurantmanager_util.read_restaurants("Lab 04/andrewsdata.txt")

def print_restaurants(alist):
    count = 1
    for value in alist:
        print("[",count,"] : ",value[0]," ", "(", value[3], ")", sep='')
        address = value[1].split('+')
        print('\t\t', address[0])
        print('\t\t', address[1])
        count += 1

def print_info(alist):

    for value in alist:
        print(value[0]," ", "(", value[3], ")", sep='')
        address = value[1].split('+')
        print('\t\t', address[0])
        print('\t\t', address[1])
        website = value[2]
       
    print('\n')

    choice = int(input("What would you like to do next? \n 1. Visit the homepage \n 2. Show on Google Maps \n 3. Show directions to this restaurant \n Your choice (1-3)? ==> "))
    print('\n')

    if choice == 1:
        webbrowser.open(website)
    if choice == 2:
        webbrowser.open('http://www.google.com/maps/place/', address)
    if choice == 3:
        webbrowser.open('http://www.google.com/maps/dir/742 Columbus Drive Perth Amboy/',address)

print_restaurants(restaurants)

x = int(input("Enter a restaurant ID: "))
print(x)
restaurant_list = [*range(1,156,1)]

for value in restaurant_list:
    if x-1 not in restaurant_list:
        print('Warning! Not a valid value!')
        break

restaurant_value = [restaurants[i] for i in [x-1]]


print_info(restaurant_value)