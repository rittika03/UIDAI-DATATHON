import pandas as pd
import numpy as np

file_path = r"D:\Aadhar Dataset UIDAI\api_data_aadhar_enrolment\api_data_aadhar_enrolment\aadhar_enrolment_cleaned.csv"
df = pd.read_csv(file_path)

df.loc[df['district'] =='Itanagar', 'states_cleaned']='Arunachal Pradesh'
df.loc[df['district'] =='Bichom', 'states_cleaned']='Arunachal Pradesh'
df.loc[df['district'] =='Keyi Panyor', 'states_cleaned']='Arunachal Pradesh'

df.loc[df['district'] =='Itanagar', 'states_cleaned']='Arunachal Pradesh'
df.loc[df['district'] =='Keyi Panyor', 'states_cleaned']='Arunachal Pradesh'

df.loc[df['district'] =='Kamrup', 'states_cleaned']='Assam'

df.loc[df['district'] =='Vav-Tharad', 'states_cleaned']='Gujarat'

df.loc[df['district'] =='Kargil', 'states_cleaned']= 'Ladakh'
df.loc[df['district'] =='Leh', 'states_cleaned']= 'Ladakh'
df.loc[df['district'] =='Leh (ladakh)', 'states_cleaned']= 'Ladakh'

df.loc[df['district'] =='Kamjong', 'states_cleaned']='Manipur'
df.loc[df['district'] =='Kangpokpi', 'states_cleaned']='Manipur'
df.loc[df['district'] =='Noney', 'states_cleaned']='Manipur'
df.loc[df['district'] =='Tengnoupal', 'states_cleaned']='Manipur'

df.loc[df['district'] =='Rupnagar', 'states_cleaned']='Punjab'

df.loc[df['district'] =='Khairthal-Tijara', 'states_cleaned']='Rajasthan'
df.loc[df['district'] =='Khairthal Tijara', 'states_cleaned']='Rajasthan'
df.loc[df['district'] =='Khairthaltijara', 'states_cleaned']='Rajasthan'
df.loc[df['district'] =='Kotputli-Behror', 'states_cleaned']='Rajasthan'
df.loc[df['district'] =='Kotputli Behror', 'states_cleaned']='Rajasthan'
df.loc[df['district'] =='Kotputlibehror', 'states_cleaned']='Rajasthan'
df.loc[df['district'] =='Phalodi', 'states_cleaned']='Rajasthan'

df.loc[df['district'] =='Soreng', 'states_cleaned']='Sikkim'
df.loc[df['district'] =='Pakyong', 'states_cleaned']='Sikkim'

df.loc[df['district'] =='Adilabad', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Hyderabad', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Karimnagar', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Khammam', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Mahabubnagar', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Medak', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Nalgonda', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Nizamabad', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Rangareddy', 'states_cleaned']='Telangana'
df.loc[df['district'] =='Warangal', 'states_cleaned']='Telangana'

# STATES

# 1 Standardizing Andhra Pradesh Districts
df['district'].replace(['Ananthapur','Ananthapuramu'],'Anantapur',inplace=True)
df['district'].replace('Visakhapatanam', 'Visakhapatnam', inplace=True)
df['district'].replace(['Spsr Nellore', 'Nellore'], 'Sri Potti Sriramulu Nellore', inplace=True)
df['district'].replace(['Cuddapah', 'Y. S. R'], 'YSR Kadapa', inplace=True)
df['district'].replace(['N. T. R'], 'NTR', inplace=True)
df['district'].replace(['chittoor'], 'Chittoor', inplace=True)
unique_andhra = np.unique(df[df['states_cleaned'] == 'Andhra Pradesh']['district'])
print(unique_andhra)
print(len(unique_andhra))


# 2 Standardizing Arunachal Pradesh Districts
unique_arunachal = np.unique(df[df['states_cleaned'] == 'Arunachal Pradesh']['district'])
print(unique_arunachal)
print(len(unique_arunachal))

# 3 Standardizing Assam Districts
df['district'].replace('North Cachar Hills', 'Dima Hasao', inplace=True)
df['district'].replace('Sibsagar', 'Sivasagar', inplace=True)
df['district'].replace('Sribhumi','Karimganj' , inplace=True)
unique_assam = np.unique(df[df['states_cleaned'] == 'Assam']['district'])
print(unique_assam)
print(len(unique_assam))

# 4 Standardizing Bihar Districts
df['district'].replace(['Aurangabad(BH)','Aurangabad(bh)'],'Aurangabad' , inplace=True)
df['district'].replace('Bhabua','Kaimur (Bhabua)', inplace=True)
df['district'].replace(['Purba Champaran','Purbi Champaran','Motihari'],'East Champaran', inplace=True)
df['district'].replace('Pashchim Champaran','West Champaran', inplace=True)
df['district'].replace('Monghyr','Munger', inplace=True)
df['district'].replace('Purnea','Purnia', inplace=True)
df['district'].replace('Samstipur','Samastipur', inplace=True)
df['district'].replace('Sheikpura','Sheikhpura', inplace=True)
unique_bihar = np.unique(df[df['states_cleaned'] == 'Bihar']['district'])
print(unique_bihar)
print(len(unique_bihar))

# 5 Standardizing Chhattisgarh Districts
df['district'].replace('Dakshin Bastar Dantewada','Dantewada', inplace=True)
df['district'].replace(['Gaurela-pendra-marwahi','Gaurella Pendra Marwahi'],'Gaurella-Pendra-Marwahi', inplace=True)
df['district'].replace(['Janjgir - Champa', 'Janjgir-champa','Janjgir Champa'],'Janjgir-Champa', inplace=True)
df['district'].replace('Kawardha','Kabeerdham', inplace=True)
df['district'].replace('Uttar Bastar Kanker','Kanker', inplace=True)
df['district'].replace(['Mohalla-Manpur-Ambagarh Chowki','Mohla-Manpur-Ambagarh Chouki'],'Mohla-Manpur-Ambagarh Chowki', inplace=True)
unique_chhattisgarh = np.unique(df[df['states_cleaned'] == 'Chhattisgarh']['district'])
print(unique_chhattisgarh)
print(len(unique_chhattisgarh))

# 6 Standardizing Goa Districts
df['district'].replace('Bardez','North Goa', inplace=True)
unique_goa = np.unique(df[df['states_cleaned'] == 'Goa']['district'])
print(unique_goa)
print(len(unique_goa))

# 7 Standardizing Gujarat Districts
df['district'].replace('Ahmadabad','Ahmedabad', inplace=True)
df['district'].replace('Banas Kantha','Banaskantha', inplace=True)
df['district'].replace('Dohad','Dahod', inplace=True)
df['district'].replace(['The Dangs','Dang'],'Dangs', inplace=True)
df['district'].replace('Panch Mahals','Panchmahals', inplace=True)
df['district'].replace('Sabar Kantha','Sabarkantha', inplace=True)
df['district'].replace('Surendra Nagar','Surendranagar', inplace=True)
unique_gujarat = np.unique(df[df['states_cleaned'] == 'Gujarat']['district'])
print(unique_gujarat)
print(len(unique_gujarat))

# 8 Standardizing Haryana Districts
df['district'].replace('Gurgaon','Gurugram', inplace=True)
df['district'].replace('Jhajjar *','Jhajjar', inplace=True)
df['district'].replace('Mewat','Nuh', inplace=True)
df['district'].replace('Yamuna Nagar','Yamunanagar', inplace=True)
unique_haryana = np.unique(df[df['states_cleaned'] == 'Haryana']['district'])
print(unique_haryana)
print(len(unique_haryana))

# 9 Standardizing Himachal Pradesh Districts
df['district'].replace(['Lahul & Spiti','Lahul and Spiti'],'Lahaul and Spiti', inplace=True)
unique_himachal = np.unique(df[df['states_cleaned'] == 'Himachal Pradesh']['district'])
print(unique_himachal)
print(len(unique_himachal))

# 10 Standardizing Jharkhand Districts
df['district'].replace('Bokaro *','Bokaro', inplace=True)
df['district'].replace('Garhwa *','Garhwa', inplace=True)
df['district'].replace(['East Singhbum','Purbi Singhbhum'],'East Singhbhum', inplace=True)
df['district'].replace('Pashchimi Singhbhum','West Singhbhum', inplace=True)
df['district'].replace('Hazaribag','Hazaribagh', inplace=True)
df['district'].replace('Kodarma','Koderma', inplace=True)
df['district'].replace('Pakaur','Pakur', inplace=True)
df['district'].replace('Palamau','Palamu', inplace=True)
df['district'].replace('Sahebganj','Sahibganj', inplace=True)
df['district'].replace('Seraikela-kharsawan','Seraikela-Kharsawan', inplace=True)
unique_jharkhand = np.unique(df[df['states_cleaned'] == 'Jharkhand']['district'])
print(unique_jharkhand)
print(len(unique_jharkhand))

# 11 Standardizing Karnataka Districts
df['district'].replace('Bagalkot *','Bagalkot', inplace=True)
df['district'].replace('Belgaum','Belagavi', inplace=True)
df['district'].replace('Bellary','Ballari', inplace=True)
df['district'].replace('Bangalore Rural','Bengaluru Rural', inplace=True)
df['district'].replace(['Bengaluru','Bangalore'],'Bengaluru Urban', inplace=True)
df['district'].replace(['Chamarajanagar *','Chamrajanagar','Chamrajnagar'],'Chamarajanagar', inplace=True)
df['district'].replace(['Chickmagalur','Chikmagalur'],'Chikkamagaluru', inplace=True)
df['district'].replace('Chikkaballapur','Chikkaballapura', inplace=True)
df['district'].replace('Davangere','Davanagere', inplace=True)
df['district'].replace('Gadag *','Gadag', inplace=True)
df['district'].replace('Hasan','Hassan', inplace=True)
df['district'].replace('Haveri *','Haveri', inplace=True)
df['district'].replace('Gulbarga','Kalaburagi', inplace=True)
df['district'].replace('Mysore','Mysuru', inplace=True)
df['district'].replace(['Ramanagar','Ramanagara'],'Bengaluru South', inplace=True)
df['district'].replace('Shimoga','Shivamogga', inplace=True)
df['district'].replace('Tumkur','Tumakuru' , inplace=True)
df['district'].replace('Udupi *','Udupi' , inplace=True)
df['district'].replace(['Bijapur','Bijapur(KAR)'],'Vijayapura', inplace=True)
df['district'].replace('yadgir' ,'Yadgir', inplace=True)
unique_karnataka = np.unique(df[df['states_cleaned'] == 'Karnataka']['district'])
print(unique_karnataka)
print(len(unique_karnataka))

# 12 Standardizing Kerala Districts
df['district'].replace('Kasargod' ,'Kasaragod', inplace=True)
unique_kerala = np.unique(df[df['states_cleaned'] == 'Kerala']['district'])
print(unique_kerala)
print(len(unique_kerala))

# 13 Standardizing Madhya Pradesh Districts
df['district'].replace('West Nimar' ,'Khargone', inplace=True)
df['district'].replace('Ashok Nagar','Ashoknagar', inplace=True)
df['district'].replace('East Nimar','Khandwa', inplace=True)
df['district'].replace('Harda *','Harda', inplace=True)
df['district'].replace('Hoshangabad','Narmadapuram', inplace=True)
df['district'].replace('Narsimhapur','Narsinghpur', inplace=True)
unique_madhya = np.unique(df[df['states_cleaned'] == 'Madhya Pradesh']['district'])
print(unique_madhya)
print(len(unique_madhya))

# 14 Standardizing Maharashtra Districts
df['district'].replace(['Ahmadnagar', 'Ahmed Nagar','Ahmednagar'],'Ahilyanagar', inplace=True)
df['district'].replace('Bid','Beed', inplace=True)
df['district'].replace('Buldana','Buldhana', inplace=True)
df['district'].replace(['Aurangabad','Chatrapati Sambhaji Nagar'],'Chhatrapati Sambhajinagar', inplace=True)
df['district'].replace('Osmanabad','Dharashiv', inplace=True)
df['district'].replace(['Gondiya','Gondiya *'],'Gondia', inplace=True)
df['district'].replace('Hingoli *','Hingoli', inplace=True)
df['district'].replace('Mumbai City','Mumbai', inplace=True)
df['district'].replace('Mumbai( Sub Urban )','Mumbai Suburban', inplace=True)
df['district'].replace('Nandurbar *','Nandurbar', inplace=True)
df['district'].replace(['Raigarh','Raigarh(MH)'],'Raigad', inplace=True)
df['district'].replace('Washim *','Washim', inplace=True)
unique_maharashtra = np.unique(df[df['states_cleaned'] == 'Maharashtra']['district'])
print(unique_maharashtra)
print(len(unique_maharashtra))

# 15 Standardizing Manipur Districts
unique_manipur = np.unique(df[df['states_cleaned'] == 'Manipur']['district'])
print(unique_manipur)
print(len(unique_manipur))

# 16 Standardizing Meghalaya Districts
unique_meghalaya = np.unique(df[df['states_cleaned'] == 'Meghalaya']['district'])
print(unique_meghalaya)
print(len(unique_meghalaya))

# 17 Standardizing Mizoram Districts
df['district'].replace('Mammit','Mamit', inplace=True)
unique_mizoram = np.unique(df[df['states_cleaned'] == 'Mizoram']['district'])
print(unique_mizoram)
print(len(unique_mizoram))

# 18 Standardizing Nagaland Districts
unique_nagaland = np.unique(df[df['states_cleaned'] == 'Nagaland']['district'])
print(unique_nagaland)
print(len(unique_nagaland))

# 19 Standardizing Odisha Districts
df['district'].replace(['ANGUL','ANUGUL','Anugal','Anugul'],'Angul', inplace=True)
df['district'].replace(['Baleshwar','Baleswar'], 'Balasore', inplace=True)
df['district'].replace('Debagarh','Deogarh', inplace=True)
df['district'].replace('Baudh','Boudh', inplace=True)
df['district'].replace('Jagatsinghpur','Jagatsinghapur', inplace=True)
df['district'].replace(['JAJPUR','Jajapur','jajpur'], 'Jajpur', inplace=True)
df['district'].replace('Kendrapara *', 'Kendrapara', inplace=True)
df['district'].replace('Kendujhar', 'Keonjhar', inplace=True)
df['district'].replace('Khorda','Khordha', inplace=True)
df['district'].replace('Nabarangapur','Nabarangpur', inplace=True)
df['district'].replace('NUAPADA','Nuapada', inplace=True)
df['district'].replace('Subarnapur','Sonapur', inplace=True)
df['district'].replace('Sundergarh','Sundargarh', inplace=True)
unique_odisha = np.unique(df[df['states_cleaned'] == 'Odisha']['district'])
print(unique_odisha)
print(len(unique_odisha))

# 20  Standardizing Punjab Districts
df['district'].replace('Firozpur','Ferozepur', inplace=True)
df['district'].replace('Muktsar','Sri Muktsar Sahib', inplace=True)
df['district'].replace('Nawanshahr','Shaheed Bhagat Singh Nagar', inplace=True)
df['district'].replace(['S.A.S Nagar(Mohali)','SAS Nagar (Mohali)'],'S.A.S Nagar', inplace=True)
unique_punjab = np.unique(df[df['states_cleaned'] == 'Punjab']['district'])
print(unique_punjab)
print(len(unique_punjab))

# 21 Standardizing Rajasthan Districts
df['district'].replace('Chittaurgarh','Chittorgarh', inplace=True)
df['district'].replace('Deeg\xa0','Deeg', inplace=True)
df['district'].replace('Dhaulpur','Dholpur', inplace=True)
df['district'].replace('Jalor','Jalore', inplace=True)
df['district'].replace('Jhunjhunun','Jhunjhunu', inplace=True)
unique_rajasthan = np.unique(df[df['states_cleaned'] == 'Rajasthan']['district'])
print(unique_rajasthan)
print(len(unique_rajasthan))

# 22 Standardizing Sikkim Districts
df['district'].replace(['East','East Sikkim'],'Gangtok', inplace=True)
df['district'].replace(['North','North Sikkim'],'Mangan', inplace=True)
df['district'].replace(['South','South Sikkim'],'Namchi', inplace=True)
df['district'].replace(['West','West Sikkim'],'Gyalshing', inplace=True)
unique_sikkim = np.unique(df[df['states_cleaned'] == 'Sikkim']['district'])
print(unique_sikkim)
print(len(unique_sikkim))

# 23 Standardizing Tamil Nadu Districts
df['district'].replace('Kanchipuram','Kancheepuram', inplace=True)
df['district'].replace('Kanyakumari','Kanniyakumari', inplace=True)
df['district'].replace('Namakkal   *','Namakkal', inplace=True)
df['district'].replace(['Thiruvarur','Tiruvallur'],'Thiruvallur', inplace=True)
df['district'].replace('Tirupattur','Tirupathur', inplace=True)
df['district'].replace('Tuticorin','Thoothukkudi', inplace=True)
df['district'].replace('Viluppuram','Villupuram', inplace=True)
unique_tamil = np.unique(df[df['states_cleaned'] == 'Tamil Nadu']['district'])
print(unique_tamil)
print(len(unique_tamil))

# 24 Standardizing Telangana Districts
df['district'].replace(['Mahabub Nagar', 'Mahbubnagar'], 'Mahabubnagar', inplace=True)
df['district'].replace(['Karim Nagar'], 'Karimnagar', inplace=True)
df['district'].replace(['rangareddi', 'K.V.Rangareddy', 'K.v. Rangareddy', 'Rangareddi'], 'Rangareddy', inplace=True)
df['district'].replace('Jangaon','Jangoan', inplace=True)
df['district'].replace( 'Komaram Bheem','Kumuram Bheem Asifabad', inplace=True)
df['district'].replace(['Medchal-malkajgiri','Medchal?malkajgiri','Medchal−malkajgiri'],'Medchal Malkajgiri', inplace=True)
df['district'].replace('Rangareddy','Ranga Reddy', inplace=True)
df['district'].replace(['Warangal (urban)','Warangal Rural','Warangal Urban'],'Warangal', inplace=True)
unique_telangana = np.unique(df[df['states_cleaned'] == 'Telangana']['district'])
print(unique_telangana)
print(len(unique_telangana))

# 25 Standardizing Tripura Districts
df['district'].replace('Dhalai  *','Dhalai', inplace=True)
unique_tripura = np.unique(df[df['states_cleaned'] == 'Tripura']['district'])
print(unique_tripura)
print(len(unique_tripura))

# 26 Standardizing Uttar Pradesh Districts
df['district'].replace('Faizabad','Ayodhya', inplace=True)
df['district'].replace('Bagpat','Baghpat', inplace=True)
df['district'].replace('Barabanki','Bara Banki', inplace=True)
df['district'].replace('Bulandshahar','Bulandshahr', inplace=True)
df['district'].replace(['Sant Ravidas Nagar','Sant Ravidas Nagar Bhadohi'],'Bhadohi',inplace=True)
df['district'].replace('Jyotiba Phule Nagar','Amroha', inplace=True)
df['district'].replace(['Kushi Nagar','Kushinagar *'],'Kushinagar',inplace=True)
df['district'].replace('Maharajganj','Mahrajganj', inplace=True)
df['district'].replace('Allahabad','Prayagraj', inplace=True)
df['district'].replace('Raebareli','Rae Bareli', inplace=True)
df['district'].replace('Shravasti','Shrawasti', inplace=True)
df['district'].replace('Siddharth Nagar','Siddharthnagar', inplace=True)
unique_up = np.unique(df[df['states_cleaned'] == 'Uttar Pradesh']['district'])
print(unique_up)
print(len(unique_up))

# 27 Standardizing Uttarakhand Districts
df['district'].replace('Hardwar','Haridwar', inplace=True)
unique_uttarakhand = np.unique(df[df['states_cleaned'] == 'Uttarakhand']['district'])
print(unique_uttarakhand)
print(len(unique_uttarakhand))

# 28 Standardizing West Bengal Districts
df['district'].replace(['24 Paraganas North','North Twenty Four Parganas'],'North 24 Parganas', inplace=True)
df['district'].replace(['24 Paraganas South','South 24 parganas','South 24 Pargana','South Twenty Four Parganas'],'South 24 Parganas', inplace=True)
df['district'].replace('KOLKATA','Kolkata', inplace=True)
df['district'].replace(['Coochbehar','Koch Bihar'],'Cooch Behar', inplace=True)
df['district'].replace(['Dinajpur Dakshin','South Dinajpur',],'Dakshin Dinajpur', inplace=True)
df['district'].replace(['Dinajpur Uttar','North Dinajpur'],'Uttar Dinajpur', inplace=True)
df['district'].replace('Darjiling','Darjeeling' , inplace=True)
df['district'].replace(['HOWRAH','Haora','Hawrah'],'Howrah', inplace=True)
df['district'].replace(['HOOGHLY','Hooghiy','Hugli','hooghly'],'Hooghly', inplace=True)
df['district'].replace(['MALDA','Maldah'],'Malda', inplace=True)
df['district'].replace(['East Midnapore','East Midnapur','Medinipur'],'Purba Medinipur' , inplace=True)
df['district'].replace(['West Medinipur','West Midnapore','Medinipur West'],'Paschim Medinipur', inplace=True)
df['district'].replace(['NADIA','nadia'],'Nadia', inplace=True)
df['district'].replace('Puruliya','Purulia', inplace=True)
df['district'].replace(['Burdwan','Barddhaman','Bardhaman'],'Purba Bardhaman', inplace=True)
unique_wb = np.unique(df[df['states_cleaned'] == 'West Bengal']['district'])
print(unique_wb)
print(len(unique_wb))

# UNION TERRITORIES

# 1 Standardizing Andaman and Nicobar Islands Districts
df['district'].replace('Nicobar','Nicobars', inplace=True)
df['district'].replace(['Andamans','South Andaman'],'South Andamans', inplace=True)
unique_an_ni = np.unique(df[df['states_cleaned'] == 'Andaman and Nicobar Islands']['district'])
print(unique_an_ni)
print(len(unique_an_ni))

# 2 Standardizing Chandigarh Districts
unique_chandigarh = np.unique(df[df['states_cleaned'] == 'Chandigarh']['district'])
print(unique_chandigarh)
print(len(unique_chandigarh))

# 3 Standardizing Dadra and Nagar Haveli and Daman and Diu Districts
df['district'].replace(['Dadra & Nagar Haveli','Dadra and Nagar Haveli'], 'Dadra And Nagar Haveli', inplace=True)
unique_dadra_daman = np.unique(df[df['states_cleaned'] == 'Dadra and Nagar Haveli and Daman and Diu']['district'])
print(unique_dadra_daman)
print(len(unique_dadra_daman))

# 4 Standardizing Delhi Districts
df['district'].replace(['North East','North East   *'],'North East Delhi', inplace=True)
df['district'].replace('Najafgarh','South West Delhi', inplace=True)
unique_delhi = np.unique(df[df['states_cleaned'] == 'Delhi']['district'])
print(unique_delhi)
print(len(unique_delhi))

# 5 Standardizing Jammu and Kashmir Districts
df['district'].replace('Badgam','Budgam', inplace=True)
df['district'].replace(['Bandipore','Bandipur'],'Bandipora', inplace=True)
df['district'].replace(['Punch','punch'],'Poonch', inplace=True)
df['district'].replace('Rajauri','Rajouri', inplace=True)
df['district'].replace('Shupiyan','Shopian', inplace=True)
unique_jk = np.unique(df[df['states_cleaned'] == 'Jammu and Kashmir']['district'])
print(unique_jk)
print(len(unique_jk))

# 6 Standardizing Ladakh Districts
df['district'].replace('Leh (ladakh)','Leh', inplace=True)
unique_ladakh = np.unique(df[df['states_cleaned'] == 'Ladakh']['district'])
print(unique_ladakh)
print(len(unique_ladakh))

# 7 Standardizing Lakshadweep Districts
unique_lakshadweep = np.unique(df[df['states_cleaned'] ==  'Lakshadweep']['district'])
print(unique_lakshadweep)
print(len(unique_lakshadweep))

# 8 Standardizing Puducherry Districts
df['district'].replace('Pondicherry','Puducherry', inplace=True)
unique_pondicherry = np.unique(df[df['states_cleaned'] == 'Puducherry']['district'])
print(unique_pondicherry)
print(len(unique_pondicherry))

df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
df.to_csv(r"D:\Aadhar Dataset UIDAI\api_data_aadhar_enrolment\api_data_aadhar_enrolment\aadhaar_enrolment_final_cleaned.csv", index=False)