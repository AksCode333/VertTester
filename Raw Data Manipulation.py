import keyboard
import serial
import tkinter as tk

SERIAL_PORT = '/dev/cu.usbserial-1420'
BAUD_RATE = 9600
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)


seen_bool = []
aquired_time = []
pressure_value = []
check = [False]
final_data = []
temp = [0]
def read_and_process_data():
    line = ser.readline().decode('utf-8').strip()

    sensorValues = line.split(',')

    seen_bool.append((sensorValues[0]))
    aquired_time.append(round(float(sensorValues[1]), 2))
    pressure_value.append(round(float(sensorValues[2]), 2))

    #Add it too the final list
    temp.clear()
    temp.append((sensorValues[0]))
    temp.append(round(float(sensorValues[1]), 2))
    temp.append(round(float(sensorValues[2]), 2))
    print(temp)
    final_data.append([(sensorValues[0]), round(float(sensorValues[1]), 2), round(float(sensorValues[2]), 2)])
 


# read_and_process_data()
# print(seen_bool)
# print(aquired_time)
# print(pressure_value)

def run():
    final_lists = []
    while check[0] == True:
            root.update()
            read_and_process_data()
            if check[0] == False:
                for i in seen_bool:
                    #  final_data.append
                    f = "filler"


# Initialize the root window TKINTER ----------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Toggle Button")
root.geometry("400x300")
root.configure(bg='gray')
# Function to toggle the variable and update Button 1 text
def on():
    check[0] = True
    print("checking")
    run()
# Function to reset the variable and update Button 1 text
def off():
    check[0] = False

def print_data():
    print(final_data)
     
def reset():
     seen_bool.clear()
     aquired_time.clear()
     pressure_value.clear()
     final_data.clear()
     
def calculate_height():
     # Filter out only the rows where the first element is "True"
    true_rows = [row for row in final_data if row[0] == 'True']
    # Get the time values for the filtered rows
    times = [row[1] for row in true_rows]
    # Calculate the time difference between consecutive "True" times
    time_differences = [times[i] - times[i-1] for i in range(1, len(times))]
    new = []
    for i in time_differences:
        if i > 60:
            new.append(i)
    print(new)
    #Equation (h = g × t2/2)
    for i in new:
        print((i/1000), "seconds    ", (9.81 * (i/1000) * (i/1000) / 2) * 12, "Inches")
        

# Create buttons and attach the functions
button1 = tk.Button(root, text="   On    ", command=on)
button1.pack(pady=10)

button2 = tk.Button(root, text="    OFF   ", command=off)
button2.pack(pady=10)

button3 = tk.Button(root, text="    Values   ", command=print_data)
button3.pack(pady=10)

button4 = tk.Button(root, text="    Reset   ", command=reset)
button4.pack(pady=10)

button5 = tk.Button(root, text="    JUMP HEIGHT   ", command=calculate_height)
button5.pack(pady=10)
# Run the Tkinter main loop
root.mainloop()
