from enum import Enum

class USER_ROLE(str, Enum):
    USER="user"
    DRIVER="driver"
    VENDOR="vendor"
    ADMIN="admin"

class USER_STATUS(str, Enum):
    ACTIVE="active"
    INACTIVE="inactive"
    BLOCKED="blocked"
    ON_HOLIDAY="on_holiday"

class VEHICLE_TYPE(str, Enum):
    TWO_WHEELER = "two_wheeler"
    FOUR_WHEELER = "four_wheeler"

class VEHICLE_BRAND(str, Enum):
    HERO = "Hero"
    BAJAJ = "Bajaj"
    TVS = "TVS"
    ROYAL_ENFIELD = "Royal Enfield"
    HONDA = "Honda"
    YAMAHA = "Yamaha"
    SUZUKI = "Suzuki"
    KAWASAKI = "Kawasaki"
    APRILIA = "Aprilia"
    MARUTI_SUZUKI = "Maruti Suzuki"
    HYUNDAI = "Hyundai"
    TATA = "Tata"
    MAHINDRA = "Mahindra"
    TOYOTA = "Toyota"
    FORD = "Ford"
    CHEVROLET = "Chevrolet"
    RENAULT = "Renault"
    KIA = "Kia"
    MITSUBISHI = "Mitsubishi"
    ISUZU = "Isuzu"
    VOLKSWAGEN = "Volkswagen"
    JEEP = "Jeep"
    FIAT = "Fiat"
    AUDI = "Audi"
    BMW = "BMW"
    MERCEDES_BENZ = "Mercedes-Benz"
    MG_MOTOR = "MG Motor"



class IndianState(str, Enum):
    ANDHRA_PRADESH = "Andhra Pradesh"
    ARUNACHAL_PRADESH = "Arunachal Pradesh"
    ASSAM = "Assam"
    BIHAR = "Bihar"
    CHHATTISGARH = "Chhattisgarh"
    GOA = "Goa"
    GUJARAT = "Gujarat"
    HARYANA = "Haryana"
    HIMACHAL_PRADESH = "Himachal Pradesh"
    JHARKHAND = "Jharkhand"
    KARNATAKA = "Karnataka"
    KERALA = "Kerala"
    MADHYA_PRADESH = "Madhya Pradesh"
    MAHARASHTRA = "Maharashtra"
    MANIPUR = "Manipur"
    MEGHALAYA = "Meghalaya"
    MIZORAM = "Mizoram"
    NAGALAND = "Nagaland"
    ODISHA = "Odisha"
    PUNJAB = "Punjab"
    RAJASTHAN = "Rajasthan"
    SIKKIM = "Sikkim"
    TAMIL_NADU = "Tamil Nadu"
    TELANGANA = "Telangana"
    TRIPURA = "Tripura"
    UTTAR_PRADESH = "Uttar Pradesh"
    UTTARAKHAND = "Uttarakhand"
    WEST_BENGAL = "West Bengal"
    ANDAMAN_NICOBAR = "Andaman and Nicobar Islands"
    CHANDIGARH = "Chandigarh"
    DADRA_NAGAR_HAVELI_AND_DAMAN_DIU = "Dadra and Nagar Haveli and Daman and Diu"
    DELHI = "Delhi"
    JAMMU_AND_KASHMIR = "Jammu and Kashmir"
    LADAKH = "Ladakh"
    LAKSHADWEEP = "Lakshadweep"
    PUDUCHERRY = "Puducherry"


STATE_DISTRICT_MAP = {
    "Andhra Pradesh": [
        "Anantapur", "Chittoor", "East Godavari", "Guntur",
        "Krishna", "Kurnool", "Prakasam", "Srikakulam",
        "Visakhapatnam", "Vizianagaram", "West Godavari", "YSR Kadapa"
    ],
    "Arunachal Pradesh": [
        "Tawang", "West Kameng", "East Kameng", "Papum Pare",
        "Kurung Kumey", "Kra Daadi", "Lower Subansiri", "Upper Subansiri",
        "West Siang", "East Siang", "Siang", "Upper Siang",
        "Lower Siang", "Lower Dibang Valley", "Dibang Valley", "Anjaw",
        "Lohit", "Namsai", "Changlang", "Tirap", "Longding"
    ],
    "Assam": [
        "Dispur", "Nagaon", "Dibrugarh", "Guwahati",
        "Silchar", "Tezpur", "Jorhat", "Sivasagar",
        "Barpeta", "Bongaigaon", "Cachar", "Darrang",
        "Kamrup", "Lakhimpur", "Morigaon", "Sonitpur",
        "Tinsukia", "Dhemaji", "Golaghat", "Karbi Anglong",
        "Karimganj", "Hailakandi", "Goalpara", "Nalbari",
        "Dhubri", "Baksa", "Chirang", "Udalguri"
    ],
    "Bihar": [
        "Patna", "Gaya", "Bhagalpur", "Muzaffarpur",
        "Purnia", "Darbhanga", "Arrah", "Begusarai",
        "Bettiah", "Buxar", "Chapra", "Samastipur",
        "Siwan", "Munger", "Nalanda", "Sitamarhi",
        "East Champaran", "West Champaran", "Supaul",
        "Madhepura", "Kishanganj", "Katihar", "Jehanabad",
        "Aurangabad", "Rohtas", "Jamui", "Khagaria",
        "Sheikhpura", "Lakhisarai", "Arwal", "Banka",
        "Gopalganj", "Saran", "Vaishali"
    ],
    "Chhattisgarh": [
        "Raipur", "Bilaspur", "Durg", "Korba",
        "Raigarh", "Jagdalpur", "Bastar", "Kanker",
        "Mahasamund", "Sukma", "Narayanpur", "Bijapur",
        "Dantewada", "Kondagaon", "Balod", "Baloda Bazar",
        "Bemetara", "Gariaband", "Mungeli", "Surajpur",
        "Gaurela Pendra Marwahi"
    ],
    "Goa": ["North Goa", "South Goa"],
    "Gujarat": [
        "Ahmedabad", "Surat", "Vadodara", "Rajkot",
        "Jamnagar", "Bhavnagar", "Anand", "Gandhinagar",
        "Junagadh", "Amreli", "Kheda", "Panchmahal",
        "Narmada", "Bharuch", "Dahod", "Patan",
        "Banaskantha", "Mehsana", "Surendranagar", "Aravalli",
        "Tapi", "Valsad", "Dang", "Chhota Udepur",
        "Mahisagar", "Devbhoomi Dwarka"
    ],
    "Haryana": [
        "Ambala", "Faridabad", "Gurgaon", "Hisar",
        "Karnal", "Kurukshetra", "Panipat", "Rohtak",
        "Sonipat", "Yamunanagar", "Jhajjar", "Bhiwani",
        "Charkhi Dadri", "Mahendragarh", "Rewari", "Panchkula",
        "Kaithal"
    ],
    "Himachal Pradesh": [
        "Shimla", "Solan", "Mandi", "Kullu",
        "Chamba", "Una", "Kangra", "Sirmaur",
        "Bilaspur", "Hamirpur", "Lahaul and Spiti", "Kinnaur"
    ],
    "Jharkhand": [
        "Ranchi", "Jamshedpur", "Dhanbad", "Bokaro",
        "Giridih", "Hazaribagh", "Dumka", "Deoghar",
        "East Singhbhum", "West Singhbhum", "Saraikela Kharsawan",
        "Godda", "Pakur", "Lohardaga", "Garhwa", "Latehar"
    ],
    "Karnataka": [
        "Bangalore Urban", "Bangalore Rural", "Mysore",
        "Mangalore", "Hubli", "Belgaum", "Dharwad",
        "Shimoga", "Chitradurga", "Hassan", "Mandya",
        "Udupi", "Chikmagalur", "Kolar", "Raichur",
        "Bellary", "Bijapur", "Gulbarga", "Tumkur",
        "Bagalkot", "Bidar", "Ramanagara", "Chamarajanagar"
    ],
    "Kerala": [
        "Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur",
        "Alappuzha", "Malappuram", "Palakkad", "Kollam",
        "Wayanad", "Idukki", "Kannur", "Pathanamthitta"
    ],
    "Madhya Pradesh": [
        "Bhopal", "Indore", "Gwalior", "Jabalpur",
        "Ujjain", "Sagar", "Satna", "Rewa",
        "Burhanpur", "Chhindwara", "Dewas", "Sehore",
        "Rajgarh", "Shivpuri", "Mandla", "Damoh",
        "Betul", "Hoshangabad", "Vidisha", "Panna",
        "Umaria", "Anuppur", "Ashoknagar", "Alirajpur",
        "Barwani", "Burhanpur", "Datia", "Dhar"
    ],
    "Maharashtra": [
        "Mumbai", "Pune", "Nagpur", "Nashik",
        "Thane", "Aurangabad", "Solapur", "Kolhapur",
        "Amravati", "Jalgaon", "Ahmednagar", "Satara",
        "Raigad", "Latur", "Parbhani", "Wardha",
        "Beed", "Buldhana", "Chandrapur", "Dhule",
        "Gadchiroli", "Gondia", "Hingoli", "Jalna",
        "Nanded", "Nandurbar", "Osmanabad", "Palghar",
        "Washim", "Yavatmal"
    ],
    "Manipur": [
        "Imphal East", "Imphal West", "Thoubal",
        "Bishnupur", "Churachandpur", "Senapati",
        "Tamenglong", "Ukhrul", "Jiribam"
    ],
    "Meghalaya": [
        "Shillong", "Nongpoh", "Tura", "Williamnagar",
        "Nongstoin", "Baghmara", "Mawkyrwat", "Resubelpara",
        "Bokajan"
    ],
    "Mizoram": [
        "Aizawl", "Lunglei", "Champhai",
        "Saiha", "Kolasib", "Lawngtlai",
        "Mamit", "Serchhip"
    ],
    "Nagaland": [
        "Kohima", "Dimapur", "Mokokchung", "Mon",
        "Tuensang", "Wokha", "Zunheboto", "Phek",
        "Kiphire"
    ],
    "Odisha": [
        "Bhubaneswar", "Cuttack", "Rourkela", "Berhampur",
        "Sambalpur", "Balasore", "Paradeep", "Baripada",
        "Puri", "Keonjhar", "Koraput", "Jagatsinghpur",
        "Mayurbhanj", "Sundargarh", "Kalahandi", "Nabarangpur",
        "Ganjam", "Bargarh", "Jharsuguda", "Balangir"
    ],
    "Punjab": [
        "Amritsar", "Ludhiana", "Jalandhar", "Patiala",
        "Bathinda", "Hoshiarpur", "Firozpur", "Fazilka",
        "Gurdaspur", "Sangrur", "Moga", "Rupnagar",
        "Muktsar", "Barnala", "Pathankot"
   
    ]
}




class IndianDistrict(Enum):
    ANANTAPUR = "Anantapur"
    CHITTOOR = "Chittoor"
    EAST_GODAVARI = "East Godavari"
    GUNTUR = "Guntur"
    TAWANG = "Tawang"
    WEST_KAMENG = "West Kameng"
    EAST_KAMENG = "East Kameng"
    PAPUM_PARE = "Papum Pare"
    DISPUR = "Dispur"
    NAGAON = "Nagaon"
    DIBRUGARH = "Dibrugarh"
    GUWAHATI = "Guwahati"
    PATNA = "Patna"
    GAYA = "Gaya"
    BHAGALPUR = "Bhagalpur"
    MUZAFFARPUR = "Muzaffarpur"
    RAIPUR = "Raipur"
    BILASPUR = "Bilaspur"
    DURG = "Durg"
    KORBA = "Korba"
    NORTH_GOA = "North Goa"
    SOUTH_GOA = "South Goa"
    AHMEDABAD = "Ahmedabad"
    SURAT = "Surat"
    VADODARA = "Vadodara"
    RAJKOT = "Rajkot"
    AMBALA = "Ambala"
    FARIDABAD = "Faridabad"
    GURGAON = "Gurgaon"
    HISAR = "Hisar"
    SHIMLA = "Shimla"
    SOLAN = "Solan"
    MANDI = "Mandi"
    KULLU = "Kullu"
    RANCHI = "Ranchi"
    JAMSHEDPUR = "Jamshedpur"
    DHANBAD = "Dhanbad"
    BOKARO = "Bokaro"
    BANGALORE = "Bangalore"
    MYSORE = "Mysore"
    MANGALORE = "Mangalore"
    HUBLI = "Hubli"
    THIRUVANANTHAPURAM = "Thiruvananthapuram"
    KOCHI = "Kochi"
    KOZHIKODE = "Kozhikode"
    THRISSUR = "Thrissur"
    BHOPAL = "Bhopal"
    INDORE = "Indore"
    GWALIOR = "Gwalior"
    JABALPUR = "Jabalpur"
    MUMBAI = "Mumbai"
    PUNE = "Pune"
    NAGPUR = "Nagpur"
    NASHIK = "Nashik"
    IMPHAL_EAST = "Imphal East"
    IMPHAL_WEST = "Imphal West"
    THOUBAL = "Thoubal"
    BISHNUPUR = "Bishnupur"
    SHILLONG = "Shillong"
    NONGPOH = "Nongpoh"
    TURA = "Tura"
    WILLIAMNAGAR = "Williamnagar"
    AIZAWL = "Aizawl"
    LUNGLEI = "Lunglei"
    CHAMPHAI = "Champhai"
    SAIHA = "Saiha"
    KOHIMA = "Kohima"
    DIMAPUR = "Dimapur"
    MOKOKCHUNG = "Mokokchung"
    MON = "Mon"
    BHUBANESWAR = "Bhubaneswar"
    CUTTACK = "Cuttack"
    ROURKELA = "Rourkela"
    BERHAMPUR = "Berhampur"
    AMRITSAR = "Amritsar"
    LUDHIANA = "Ludhiana"
    JALANDHAR = "Jalandhar"
    PATIALA = "Patiala"
    JAIPUR = "Jaipur"
    JODHPUR = "Jodhpur"
    UDAIPUR = "Udaipur"
    KOTA = "Kota"
    GANGTOK = "Gangtok"
    PAKYONG = "Pakyong"
    NAMCHI = "Namchi"
    MANGAN = "Mangan"
    CHENNAI = "Chennai"
    COIMBATORE = "Coimbatore"
    MADURAI = "Madurai"
    SALEM = "Salem"
    HYDERABAD = "Hyderabad"
    WARANGAL = "Warangal"
    NIZAMABAD = "Nizamabad"
    KARIMNAGAR = "Karimnagar"
    AGARTALA = "Agartala"
    UDAIPUR_TRIPURA = "Udaipur"
    DHARMANAGAR = "Dharmanagar"
    KAILASAHAR = "Kailasahar"
    LUCKNOW = "Lucknow"
    KANPUR = "Kanpur"
    AGRA = "Agra"
    VARANASI = "Varanasi"
    DEHRADUN = "Dehradun"
    HARIDWAR = "Haridwar"
    NAINITAL = "Nainital"
    RISHIKESH = "Rishikesh"
    KOLKATA = "Kolkata"
    HOWRAH = "Howrah"
    DURGAPUR = "Durgapur"
    ASANSOL = "Asansol"
    PORT_BLAIR = "Port Blair"
    CHANDIGARH = "Chandigarh"
    SILVASSA = "Silvassa"
    DAMAN = "Daman"
    NEW_DELHI = "New Delhi"
    DWARKA = "Dwarka"
    ROHINI = "Rohini"
    SRINAGAR = "Srinagar"
    JAMMU = "Jammu"
    ANANTNAG = "Anantnag"
    LEH = "Leh"
    KARGIL = "Kargil"
    KAVARATTI = "Kavaratti"
    PUDUCHERRY = "Puducherry"
    KARAIKAL = "Karaikal"
    MAHE = "Mahe"
    YANAM = "Yanam"

class VEHICLE_STATUS(str, Enum):
    AVAILABLE= "available"
    NOT_AVAILABLE="not_available"
    BOOKED= "booked"

class OTP_TYPE(str, Enum):
    VERIFICATION= "verification",
    RESET_PASSWORD="reset_password",
    LOGIN = "login"

class OTP_EXPIRY(int, Enum):
    TEN_MINUTS = 10,
    FIFTEEN_MINUTS = 15,
    THIRTY_MINUTS = 30



