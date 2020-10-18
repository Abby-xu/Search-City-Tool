import streamlit as st
from PIL import Image
import pydeck as pdk
import pandas as pd
import numpy as np
import webbrowser
import time
import copy
import csv
# from streamlit.ScriptRunner import StopException, RerunException
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def main():
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://sfwallpaper.com/images/background-image-for-website-1.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    local_css("style.css")
   # t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"
    #st.markdown(t, unsafe_allow_html=True)
    

    st.title("Search City Tool")
    #st.header("By completing the following survey to find cities that fit you the best")
    t = "<div><span class = 'bold'>By completing the following survey to find cities that fit you the best</span></div>"
    st.markdown(t, unsafe_allow_html=True)
    img = Image.open("american map.jpg")
    st.image(img,width = 700)
    option_list = []


    pollution_sub = "<div><span class = 'color'>Consider the pollution as an essential factor to rank your cities?</span></div>"
    st.markdown(pollution_sub, unsafe_allow_html=True)
    pollution_consideration = st.radio((""), ("Yes","No"))
    if(pollution_consideration == 'Yes'):
        st.success("Yes")
        option_list.append(1)
    else:
        st.success('No')
        option_list.append(0)

    crime_sub = "<div><span class = 'color'>Consider the crime rate as an essential factor to rank your cities?</span></div>"
    st.markdown(crime_sub, unsafe_allow_html=True)
    crime_status = st.radio((""), ("Yes","No"),key=1)
    if(crime_status == 'Yes'):
        st.success("Yes")
        option_list.append(1)
    else:
        st.success("No")
        option_list.append(0)

    income_sub = "<div><span class = 'color'>What is your expected average income?</span></div>"
    st.markdown(income_sub, unsafe_allow_html=True)
    income_option = st.selectbox(
        (""),
        ('None','Low','Medium','High'))
    st.write('You selected:', income_option)
    if(income_option == 'None'):
        option_list.append(0)
    elif(income_option == "Low"): 
        option_list.append(1)
    elif(income_option == 'Medium'): 
        option_list.append(2)
    else: 
        option_list.append(3)


    education_sub = "<div><span class = 'color'>Expected Eductional Level?</span></div>"
    st.markdown(education_sub, unsafe_allow_html=True)
    education_option = st.selectbox(
        (""),
        ('None','Low','Medium','High'), key = 0)
    st.write('You selected:', education_option)
    if(education_option == 'None'):
        option_list.append(0)
    elif(education_option == "Low"): 
        option_list.append(1)
    elif(education_option == 'Medium'): 
        option_list.append(2)
    else: 
        option_list.append(3)


    health_sub = "<div><span class = 'color'>Expected Health Care Level?</span></div>"
    st.markdown(health_sub, unsafe_allow_html=True)
    health_option = st.selectbox(
        (""),
        ('None','Low','Medium','High'), key = 1)
    st.write('You selected:', health_option)
    if(health_option == 'None'):
        option_list.append(0)
    elif(health_option == "Low"): 
        option_list.append(1)
    elif(health_option == 'Medium'): 
        option_list.append(2)
    else: 
        option_list.append(3)


    population_sub = "<div><span class = 'color'>Expected Population Density?</span></div>"
    st.markdown(population_sub, unsafe_allow_html=True)
    population_option = st.selectbox(
        (""),
        ('None','Low','Medium','High'), key = 2)
    st.write('You selected:', population_option)
    if(population_option == 'None'):
        option_list.append(0)
    elif(population_option == "Low"): 
        option_list.append(1)
    elif(population_option == 'Medium'): 
        option_list.append(2)
    else: 
        option_list.append(3)




    # st.button("READY TO SUBMIT YOUR INFO")
    if st.button("Submit"):
        my_bar = st.progress(0)
        for n in range(100):
            my_bar.progress(n)
            time.sleep(0.000001)
        print(option_list)
        with st.spinner('Waiting'):
            time.sleep(0.1)
        st.success('Submmited')
    return option_list

def reformat(list0):
    list_formatted = []
    for n in range(len(list0)):
        dif = abs(max(list0) - min(list0))
        list_formatted.append((list0[n] - min(list0)) / dif * 100)
    return list_formatted


# print for checking cityData/CityData/data
def print_data(list1):
    for n in range(len(list1)):
        print(list1[n])
    print("length: ", len(list1))

###### def func ######
def card(rank,city_name,avg_income=100,population=1000,crime=23,img="1.jpg",sentence="this is a sentence",link='https://realestate.usnews.com/places/rankings/best-places-to-live'):

    st.markdown('''----''')

    col1, col2 = st.beta_columns(2)
    col1.header(city_name)
    col1.markdown(":sunglasses: #"+str(rank)+" in Best Places to live")
    col1.write(sentence)
    if st.button("more",key=rank):
        webbrowser.open_new_tab(link)
    # col1.markdown("[more](https://realestate.usnews.com/places/rankings/best-places-to-live)")

    image=Image.open(img)
    col2.image(image,width=300)
    col2.subheader("Average income:"+str(avg_income))
    col2.subheader("Population:"+str(population))
    col2.subheader("Crime rate:"+str(crime))

    st.markdown('''----''')

def result(result_data):
    # Background
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://sfwallpaper.com/images/background-image-for-website-1.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Text/Title
    st.title("Search Results")

    # Let user choose the range of showing cities (5-15)
    st.subheader("Please selected the number of cities you wanna check")
    city_show=st.slider("",min_value=1, max_value=15, step=1)
    st.write("There is the list of", city_show, "cities we selected for you")

    # Make the range of user selected
    cities_name=result_data[0][:city_show]
    lat=result_data[1][:city_show]
    lon=result_data[2][:city_show]
    avg_income=result_data[3][:city_show] # avg_income
    population=result_data[4][:city_show]
    crime_rate=result_data[5][:city_show]
    sentence=result_data[6][:city_show]
    pic=result_data[7][:city_show]
    link=result_data[8][:city_show]
    

    # Map the cities
    map_data = pd.DataFrame({
        'awesome cities' : cities_name,
        'lat' : lat,
        'lon' : lon
    })
    st.map(map_data)

    # Make a list of cities
    for i in range(0,len(cities_name)):
        card(rank=i+1,city_name=cities_name[i],img="photo_city/"+str(pic[i]),sentence=sentence[i],avg_income=avg_income[i],population=population[i],crime=crime_rate[i],link=link[i])


if __name__ == '__main__':
    option_list = main()

    # cities_name=['San Jose', 'San Francisco', 'Seattle', 'San Diego', 'Austin', 'Boston', 'Portland', 'Denver', 'Charlotte', 'New York', 'Minneapolis', 'Sacramento', 'Los Angeles', 'Las Vegas', 'Omaha', 'Chicago', 'Oklahoma City', 'Atlanta', 'Phoenix', 'Jacksonville', 'San Antonio', 'Albuquerque', 'Kansas City', 'Columbus', 'Houston', 'Louisville', 'Wichita', 'Dallas', 'Baltimore', 'El Paso', 'Indianapolis', 'Fresno', 'Philadelphia', 'Tucson', 'Memphis', 'Milwaukee', 'Miami', 'Cleveland', 'Detroit']
    # lat=[37.279518, 37.733795, 47.60621, 32.834686, 30.266666, 42.361145, 45.523064, 39.742043, 35.227085, 40.73061, 44.986656, 38.575764, 34.052235, 36.114647, 41.25716, 41.881832, 35.481918, 33.753746, 33.448376, 30.332184, 29.424349, 35.106766, 39.099724, 39.983334, 29.749907, 38.328732, 37.697948, 32.779167, 39.299236, 31.772543, 39.791, 36.746841, 39.952583, 32.25346, 35.1175, 43.038902, 25.761681, 41.505493, 42.331429]
    # lon=[-121.867905, -122.446747, -122.33207, -117.130775, -97.73333, -71.057083, -122.676483, -104.991531, -80.843124, -73.935242, -93.258133, -121.478851, -118.243683, -115.172813, -95.995102, -87.623177, -97.508469, -84.38633, -112.07403, -81.655647, -98.491142, -106.629181, -94.578331, -82.98333, -95.358421, -85.764771, -97.314835, -96.808891, -76.609383, -106.460953, -86.148003, -119.772591, -75.165222, -110.911789, -89.971107, -87.906471, -80.191788, -81.68129, -83.045753]
    # pic=['San_Jose.jpg', 'San_Francisco.jpg', 'Seattle.jpg', 'San_Diego.jpg', 'Austin.jpg', 'Boston.jpg', 'Portland.jpg', 'Denver.jpg', 'Charlotte.jpg', 'New_York.jpg', 'Minneapolis.jpg', 'Sacramento.jpg', 'Los_Angeles.jpg', 'Las_Vegas.jpg', 'Omaha.jpg', 'Chicago.jpg', 'Oklahoma_City.jpg', 'Atlanta.jpg', 'Phoenix.jpg', 'Jacksonville.jpg', 'San_Antonio.jpg', 'Albuquerque.jpg', 'Kansas_City.jpg', 'Columbus.jpg', 'Houston.jpg', 'Louisville.jpg', 'Wichita.jpg', 'Dallas.jpg', 'Baltimore.jpg', 'El_Paso.jpg', 'Indianapolis.jpg', 'Fresno.jpg', 'Philadelphia.jpg', 'Tucson.jpg', 'Memphis.jpg', 'Milwaukee.jpg', 'Miami.jpg', 'Cleveland.jpg', 'Detroit.jpg']

    # result_data=[cities_name,lat,lon,pic]
    # result(result_data)


    cityData = []
    select = option_list  # input list[Pollution(0/1), Crime(0/1), income(0-3), education(0-3), health care(0-3), pop-Density(0-3)]
    data = []  # output list[City, lat, lon, avg_income, population, crime rate]


    with open("dataset1.csv", "r") as cityDataFile:
        cityData = cityDataFile.readlines()

        # import data => list
        for i in range(len(cityData)):
            if i == 0: continue
            cityData[i] = cityData[i].split(";")
            Avg_income = ""
            Avg_income = cityData[i][1]  # 'Average income'
            for j in range(len(cityData[i])):
                # cityData[i][j] = cityData[i][j].strip()
                if j == 0: cityData[i][j] = cityData[i][j].strip()         # 'City'
                if j == 1: cityData[i][j] = float(cityData[i][j][1:-1])    # 'Average income' striped
                if j == 2: cityData[i][j] = float(cityData[i][j])          # 'Education'
                if j == 3: cityData[i][j] = float(cityData[i][j])          # 'Density(Persons/Square Mile)'
                if j == 4: cityData[i][j] = int(cityData[i][j])            # 'Population'
                if j == 5: cityData[i][j] = int(cityData[i][j])            # 'Pollution'
                if j == 6: cityData[i][j] = float(cityData[i][j])          # 'Crime rate',
                if j == 7: cityData[i][j] = float(cityData[i][j])          # 'Latitude'
                if j == 8: cityData[i][j] = float(cityData[i][j].strip())  # 'Longitude'
                if j == 9: cityData[i][j] = cityData[i][j].strip()         # 'Sentence'
            cityData[i].append(cityData[i][0].replace(" ", "_")+".jpg")    # 'Picture name
            cityData[i].append(Avg_income)
            # cityData[i].append()
        del(cityData[0])

    # print for checking
    # print_data(cityData)

    ###################################
    #         Median analysis         #
    ###################################
    CityData = copy.deepcopy(cityData)
    # construct and copy
    # print_data(CityData)

    AverageIncome = []
    Education = []
    Density = []
    Population = []
    Pollution = []
    CrimeRate = []
    for i in range(len(CityData)):
        AverageIncome.append(CityData[i][1])
        Education.append(CityData[i][2])
        Density.append(CityData[i][3])
        Population.append(CityData[i][4])
        Pollution.append(CityData[i][5])
        CrimeRate.append(CityData[i][6])
    for i in range(len(CityData)):
        CityData[i][1] = reformat(AverageIncome)[i]
        CityData[i][2] = reformat(Education)[i]
        CityData[i][3] = reformat(Density)[i]
        CityData[i][4] = reformat(Population)[i]
        CityData[i][5] = reformat(Pollution)[i]
        CityData[i][6] = reformat(CrimeRate)[i]

    # # print for checking
    # print("-----------------##1##----------------")
    # printData(cityData)
    # print("-----------------##2##----------------")
    # printData(CityData)


    ##################################
    #        Weight analysis         #
    ##################################
    # score = a*P + b*C + c*I + d*E + f*H + g*POP
    # a + b + c + ... + g = 1
    # select[6] : [Pollution(0/1), Crime(0/1), income(0-3), education(0-3), health care(0-3), pop-Density(0-3)]

    # select = [0, 0, 3, 3, 1, 3]
    scoreData = []  # Score list
    coefficient = []  # list for statical weight
    for i in range(len(select)):
        coefficient.append(select[i]/sum(select))

    # Calculate score
    for i in range(len(CityData)):
        score = 0
        for j in range(len(coefficient)):
            score += coefficient[j] * CityData[i][j + 1]
        scoreData.append([score, cityData[i]])

    scoreData.sort(reverse=True) # sort with score
    # sorted(scoreData,key=lambda scoreData:scoreData[0], reverse=True)

    # print_data(scoreData)

    ##################################
    #        Output data list        #
    ##################################
    for i in range(15):
        data.append([scoreData[i][1][0],   # City
                    scoreData[i][1][7],   # lat
                    scoreData[i][1][8],   # lon
                    scoreData[i][1][11],  # Average income
                    scoreData[i][1][4],   # Population
                    round(scoreData[i][1][6],3),   # Crime rate
                    scoreData[i][1][9],   # Sentence
                    scoreData[i][1][10],  # Picture name
                    "https://en.wikipedia.org/wiki/"+scoreData[i][1][0].replace(" ", "_")  # Website
                    ])

    # print_data(data)
    data_read = []
    for i in range(len(data[0])):
        data_column = []
        for j in range(len(data)):
            data_column.append(data[j][i])
        data_read.append(data_column)

    result(data_read)