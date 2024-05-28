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
    if 'schedule' not in st.session_state:
        st.session_state['schedule'] = []
    with open('final_times.txt', 'r') as file:
        for line in file:
            line_list = line.strip().split(',')
            days = line_list[0]
            times = line_list[1]
            # st.write(f"{days} - {day} | {times} - {time}")
            # st.write((days == day) and (times == time))
            if days == day and times == time:
                # st.write(line_list[0])
                # st.write(line_list[1])
                # st.write(line_list[2])
                st.session_state.schedule.append(line_list)

def display_schedule():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("Days")
    with col2:
        st.write("Time")
    with col3:
        st.write("Final time")
    with col4:
        st.write("Update")
    col5, col6, col7, col8 = st.columns(4)
    index = 0
    for line in st.session_state.schedule:
        st.write(line)
        # with col5:
        #     st.write(days)
        # with col6:
        #     st.write(time)
        # with col7:
        #     st.write(final)
        st.divider()
        # with col8:
        #     delete = st.button("Delete", key=f"index-{index}")
        #     index+=1
            
    
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
    st.session_state.schedule.append((days, time, final_time))
    display_schedule()
    st.session_state.add = False


