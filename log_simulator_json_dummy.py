# # import socket
# # import os
# # import json
# # import ast
# # from datetime import datetime
# # import getpass

# # # Server details
# # SERVER_IP = "10.10.100.55"
# # SERVER_PORT = 9003

# # def send_updated_log(file_path):
# #     # Verify the log file exists
# #     if not os.path.isfile(file_path):
# #         print(f"Error: File '{file_path}' does not exist.")
# #         return

# #     # Read the single log line from the file
# #     try:
# #         with open(file_path, 'r') as file:
# #             line = file.readline().strip()
# #     except Exception as e:
# #         print(f"Error reading file: {e}")
# #         return

# #     # Expected format: "<old_date_time> - INFO - <dictionary>"
# #     parts = line.split(" - INFO - ", 1)
# #     if len(parts) != 2:
# #         print("Error: Unexpected file format. Couldn't find '- INFO -' separator.")
# #         return

# #     log_dict_str = parts[1]

# #     # Safely evaluate the dictionary string from the log
# #     try:
# #         log_data = ast.literal_eval(log_dict_str)
# #     except Exception as e:
# #         print(f"Error parsing log dictionary: {e}")
# #         return

# #     # Get the current date and time
# #     current_time = datetime.now()

# #     # Update the log data with current date and time values
# #     log_data['date']  = current_time.day
# #     log_data['month'] = current_time.month
# #     log_data['year']  = current_time.year
# #     log_data['hh']    = current_time.hour
# #     log_data['mm']    = current_time.minute
# #     log_data['ss']    = current_time.second

# #     # Update the 'user' field with the current system user
# #     log_data['user'] = getpass.getuser()
# #     log_data['mitre_technique_no'] = log_data.get('mitre_technique_no', 'NA')


# #     # Optionally, you can generate a new event_id if needed:
# #     # log_data['event_id'] = generate_event_id()

# #     # Convert the updated log dictionary to a JSON string for transmission
# #     message = json.dumps(log_data)

# #     # Create a UDP socket and send the JSON data
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #     try:
# #         sock.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))
# #         print(f"Successfully sent updated log to {SERVER_IP}:{SERVER_PORT}")
# #     except Exception as e:
# #         print(f"Error sending UDP message: {e}")
# #     finally:
# #         sock.close()

# # if __name__ == "__main__":
# #     log_file_path = "high_volume_data_transfer.log"  # Ensure this path is correct
# #     send_updated_log(log_file_path)

# import socket
# import os
# import json
# import ast
# from datetime import datetime
# import getpass

# # Server details
# SERVER_IP = "10.10.100.55"
# SERVER_PORT = 9003

# def send_updated_log(file_path):
#     # Verify the log file exists
#     if not os.path.isfile(file_path):
#         print(f"Error: File '{file_path}' does not exist.")
#         return

#     # Read the single log line from the file
#     try:
#         with open(file_path, 'r') as file:
#             line = file.readline().strip()
#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return

#     # Expected format: "<old_date_time> - INFO - <dictionary>"
#     parts = line.split(" - INFO - ", 1)
#     if len(parts) != 2:
#         print("Error: Unexpected file format. Couldn't find '- INFO -' separator.")
#         return

#     log_dict_str = parts[1]

#     # Safely evaluate the dictionary string from the log
#     try:
#         log_data = ast.literal_eval(log_dict_str)
#     except Exception as e:
#         print(f"Error parsing log dictionary: {e}")
#         return

#     # Get the current date and time
#     current_time = datetime.now()

#     # Update the log data with current date and time values
#     log_data['date']  = current_time.day
#     log_data['month'] = current_time.month
#     log_data['year']  = current_time.year
#     log_data['hh']    = current_time.hour
#     log_data['mm']    = current_time.minute
#     log_data['ss']    = current_time.second

#     # Update the 'user' field with the current system user
#     log_data['user'] = getpass.getuser()
#     log_data['mitre_technique_no'] = log_data.get('mitre_technique_no', 'NA')
    
#     # Add log_text as the last field
#     log_data['log_text'] = log_dict_str  # Keeping the original log content

#     # Convert the updated log dictionary to a JSON string for transmission
#     message = json.dumps(log_data)

#     # Create a UDP socket and send the JSON data
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         sock.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))
#         print(f"Successfully sent updated log to {SERVER_IP}:{SERVER_PORT}")
#     except Exception as e:
#         print(f"Error sending UDP message: {e}")
#     finally:
#         sock.close()
# def create_dummy_data():
#     data = {
#         'HEADER': {
#             'sourceId': 4,
#             'destId': 4,
#             'msgId': 4000
#         },
#         'MESSAGE': {
#             'eventId': 'EVENT_123',
#             'date': 12,
#             'month': 11,
#             'year': 2025,
#             'hh': 10,
#             'mm': 51,
#             'ss': 59,            
#             'eventType': 1,
#             'eventSubType': 7,
#             'attackerInfo': 'Attacker_Info',
#             'component': 1, # Example Value
#             "user": "test_user",
#             'resourceInfo': 'Resource_Example',
#             'severity': 2,  # Example severity level
#             'eventReason': 'Dummy Test Event',
#             'pid': 1234,
#             'deviceType': 1,
#             'deviceMacId': '00:11:22:33:44:55',
#             'deviceIP': '192.168.1.100',
#             'srcId': 12,  # Example Source ID
#             'logText': 'Test log message'
#         }
#     }
#     return data

# if __name__ == "__main__":
#     data = create_dummy_data()
#     #log_file_path = "/home/jyoti/Desktop/Test_simulator/Authentication_event/successful_login.log"  # Ensure this path is correct
#     send_updated_log(data)


import socket
import json
from datetime import datetime
import getpass  

# Server details
SERVER_IP = "10.10.100.56"
SERVER_PORT = 9003

def create_dummy_data():
    current_time = datetime.now()
    data = {
        'HEADER': {
            'sourceId': 4,
            'destId': 4,
            'msgId': 4000
        },
        'MESSAGE': {
            'eventId': 'EVENT_123',
            'date': current_time.day,
            'month': current_time.month,
            'year': current_time.year,
            'hh': current_time.hour,
            'mm': current_time.minute,
            'ss': current_time.second,
            'eventType': 1,
            'eventSubType': 1,
            'attackerInfo': 'Attacker_Info',
            'component': 1,
            "user": getpass.getuser(),
            'resourceInfo': 'Resource_Example',
            'severity': 2,
            'eventReason': 'Dummy Test Event',
            'pid': 1234,
            'deviceType': 1,
            'deviceMacId': '00:11:22:33:44:55',
            'deviceIP': '192.168.1.100',
            'srcId': 12,
            'logText': 'Test log message'
        }
    }
    return data

def send_dummy_data():
    dummy_data = create_dummy_data()
    message = json.dumps(dummy_data)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))
        print(f"Successfully sent dummy data to {SERVER_IP}:{SERVER_PORT}")
    except Exception as e:
        print(f"Error sending UDP message: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    send_dummy_data()
