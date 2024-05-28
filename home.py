import streamlit as st

def get_days()-> list:
    return ["Mondays", "Tuesday", "Wednesday", "Thursday",
            "MWF", "MW", "TR"]
def get_times()->list:
    return ["7:30am - 8:20 am", "8:30 am - 9:20 am", "9:30 am - 10:20 am",
            "9:00 am - 10:20 am", "10:30 am - 11:20 am", "10:30 am - 11:50 am", 
            "11:30 am - 12:20", "12:30 pm - 1:20 pm", "12:00 pm - 1:20 pm"
            "1:30 pm - 2:20 pm","1:30 - 2:50 pm", "2:30 - 3:20 pm", 
            "3:00 pm - 4:20 pm", "4:30 pm - 5:50 pm", "4:30 pm - 7:20 pm",
            "6:00 pm - 7:20 pm", "6:00 pm - 8:50 pm", "7:30 am - 8:50 am"]
def get_final_time(day: str, time: str) -> str:
    #read the final_times file and search for the day and time and return the final time
    st.session_state['schedule'] = []
    with open('final_times.cvs', 'r') as file:
        for line in file:
            days, times , _ = line.strip().split(',')
            if days == day and times == time:
                print(line)
                st.session_state.schedule.append(line)

def display_schedule():
    col1, col2, col3 = st.columns(3)
    with col1:
        print("Days")
    with col2:
        print("Time")
    with col3:
        print("Final time")
    col4, col5, col6, col7 = st.columns(4)
    index = 0
    for days, time, final in st.session_state.schedule:
        with col4:
            print(days)
        with col5:
            print(time)
        with col6:
            print(final)
        st.divider()
        with col7:
            delete = st.button("Delete", ke=f"index-{index}")
            
    
st.header("Welcome to the place where you will find your Final schedule in a pleasent way")
st.title("Select the days and time you have your class to see your final test schedule")



class_day_list = get_days()
days = st.selectbox(
    "Select the your class days",
    class_day_list, 
    placeholder="Day(s)"
)
class_time_list = get_times()
time = st.selectbox(
    "Select the time of your class",
    class_time_list,
    placeholder="Time"
)
if 'schedule' not in st.session_state:
    st.session_state.schedule = []
st.session_state.schedule.append((days, time))

if 'add' not in st.session_state:
    st.session_state.add = False

add = st.button("Add to schedule", key="Add")

if add:
    final_time = get_final_time(days, time)
    st.session_state.schedule.add((days, time, final_time))
    display_schedule()
    st.session_state.add = False


