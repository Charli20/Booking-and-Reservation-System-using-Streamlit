import streamlit as st
import pymysql
from datetime import datetime, timedelta
import pandas as pd





# Connect to the MySQL database
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='chalidu123',
    database='sunset_adventures'
)

# Define packages

water_sports_packages = {
    "Jet-SKI Riding Waligama": 2000,
    "Jet-SKI Riding Bentota": 3000,
    "Jet-SKI Riding Unawatuna": 3000,
    "Boat Riding Bentota": 1000,
    "Boat Riding Hikkaduwa": 600,
    "Boat Riding Waligama": 700,
    "Boat Riding Tangalle": 600,
    "Surfing Arugamba": 2000,
    "Surfing Tangalle": 2000,
    "Coral watching Mirissa": 2000,
    "Coral watching Hikkaduwa": 2000,
    "Scuba Diving Bentota": 3000,
    "Scuba Diving Hikkaduwa": 2500,
    "Scuba Diving Ahungalla": 2500,
    "Scuba Diving Unawatuna": 2000,
    " Snorkeling Unawatuna": 2000,
    " Snorkeling Hikkaduwa":1500,
    " Snorkeling Koggala": 1500,
    " Snorkerling Ahungalla": 2000,
    "Deap Sea Fishing Mirissa": 8500,
    "Deap Sea Fishing Tangalle": 9500,
    "Deap Sea Fishing Bentota": 9000,
    "Dolphin & Whale watching Mirissa": 6000,
    "Seaplane Ride": 9000,
    "Turtle Hatchery Koggala": 1500,
    "Turtle Hatchery Induruwa": 2000,
    "Turtle Hatchery Koggala": 1500
}


city_tour_packages = {
    "Galle City Tour ": 6500,
    "Mathara City Tour": 7000,
    "Katharagama wonders Tour": 7500
}


beach_tour_packages = {
   "Unawatuna Beach Escape": 26000,
   "Tangalle Serenity Retreat":  23000,
   "Weligama Retreat": 28000,
   "Ahungalla Retreat": 34000,
   "Mirissa Relaxation": 28000,
   "Hikkaduwa Getaway": 25000,
   "Dikwella Bliss": 22000,
   "Galle Wellness Getaway": 32000

}


sunset_beach_packages = {
    "Bed & Breakfast" : 18000,
    "Half Board" : 22500,
    "Full Board" : 28000
}

sunset_lagoon_packages = {
    "Bed & Breakfast" : 23000,
    "Half Board" : 28000,
    "Full Board" : 33500
}

sunset_blue_packages = {
    "Bed & Breakfast" : 25000,
    "Half Board" : 30000,
    "Full Board" : 34500
}

sunset_resort_packages = {
    "Bed & Breakfast" : 28000,
    "Half Board" : 32000,
    "Full Board" : 38000
}

sunset_ocean_packages = {
    "Bed & Breakfast" : 30000,
    "Half Board" : 35000,
    "Full Board" : 40000
}


wild_safari_packages = {
    "Yala Adventure Safari (Half day)": 8000,
    "Udawalawe Adventure Safari (Half day)": 8000,
    "Yala Adventure Safari (2 days)": 15000,
    "Udawalawe Adventure Safari (2 days)": 15000,
    "Udawalawe Wildlife Exploration (3 days)": 28000,
    "Yala and Udawalawe Combo Safari (3 days)": 25000,
    "Wildlife Extravaganza Tour (5 days)": 36000,
    "Sri Lankan Safari Explorer (6 days)": 40000,

    "Ridiyagama Safari Park": 4000,
    "Hambantota Birds Park": 3500
}

my_cursor = connection.cursor()

def booking():
    page_bg_img = """
            <style>
                [data-testid="stAppViewContainer"] {
                    background-image: url("");
                    background-size: cover;
                }
                [data-testid="stHeader"] {
                    background-color: rgba(0, 0, 0, 0);
                }
                [data-testid="stSidebar"] {
                    background-color: rgba(0, 0, 0, 0);
                }
            </style>
        """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    option1 = st.sidebar.radio("Select a Service", ("City Tours","Beach Tours", "Water Sports", "Wild Safari", "Accommodation","Booking"))

    if option1 == "Booking":

        page_bg_img = """
                        <style>
                            [data-testid="stAppViewContainer"] {
                                background-image: url("https://wallpapers.com/images/hd/faded-background-dukmpz8g0k0772ho.jpg");
                                background-size: cover;
                            }
                            [data-testid="stHeader"] {
                                background-color: rgba(0, 0, 0, 0);
                            }
                            [data-testid="stSidebar"] {
                                background-color: rgba(0, 0, 0, 0);
                            }
                        </style>
                    """
        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.title("SUN-SET Adventures Booking Page")
        st.title("Fill the form")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        customer_national_id = st.text_input("National ID")
        phone_number = st.text_input("Phone Number")

        if st.button("Done"):
            try:

                sql = """
                                INSERT INTO customer (first_name, last_name, customer_id, email, phone_number)
                                VALUES (%s, %s, %s, %s, %s)
                            """

                with connection.cursor() as cursor:
                    cursor.execute(sql, (first_name, last_name, customer_national_id, email, phone_number))
                    connection.commit()

                st.success("Reservation Success")
            except Exception as e:
                st.error(f"Error: {str(e)}")

        st.header("Select Packages")
        # Display checkboxes for all services
        st.sidebar.header("Select Packages")
        select = st.selectbox("Select a Service", (
            "City Tours", "Beach Tours", "Water Sports", "Wild Safari", "Accommodation"))

        if select == "Water Sports":
            st.write("per person")
            # Display checkboxes for water sports packages
            selected_water_sports_packages = []
            for package, price in water_sports_packages.items():
                checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_water_sports_packages.append(package)

            selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
            selected_time = st.time_input("Select Time", key="time_picker1")

            # Combine date and time into a one
            selected_datetime = datetime.combine(selected_date, selected_time)

            # Get the payment method
            payment_method = st.radio("Select the payment method", ("Cash", "Card"))

            # Get the number of people
            no_of_people = st.number_input("Number of People", min_value=1, value=1)
            # Discounts
            if no_of_people >= 10:
                n = 25
            elif no_of_people >= 8:
                n = 20
            elif no_of_people >= 6:
                n = 15
            elif no_of_people >= 4:
                n = 10
            elif no_of_people >= 2:
                n = 5
            else:
                n = 0
            # Calculate total price
            net_price = sum(
                [water_sports_packages[package] for package in selected_water_sports_packages])

            discount = sum(
                [water_sports_packages[package] for package in selected_water_sports_packages]) * (n / 100)

            total_price = (net_price * (no_of_people)) - (discount)

            special_requirement = st.text_area("Special requirement")

            st.subheader("Selected Packages:")
            for package in selected_water_sports_packages:
                st.write(f"- {package}")

            st.subheader("Selected Date and Time:")
            st.write(selected_datetime)

            st.subheader("Number of People:")
            st.write(no_of_people)

            st.subheader("Total Price:")
            st.write(f"LKR {total_price}")

            if st.button("Submit"):
                try:

                    sql = """
                                INSERT INTO water_sports (  customer_id, location, no_of_people, price, date_time, payment_method, special_requirement)
                                VALUES (%s, %s, %s, %s, %s, %s, %s )
                            """

                    with connection.cursor() as cursor:
                        for package in selected_water_sports_packages:
                            cursor.execute(sql, (
                            customer_national_id, package, no_of_people, total_price, selected_datetime, payment_method,
                            special_requirement))
                        connection.commit()

                    st.success("Reservation Successfull")
                except Exception as e:
                    st.error(f"Error: {str(e)}")



        elif select == "City Tours":
            st.write("per person")
            # Display checkboxes for city tour packages
            selected_city_tour_packages = []
            for package, price in city_tour_packages.items():
                checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_city_tour_packages.append(package)
            selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
            selected_time = st.time_input("Select Time", key="time_picker1")

            selected_datetime = datetime.combine(selected_date, selected_time)

            # Get the payment method
            payment_method = st.radio("Select the payment method", ("Cash", "Card"))

            no_of_people = st.number_input("Number of People", min_value=1, value=1)
            if no_of_people >= 20:
                n = 25
            elif no_of_people >= 15:
                n = 20
            elif no_of_people >= 10:
                n = 15
            elif no_of_people >= 6:
                n = 10
            elif no_of_people >= 4:
                n = 5
            else:
                n = 0

            net_price = sum(
                [city_tour_packages[package] for package in selected_city_tour_packages])

            discount = sum(
                [city_tour_packages[package] for package in selected_city_tour_packages]) * (n / 100)

            total_price = (net_price * (no_of_people)) - (discount)

            special_requirement = st.text_area("Special requirement")

            st.subheader("Selected Packages:")
            for package in selected_city_tour_packages:
                st.write(f"- {package}")

            st.subheader("Selected Date and Time:")
            st.write(selected_datetime)

            st.subheader("Number of People:")
            st.write(no_of_people)

            st.subheader("Total Price:")
            st.write(f"LKR {total_price}")

            if st.button("Submit"):
                try:

                    sql = """
                                INSERT INTO city_tours ( customer_id, location, no_of_people, price, date_time, payment_method, special_requirement)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """

                    with connection.cursor() as cursor:
                        for package in selected_city_tour_packages:
                            cursor.execute(sql, (
                            customer_national_id, package, no_of_people, total_price, selected_datetime, payment_method,
                            special_requirement))
                        connection.commit()

                    st.success("Reservation Successfull")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        elif select == "Beach Tours":
            st.write("per person")
            # Display checkboxes for Beach tour packages
            selected_beach_tour_packages = []
            for package, price in beach_tour_packages.items():
                checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_beach_tour_packages.append(package)
            selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
            selected_time = st.time_input("Select Time", key="time_picker1")

            selected_datetime = datetime.combine(selected_date, selected_time)

            # Get the payment method
            payment_method = st.radio("Select the payment method", ("Cash", "Card"))

            no_of_people = st.number_input("Number of People", min_value=1, value=1)

            # Discount
            if no_of_people >= 9:
                n = 15
            elif no_of_people >= 6:
                n = 10
            elif no_of_people >= 3:
                n = 5
            else:
                n = 0
            net_price = sum([beach_tour_packages[package] for package in selected_beach_tour_packages]) * no_of_people

            discount = net_price * (n / 100)

            total_price = (net_price) - (discount)

            special_requirement = st.text_area("Special requirement")

            st.subheader("Selected Packages:")
            for package in selected_beach_tour_packages:
                st.write(f"- {package}")

            st.subheader("Selected Date and Time:")
            st.write(selected_datetime)

            st.subheader("Number of People:")
            st.write(no_of_people)

            st.subheader("Total Price:")
            st.write(f"LKR {total_price}")

            if st.button("Submit"):
                try:

                    sql = """
                                INSERT INTO beach_tours ( customer_id , location, no_of_people, price, date_time , payment_method, special_requirement)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """

                    with connection.cursor() as cursor:
                        for package in selected_beach_tour_packages:
                            cursor.execute(sql, (
                            customer_national_id, package, no_of_people, total_price, selected_datetime, payment_method,
                            special_requirement))
                        connection.commit()

                    st.success("Reservation Successfull")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        elif select == "Wild Safari":
            st.write("per person ")
            # Display checkboxes for wild safari packages
            selected_wild_safari_packages = []
            for package, price in wild_safari_packages.items():
                checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_wild_safari_packages.append(package)
            selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
            selected_time = st.time_input("Select Time", key="time_picker1")

            selected_datetime = datetime.combine(selected_date, selected_time)

            # Get the payment method
            payment_method = st.radio("Select the payment method", ("Cash", "Card"))

            no_of_people = st.number_input("Number of People", min_value=1, value=1)
            # Discount
            if no_of_people >= 10:
                n = 25
            elif no_of_people >= 8:
                n = 20
            elif no_of_people >= 6:
                n = 15
            elif no_of_people >= 4:
                n = 10
            elif no_of_people >= 2:
                n = 5
            else:
                n = 0
            # Calculate total price
            net_price = sum(
                [wild_safari_packages[package] for package in selected_wild_safari_packages])

            discount = sum(
                [wild_safari_packages[package] for package in selected_wild_safari_packages]) * (n / 100)

            total_price = (net_price * (no_of_people)) - (discount)

            special_requirement = st.text_area("Special requirement")

            st.subheader("Selected Packages:")
            for package in selected_wild_safari_packages:
                st.write(f"- {package}")

            st.subheader("Selected Date and Time:")
            st.write(selected_datetime)

            st.subheader("Number of People:")
            st.write(no_of_people)

            st.subheader("Total Price:")
            st.write(f"LKR {total_price}")

            if st.button("Submit"):
                try:

                    sql = """
                                INSERT INTO wild_safari ( customer_id, location, no_of_people, price, date_time, payment_method, special_requirement)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """

                    with connection.cursor() as cursor:
                        for package in selected_wild_safari_packages:
                            cursor.execute(sql, (
                            customer_national_id, package, no_of_people, total_price, selected_datetime, payment_method,
                            special_requirement))
                        connection.commit()

                    st.success("Reservation Successfull")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        elif select == "Accommodation":

            selected_date = st.date_input("Select Checkin Date", min_value=datetime.now(), key="date_picker")
            selected_time = st.time_input("Select Checkin Time", key="time_picker1")

            selected_datetime = datetime.combine(selected_date, selected_time)

            selected_date1 = st.date_input("Select Checkout Date", min_value=datetime.now(), key="date_picker2")
            selected_time1 = st.time_input("Select Checkout Time", key="time_picker3")

            selected_datetime1 = datetime.combine(selected_date1, selected_time1)

            # Calculating the days
            no_days = (selected_datetime1 - selected_datetime).days

            # Get the payment method
            payment_method = st.radio("Select the payment method", ("Cash", "Card"))

            # Get the number of people
            num_people = st.number_input("Number of People", min_value=1, value=1)
            if num_people >= 10:
                num = 15
            elif num_people >= 8:
                num = 10
            elif num_people >= 6:
                num = 7
            elif num_people >= 4:
                num = 5
            else:
                num = 0
            option = st.selectbox("Select a Service", (
            "Sun-Set Beach Mirissa", "Sun-Set Lagoon Tangalle", "Sun-Set Blue Weligama", "Sun-Set Resort Unawatuna",
            "Sun-Set Ocean Ahungalla"))

            if option == "Sun-Set Beach Mirissa":

                selected_sunset_beach_packages = []
                for package, price in sunset_beach_packages.items():
                    checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_sunset_beach_packages.append(package)

                # Calculate total price
                net_price = sum(
                    [sunset_beach_packages[package] for package in selected_sunset_beach_packages]) * (
                                        num_people + no_days)

                discount = sum(
                    [sunset_beach_packages[package] for package in selected_sunset_beach_packages]) * (num / 100)

                total_price = (net_price - discount)

                special_requirement = st.text_area("Special requirement")

                st.subheader("Selected Packages:")
                for package in selected_sunset_beach_packages:
                    st.write(f"- {package}")

                st.subheader("Selected Date and Time:")
                st.write(selected_datetime)

                st.subheader("Number of People:")
                st.write(num_people)

                st.subheader("Total Price:")
                st.write(f"LKR {total_price}")

                if st.button("Success"):
                    try:

                        sql = """
                                            INSERT INTO accommodation (customer_id ,hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method, special_requirement)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """

                        with connection.cursor() as cursor:
                            for package in selected_sunset_beach_packages:
                                cursor.execute(sql, (
                                    customer_national_id, package, option, num_people, total_price, selected_datetime,
                                    selected_datetime1, payment_method, special_requirement))
                                connection.commit()

                        st.success("Reservation Successfull")

                    except Exception as e:
                        st.error(f"Error: {str(e)}")

            elif option == "Sun-Set Lagoon Tangalle":

                selected_sunset_lagoon_packages = []
                for package, price in sunset_lagoon_packages.items():
                    checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_sunset_lagoon_packages.append(package)
                # Calculate total price
                net_price = sum(
                    [sunset_lagoon_packages[package] for package in selected_sunset_lagoon_packages]) * (
                                        num_people + no_days)

                discount = sum(
                    [sunset_lagoon_packages[package] for package in selected_sunset_lagoon_packages]) * (num / 100)

                Total_price = (net_price - discount)

                special_requirement = st.text_area("Special requirement")

                st.subheader("Selected Packages:")
                for package in selected_sunset_lagoon_packages:
                    st.write(f"- {package}")

                st.subheader("Selected Date and Time:")
                st.write(selected_datetime)

                st.subheader("Number of People:")
                st.write(num_people)

                st.subheader("Total Price:")
                st.write(f"LKR {Total_price}")

                if st.button("Success"):
                    try:

                        sql = """
                                               INSERT INTO accommodation (customer_id,hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_mehtod, special_requirement)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                          """

                        with connection.cursor() as cursor:
                            for package in selected_sunset_lagoon_packages:
                                cursor.execute(sql, (
                                    customer_national_id, package, option, num_people, Total_price, selected_datetime,
                                    selected_datetime1, payment_method, special_requirement))
                                connection.commit()

                        st.success("Reservation Successfull")

                    except Exception as e:
                        st.error(f"Error: {str(e)}")

            elif option == "Sun-Set Blue Weligama":

                selected_sunset_blue_packages = []
                for package, price in sunset_blue_packages.items():
                    checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_sunset_blue_packages.append(package)

                net_price = sum(
                    [sunset_blue_packages[package] for package in selected_sunset_blue_packages]) * (
                                        num_people + no_days)

                discount = sum(
                    [sunset_blue_packages[package] for package in selected_sunset_blue_packages]) * (num / 100)

                Total_price = (net_price - discount)

                special_requirement = st.text_area("Special requirement")

                st.subheader("Selected Packages:")
                for package in selected_sunset_blue_packages:
                    st.write(f"- {package}")

                st.subheader("Selected Date and Time:")
                st.write(selected_datetime)

                st.subheader("Number of People:")
                st.write(num_people)

                st.subheader("Total Price:")
                st.write(f"LKR {Total_price}")

                if st.button("Success"):
                    try:

                        sql = """
                                               INSERT INTO accommodation (customer_id, hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method special_requirement)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                          """

                        with connection.cursor() as cursor:
                            for package in selected_sunset_blue_packages:
                                cursor.execute(sql, (
                                    customer_national_id, package, option, num_people, Total_price, selected_datetime,
                                    selected_datetime1, payment_method, special_requirement))
                                connection.commit()

                        st.success("Reservation Successfull")

                    except Exception as e:
                        st.error(f"Error: {str(e)}")

            elif option == "Sun-Set Resort Unawatuna":

                selected_sunset_resort_packages = []
                for package, price in sunset_resort_packages.items():
                    checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_sunset_resort_packages.append(package)
                # Calculate total price
                net_price = sum(
                    [sunset_resort_packages[package] for package in selected_sunset_resort_packages]) * (
                                        num_people + no_days)

                discount = sum(
                    [sunset_resort_packages[package] for package in selected_sunset_resort_packages]) * (num / 100)

                Total_price = (net_price - discount)

                special_requirement = st.text_area("Special requirement")

                st.subheader("Selected Packages:")
                for package in selected_sunset_resort_packages:
                    st.write(f"- {package}")

                st.subheader("Selected Date and Time:")
                st.write(selected_datetime)

                st.subheader("Number of People:")
                st.write(num_people)

                st.subheader("Total Price:")
                st.write(f"LKR {Total_price}")

                if st.button("Success"):
                    try:

                        sql = """
                                               INSERT INTO accommodation (customer_id, hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method, special_requirement)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                          """

                        with connection.cursor() as cursor:
                            for package in selected_sunset_resort_packages:
                                cursor.execute(sql, (
                                    customer_national_id, package, option, num_people, Total_price, selected_datetime,
                                    selected_datetime1, payment_method, special_requirement))
                                connection.commit()

                        st.success("Reservation Successfull")

                    except Exception as e:
                        st.error(f"Error: {str(e)}")



            elif option == "Sun-Set Ocean Ahungalla":

                selected_sunset_ocean_packages = []
                for package, price in sunset_ocean_packages.items():
                    checkbox_state = st.checkbox(package, key=package)
                if checkbox_state:
                    selected_sunset_ocean_packages.append(package)

                net_price = sum(
                    [sunset_ocean_packages[package] for package in selected_sunset_ocean_packages]) * (
                                        num_people + no_days)

                discount = sum([sunset_ocean_packages[package] for package in selected_sunset_ocean_packages]) * (
                            num / 100)

                Total_price = (net_price - discount)

                special_requirement = st.text_area("Special requirement")

                st.subheader("Selected Packages:")
                for package in selected_sunset_ocean_packages:
                    st.write(f"- {package}")

                st.subheader("Selected Date and Time:")
                st.write(selected_datetime)

                st.subheader("Number of People:")
                st.write(num_people)

                st.subheader("Total Price:")
                st.write(f"LKR {Total_price}")

                if st.button("Success"):
                    try:

                        sql = """
                                                  INSERT INTO accommodation (customer_id ,hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method, special_requirement)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                             """

                        with connection.cursor() as cursor:
                            for package in selected_sunset_ocean_packages:
                                cursor.execute(sql, (
                                    customer_national_id, package, option, num_people, Total_price, selected_datetime,
                                    selected_datetime1, payment_method, special_requirement))
                                connection.commit()

                        st.success("Reservation Successfull")

                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    elif option1 == "City Tours":
         page_bg_img = """
                <style>
                    [data-testid="stAppViewContainer"] {
                        background-image: url("https://images.musement.com/cover/0084/26/thumb_8325013_cover_header.jpeg");
                        background-size: cover;
                    }
                    [data-testid="stHeader"] {
                        background-color: rgba(0, 0, 0, 0);
                    }
                    [data-testid="stSidebar"] {
                        background-color: rgba(0, 0, 0, 0);
                    }
                </style>
            """
         st.markdown(page_bg_img, unsafe_allow_html=True)
         st.header("Discover enchanting cities with Sunset Adventures. Tailored city tours, expert guides, and unforgettable sunsets. Your passport to unique, personalized experiences. Explore with us today!")


        # Define the  packages details
         galle_tour_info = """
         # City Tour Packages:
          ## 1.Galle City Tour

         **Duration:** Full day

         **Highlights:**
         Explore Galle's UNESCO World Heritage Site, including the Galle Fort, Dutch Reformed Church, and charming cobblestone streets. This guided tour offers historical insights into Katharagama, covering the entire Galle Fort area. Experience breathtaking views, delve into colonial history, hear interesting backstories, and gain detailed insights into the modern Sri Lankan culture intertwined with the colonial era. The tour concludes with the opportunity to enjoy the sundown (during the evening tour) on the horizon before leaving the fort premises.

         Discover one of Sri Lanka’s most diverse cities, Galle, on this half-day private guided tour. The itinerary includes stops at Galle Fort, Mahamodara turtle farm, Kaluwella gem museum, a silk factory, a spice garden, the Peace Pagoda in Rumassala, Yatagala Buddhist temple, and relaxation time on the beach.

         Galle, a major city in Sri Lanka, situated on the southwestern tip, was known as Gimhathiththa before the arrival of the Portuguese in the 16th century. Galle reached its peak during the 18th century, the Dutch colonial period. It stands as the best-preserved fortified city built by the Portuguese in South and Southeast Asia. The Galle Fort, a UNESCO world heritage site, is the largest remaining fortress in Asia built by European occupiers.

         **Price:**
         - Age under 8 years old no charges 
         - Per person: LKR 6500
         - Lowest price guarantee. Reserve now & pay later. Free cancellation.

         **What to expect:**
         **Itinerary:**

         - **Galle Fort:** Explore the main tourist attraction heritage site, dating back more than 400 years.
           - *Duration: 1 hour*

         - **Mahamodara:** Visit a turtle farm and hatchery center to see turtles, baby turtles, and the hatching of turtle eggs.
           - *Duration: 30 minutes*

         - **Kaluwella:** Tour a gem museum, witnessing the carving of precious stones into beautiful gems.
           - *Duration: 30 minutes*

         - **Modern's (Looms & Crafts):** Visit a silk factory in Galle, observing the process of making silk clothes.
           - *Duration: 20 minutes*

         - **Unawatuna:** Explore a spice garden and shop for unique spices in Sri Lanka.
           - *Duration: 30 minutes*

         - **Jungle Beach:** Experience the diverse area with a beautiful beach and visit the Peace Pagoda in Rumassala.
           - *Duration: 30 minutes*

         - **Unawatuna Beach:** Relax on the most beautiful beach in Sri Lanka.
           - *Duration: 30 minutes*

         - **Yatagala Raja Maha Viharaya:** Visit an ancient temple with beautiful Buddha statues, enjoying quiet and calm nature.
           - *Duration: 30 minutes*

         - **Galle:** Explore the fish market and fruit market, where you can buy local fruits.
           - *Duration: 20 minutes*

         **Departure details:**
         Traveler pickup is offered from any hotel in Galle, Hikkaduwa, Unawatuna, Mirissa, Koggala area.
         Ports: Galle Port

         **Above rates include:**
         - Air-conditioned private vehicle.
         - Service of an English-speaking chauffeur guide.
         - Entrance ticket to the National Maritime Museum.
         - Lunch in the sunset restaurant.
         - Tea & snacks are available.

         **Above rates exclude:**
         - Cost of meals and beverages.
         - Video and camera permits.
         - Expenses of personal nature.
         - Any other services not specified above.
         """



         matara_tour_info = """
         # City Tour Packages:
         ## 2.Matara City Tour

         **Duration:** Full day


         **Highlights**
         Matara, a key city in Sri Lanka, boasts historic ramparts, Dutch architecture, and a preserved fort. The Matara City Tour includes visits to the star fort and Old Dutch Trade Center. Other attractions encompass Weherahena Buddhist Temple, Matara Paravi Duwa Temple on Pigeon Island, and a Snake Farm at Thelijjawila. Indulge in a luxurious lunch at Sunset Beach Mirissa, followed by a visit to the Sun Set Tea Factory Godagama for a tea-testing experience and snacks. The tour ensures a glimpse into Matara's rich history, blending cultural and natural wonders.
         
         **Matara City Tour:**
         Explore the star fort and Dutch Reformed Church.
         *Duration: 1 hour*

         **Old Dutch Trade Center (Nupe Market):**
         A historic European-built structure located 3.2 km from Matara fort.
         *Duration: 1 hour*

         **Weherahena Buddhist Temple:**
         Visit a unique tunnel temple, the world's first and largest.
         *Duration: 1 hour*

         **Lunch at Sunset Beach Mirissa:**
         Indulge in luxurious cuisine.
         *Duration: 1 hour*

         **Matara Paravi Duwa Temple (Pigeon Island):**
         Explore a Buddhist temple on a small island.
         *Duration: 30 minutes*

         **Snake Farm Thelijjawila:**
         Conservatory and Ayurveda treatment center for snakes.
         *Duration: 30 minutes*

         **Sun Set Tea Factory Godagama:**
         Visit a tea factory for testing and enjoy snacks.
         *Duration: 1-2 hours*

         **Departure details:**
         Free traveler pickup from any hotel in Matara, Mirissa, Polhena, Waligama area.
         
         **Price:**
         - Age under 8 years old no charges 
         - Per person: LKR 7000
         - Lowest price guarantee. Reserve now & pay later. Free cancellation.

         **Above rates include:**
         - Air-conditioned private vehicle.
         - Service of an English-speaking chauffeur guide.
         - Entrance tickets to Nupe Market, Snake Farm, and Tea Factory.
         - Lunch at Sunset Beach Mirissa.
         - Tea and snacks.

         **Above rates exclude:**
         - Video and camera permits.
         - Expenses of personal nature.
         - Any other services not specified above.
         """

         # Display
         st.markdown(galle_tour_info)
         col1, col2 = st.columns([4, 4])
         col1.image(
             "https://cdn.inspiringvacations.com/eyJrZXkiOiIxYzZmZjEzZS02NDYzLTQ0N2ItOWU4OS0wNGM1YTkzMGE2NzIuanBlZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJ3aWR0aCI6ODAwfX19")
         col1.text("Galle fort streets")

         col2.image("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/24/05/e0/galle-fort.jpg?w=1200&h=1200&s=1")
         col2.text("Galle fort")

         col1.image("https://negombotourservice.com/wp-content/uploads/2020/06/galle02.jpg")
         col1.text("Galle fort lighthouse")

         col2.image("https://images.immediate.co.uk/production/volatile/sites/2/2021/05/Hoppers-065-ac0d210.jpg?quality=90&resize=556,505")
         col2.text("Luxurious cuisines")

         st.markdown(matara_tour_info)
         col1, col2 = st.columns([6, 6,])

         col1.image("https://mahaweli.lk/wp-content/uploads/2022/12/Star-Fort-in-Matara.jpg")
         col1.text("Matara Fort")

         col2.image("https://artra.lk/uploads/article/wide/1649124014_wide.jpg")
         col2.text("Star fort")

         col1.image("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/fc/35/0b/parey-dewa.jpg?w=1200&h=1200&s=1")
         col1.text("Paravi duwa temple")

         col2.image("https://static.wixstatic.com/media/017d2f_83c02422edd140cda9d464d83905f0ca~mv2.jpg/v1/fill/w_500,h_300,al_c,q_80/Tea-500x300.jpg")
         col2.text("Tea Testing")


         tour_details = """
         # Explore Katharagama's Spiritual Wonders - Half-Day Guided Tour

         **Duration:** Half day

         **Highlights:**
         Immerse yourself in the sacred town of Kataragama, revered by Buddhists, Hindus, and the indigenous Vedda people. 
         Uncover the area's rich history with breathtaking views and religious worship.

         ## Tour Itinerary:
         """

         kirivehera_info = """
         1. **Kiri Vehera Temple (1 hour):**
            - Discover the ancient Buddhist stupa, Kiri Vehera, dating back over 2000 years to the 3rd century BC.
            - Built by King Mahanaga, it offers a profound glimpse into Sri Lanka's religious heritage.
         """
         katharagamadevalaya_info = """
         2. **Katharagama Devalaya (1 hour):**
            - Embark on a spiritual journey exploring the mysteries of Kataragama Devalaya.
            - History resonates through sacred rituals, providing insights into the profound cultural and spiritual fabric of Sri Lanka.
         """

         lunch_info = """
         3. **Lunch at 5-star hotel (1 hour):**
            - Indulge in a delectable lunch at a luxurious 5-star hotel, savoring culinary delights to rejuvenate your senses.
         """

         wadihitikanda_info = """
         4. **Wadihiti Kanda (1 - 2 hours):**
            - Ascend the mystical heights of Wedihiti Kanda, steeped in folklore.
            - Legend has it that King Dutugemunu vowed to build a shrine where an arrow fell, marking the birthplace of Kataragama Devalaya.
         """

         thissamaharama_info = """
         5. **Thissamaharama Lake (20 minutes):**
            - Enjoy a brief stop at Thissamaharama Lake, soaking in the tranquil surroundings.
         """

         price_info = """
         **Price:**
         - Per person: LKR 7500
         - Kids under 6: Free
         - Lowest price guarantee. Reserve now & pay later. Free cancellation.


         **What to expect:**
         - Air-conditioned private vehicle.
         - Service of an English-speaking chauffeur guide.
         - Entrance tickets to Kiri Vehera Temple, Katharagama Temple, and Wadihiti Kanda.
         - Jeep ride in Wadihiti Kanda.
         - Lunch at a 5-star restaurant.
         - Tea & snacks.

         **Departure details:**
         - Traveler pickup is available from any hotel in Hambantota, Thissamaharama, Yala, and Katharagama.

         **Note:**
         - Video and camera permits not included.
         - Expenses of a personal nature are excluded.
         - Any other services not specified above are not included.
         """

         # Display the tour details
         st.markdown(tour_details)

         col1, col2, col3 = st.columns([6, 2, 6])

         col1.markdown(kirivehera_info)
         col1.image("https://as2.ftcdn.net/v2/jpg/05/86/16/55/1000_F_586165515_PtrjNWtUxNN0yu8TKYBF9Mn9Glzkqrq7.jpg")

         col3.markdown(katharagamadevalaya_info)
         col3.image("https://gestupanalakeview.lk/wp-content/uploads/2023/04/dewalaya-e1682261512553.jpg")

         col1.markdown(lunch_info)
         col1.image("https://menafn.com/updates/pr/2019-06/29/CG_9511e73d-8image_story.jpg")

         col3.markdown(thissamaharama_info)
         col3.image(
             "https://lh3.googleusercontent.com/pw/ACtC-3fFO5nccuTN_vHOIJHDftVCIcFw1DqdYPxSKFXX82_GONX5m6xtEXtJW5u4XLmY__-kf28v-iMfLDcn4irvNFU97CUyeViNaZlBWd_zgr-cTSIA0bOG2Kei0J7wih4Yf3d3kb57i06NRkbQv0oF9xSh=s496-no?authuser=1")

         col1.markdown(wadihitikanda_info)
         col1.image("https://www.discover.lk/assets/Wedihiti-Kanda2__Resampled.jpg")

         st.markdown(price_info)





    elif option1 == "Beach Tours":

         page_bg_img = """
                <style>
                    [data-testid="stAppViewContainer"] {
                        background-image: url("https://www.back-packer.org/wp-content/uploads/sch%C3%B6nste-str%C3%A4nde-in-sri-lanka_mirissa-620x411.jpg");
                        background-size: cover;jpg
                    }
                    [data-testid="stHeader"] {
                        background-color: rgba(0, 0, 0, 0);
                    }
                    [data-testid="stSidebar"] {
                        background-color: rgba(0, 0, 0, 0);
                    }
                </style>
            """
         st.markdown(page_bg_img, unsafe_allow_html=True)
         # Introduction
         st.markdown("# Welcome to Sun Set Adventures - Your Gateway to Unforgettable Beach Tours")
         st.markdown(
             "At Sun Set Adventures, we take pride in curating the best beach tour packages that promise not just a getaway, but an experience of a lifetime. Dive into the beauty of Sri Lanka's southern coast with our meticulously crafted tours, blending sun, sea, and cultural richness.")

         col1,col2 ,col3 = st.columns([7,2,7])

         unawatuna_info = """
         ## 1.Unawatuna Beach Escape:
            Destinations: Unawatuna
            Duration: 2 days/1 night
            Inclusions: Airport transfers to  Unawatuna, beachfront accommodation in Sun Set resort Unawatuna (full board), and traditional Sri Lankan cuisine.
            Price:
           - Adults: LKR 26000
           - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         mirissa_info = """
         ## 2.Mirissa Relaxation:
           Destination: Mirissa
           Duration: 2 days/1 night
           Inclusions: Airport transfers to Mirissa, beachfront accommodation in Sun Set Beach (full board), beachside yoga, and a delightful seafood dinner.
           Price:
           - Adults: LKR 28000
           - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         tangalle_info = """
         ## 3.Tangalle Serenity Retreat:
            Destination: Tangalle
            Duration: 2 days/1 night
            Inclusions: Airport transfers to Tangalle, accommodation in  Sun Set Lagoon (full board), Tangalle beach relaxation, and a rejuvenating spa treatment.
            Price:
            - Adults: LKR 23000
            - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         hikkaduwa_info = """
         ## 4.Hikkaduwa Getaway:
            Destination: Hikkaduwa
            Duration: 2 days/1 night
            Inclusions: Transport from Airport to Hikkaduwa, accommodation in a 5 star hotel (full board), and an unforgettable beach party experience.
            Price:
            - Adults: LKR 25000
            - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         weligama_info = """
         ## 5.Weligama Retreat:
            Destination: Weligama
            Duration: 2 days/1 night
            Inclusions: Transport from Airport to Weligama, accommodation in Sun Set Blue (full board), beachfront yoga, and a delightful seafood barbecue.
            Price:
            - Adults: LKR 28000
            - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         dikwella_info = """
         ## 6.Dikwella Bliss:
            Destination: Dikwella
            Duration: 2 days/1 night
            Inclusions: Transport from Airport to Dikwella, 5 star hotel accommodation (full board), exploration of Dikwella's Blow Hole, and a memorable beachside dining experience.
            Price:
            - Adults: LKR 22000
            - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """
         ahungalla_info = """
         ## 7.Ahungalla Retreat:
            Destination: Ahungalla
            Duration: 2 days/1 night
            Inclusions: Transport from Airport to Ahungalla, luxury beachfront resort in Sun Set Ocean (full board), beachside relaxation, and immersive cultural experiences.
            Price:
            - Adults: LKR 34000
            - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         galle_info = """
         ## 8.Galle Wellness Getaway:
            Destination: Galle
            Duration: 2 days/1 night
            Inclusions: Transport from Airport to Galle, wellness retreat accommodation in a 5 star (full board), yoga, meditation sessions, spa treatments, organic cooking class, and serene beach walks.
            Price:
            - Adults: LKR 32000
            - Kids Under 6 free. Lowest price guarantee. Reserve now & pay later. Free cancellation.
         """

         col1.markdown(unawatuna_info)
         col1.image(
             "https://static.saltinourhair.com/wp-content/uploads/2016/11/23154233/things-to-do-unawatuna-sri-lanka-beach-header.jpg")

         col3.markdown(mirissa_info)
         col3.image("https://i.ytimg.com/vi/JyEXVZiDcIs/maxresdefault.jpg")

         col1.markdown(tangalle_info)
         col1.image("https://i.ytimg.com/vi/OGY3GCj7TgQ/maxresdefault.jpg")

         col3.markdown(hikkaduwa_info)
         col3.image(
             "https://www.lankainoratravel.com/assets/img/main/inora_travel_lanka_Hikkaduwa/inora-travel-lanka-hikkaduwa-beach.jpg")

         col1.markdown(weligama_info)
         col1.image("https://sunnysltravels.com/wp-content/uploads/2022/11/Best-places-to-visit-in-Weligama.jpg")

         col3.markdown(dikwella_info)
         col3.image(
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPMBP7VhlnKdCu_xROfFUDQBPGZ_h61K0dOSrybP-ADpEfkn7wJA2S2jRKQwa-YWsEJMs&usqp=CAU")

         col1.markdown(ahungalla_info)
         col1.image("https://media-cdn.tripadvisor.com/media/photo-s/15/bd/4b/01/enjoy-your-meals-directly.jpg")

         col3.markdown(galle_info)
         col3.image("https://www.holidify.com/images/cmsuploads/compressed/shutterstock_401321713_20191113110713.jpg")



    elif option1 == "Accommodation":
           page_bg_img = """
                <style>
                    [data-testid="stAppViewContainer"] {
                        background-image: url("https://i0.wp.com/magnificentsrilanka.com/wp-content/uploads/2021/07/taj.jpg?fit=1024%2C768&ssl=1");
                        background-size: cover;
                    }
                    [data-testid="stHeader"] {
                        background-color: rgba(0, 0, 0, 0);
                    }
                    [data-testid="stSidebar"] {
                        background-color: rgba(0, 0, 0, 0);
                    }
                </style>
            """
           st.markdown(page_bg_img, unsafe_allow_html=True)


           hotel_details = """
           # Welcome to our collection of Sunset Adventure Hotels

           ## 1.Sunset Beach Mirissa:
           ***Embark on a journey of tranquility at Sunset Beach Mirissa. Nestled along the pristine shores, this beachfront retreat beckons with an idyllic escape. Breathtaking sunset views accompany your stay, embracing you in warm hospitality and modern amenities. Let the soothing rhythm of the waves create the perfect backdrop for a memorable seaside getaway.***


           - **Bed and Breakfast:** LKR 18,000 per person per night
           - **Half Board:** LKR 22,500 per person per night
           - **Full Board:** LKR 28,000 per person per night
           """

           lagoon_info = """
           ## 2.Sunset Lagoon Tangalle:
           ***Discover serenity at Sunset Lagoon Tangalle, a hidden gem set against the backdrop of a picturesque lagoon. With lush surroundings and stunning sunset vistas, this hotel promises a harmonious blend of nature and comfort. Unwind in a peaceful atmosphere, making it an ideal retreat for nature enthusiasts.***

           - **Bed and Breakfast:** LKR 23,000 per person per night
           - **Half Board:** LKR 28,000 per person per night
           - **Full Board:** LKR 33,500 per person per night
           """

           blue_info = """
           ## 3.Sunset Blue Weligama:
           ***Experience coastal bliss at Sunset Blue Weligama, a boutique hotel perched on the shores. Admire vibrant sunset hues over the vast blue ocean from the hotel's vantage points. With modern design, personalized service, and a beachfront location, Sunset Blue Weligama ensures a chic and memorable stay on the southern coast.***

           - **Bed and Breakfast:** LKR 25,000 per person per night
           - **Half Board:** LKR 30,000 per person per night
           - **Full Board:** LKR 34,500 per person per night
           """

           ocean_info = """
           ## 4.Sunset Ocean Ahungalla:
           ***Indulge in luxury at Sunset Ocean Ahungalla, an upscale resort overlooking the Indian Ocean. Relish spectacular sunset views while enjoying world-class amenities. Immerse yourself in the serene surroundings, where the sun's descent over the ocean creates a mesmerizing spectacle.***

           - **Bed and Breakfast:** LKR 30,000 per person per night
           - **Half Board:** LKR 35,000 per person per night
           - **Full Board:** LKR 40,000 per person per night
           """

           unawatuna_info = """
           ## 5.Sunset Resort Unawatuna:
           ***Escape to paradise at Sunset Resort Unawatuna, nestled in the charming coastal town. Lush gardens, a serene ambiance, and proximity to the beach promise a relaxing stay. Revel in enchanting sunset views, creating the perfect backdrop for a memorable coastal holiday.***

           - **Bed and Breakfast:** LKR 28,000 per person per night
           - **Half Board:** LKR 32,000 per person per night
           - **Full Board:** LKR 38,000 per person per night
           """

           # Display the hotel details
           st.markdown(hotel_details)
           st.image("https://indiaoutbound.info/wp-content/uploads/2023/03/Shangrila.jpg")

           st.markdown(lagoon_info)
           st.image(
               "https://images.squarespace-cdn.com/content/v1/5956050736e5d3e59a162d74/1565765647167-THFIUTP7JUIPQBFYWWC0/Yala-93-20180425.jpg?format=2500w")

           st.markdown(blue_info)
           st.image(
               "https://cf.bstatic.com/xdata/images/hotel/max1024x768/100601160.jpg?k=34859d7a6892838a2714273e9d024783e073f9f6336950df914405a09360f2a4&o=&hp=1")

           st.markdown(ocean_info)
           st.image("https://www.islandlife.lk/wp-content/uploads/2018/07/b5a1bb64-best_beach_hotels_in_sri_lanka.jpg")

           st.markdown(unawatuna_info)
           st.image("https://cinnamonweb.blob.core.windows.net/cinnamonweb-prd/2023-07/207x149_Hikka_040723.png")

    elif option1 == "Wild Safari":
        page_bg_img = """
                   <style>
                       [data-testid="stAppViewContainer"] {
                           background-image: url( "https://www.thesrilankatravelblog.com/wp-content/uploads/2022/01/protect-the-environment-on-your-sri-lanka-wildlife-safari-slider-1.jpg");
                           background-size: cover;
                       }
                       [data-testid="stHeader"] {
                           background-color: rgba(0, 0, 0, 0);
                       }
                       [data-testid="stSidebar"] {
                       
                           background-color: rgba(0, 0, 0, 0);
                       }
                   </style>
               """
        st.markdown(page_bg_img, unsafe_allow_html=True)

        yala_info = """
        # Yala National Park:
        **Yala National Park, situated in the southeastern corner of Sri Lanka, is the country's most renowned and second-largest national park. Known for its diverse ecosystems and abundant wildlife, Yala attracts nature enthusiasts, wildlife photographers, and adventurers from around the world. Established in 1938, the park spans approximately 979 square kilometers and is an integral part of the broader Yala Block, connecting to the Ruhuna National Park and Kataragama Wildlife Sanctuary.**
        """
        udawalawe_info = """
        # Udawalawe National Park:
        **Udawalawe National Park, located in the southern part of Sri Lanka, is renowned for its rich biodiversity and is particularly famous for its large population of wild elephants. Established in 1972, the park spans across the Sabaragamuwa and Uva provinces, encompassing an area of approximately 30,821 hectares.**

        """

        package1_info = """
        ### Package available in Yala and Udawalawe national park


        ## 1.Yala Adventure Safari (Half day):

        **Destination:** Yala National Park, Sri Lanka      
        **Duration:** 6 - 8 hour
        **Inclusions:**
        -Half-day jeep safari in Yala National Park.
        -Guided visit to Yala's ancient Sithulpawwa Rock Temple.
        -Guided nature walks.
        -Birdwatching.
        -lunch included.
        **Price:** 8000
        """
        package2_info = """
        # 2.Udawalawe Adventure Safari (Half day):

        **Destination:** Udawalawe National Park, Sri Lanka
        **Duration:** 5 - 6 hour
        **Inclusions:** 
        -Half-day jeep safari in Udawalawe National Park.
        -Guided nature walks.
        -Birdwatching.
        -lunch included.
        **Price:** 8000
        """

        package3_info = """
        ## 3.Yala Adventure Safari (2 days):

        **Destination:** Yala National Park, Sri Lanka
        **Duration:** 2 days/1 night
        **Inclusions:**
        -Full-day jeep safari in Yala National Park.
        -Guided visit to Yala's ancient Sithulpawwa Rock Temple.
        -Accommodation in a safari camp.
        -Guided nature walks.
        -Birdwatching.
        -All meals included.
        **Price:** 15000
        """
        package4_info = """
        ## 4.Udawalawe Adventure Safari (2 days):

        **Destination:** Udawalawe National Park, Sri Lanka
        **Duration:** 2 days/1 night
        **Inclusions:**
        -Full-day jeep safari in Udawalawe National Park.
        -Accommodation in a safari camp.
        -Guided nature walks.
        -Birdwatching.
        -All meals included.
        **Price:** 15000
        """

        package5_info = """
        ## 5.Udawalawe Wildlife Exploration (3 days):

        **Destination:** Udawalawe National Park, Sri Lanka
        **Duration:** 3 days/2 nights
        **Inclusions:**
        -Jeep safari in Udawalawe National Park.
        -Visit to the Elephant Transit Home.
        -Accommodation in a wildlife resort.
        -Nature photography sessions.
        -All meals included.
        **Price:** 28000
        """

        package6_info = """
        ## 6.Yala and Udawalawe Combo Safari (3 days):

        **Destination:** Yala and Udawalawe National Parks, Sri Lanka
        **Duration:** 4 days/3 nights
        **Inclusions:**
        -Full-day jeep safari in Yala National Park.
        -Half-day safari in Udawalawe National Park.
        -Accommodation in safari lodges.
        -Birdwatching excursions.
        -All meals included.
        **Price:** 25000
        """

        package7_info = """
        ## 7.Wildlife Extravaganza Tour (5 days):

        **Destination:** Yala and Udawalawe National Parks, Sri Lanka
        **Duration:** 5 days/4 nights
        **Inclusions:**
        -Jeep safaris in Yala and Udawalawe.
        -Visit to the Udawalawe Elephant Transit Home.
        -Accommodation in luxury tents.
        -Educational sessions on local flora and fauna.
        -All meals included.
        **Price:** 36000
        """

        package8_info = """
        ## 8.Sri Lankan Safari Explorer (6 days):

        **Destination:** Yala and Udawalawe National Parks, Sri Lanka
        **Duration:** 6 days/5 nights
        **Inclusions:**
        -Full-day safaris in both parks.
        -Guided visit to Yala's ancient Sithulpawwa Rock Temple.
        -Stay in eco-friendly accommodations.
        -Evening cultural performances.
        -All meals included.
        **Price:** 40000
        """

        safari_park_info = """
        ## 2.Ridiyagama Safari Park
        
        **Experience Sri Lanka’s first Open Zoo safari park. Divided into six zones, this 500-acre park is home to an interesting wildlife mix. You can tour the park by bus or a safari jeep while watching the animals roam freely. Expect zebras and giraffes amidst unique creatures like Bactrian camels, Indian blue bulls and African cape buffaloes. The main highlights here are the Bengal tigers, African lions and Sri Lankan elephants—so be sure to keep your eyes peeled.**
        **Duration:** 2 - 3 hours

        **Departure details:**
        Free traveler pickup from any hotel in Tangalle, Udawalawa, Ambalantota , Mattala, Hambantota area.

        **Inclusions:**
         -Entrance tickets to Ridigama Safari park
         -Guided Jeep safari in Ridigama Safari park

        **Price:** 4000
        """

        bird_park_info = """
        ## 3.Hambantota Birds Park
        **Asia's largest Birds Park and Research Centre in Hambantota Sri Lanka Birds Park is a home to endemic and exotic birds with over 180 varieties and around 3200 birds. The park which is located in the Southern part of the island expands on a landscape of 35 acres dedicated for bird enthusiast and for those who study ornithology.**
        **Duration:** 2 - 3 hours

        **Departure details:**
        Free traveler pickup from any hotel in Hambantota, Ambalantota, Mattala, Thissamaharama area.

        **Inclusions:**
         -Entrance tickets to Hambantota birds park
         -Guided Jeep safari in Hambantota birds park
        Price: 3500
        """

        st.header(
            "Embark on thrilling safaris with our adventure website, exploring the wild's wonders in just a click!")
        st.markdown(yala_info)
        st.image("https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/f2/0f/25.jpg")
        st.image("https://deyotours.com/wp-content/uploads/2022/10/Yala-rock.jpg")

        st.markdown(udawalawe_info)
        st.image("https://us.lakpura.com/cdn/shop/files/74.jpg?v=1653300776&width=3840")
        st.image(
            "https://blankcanvas-media.s3.eu-west-2.amazonaws.com/wp-content/uploads/2021/02/22203111/Udawalawe-National-Park3-600x600.jpg")

        col1, col2, col3 = st.columns([6, 2, 6])
        col1.markdown(package1_info)
        col3.markdown(package2_info)

        col1.markdown(package3_info)
        col3.markdown(package4_info)

        col1.markdown(package5_info)
        col3.markdown(package6_info)

        col1.markdown(package7_info)
        col3.markdown(package8_info)

        col1.image(
            "https://www.researchgate.net/publication/320857265/figure/fig1/AS:559092286853122@1510309396356/Distribution-of-vegetation-sampling-plots-at-Udawalawe-National-Park-The-sampling-plots.png")
        col1.text("Udawalawe national park map")

        col3.image("https://www.my-wildlife.com/wp-content/uploads/2020/05/yala-map.jpg")
        col3.text("Yala Safari park map")

        st.markdown(safari_park_info)
        st.image(
            "https://lh3.googleusercontent.com/pw/ACtC-3fG9hTBTHpB2TrwZJ0Ijg3KvlNUEvhzOsKzDZaqYGdLyDhZ_vZ-QqV0jG2IYcLU2izVNM2Qbgj0eqbs9e7aN0ktHbrsYVfkERjgCvbW9NJx6ds_n8D_R9-53w36RQyx8IO6OJSMu4u0IHDCaDhyfxon=w498-h450-no?authuser=2")

        st.image(
            "https://lh3.googleusercontent.com/pw/ACtC-3e_8n05Rk_hbBB1bmIGxstSrxy-Wd1z5-sojNwBD6iAKkwf78DD_IVdZtWJW89VsgqP2HENV2dytU6Ol-UdsdigvEYRHHzjeGJ5Mvmn4Dab4x6g5hjYMRYar2vDWvwGAJkJNyNyzJb0TlQ3q4u2qtg8=w492-h260-no?authuser=2")

        st.image("https://www.leszoosdanslemonde.com/zoos/asie/sri_lanka/ridiyagama/maps/ridiyagama_plan_2016ca.JPG")
        st.text("map")

        st.markdown(bird_park_info)
        st.image("https://paradisetravelagencybali.com/wp-content/uploads/2020/10/Bali-Bird-Park-Activity.jpg")

        st.image("https://www.birdspark.lk/wp-content/uploads/2020/01/Toco-Toucan-Ramphastos-Toco-1-scaled.jpg")

        st.image("https://www.birdspark.lk/wp-content/uploads/2016/10/Birds-Park-map-with-instruction-1.jpg")
        st.text("map")

    elif option1 == "Water Sports":
        page_bg_img = """
                   <style>
                       [data-testid="stAppViewContainer"] {
                           background-image: url("https://pyt-blogs.imgix.net/2021/05/aakankshaa-melkot-m5gYCrcwUgQ-unsplash.jpg?auto=format&fit=scale&h=683&ixlib=php-3.3.0&w=1024&wpsize=large");
                           background-size: cover;
                       }
                       [data-testid="stHeader"] {
                           background-color: rgba(0, 0, 0, 0);
                       }
                       [data-testid="stSidebar"] {
                           background-color: rgba(0, 0, 0, 0);
                       }
                   </style>
               """
        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.header("ENJOY YOURSELF WITH WATER SPORTS")
        st.subheader("Discover the thrill of water sports in the idyllic setting of Sri Lanka, with over 1600km of coastline, the Southern coast stands out as a prime destination. At Sunset Adventures, we specialize in providing exceptional water sports experiences. Our skilled and experienced instructors prioritize your safety and enjoyment in all underwater activities. Explore our diverse water sports packages and detailed offerings, and once you've found your perfect adventure, secure your spot by booking now.")


        col1,col2 = st.columns([5,5])
        col1.subheader("1.Jet-SKI Riding")
        col1.image("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/fb/3c/2e/caption.jpg?w=500&h=400&s=1")
        col1.markdown("Duration: 1 hour")
        col1.markdown("Highlights: Experience an adrenaline-pumping Jet-SKI adventure along the scenic  southern coast of Srilanka. Enjoy professional guidance, safety equipment, and high-speed excitement against a stunning coastal backdrop.")
        col1.markdown("Price: LKR 2000 onwards")
        col1.markdown("Locations: Waligama, Bentota, Unawatuna")

        col2.subheader("2.Surfing")
        col2.image("https://media1.thrillophilia.com/filestore/7lszi5jfopaylvywmpuccqm5popt_shutterstock_1289173198.jpg?w=305&h=230&dpr")
        col2.markdown("Duration: Half-day")
        col2.markdown(" Highlights: Surfing lessons for beginners and challenging breaks for experienced surfers in Arugam Bay and Tangalle. Surfboards and instructors provided. Tailored for surf enthusiasts seeking the perfect balance of challenge and thrill.")
        col2.markdown("Price: LKR 2000 ")
        col2.markdown("Location: Arugam Bay, Tangalle")

        col1.subheader("3.Boat Riding")
        col1.image("https://media1.thrillophilia.com/filestore/qq81jatsawe3fxvcpo97cc07bp9c_shutterstock_1730473138.jpg?w=305&h=230&dpr")
        col1.markdown("Duration: 2 hours")
        col1.markdown("Highlights: Leisurely boat ride exploring vibrant marine life and coral reefs of southern coast. Ideal for a relaxed coastal adventure with snacks included. Glide through azure waters and enjoy a scenic shoreline cruise.")
        col1.markdown("Price: LKR 600 onwards")
        col1.markdown("Locations: Waligama, Bentota, Hikkaduwa, Tangalle")

        col2.subheader("4.Dolphine & Whale Watching")
        col2.image("https://wisetravelgenie.com/wp-content/uploads/2020/08/Cost-Of-Whale-Watching-Mirissa-Srilanka1-1024x682.jpg")
        col2.markdown("Duration: 2-4 hours")
        col2.markdown("Highlights: Expert-guided boat tour to witness majestic whales in their natural habitat off the coast of Mirissa. An unforgettable experience for nature enthusiasts, including lunch and tea. Embark on a journey to encounter gentle giants.")
        col2.markdown("Price: LKR 6000")
        col2.markdown("Location: Mirissa")

        col1.subheader("5.Snorkeling Diving")
        col1.image("https://www.sazylankatours.com/wp-content/uploads/2022/08/Diving-and-Snorkeling-Sri-Lanka.jpg")
        col1.markdown("Duration: 1 - 2 hours")
        col1.markdown(" Highlights: Immerse yourself in the crystal-clear waters, discovering a kaleidoscope of marine life and colorful coral reefs through an exhilarating snorkeling experience.")
        col1.markdown("Price: LKR 1500 onwards")
        col1.markdown("Locations: Hikkaduwa, Koggala, Ahungalla, Unawatuna")

        col2.subheader("6.Scuba Diving")
        col2.image("https://www.talesofceylon.com/wp-content/uploads/2020/10/shutterstock_141494944-scaled.jpg")
        col2.markdown("Duration: 2-4 hours")
        col2.markdown("Highlights: Dive into the enchanting world beneath the waves with our Scuba Diving adventure. Explore vibrant coral reefs, encounter exotic marine life, and experience the thrill of underwater exploration guided by certified instructors.")
        col2.markdown("Price: LKR 2500 onwards")
        col2.markdown("Locations: Bentota, Hikkaduwa, Ahungalla, Unawatuna")

        col1.subheader("7.Deep Sea Fishing")
        col1.image("https://www.bestofceylon.com/images/best-experiences/deep-sea-fishing-in-hikkaduwa/hikkaduwa1.jpg")
        col1.markdown("Duration: 1 - 3 hours ")
        col1.markdown("Highlights: Set sail for an exciting deep-sea fishing adventure, aiming for a catch of the day amidst the vast and bountiful waters of the Southern coast.")
        col1.markdown("Price:  LKR 8500 onwards")
        col1.markdown("Locations: Mirissa, Tangalle, Bentota")

        col2.subheader("8.Coral Watching")
        col2.image("https://www.srilankadaytours.com/images/snorkelling-at-hikkaduwa.jpg")
        col2.markdown("Duration: 1 hour")
        col2.markdown("Highlights: Dive into the mesmerizing world of vibrant coral formations, exploring the underwater beauty and biodiversity of Sri Lanka's coastal areas.")
        col2.markdown("Price: LKR 2000")
        col2.markdown("Locations: Hikkaduwa,Mirissa")

        col1.subheader("9.Turtle Hatchery")
        col1.image("https://charliepauly.com/wp-content/uploads/2020/03/Koggala-Turtle-Hatchery-Sri-Lanka-%E2%80%93-A-Complete-Guide-To-Visiting-0.jpg")
        col1.markdown("Duration: 1 hour")
        col1.markdown(" Highlights: Witness the marvel of turtle conservation efforts, where adorable hatchlings are nurtured for a successful release into the ocean.")
        col1.markdown("Price: LKR 1500 onwards")
        col1.markdown("Location: Koggala, Induruwa, Kogalla")



        col2.subheader("10. Seaplane Ride")
        col2.image("https://d30od4ebpi69u8.cloudfront.net/2019/01/echo.jpg")
        col2.markdown("Duration: 1 - 2 hour")
        col2.markdown(" Scenic Domastic plane journey offering breathtaking aerial views of southern coastal landscapes. Perfect for those seeking a unique and luxurious adventure. Revel in panoramic views on this once-in-a-lifetime aerial adventure, including a snack in the air.")
        col2.markdown("Price: LKR 9000")
        col2.markdown("Location: Galle")




def employee_login():
    page_bg_img = """
                  <style>
                      [data-testid="stAppViewContainer"] {
                          background-image: url("https://wallpapers.com/images/hd/faded-background-dukmpz8g0k0772ho.jpg");
                          background-size: cover;
                      }
                      [data-testid="stHeader"] {
                          background-color: rgba(0, 0, 0, 0);
                      }
                      [data-testid="stSidebar"] {
                          background-color: rgba(0, 0, 0, 0);
                      }
                  </style>
              """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Function to check login credentials
    def check_login(username, password):
        return username == "user" and password == "chalidu123"

    # Display login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.button("Login"):
        if check_login(username, password):
            st.success("Login successful")
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password. Please try again.")
            st.session_state.logged_in = False

    # Continue only if logged in
    if st.session_state.logged_in:
        option = st.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

        if option == "Create":
                st.markdown(page_bg_img, unsafe_allow_html=True)
                st.title("SUN-SET Adventures Booking Page")
                st.title("Fill the form")
                first_name = st.text_input("First Name")
                last_name = st.text_input("Last Name")
                email = st.text_input("Email")
                customer_national_id = st.text_input("National ID")
                phone_number = st.text_input("Phone Number")

                if st.button("Done"):
                    try:

                        sql = """
                                        INSERT INTO customer (first_name, last_name, customer_id, email, phone_number)
                                        VALUES (%s, %s, %s, %s, %s)
                                    """

                        with connection.cursor() as cursor:
                            cursor.execute(sql, (first_name, last_name, customer_national_id, email, phone_number))
                            connection.commit()

                        st.success("Added to Database Successfully!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

                st.header("Select Packages")
                # Display checkboxes for all services
                st.sidebar.header("Select Packages")
                select = st.selectbox("Select a Service", (
                    "City Tours", "Beach Tours", "Water Sports", "Wild Safari", "Accommodation"))

                if select == "Water Sports":
                    st.write("per person")
                    # Display checkboxes for water sports packages
                    selected_water_sports_packages = []
                    for package, price in water_sports_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_water_sports_packages.append(package)

                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    # Combine date and time into a one
                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    # Get the number of people
                    no_of_people = st.number_input("Number of People", min_value=1, value=1)
                    # Discounts
                    if no_of_people >= 10:
                        n = 25
                    elif no_of_people >= 8:
                        n = 20
                    elif no_of_people >= 6:
                        n = 15
                    elif no_of_people >= 4:
                        n = 10
                    elif no_of_people >= 2:
                        n = 5
                    else:
                        n = 0
                    # Calculate total price
                    net_price = sum(
                        [water_sports_packages[package] for package in selected_water_sports_packages])

                    discount = sum(
                        [water_sports_packages[package] for package in selected_water_sports_packages]) * (n / 100)

                    total_price = (net_price * (no_of_people)) - (discount)

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_water_sports_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Submit"):
                        try:

                            sql = """
                                        INSERT INTO water_sports (  customer_id, location, no_of_people, price, date_time, payment_method, special_requirement)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s )
                                    """

                            with connection.cursor() as cursor:
                                for package in selected_water_sports_packages:
                                    cursor.execute(sql, (
                                    customer_national_id, package, no_of_people, total_price, selected_datetime,
                                    payment_method, special_requirement))
                                connection.commit()

                            st.success("Added to Database Successfully!")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")



                elif select == "City Tours":
                    st.write("per person")
                    # Display checkboxes for city tour packages
                    selected_city_tour_packages = []
                    for package, price in city_tour_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_city_tour_packages.append(package)
                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    no_of_people = st.number_input("Number of People", min_value=1, value=1)
                    if no_of_people >= 20:
                        n = 25
                    elif no_of_people >= 15:
                        n = 20
                    elif no_of_people >= 10:
                        n = 15
                    elif no_of_people >= 6:
                        n = 10
                    elif no_of_people >= 4:
                        n = 5
                    else:
                        n = 0

                    net_price = sum(
                        [city_tour_packages[package] for package in selected_city_tour_packages])

                    discount = sum(
                        [city_tour_packages[package] for package in selected_city_tour_packages]) * (n / 100)

                    total_price = (net_price * (no_of_people)) - (discount)

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_city_tour_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Submit"):
                        try:

                            sql = """
                                        INSERT INTO city_tours ( customer_id, location, no_of_people, price, date_time, payment_method, special_requirement)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                                    """

                            with connection.cursor() as cursor:
                                for package in selected_city_tour_packages:
                                    cursor.execute(sql, (
                                    customer_national_id, package, no_of_people, total_price, selected_datetime,
                                    payment_method, special_requirement))
                                connection.commit()

                            st.success("Added to Database Successfully!")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

                elif select == "Beach Tours":
                    st.write("per person")
                    # Display checkboxes for Beach tour packages
                    selected_beach_tour_packages = []
                    for package, price in beach_tour_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_beach_tour_packages.append(package)
                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    no_of_people = st.number_input("Number of People", min_value=1, value=1)

                    # Discount
                    if no_of_people >= 9:
                        n = 15
                    elif no_of_people >= 6:
                        n = 10
                    elif no_of_people >= 3:
                        n = 5
                    else:
                        n = 0
                    net_price = sum(
                        [beach_tour_packages[package] for package in selected_beach_tour_packages]) * no_of_people

                    discount = net_price * (n / 100)

                    total_price = (net_price) - (discount)

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_beach_tour_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Submit"):
                        try:

                            sql = """
                                        INSERT INTO beach_tours ( customer_id , location, no_of_people, price, date_time , payment_method, special_requirement)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                                    """

                            with connection.cursor() as cursor:
                                for package in selected_beach_tour_packages:
                                    cursor.execute(sql, (
                                    customer_national_id, package, no_of_people, total_price, selected_datetime,
                                    payment_method, special_requirement))
                                connection.commit()

                            st.success("Added to Database Successfully!")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

                elif select == "Wild Safari":
                    st.write("per person ")
                    # Display checkboxes for wild safari packages
                    selected_wild_safari_packages = []
                    for package, price in wild_safari_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_wild_safari_packages.append(package)
                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    no_of_people = st.number_input("Number of People", min_value=1, value=1)
                    # Discount
                    if no_of_people >= 10:
                        n = 25
                    elif no_of_people >= 8:
                        n = 20
                    elif no_of_people >= 6:
                        n = 15
                    elif no_of_people >= 4:
                        n = 10
                    elif no_of_people >= 2:
                        n = 5
                    else:
                        n = 0
                    # Calculate total price
                    net_price = sum(
                        [wild_safari_packages[package] for package in selected_wild_safari_packages])

                    discount = sum(
                        [wild_safari_packages[package] for package in selected_wild_safari_packages]) * (n / 100)

                    total_price = (net_price * (no_of_people)) - (discount)

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_wild_safari_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Submit"):
                        try:

                            sql = """
                                        INSERT INTO wild_safari ( customer_id, location, no_of_people, price, date_time, payment_method, special_requirement)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                                    """

                            with connection.cursor() as cursor:
                                for package in selected_wild_safari_packages:
                                    cursor.execute(sql, (
                                    customer_national_id, package, no_of_people, total_price, selected_datetime,
                                    payment_method, special_requirement))
                                connection.commit()

                            st.success("Added to Database Successfully!")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

                elif select == "Accommodation":

                    selected_date = st.date_input("Select Checkin Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Checkin Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    selected_date1 = st.date_input("Select Checkout Date", min_value=datetime.now(), key="date_picker2")
                    selected_time1 = st.time_input("Select Checkout Time", key="time_picker3")

                    selected_datetime1 = datetime.combine(selected_date1, selected_time1)

                    # Calculating the days
                    no_days = (selected_datetime1 - selected_datetime).days

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    # Get the number of people
                    num_people = st.number_input("Number of People", min_value=1, value=1)
                    if num_people >= 10:
                        num = 15
                    elif num_people >= 8:
                        num = 10
                    elif num_people >= 6:
                        num = 7
                    elif num_people >= 4:
                        num = 5
                    else:
                        num = 0
                    option = st.selectbox("Select a Service", (
                    "Sun-Set Beach Mirissa", "Sun-Set Lagoon Tangalle", "Sun-Set Blue Weligama",
                    "Sun-Set Resort Unawatuna", "Sun-Set Ocean Ahungalla"))

                    if option == "Sun-Set Beach Mirissa":

                        selected_sunset_beach_packages = []
                        for package, price in sunset_beach_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_sunset_beach_packages.append(package)

                        # Calculate total price
                        net_price = sum(
                            [sunset_beach_packages[package] for package in selected_sunset_beach_packages]) * (
                                                num_people + no_days)

                        discount = sum(
                            [sunset_beach_packages[package] for package in selected_sunset_beach_packages]) * (
                                               num / 100)

                        total_price = (net_price - discount)

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_beach_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {total_price}")

                        if st.button("Success"):
                            try:

                                sql = """
                                                    INSERT INTO accommodation (customer_id ,hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method, special_requirement)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                """

                                with connection.cursor() as cursor:
                                    for package in selected_sunset_beach_packages:
                                        cursor.execute(sql, (
                                            customer_national_id, package, option, num_people, total_price,
                                            selected_datetime,
                                            selected_datetime1, payment_method, special_requirement))
                                        connection.commit()

                                st.success("Added to Database Successfully!")

                            except Exception as e:
                                st.error(f"Error: {str(e)}")

                    elif option == "Sun-Set Lagoon Tangalle":

                        selected_sunset_lagoon_packages = []
                        for package, price in sunset_lagoon_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_sunset_lagoon_packages.append(package)
                        # Calculate total price
                        net_price = sum(
                            [sunset_lagoon_packages[package] for package in selected_sunset_lagoon_packages]) * (
                                                num_people + no_days)

                        discount = sum(
                            [sunset_lagoon_packages[package] for package in selected_sunset_lagoon_packages]) * (
                                               num / 100)

                        Total_price = (net_price - discount)

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_lagoon_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {Total_price}")

                        if st.button("Success"):
                            try:

                                sql = """
                                                       INSERT INTO accommodation (customer_id,hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_mehtod, special_requirement)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                  """

                                with connection.cursor() as cursor:
                                    for package in selected_sunset_lagoon_packages:
                                        cursor.execute(sql, (
                                            customer_national_id, package, option, num_people, Total_price,
                                            selected_datetime,
                                            selected_datetime1, payment_method, special_requirement))
                                        connection.commit()

                                st.success("Added to Database Successfully!")

                            except Exception as e:
                                st.error(f"Error: {str(e)}")

                    elif option == "Sun-Set Blue Weligama":

                        selected_sunset_blue_packages = []
                        for package, price in sunset_blue_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_sunset_blue_packages.append(package)

                        net_price = sum(
                            [sunset_blue_packages[package] for package in selected_sunset_blue_packages]) * (
                                                num_people + no_days)

                        discount = sum(
                            [sunset_blue_packages[package] for package in selected_sunset_blue_packages]) * (num / 100)

                        Total_price = (net_price - discount)

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_blue_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {Total_price}")

                        if st.button("Success"):
                            try:

                                sql = """
                                                       INSERT INTO accommodation (customer_id, hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method special_requirement)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                  """

                                with connection.cursor() as cursor:
                                    for package in selected_sunset_blue_packages:
                                        cursor.execute(sql, (
                                            customer_national_id, package, option, num_people, Total_price,
                                            selected_datetime,
                                            selected_datetime1, payment_method, special_requirement))
                                        connection.commit()

                                st.success("Added to Database Successfully!")

                            except Exception as e:
                                st.error(f"Error: {str(e)}")

                    elif option == "Sun-Set Resort Unawatuna":

                        selected_sunset_resort_packages = []
                        for package, price in sunset_resort_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_sunset_resort_packages.append(package)
                        # Calculate total price
                        net_price = sum(
                            [sunset_resort_packages[package] for package in selected_sunset_resort_packages]) * (
                                                num_people + no_days)

                        discount = sum(
                            [sunset_resort_packages[package] for package in selected_sunset_resort_packages]) * (
                                               num / 100)

                        Total_price = (net_price - discount)

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_resort_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {Total_price}")

                        if st.button("Success"):
                            try:

                                sql = """
                                                       INSERT INTO accommodation (customer_id, hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method, special_requirement)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                  """

                                with connection.cursor() as cursor:
                                    for package in selected_sunset_resort_packages:
                                        cursor.execute(sql, (
                                            customer_national_id, package, option, num_people, Total_price,
                                            selected_datetime,
                                            selected_datetime1, payment_method, special_requirement))
                                        connection.commit()

                                st.success("Added to Database Successfully!")

                            except Exception as e:
                                st.error(f"Error: {str(e)}")



                    elif option == "Sun-Set Ocean Ahungalla":

                        selected_sunset_ocean_packages = []
                        for package, price in sunset_ocean_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_sunset_ocean_packages.append(package)

                        net_price = sum(
                            [sunset_ocean_packages[package] for package in selected_sunset_ocean_packages]) * (
                                                num_people + no_days)

                        discount = sum(
                            [sunset_ocean_packages[package] for package in selected_sunset_ocean_packages]) * (
                                               num / 100)

                        Total_price = (net_price - discount)

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_ocean_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {Total_price}")

                        if st.button("Success"):
                            try:

                                sql = """
                                                          INSERT INTO accommodation (customer_id ,hotel, package, no_of_people, price, checkin_datetime, checkout_datetime, payment_method, special_requirement)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                     """

                                with connection.cursor() as cursor:
                                    for package in selected_sunset_ocean_packages:
                                        cursor.execute(sql, (
                                            customer_national_id, package, option, num_people, Total_price,
                                            selected_datetime,
                                            selected_datetime1, payment_method, special_requirement))
                                        connection.commit()

                                st.success("Added to Database Successfully!")

                            except Exception as e:
                                st.error(f"Error: {str(e)}")

        elif option == "Update":
                st.subheader("Update a Record")
                reservation_id = st.number_input("Reservation ID: ")
                update = st.selectbox("Select the service",
                                      ("Water sports", "City Tours", "Beach Tours", "Wild Safari", "Accommodation"))

                if update == "Water sports":
                    st.write("per person")
                    # Display checkboxes for water sports packages
                    selected_water_sports_packages = []
                    for package, price in water_sports_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_water_sports_packages.append(package)

                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    # Combine date and time into one
                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    # Get the number of people
                    no_of_people = st.number_input("Number of People", min_value=1, value=1)

                    # Discounts
                    if no_of_people >= 10:
                        n = 25
                    elif no_of_people >= 8:
                        n = 20
                    elif no_of_people >= 6:
                        n = 15
                    elif no_of_people >= 4:
                        n = 10
                    elif no_of_people >= 2:
                        n = 5
                    else:
                        n = 0

                    # Calculate total price
                    net_price = sum([water_sports_packages[package] for package in selected_water_sports_packages])
                    discount = net_price * (n / 100)
                    total_price = (net_price * no_of_people) - discount

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_water_sports_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Update"):
                        sql = "update water_sports set location=%s, no_of_people=%s, price=%s, date_time=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                        val = ( package, no_of_people, total_price, selected_datetime, payment_method, special_requirement,reservation_id)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record updated successfully")

                elif update == "City Tours":
                    st.write("per person")
                    # Display checkboxes for city tour packages
                    selected_city_tour_packages = []
                    for package, price in city_tour_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_city_tour_packages.append(package)

                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    no_of_people = st.number_input("Number of People", min_value=1, value=1)

                    # Discount
                    if no_of_people >= 20:
                        n = 25
                    elif no_of_people >= 15:
                        n = 20
                    elif no_of_people >= 10:
                        n = 15
                    elif no_of_people >= 6:
                        n = 10
                    elif no_of_people >= 4:
                        n = 5
                    else:
                        n = 0

                    net_price = sum([city_tour_packages[package] for package in selected_city_tour_packages])

                    discount = net_price * (n / 100)
                    total_price = (net_price * no_of_people) - discount

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_city_tour_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Update"):
                        sql = "update city_tours set location=%s, no_of_people=%s, price=%s, date_time=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                        val = (
                        package, no_of_people, total_price, selected_datetime, payment_method, special_requirement,
                        reservation_id)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record updated successfully")


                elif update == "Beach Tours":
                    st.write("per person")
                    # Display checkboxes for Beach tour packages
                    selected_beach_tour_packages = []
                    for package, price in beach_tour_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_beach_tour_packages.append(package)
                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    no_of_people = st.number_input("Number of People", min_value=1, value=1)

                    # Discount
                    if no_of_people >= 9:
                        n = 15
                    elif no_of_people >= 6:
                        n = 10
                    elif no_of_people >= 3:
                        n = 5
                    else:
                        n = 0

                    net_price = sum(
                        [beach_tour_packages[package] for package in selected_beach_tour_packages]) * no_of_people
                    discount = net_price * (n / 100)
                    total_price = net_price - discount

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_beach_tour_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Update"):
                        sql = "update beach_tours set location=%s, no_of_people=%s, price=%s, date_time=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                        val = (
                        package, no_of_people, total_price, selected_datetime, payment_method, special_requirement,
                        reservation_id)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record updated successfully")


                elif update == "Wild Safari":
                    st.write("per person")
                    # Display checkboxes for wild safari packages
                    selected_wild_safari_packages = []
                    for package, price in wild_safari_packages.items():
                        checkbox_state = st.checkbox(package, key=package)
                        if checkbox_state:
                            selected_wild_safari_packages.append(package)
                    selected_date = st.date_input("Select Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    no_of_people = st.number_input("Number of People", min_value=1, value=1)

                    # Discount
                    if no_of_people >= 10:
                        n = 25
                    elif no_of_people >= 8:
                        n = 20
                    elif no_of_people >= 6:
                        n = 15
                    elif no_of_people >= 4:
                        n = 10
                    elif no_of_people >= 2:
                        n = 5
                    else:
                        n = 0

                    # Calculate total price
                    net_price = sum([wild_safari_packages[package] for package in selected_wild_safari_packages])
                    discount = net_price * (n / 100)
                    total_price = net_price - discount

                    special_requirement = st.text_area("Special requirement")

                    st.subheader("Selected Packages:")
                    for package in selected_wild_safari_packages:
                        st.write(f"- {package}")

                    st.subheader("Selected Date and Time:")
                    st.write(selected_datetime)

                    st.subheader("Number of People:")
                    st.write(no_of_people)

                    st.subheader("Total Price:")
                    st.write(f"LKR {total_price}")

                    if st.button("Update"):
                        sql = "update wild_safari set location=%s, no_of_people=%s, price=%s, date_time=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                        val = (
                        package, no_of_people, total_price, selected_datetime, payment_method, special_requirement,
                        reservation_id)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record updated successfully")


                elif update == "Accommodation":
                    selected_date = st.date_input("Select Check-in Date", min_value=datetime.now(), key="date_picker")
                    selected_time = st.time_input("Select Check-in Time", key="time_picker1")

                    selected_datetime = datetime.combine(selected_date, selected_time)

                    selected_date1 = st.date_input("Select Check-out Date", min_value=datetime.now(),
                                                   key="date_picker2")
                    selected_time1 = st.time_input("Select Check-out Time", key="time_picker3")

                    selected_datetime1 = datetime.combine(selected_date1, selected_time1)

                    # Calculating the days
                    no_days = (selected_datetime1 - selected_datetime).days

                    # Get the payment method
                    payment_method = st.radio("Select the payment method", ("Cash", "Card"))

                    # Get the number of people
                    num_people = st.number_input("Number of People", min_value=1, value=1)

                    # Discount
                    if num_people >= 10:
                        num = 15
                    elif num_people >= 8:
                        num = 10
                    elif num_people >= 6:
                        num = 7
                    elif num_people >= 4:
                        num = 5
                    else:
                        num = 0

                    option = st.selectbox("Select a Service", (
                    "Sun-Set Beach Mirissa", "Sun-Set Lagoon Tangalle", "Sun-Set Blue Weligama",
                    "Sun-Set Resort Unawatuna", "Sun-Set Ocean Ahungalla"))

                    if option == "Sun-Set Beach Mirissa":
                        selected_sunset_beach_packages = []
                        for package, price in sunset_beach_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                            if checkbox_state:
                                selected_sunset_beach_packages.append(package)

                        # Calculate total price
                        net_price = sum(
                            [sunset_beach_packages[package] for package in selected_sunset_beach_packages]) * (
                                                num_people + no_days)
                        discount = sum(
                            [sunset_beach_packages[package] for package in selected_sunset_beach_packages]) * (
                                               num / 100)
                        total_price = net_price - discount

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_beach_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {total_price}")

                        if st.button("Update"):
                            sql = "update accommodation set hotel=%s, package=%s, no_of_people=%s, price=%s, checkin_datetime=%s, checkout_datetime=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                            val = (package, option, num_people, total_price, selected_datetime, selected_datetime1,
                                   payment_method, special_requirement, reservation_id)
                            my_cursor.execute(sql, val)
                            connection.commit()
                            st.success("Record updated successfully")

                    elif option == "Sun-Set Lagoon Tangalle":
                        selected_sunset_lagoon_packages = []
                        for package, price in sunset_lagoon_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                            if checkbox_state:
                                selected_sunset_lagoon_packages.append(package)

                        # Calculate total price
                        net_price = sum(
                            [sunset_lagoon_packages[package] for package in selected_sunset_lagoon_packages]) * (
                                                num_people + no_days)
                        discount = sum(
                            [sunset_lagoon_packages[package] for package in selected_sunset_lagoon_packages]) * (
                                               num / 100)
                        total_price = net_price - discount

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_lagoon_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {total_price}")

                        if st.button("Update"):
                            sql = "update accommodation set hotel=%s, package=%s, no_of_people=%s, price=%s, checkin_datetime=%s, checkout_datetime=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                            val = (package, option, num_people, total_price, selected_datetime, selected_datetime1,
                                   payment_method, special_requirement, reservation_id)
                            my_cursor.execute(sql, val)
                            connection.commit()
                            st.success("Record updated successfully")


                    # Sun-Set Blue Weligama
                    elif option == "Sun-Set Blue Weligama":
                        selected_sunset_blue_packages = []
                        for package, price in sunset_blue_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                            if checkbox_state:
                                selected_sunset_blue_packages.append(package)

                        # Calculate total price
                        net_price = sum(
                            [sunset_blue_packages[package] for package in selected_sunset_blue_packages]) * (
                                                num_people + no_days)
                        discount = sum([sunset_blue_packages[package] for package in selected_sunset_blue_packages]) * (
                                    num / 100)
                        total_price = net_price - discount

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_blue_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {total_price}")

                        if st.button("Update"):
                            sql = "update accommodation set hotel=%s, package=%s, no_of_people=%s, price=%s, checkin_datetime=%s, checkout_datetime=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                            val = (package, option, num_people, total_price, selected_datetime, selected_datetime1,
                                   payment_method, special_requirement, reservation_id)
                            my_cursor.execute(sql, val)
                            connection.commit()
                            st.success("Record updated successfully")

                    # Sun-Set Resort Unawatuna
                    elif option == "Sun-Set Resort Unawatuna":
                        selected_sunset_resort_packages = []
                        for package, price in sunset_resort_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                            if checkbox_state:
                                selected_sunset_resort_packages.append(package)

                        # Calculate total price
                        net_price = sum(
                            [sunset_resort_packages[package] for package in selected_sunset_resort_packages]) * (
                                                num_people + no_days)
                        discount = sum(
                            [sunset_resort_packages[package] for package in selected_sunset_resort_packages]) * (
                                               num / 100)
                        total_price = net_price - discount

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_resort_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {total_price}")

                        if st.button("Update"):
                            sql = "update accommodation set hotel=%s, package=%s, no_of_people=%s, price=%s, checkin_datetime=%s, checkout_datetime=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                            val = (package, option, num_people, total_price, selected_datetime, selected_datetime1,
                                   payment_method, special_requirement, reservation_id)
                            my_cursor.execute(sql, val)
                            connection.commit()
                            st.success("Record updated successfully")


                    elif option == "Sun-Set Ocean Ahungalla":
                        selected_sunset_ocean_packages = []
                        for package, price in sunset_ocean_packages.items():
                            checkbox_state = st.checkbox(package, key=package)
                            if checkbox_state:
                                selected_sunset_ocean_packages.append(package)

                        # Calculate total price
                        net_price = sum(
                            [sunset_ocean_packages[package] for package in selected_sunset_ocean_packages]) * (
                                                num_people + no_days)
                        discount = sum(
                            [sunset_ocean_packages[package] for package in selected_sunset_ocean_packages]) * (
                                               num / 100)
                        total_price = net_price - discount

                        special_requirement = st.text_area("Special requirement")

                        st.subheader("Selected Packages:")
                        for package in selected_sunset_ocean_packages:
                            st.write(f"- {package}")

                        st.subheader("Selected Date and Time:")
                        st.write(selected_datetime)

                        st.subheader("Number of People:")
                        st.write(num_people)

                        st.subheader("Total Price:")
                        st.write(f"LKR {total_price}")

                        if st.button("Update"):
                            sql = "update accommodation set hotel=%s, package=%s, no_of_people=%s, price=%s, checkin_datetime=%s, checkout_datetime=%s, payment_method=%s, special_requirement=%s where Reservation_id=%s"
                            val = (package, option, num_people, total_price, selected_datetime, selected_datetime1,
                                   payment_method, special_requirement, reservation_id)
                            my_cursor.execute(sql, val)
                            connection.commit()
                            st.success("Record updated successfully")

        elif option == "Delete":
                st.subheader("Delete a Record")
                reservation_id = st.number_input("Enter the person ID: ")
                delete_option = st.selectbox("Delete service", (
                "Water sports", "City Tours", "Beach Tours", "Wild Safari", "Accommodation"))

                if delete_option == "Water sports":
                    if st.button("Delete"):
                        sql = "delete from water_sports where reservation_id=%s"
                        val = (reservation_id,)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record deleted successfully")

                elif delete_option == "City Tours":
                    if st.button("Delete"):
                        sql = "delete from city_tours where reservation_id=%s"
                        val = (reservation_id,)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record deleted successfully")

                elif delete_option == "Beach Tours":
                    if st.button("Delete"):
                        sql = "delete from beach_tours where reservation_id=%s"
                        val = (reservation_id,)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record deleted successfully")

                elif delete_option == "Wild Safari":
                    if st.button("Delete"):
                        sql = "delete from wild_safari where reservation_id=%s"
                        val = (reservation_id,)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record deleted successfully")

                elif delete_option == "Accommodation":
                    hotel = st.selectbox("Select a Service", (
                    "Sun-Set Beach Mirissa", "Sun-Set Lagoon Tangalle", "Sun-Set Blue Weligama",
                    "Sun-Set Resort Unawatuna", "Sun-Set Ocean Ahungalla"))

                    if st.button("Delete"):
                        # Corrected SQL query with parameters
                        sql = "DELETE FROM accommodation WHERE reservation_id = %s AND hotel = %s"
                        val = (reservation_id, hotel)
                        my_cursor.execute(sql, val)
                        connection.commit()
                        st.success("Record deleted successfully")

        elif option == "Read":
            st.subheader("Read Records")
            read = st.selectbox("Select a Service",
                                ("City Tours", "Beach Tours", "Water Sports", "Wild Safari", "Accommodation"))

            if read == "Water Sports":
                query = """
                    SELECT c.customer_id, c.first_name, c.last_name, wa.Reservation_id, wa.location, wa.price, wa.no_of_people,
                           wa.date_time, wa.payment_method, wa.special_requirement
                    FROM water_sports wa
                    JOIN customer c ON wa.customer_id = c.customer_id
                """
                my_cursor.execute(query)
                result = my_cursor.fetchall()
                columns = [desc[0] for desc in my_cursor.description]
                df = pd.DataFrame(result, columns=columns)
                st.table(df)

            elif read == "City Tours":
                query = """
                    SELECT c.customer_id, c.first_name, c.last_name, ct.Reservation_id, ct.location, ct.price, ct.no_of_people,
                           ct.date_time, ct.payment_method, ct.special_requirement
                    FROM city_tours ct
                    JOIN customer c ON ct.customer_id = c.customer_id
                """
                my_cursor.execute(query)
                result = my_cursor.fetchall()
                columns = [desc[0] for desc in my_cursor.description]
                df = pd.DataFrame(result, columns=columns)
                st.table(df)

            elif read == "Beach Tours":
                query = """
                    SELECT c.customer_id, c.first_name, c.last_name, bt.Reservation_id, bt.location, bt.price, bt.no_of_people,
                           bt.date_time, bt.payment_method, bt.special_requirement
                    FROM beach_tours bt
                    JOIN customer c ON bt.customer_id = c.customer_id
                """
                my_cursor.execute(query)
                result = my_cursor.fetchall()
                columns = [desc[0] for desc in my_cursor.description]
                df = pd.DataFrame(result, columns=columns)
                st.table(df)

            elif read == "Wild Safari":
                query = """
                    SELECT c.customer_id, c.first_name, c.last_name, ws.Reservation_id, ws.location, ws.price, ws.no_of_people,
                           ws.date_time, ws.payment_method, ws.special_requirement
                    FROM wild_safari ws
                    JOIN customer c ON ws.customer_id = c.customer_id
                """
                my_cursor.execute(query)
                result = my_cursor.fetchall()
                columns = [desc[0] for desc in my_cursor.description]
                df = pd.DataFrame(result, columns=columns)
                st.table(df)

            elif read == "Accommodation":
                query = """
                    SELECT c.customer_id, c.first_name, c.last_name, a.Reservation_id, a.hotel, a.package, a.checkin_datetime,
                           a.checkout_datetime, a.price, a.no_of_people, a.payment_method, a.special_requirement
                    FROM accommodation a
                    JOIN customer c ON a.customer_id = c.customer_id
                """
                my_cursor.execute(query)
                result = my_cursor.fetchall()
                columns = [desc[0] for desc in my_cursor.description]
                df = pd.DataFrame(result, columns=columns)
                st.table(df)

    else:
        st.warning("Invalid username or password. Please try again.")


def login():
    page_bg_img = """
                      <style>
                          [data-testid="stAppViewContainer"] {
                              background-image: url("https://wallpapers.com/images/hd/faded-background-dukmpz8g0k0772ho.jpg");
                              background-size: cover;
                          }
                          [data-testid="stHeader"] {
                              background-color: rgba(0, 0, 0, 0);
                          }
                          [data-testid="stSidebar"] {
                              background-color: rgba(0, 0, 0, 0);
                          }
                      </style>
                  """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.header("welocme")




def main():
    page_bg_img = """
        <style>
            [data-testid="stAppViewContainer"] {
                background-image: url("https://cdn.pixabay.com/photo/2017/06/29/18/37/sri-lanka-2455695_1280.jpg");
                background-size: cover;
            }
            [data-testid="stHeader"] {
                background-color: rgba(0, 0, 0, 0);
            }
            [data-testid="stSidebar"] {
                background-color: rgba(0, 0, 0, 0);
            }
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


    selected_option = st.sidebar.selectbox("Select Your Service:", ["Homepage", "Customer", "Employee"])


    if selected_option == "Homepage":
        st.header("SUNSET ADVENTURES")

    elif selected_option == "Customer":
        booking()
    elif selected_option == "Employee":
        employee_login()


if __name__ == "__main__":
    main()