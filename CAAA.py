import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText
from email import encoders  
import matplotlib.pyplot as plt
from datetime import datetime

class AttendanceTaker:
    def __init__(self, class_name):
        self.class_name = class_name
        self.student_attendance = {}
        self.row = 2

    def swipe_card(self, student_id, swipe_time=None):
        if student_id not in self.student_attendance:
            self.student_attendance[student_id] = {"name": self.get_student_name(student_id), "attendance": []}

        if swipe_time is None:
            swipe_time = datetime.now()

        if not self.student_attendance[student_id]["attendance"]:
            attendance_status = "Present"  # Assume present for the first swipe
        else:
            attendance_status = "Present" if self.student_attendance[student_id]["attendance"][-1]["status"] == "Present" else "Absent"

        self.student_attendance[student_id]["attendance"].append({"status": attendance_status, "time": swipe_time})

        if len(self.student_attendance[student_id]["attendance"]) > 1:
            prev_status = self.student_attendance[student_id]["attendance"][-2]["status"]
            current_status = self.student_attendance[student_id]["attendance"][-1]["status"]
            if prev_status != current_status:
                if current_status == "Absent":
                    self.send_absence_notification(student_id, swipe_time)
                else:
                    self.send_presence_notification(student_id, swipe_time)

    def get_student_name(self, student_id):
        # Simulated database query
        student_names = {
            "123456789": "John Doe",
            "987654321": "Jane Smith"
        }
        return student_names.get(student_id, "Unknown")

    def generate_spreadsheet(self):
        pass  # Not used in this modified version

    def send_absence_notification(self, student_id, swipe_time):
        sender_email = "olubakindetito@gmail.com"
        receiver_email = "tolubaki@udel.edu"
        password = "cxfg alju sfta mnha"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"Absent Notification for {self.class_name}"

        current_date = swipe_time.strftime("%Y-%m-%d")
        body = f"Subject: Absence Notification for {self.class_name} - {current_date}\n\nDear [Recipient's Name],\n\nWe regret to inform you that according to our records, {self.get_student_name(student_id)} was marked absent in the {self.class_name} session held on {current_date}.\n\nIf you believe this absence was recorded in error, please reach out to us for further assistance.\n\nRegards,\nAttendance System"
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Absent notification sent successfully for student: {self.get_student_name(student_id)}")
        except Exception as e:
            print(f"Failed to send absence notification for student: {self.get_student_name(student_id)}, Error: {e}")

    def send_presence_notification(self, student_id, swipe_time):
        sender_email = "olubakindetito@gmail.com"
        receiver_email = "tolubaki@udel.edu"
        password = "cxfg alju sfta mnha"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"Presence Notification for {self.class_name}"

        current_date = swipe_time.strftime("%Y-%m-%d")
        body = f"Subject: Presence Notification for {self.class_name} - {current_date}\n\nDear [Recipient's Name],\n\nWe are pleased to inform you that according to our records, {self.get_student_name(student_id)} was marked present in the {self.class_name} session held on {current_date}.\n\nThank you for your commitment to attending the session.\n\nRegards,\nAttendance System"
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Presence notification sent successfully for student: {self.get_student_name(student_id)}")
        except Exception as e:
            print(f"Failed to send presence notification for student: {self.get_student_name(student_id)}, Error: {e}")

    def send_email_notification(self):
        sender_email = "olubakindetito@gmail.com"
        receiver_email = "tolubaki@udel.edu"
        password = "cxfg alju sfta mnha"  

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"{self.class_name} Attendance Report"

        current_date = datetime.now().strftime("%Y-%m-%d")
        body = f"Subject: Attendance Report for {self.class_name} - {current_date}\n\nDear [Recipient's Name],\n\nI hope this message finds you well.\n\nThis email serves as an official attendance report for the {self.class_name} session held on {current_date}. As per our records, you were marked present for the entirety of the class.\n\nShould you have any questions or concerns regarding your attendance or require further documentation, please do not hesitate to reach out to us.\n\nThank you for your commitment to your academic pursuits. We look forward to your continued participation and engagement in future sessions.\n\nRegards,\nAttendance System"
        message.attach(MIMEText(body, "plain"))

        # Attach the pie chart image
        image_path = 'attendance_pie_chart.png'
        self.visualize_attendance(image_path)
        with open(image_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(image_path)}')
        message.attach(part)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email notification sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def visualize_attendance(self, image_path):
        students = list(self.student_attendance.keys())
        present_counts = [5] * len(students)
        absent_counts = [2] * len(students)  # Changed to 1 to simulate absence

        labels = ['Present', 'Absent']
        sizes = [sum(present_counts), sum(absent_counts)]
        colors = ['lightgreen', 'lightcoral']

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Attendance Visualization')
        plt.savefig(image_path)  # Save the pie chart as an image

if __name__ == "__main__":
    attendance_taker = AttendanceTaker("Mathematics")

    # Manually updating the attendance status
    # Simulating a student being absent
    student_id = "123456789"
    attendance_taker.swipe_card(student_id)  # This will mark the student as absent with the current time

    # Simulating a student being present at a specific time
    student_id = "987654321"
    swipe_time = datetime(2024, 3, 2, 10, 30)  # Simulating the student swiping their card at 10:30 AM
    attendance_taker.swipe_card(student_id, swipe_time=swipe_time)  # This will mark the student as present at the specified time

    # Sending the email notification with pie chart representation
    attendance_taker.send_email_notification()
