from flask import Flask,render_template,request
from flask_cors import cross_origin
import pickle
import pandas as pd


app=Flask(__name__)
model = pickle.load(open("flight_price_prediction.pkl", "rb"))

@app.route('/')
@app.route('/home')
@cross_origin()
def home():
    return render_template('front.html')

@app.route('/flight',methods=["GET","POST"])
@cross_origin()
def flight():
    if request.method == "POST":

        #Departure Date And Time
        date_dep = request.form["Dep_Time"]
        departure_day= int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        departure_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)


        departure_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        departure_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)


        # Arrival Date And Time
        date_arr = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)


        # Duration
        duration_hour = abs(arrival_hour- departure_hour)
        duration_min = abs(arrival_min - departure_min)


        #Stops
        Stops = int(request.form["stops"])

        # Airline
        airline = request.form['airline']
        if (airline == 'Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Air_Asia=0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Air Asia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif (airline == 'Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Air_Asia = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        # Source
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            source_Delhi = 1
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0
            source_Banglore = 0

        elif (Source == 'Kolkata'):
            source_Delhi = 0
            source_Kolkata = 1
            source_Mumbai = 0
            source_Chennai = 0
            source_Banglore = 0

        elif (Source == 'Mumbai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 1
            source_Chennai = 0
            source_Banglore = 0

        elif (Source == 'Chennai'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 1
            source_Banglore = 0

        elif (Source == 'Banglore'):
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0
            source_Banglore = 1

        else:
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0
            source_Banglore = 0


        # Destination
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            destination_Cochin = 1
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0
            destination_Banglore=0

        elif (Destination == 'Delhi'):
            destination_Cochin = 0
            destination_Delhi = 1
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0
            destination_Banglore = 0

        elif (Destination == 'New_Delhi'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 1
            destination_Hyderabad = 0
            destination_Kolkata = 0
            destination_Banglore = 0

        elif (Destination == 'Hyderabad'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 1
            destination_Kolkata = 0
            destination_Banglore = 0

        elif (Destination == 'Kolkata'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 1
            destination_Banglore = 0

        elif (Destination == 'Banglore'):
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0
            destination_Banglore = 1

        else:
            destination_Cochin = 1
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0
            destination_Banglore = 0

        prediction = model.predict([[
            Stops,
            departure_day,
            departure_month,
            departure_hour,
            departure_min,
            arrival_hour,
            arrival_min,
            duration_hour,
            duration_min,
            Air_Asia,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            source_Banglore,
            source_Chennai,
            source_Delhi,
            source_Kolkata,
            source_Mumbai,
            destination_Banglore,
            destination_Cochin,
            destination_Delhi,
            destination_Hyderabad,
            destination_Kolkata,
            destination_New_Delhi
        ]])

        price = round(prediction[0], 2)
        if(Source==Destination or (duration_hour+duration_min)==0):
            price=0.0

        return render_template('flight.html', prediction="Your Flight price is Rs. {}".format(price))

    return render_template("flight.html")

choice = ''
lstmain=[]
flager=False

@app.route('/corona',methods=["GET","POST"])
@cross_origin()
def corona():
    global choice
    global lstmain
    global flager


    df = pd.read_csv('Covid-19 dataset')

    if request.method == "POST":

        if(choice==''):

            choice = request.form['choice']
            flager=False

        elif (choice == 'one'):

            country = request.form['sing_country_yearly']
            lstmain = [['Months', 'Average Cases', 'Average Deaths']]
            lstm = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
            lst = df[df['countriesAndTerritories'] == country].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst2 = df[df['countriesAndTerritories'] == country].groupby('month').agg({'deaths': 'mean'})[
                'deaths'].reindex(index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            for i in range(len(lst)):
                lstmain.append([lstm[i], lst[i], lst2[i]])

            flager=True

            return render_template('Corona_chart.html',lstmain=lstmain)



        elif (choice == 'two'):

            country = request.form['sing_country_monthly']
            month = request.form['sing_country_month']
            lstmain = [[month, 'Cases', 'Deaths']]
            lstm = list(range(1, 32))
            lst = df[(df['countriesAndTerritories'] == country) & (df['month'] == month)]['cases'].tolist()
            lst2 = df[(df['countriesAndTerritories'] == country) & (df['month'] == month)]['deaths'].tolist()
            for i in range(len(lst)):
                lstmain.append([lstm[i], lst[i], lst2[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)



        elif (choice == 'three'):
            country1 = request.form['two_country_yearly1']
            country2 = request.form['two_country_yearly2']
            strg1 = 'Average Cases of ' + country1
            strg2 = 'Average Deaths of ' + country1
            strg3 = 'Average Cases of ' + country2
            strg4 = 'Average Deaths of ' + country2
            lstm = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
            lstmain = [['Months', strg1, strg2, strg3, strg4]]
            lst1 = df[df['countriesAndTerritories'] == country1].groupby('month').agg({'cases': 'mean'})[
                'cases'].reindex(index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst21 = df[df['countriesAndTerritories'] == country1].groupby('month').agg({'deaths': 'mean'})[
                'deaths'].reindex(index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst2 = df[df['countriesAndTerritories'] == country2].groupby('month').agg({'cases': 'mean'})[
                'cases'].reindex(index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst22 = df[df['countriesAndTerritories'] == country2].groupby('month').agg({'deaths': 'mean'})[
                'deaths'].reindex(index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst21[i], lst2[i], lst22[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'four'):
            country1 = request.form['two_country_monthly1']
            country2 = request.form['two_country_monthly2']
            month = request.form['two_country_month']
            strg1 = 'Cases of ' + country1
            strg2 = 'Deaths of ' + country1
            strg3 = 'Cases of ' + country2
            strg4 = 'Deaths of ' + country2
            lstm = list(range(1, 32))
            lstmain = [[month, strg1, strg2, strg3, strg4]]
            lst1 = df[(df['countriesAndTerritories'] == country1) & (df['month'] == month)]['cases'].tolist()
            lst21 = df[(df['countriesAndTerritories'] == country1) & (df['month'] == month)]['deaths'].tolist()
            lst2 = df[(df['countriesAndTerritories'] == country2) & (df['month'] == month)]['cases'].tolist()
            lst22 = df[(df['countriesAndTerritories'] == country2) & (df['month'] == month)]['deaths'].tolist()
            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst21[i], lst2[i], lst22[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'five'):
            continent = request.form['sing_continent_yearly']
            lstm = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
            lstmain = [['Months', 'Average Cases', 'Average Deaths']]
            lst = df[df['continentExp'] == continent].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst2 = df[df['continentExp'] == continent].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            for i in range(len(lst)):
                lstmain.append([lstm[i], lst[i], lst2[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'six'):
            continent = request.form['sing_continent_monthly']
            month = request.form['sing_continent_month']
            lstm = list(range(1, 32))
            lstmain = [[month, 'Average Cases', 'Average Deaths']]
            lst=df[(df['continentExp']==continent) & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst2 = df[(df['continentExp']==continent) & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            for i in range(len(lst)):
                lstmain.append([lstm[i], lst[i], lst2[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'seven'):
            continent1 = request.form['two_continent_yearly1']
            continent2 = request.form['two_continent_yearly2']
            strg1 = 'Average Cases of ' + continent1
            strg2 = 'Average Deaths of ' + continent1
            strg3 = 'Average Cases of ' + continent2
            strg4 = 'Average Deaths of ' + continent2
            lstm = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
            lstmain = [['Months', strg1, strg2, strg3, strg4]]
            lst1 = df[df['continentExp'] == continent1].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst21 = df[df['continentExp'] == continent1].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst2 = df[df['continentExp'] == continent2].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst22 = df[df['continentExp'] == continent2].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst21[i], lst2[i], lst22[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'eight'):
            continent1 = request.form['two_continent_monthly1']
            continent2 = request.form['two_continent_monthly2']
            month = request.form['two_continent_month']
            strg1 = 'Average Cases of ' + continent1
            strg2 = 'Average Deaths of ' + continent1
            strg3 = 'Average Cases of ' + continent2
            strg4 = 'Average Deaths of ' + continent2
            lstm = list(range(1, 32))
            lstmain = [[month, strg1, strg2, strg3, strg4]]
            lst1 = df[(df['continentExp']==continent1) & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst21 = df[(df['continentExp']==continent1) & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            lst2 = df[(df['continentExp']==continent2) & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst22 = df[(df['continentExp']==continent2) & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst21[i], lst2[i], lst22[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif  (choice == 'nine'):
            lstm = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
            strg1 = 'Average Cases of Asia'
            strg2 = 'Average Cases of Europe'
            strg3 = 'Average Cases of Africa'
            strg4 = 'Average Cases of America'
            strg5 = 'Average Cases of Oceania'
            strg6 = 'Average Cases of Other'
            lstmain = [['Months', strg1, strg2, strg3, strg4, strg5, strg6]]
            lst1 = df[df['continentExp'] == 'Asia'].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst2 = df[df['continentExp'] == 'Europe'].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst3 = df[df['continentExp'] == 'Africa'].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst4 = df[df['continentExp'] == 'America'].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst5 = df[df['continentExp'] == 'Oceania'].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst6 = df[df['continentExp'] == 'Other'].groupby('month').agg({'cases': 'mean'})['cases'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst2[i], lst3[i], lst4[i], lst5[i], lst6[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif  (choice == 'ten'):
            lstm = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']
            strg1 = 'Average Deaths of Asia'
            strg2 = 'Average Deaths of Europe'
            strg3 = 'Average Deaths of Africa'
            strg4 = 'Average Deaths of America'
            strg5 = 'Average Deaths of Oceania'
            strg6 = 'Average Deaths of Other'
            lstmain = [['Months', strg1, strg2, strg3, strg4, strg5, strg6]]
            lst1 = df[df['continentExp'] == 'Asia'].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst2 = df[df['continentExp'] == 'Europe'].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst3 = df[df['continentExp'] == 'Africa'].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst4 = df[df['continentExp'] == 'America'].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst5 = df[df['continentExp'] == 'Oceania'].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            lst6 = df[df['continentExp'] == 'Other'].groupby('month').agg({'deaths': 'mean'})['deaths'].reindex(
                index=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']).tolist()
            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst2[i], lst3[i], lst4[i], lst5[i], lst6[i]])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'eleven'):
            month = request.form['all_continent_monthc']
            strg1 = 'Cases of Asia'
            strg2 = 'Cases of Europe'
            strg3 = 'Cases of Africa'
            strg4 = 'Cases of America'
            strg5 = 'Cases of Oceania'
            strg6 = 'Cases of Other'
            lstm = list(range(1, 32))
            lstmain = [[month, strg1, strg2, strg3, strg4, strg5, strg6]]
            lst1 = df[(df['continentExp']=='Asia') & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst2 = df[(df['continentExp']=='Europe') & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst3 = df[(df['continentExp']=='Africa') & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst4 = df[(df['continentExp']=='America') & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()
            lst5 = df[(df['continentExp']=='Oceania') & (df['month']==month)].groupby('day').agg({'cases':'mean'})['cases'].tolist()


            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst2[i], lst3[i], lst4[i], lst5[i],0])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)


        elif (choice == 'twelve'):
            month = request.form['all_continent_monthd']
            strg1 = 'Deaths of Asia'
            strg2 = 'Deaths of Europe'
            strg3 = 'Deaths of Africa'
            strg4 = 'Deaths of America'
            strg5 = 'Deaths of Oceania'
            strg6 = 'Deaths of Other'
            lstm = list(range(1, 32))
            lstmain = [[month, strg1, strg2, strg3, strg4, strg5,strg6]]
            lst1 = df[(df['continentExp']=='Asia') & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            lst2 = df[(df['continentExp']=='Europe') & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            lst3 = df[(df['continentExp']=='Africa') & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            lst4 = df[(df['continentExp']=='America') & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()
            lst5 = df[(df['continentExp']=='Oceania') & (df['month']==month)].groupby('day').agg({'deaths':'mean'})['deaths'].tolist()

            for i in range(len(lst1)):
                lstmain.append([lstm[i], lst1[i], lst2[i], lst3[i], lst4[i], lst5[i],0])
            flager = True
            return render_template('Corona_chart.html',lstmain=lstmain)

    if (flager==True):
        choice=''

        return render_template("Corona.html", choice=choice)

    return render_template("Corona.html",lstmain=lstmain,choice=choice)

if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0')
