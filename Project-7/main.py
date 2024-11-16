from tkinter import *
from tkinter import ttk
import requests
from PIL import Image,ImageTk
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=c69041c35558a0c5c18fa3e7bf32bc21").json()
    weather_show1.config(text=data["weather"][0]["main"])

    weather_desc1.config(text=data["weather"][0]["description"])

    temp_show1.config(text=f"{data["main"]["temp"]-273.18:.2f} °C")

    temp_min1.config(text=f"{data["main"]["temp_min"]-282.27:.2f} °C")

    temp_max1.config(text=f"{data["main"]["temp_max"]-271.15:.2f} °C")

    pressure_show1.config(text=f"{data["main"]["pressure"]} hPa")

# Initialize the main window
win = Tk()

# Title of application
win.title("Weather")

# Bg color of application
win.config(bg="#0D1B2A")

# App box sizing
win.geometry("500x550")

# No resizing
win.resizable(False, False)

# Name label at top of the app (Font and place)
name_label = Label(win, text="Weather Check", font=("Times New Roman", 40, "bold", "underline"), bg="#0D1B2A", fg="white")
name_label.place(x=15, y=15, height=50, width=470)

# Select state (Font and Place)
select_state = Label(win, text="Select State:", font=("Times New Roman", 17, "bold"), bg="#0D1B2A", fg="#FAF9F6")
select_state.place(x=65, y=105, height=38, width=150)

# Data for states and their corresponding cities
states_and_cities = {
 "Andhra Pradesh": [
        "Visakhapatnam", "Vijayawada", "Tirupati", "Guntur", "Nellore", 
        "Kakinada", "Kadapa", "Anantapur", "Chittoor", "East Godavari", 
        "West Godavari", "Krishna", "Srikakulam", "Vizianagaram", "Prakasam", "Rayalaseema"
    ],
    "Arunachal Pradesh": [
        "Itanagar", "Naharlagun", "Pasighat", "Daporijo", "Aalo", 
        "Tezu", "Bomdila", "Ziro", "Tawang", "Seppa"
    ],
    "Assam": [
        "Guwahati", "Dibrugarh", "Silchar", "Tezpur", "Nagaon", 
        "Jorhat", "Tinsukia", "Karimganj", "Goalpara", "Bongaigaon"
    ],
    "Bihar": [
        "Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga", 
        "Purnia", "Saharsa", "Bhagalpur", "Katihar", "Samastipur"
    ],
    "Chhattisgarh": [
        "Raipur", "Bhilai", "Durg", "Korba", "Raigarh", 
        "Bilaspur", "Jagdalpur", "Dantewada", "Kanker", "Kabirdham"
    ],
    "Goa": [
        "Panaji", "Margao", "Mapusa", "Ponda", "Vasco da Gama", 
        "Bicholim", "Sankhali", "Canacona", "Quepem", "Sanguem"
    ],
    "Gujarat": [
        "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", 
        "Bhavnagar", "Junagadh", "Anand", "Nadiad", "Mehsana"
    ],
    "Haryana": [
    "Kurukshetra",
    "Ambala","Faridabad","Gurugram","Hisar","Karnal","Panipat","Panchkula","Rohtak","Sonipat","Fatehabad","Bhiwani","Sirsa","Jind","Mohindergarh","Nuh","Rewari","Yamunanagar","Jhajjar","Charkhi Dadri","Palwal","Taraori","Hansi","Dabwali","Tohana",
    "Narwana","Assandh",
    "Kaithal",
    "Gohana",
    "Fatehgarh Sahib",
    "Pehowa",
    "Ratia",
    "Jatusana",
    "Mandi Dabwali",
    "Kharkhoda",
    "Sewah",
    "Shahabad Markanda",
    "Sarsa",
    "Badli",
    "Bawal",
    "Ganaur",
    "Israna",
    "Kharkhoda",
    "Naraingarh",
    "Rohka",
    "Khanpur",
    "Bhiwani",
    "Bahadurgarh",
    "Dharuhera",
    "Manesar",
    "Palwal",
    ],
    "Himachal Pradesh": [
        "Shimla", "Dharamshala", "Kullu", "Solan", "Mandi", 
        "Bilaspur", "Hamirpur", "Kinnaur", "Lahaul", "Spiti"
    ],
    "Jharkhand": [
        "Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Giridih", 
        "Deoghar", "Dumka", "Chatra", "Palamu", "Ramgarh"
    ],
    "Karnataka": [
        "Bengaluru", "Mysuru", "Mangalore", "Hubli", "Dharwad", 
        "Bellary", "Kolar", "Tumkur", "Udupi", "Chikmagalur"
    ],
    "Kerala": [
        "Thiruvananthapuram", "Kochi", "Kozhikode", "Kottayam", "Malappuram", 
        "Palakkad", "Thrissur", "Ernakulam", "Idukki", "Alappuzha"
    ],
    "Madhya Pradesh": [
        "Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain", 
        "Sagar", "Satna", "Chhindwara", "Khandwa", "Dewas"
    ],
    "Maharashtra": [
        "Mumbai", "Pune", "Nagpur", "Thane", "Nashik", 
        "Aurangabad", "Solapur", "Akola", "Jalna", "Buldhana"
    ],
    "Manipur": [
        "Imphal", "Thoubal", "Kakching", "Churachandpur", "Senapati", 
        "Tamenglong", "Ukhrul", "Bishnupur", "Jiribam", "Kangpokpi"
    ],
    "Meghalaya": [
        "Shillong", "Tura", "Jowai", "Nongstoin", "Williamnagar", 
        "Bholaganj", "Mawphlang", "Khliehriat", "Sohra", "Baghmara"
    ],
    "Mizoram": [
        "Aizawl", "Lunglei", "Siaha", "Champhai", "Kolasib", 
        "Mamit", "Lawngtlai", "Serchhip", "Hnahthial", "Lunglei"
    ],
    "Nagaland": [
        "Kohima", "Dimapur", "Mokokchung", "Wokha", "Zunheboto", 
        "Phek", "Tuensang", "Mon", "Longleng", "Kiphire"
    ],
    "Odisha": [
        "Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur", 
        "Puri", "Baleswar", "Kendrapara", "Dhenkanal", "Jagatsinghpur"
    ],
    "Punjab": [
        "Chandigarh", "Amritsar", "Ludhiana", "Patiala", "Jalandhar", 
        "Bathinda", "Moga", "Ferozepur", "Faridkot", "Sangrur"
    ],
    "Rajasthan": [
        "Jaipur", "Udaipur", "Jodhpur", "Kota", "Ajmer", 
        "Bikaner", "Tonk", "Sikar", "Dholpur", "Pali"
    ],
    "Sikkim": [
        "Gangtok", "Namchi", "Mangan", "Gyalshing", "Pakyong", 
        "Rangpo", "Jorethang", "Singtam", "Soreng", "Rongli"
    ],
    "Tamil Nadu": [
        "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", 
        "Tirunelveli", "Thanjavur", "Vellore", "Erode", "Kanyakumari"
    ],
    "Telangana": [
        "Hyderabad", "Warangal", "Khammam", "Nizamabad", "Karimnagar", 
        "Mahbubnagar", "Ranga Reddy", "Medak", "Adilabad", "Nalgonda"
    ],
    "Tripura": [
        "Agartala", "Belonia", "Dharmanagar", "Udaipur", "Ambassa", 
        "Kailashahar", "Khowai", "Teliamura", "Moharpara", "Sonamura"
    ],
    "Uttar Pradesh": [
        "Lucknow", "Kanpur", "Agra", "Varanasi", "Meerut", 
        "Ghaziabad", "Allahabad", "Aligarh", "Bareilly", "Firozabad"
    ],
    "Uttarakhand": [
        "Dehradun", "Haridwar", "Nainital", "Rudrapur", "Roorkee", 
        "Haldwani", "Pauri Garhwal", "Almora", "Tehri Garhwal", "Champawat"
    ],
    "West Bengal": [
        "Kolkata", "Siliguri", "Darjeeling", "Howrah", "Durgapur", 
        "Asansol", "Malda", "Bardhaman", "Kalyani", "Berhampore"
    ],
    "Andaman and Nicobar Islands": ["Port Blair", "Neil Island", "Havelock"],
    "Chandigarh": ["Chandigarh"],
    "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu"],
    "Lakshadweep": ["Kavaratti"],
    "Delhi": ["Delhi"],
    "Puducherry": ["Puducherry"],
}


# Dropdown for states
state_dropdown = ttk.Combobox(win, values=list(states_and_cities.keys()), font=("Times New Roman", 15))
state_dropdown.place(x=225, y=105, height=38, width=200)


# Label for city selection
select_city = Label(win, text="Select City:", font=("Times New Roman", 17, "bold"), bg="#0D1B2A", fg="#FAF9F6")
select_city.place(x=65, y=155, height=38, width=150)


# Dropdown for cities
city_name = StringVar()
city_dropdown = ttk.Combobox(win, font=("Times New Roman", 15),textvariable=city_name)
city_dropdown.place(x=225, y=155, height=38, width=200)


# Function to update city dropdown based on selected state
def update_cities(event):
    selected_state = state_dropdown.get()
    city_dropdown['values'] = states_and_cities.get(selected_state, [])
    city_dropdown.set('')  # Reset city selection


# Bind the state dropdown to update cities
state_dropdown.bind("<<ComboboxSelected>>", update_cities)


# Data for weather forecast labels
weather_show = Label(win, text="Weather Climate:", fg="#87CEEB", bg="#0D1B2A", font=("Times New Roman", 16))
weather_show.place(x=65, y=280, height=38, width=190)

weather_show1 = Label(win, fg="#FAF9F6", bg="#0D1B2A", font=("Times New Roman", 14))
weather_show1.place(x=235, y=280, height=38, width=70)


# Weather description 
weather_desc = Label(win, text="Weather Description:", fg="#87CEEB", bg="#0D1B2A", font=("Times New Roman", 16))
weather_desc.place(x=65, y=310, height=38, width=170)

weather_desc1 = Label(win, fg="#FAF9F6", bg="#0D1B2A", font=("Times New Roman", 14))
weather_desc1.place(x=235, y=310, height=38, width=120)


# temp_show
temp_show = Label(win, text="Temperature:", fg="#4682B4", bg="#0D1B2A", font=("Times New Roman", 16))
temp_show.place(x=65, y=380, height=38, width=150)

temp_show1 = Label(win, fg="#FAF9F6", bg="#0D1B2A", font=("Times New Roman", 14))
temp_show1.place(x=200, y=380, height=38, width=90)


# minimum temp
temp_min = Label(win, text="Min Temperature:", fg="#4682B4", bg="#0D1B2A", font=("Times New Roman", 16))
temp_min.place(x=65, y=410, height=38, width=150)

temp_min1 = Label(win, fg="#FAF9F6", bg="#0D1B2A", font=("Times New Roman", 14))
temp_min1.place(x=220, y=410, height=38, width=90)


# MAx temp
temp_max = Label(win, text="Max Temperature:", fg="#4682B4", bg="#0D1B2A", font=("Times New Roman", 16))
temp_max.place(x=65, y=440, height=38, width=150)

temp_max1 = Label(win, fg="#FAF9F6", bg="#0D1B2A", font=("Times New Roman", 14))
temp_max1.place(x=220, y=440, height=38, width=100)

pressure_show = Label(win, text="Pressure:", fg="#4682B4", bg="#0D1B2A", font=("Times New Roman", 16))
pressure_show.place(x=65, y=470, height=38, width=150)

pressure_show1 = Label(win, fg="#FAF9F6", bg="#0D1B2A", font=("Times New Roman", 14))
pressure_show1.place(x=180, y=470, height=38, width=100)


# Done button
done_button = Button(win, text="Done", font=("Times New Roman", 15), bg="#66B2D4", command=data_get)
done_button.place(x=345, y=210, height=30, width=120)


# Run the application
win.mainloop()

