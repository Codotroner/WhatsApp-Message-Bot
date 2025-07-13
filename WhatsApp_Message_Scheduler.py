import pywhatkit as kit

def send_whatsapp_message(phone_number, message, hour, minute):
    kit.sendwhatmsg(phone_number, message, hour, minute)

if __name__ == "__main__":
    number = input("Enter phone number with country code (e.g., +91xxxxxxxxxx): ")
    msg = input("Enter the message to send: ")
    hour = int(input("Enter hour (24-hour format): "))
    minute = int(input("Enter minute: "))

    send_whatsapp_message(number, msg, hour, minute)